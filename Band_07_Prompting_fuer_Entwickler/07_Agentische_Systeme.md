# Kapitel 7: Agentische Systeme – KI, die handelt

Tool Use (Kapitel 6) gibt KI Hände. Agentische Systeme geben ihr einen Plan.

Ein Agent ist ein LLM, das:
1. Ein Ziel bekommt
2. Einen Plan erstellt
3. Tools nutzt, um Schritte auszuführen
4. Ergebnisse bewertet
5. Den Plan anpasst
6. Iteriert, bis das Ziel erreicht ist

Der Unterschied zu einem einfachen Tool-Use-Call: Ein Agent arbeitet autonom über mehrere Schritte. Er entscheidet selbst, welches Tool als Nächstes kommt.

## Agent-Architektur

```
                    ┌──────────────┐
                    │     ZIEL     │
                    │  (User-Input)│
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
              ┌────▶│    PLANEN    │◀────┐
              │     │  (LLM denkt) │     │
              │     └──────┬───────┘     │
              │            │             │
              │     ┌──────▼───────┐     │
              │     │   HANDELN    │     │
              │     │ (Tool nutzen)│     │
              │     └──────┬───────┘     │
              │            │             │
              │     ┌──────▼───────┐     │
              │     │  BEOBACHTEN  │     │
              │     │ (Ergebnis)   │     │
              │     └──────┬───────┘     │
              │            │             │
              │     ┌──────▼───────┐     │
              └─────│  BEWERTEN    │─────┘
                    │ Ziel erreicht?│
                    └──────┬───────┘
                           │ Ja
                    ┌──────▼───────┐
                    │   ANTWORT    │
                    └──────────────┘
```

## Der einfachste Agent: ReAct-Loop

```python
import anthropic
import json

client = anthropic.Anthropic()

SYSTEM_PROMPT = """Du bist ein hilfreicher Agent.
Du hast Zugang zu Tools, um Aufgaben zu erledigen.

Arbeite Schritt für Schritt:
1. Überlege, was du als Nächstes tun musst
2. Nutze ein Tool
3. Beobachte das Ergebnis
4. Entscheide: Bist du fertig oder brauchst du mehr Schritte?

Wenn du die Aufgabe erledigt hast, antworte dem User direkt."""

def run_agent(user_task: str, tools: list, max_steps: int = 10) -> str:
    messages = [{"role": "user", "content": user_task}]

    for step in range(max_steps):
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        # Wenn keine Tool-Calls → Agent ist fertig
        if response.stop_reason == "end_turn":
            return next(
                block.text for block in response.content
                if block.type == "text"
            )

        # Tool-Calls ausführen
        messages.append({"role": "assistant", "content": response.content})

        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  Schritt {step+1}: {block.name}({json.dumps(block.input, ensure_ascii=False)[:100]})")
                result = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        messages.append({"role": "user", "content": tool_results})

    return "Agent hat das Schritt-Limit erreicht."
```

## MCP – Model Context Protocol

MCP ist Anthropics offener Standard, der Agenten mit externen Systemen verbindet. Statt für jedes Tool eigenen Code zu schreiben, definiert MCP ein einheitliches Protokoll.

### Was MCP löst

Ohne MCP:
```
Agent ──> Custom Code ──> Datenbank
Agent ──> Custom Code ──> Dateisystem
Agent ──> Custom Code ──> GitHub API
Agent ──> Custom Code ──> Slack API
```

Mit MCP:
```
Agent ──> MCP Client ──> MCP Server (DB)
                     ──> MCP Server (Dateien)
                     ──> MCP Server (GitHub)
                     ──> MCP Server (Slack)
```

### MCP-Architektur

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   MCP Host  │────▶│  MCP Client  │────▶│  MCP Server  │
│ (Claude,    │     │ (SDK)        │     │ (dein Code)  │
│  Cursor,    │     │              │     │              │
│  deine App) │     │              │     │ - Tools      │
└─────────────┘     └──────────────┘     │ - Resources  │
                                         │ - Prompts    │
                                         └──────────────┘
```

### Einen MCP-Server schreiben (Python)

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Mein Firmen-MCP-Server")

@mcp.tool()
def search_knowledge_base(query: str, max_results: int = 5) -> str:
    """Durchsucht die interne Wissensdatenbank des Unternehmens.
    Nutze dieses Tool für Fragen zu Firmenrichtlinien,
    Prozessen und internem Wissen."""
    results = db.search(query, limit=max_results)
    return json.dumps(results)

@mcp.tool()
def create_jira_ticket(
    title: str,
    description: str,
    priority: str = "medium",
    assignee: str | None = None
) -> str:
    """Erstellt ein Jira-Ticket. Nutze dieses Tool wenn der User
    ein Ticket, Issue oder Task erstellen möchte."""
    ticket = jira_client.create_issue(
        project="PROJ",
        summary=title,
        description=description,
        priority=priority,
        assignee=assignee
    )
    return json.dumps({"ticket_id": ticket.key, "url": ticket.url})

@mcp.resource("file://docs/{path}")
def read_document(path: str) -> str:
    """Liest ein Dokument aus dem Docs-Verzeichnis."""
    return (Path("docs") / path).read_text()

# Server starten
mcp.run()
```

### MCP-Server nutzen (in Claude Code)

```json
// .claude/settings.json oder ~/.claude.json
{
  "mcpServers": {
    "firmen-kb": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        "DB_URL": "postgresql://..."
      }
    }
  }
}
```

Jetzt kann Claude Code automatisch deine Wissensdatenbank durchsuchen und Jira-Tickets erstellen.

## Multi-Agent-Systeme

Für komplexe Aufgaben: Mehrere spezialisierte Agenten, die zusammenarbeiten.

### Orchestrator-Pattern

```python
async def orchestrator(task: str) -> str:
    """Ein Orchestrator delegiert an spezialisierte Agenten."""

    # Schritt 1: Aufgabe analysieren und Plan erstellen
    plan = await planning_agent(task)

    # Schritt 2: Teilaufgaben an Spezialisten delegieren
    results = {}
    for subtask in plan.subtasks:
        if subtask.type == "research":
            results[subtask.id] = await research_agent(subtask)
        elif subtask.type == "code":
            results[subtask.id] = await coding_agent(subtask)
        elif subtask.type == "review":
            results[subtask.id] = await review_agent(subtask)

    # Schritt 3: Ergebnisse zusammenführen
    final = await synthesis_agent(task, results)
    return final
```

### Supervisor-Pattern

```python
async def supervisor_loop(task: str, agents: dict) -> str:
    """Ein Supervisor wählt den nächsten Agent und überwacht den Fortschritt."""
    context = {"task": task, "history": [], "status": "in_progress"}

    while context["status"] != "done":
        # Supervisor entscheidet, welcher Agent als Nächstes dran ist
        decision = await supervisor_decide(context, list(agents.keys()))

        if decision.action == "delegate":
            result = await agents[decision.agent](decision.subtask, context)
            context["history"].append({
                "agent": decision.agent,
                "task": decision.subtask,
                "result": result
            })

        elif decision.action == "done":
            context["status"] = "done"

    return await compile_final_answer(context)
```

## Anthropic Agent SDK

Anthropics SDK für den Bau produktionsreifer Agenten:

```python
from claude_agent_sdk import Agent, tool

class ResearchAgent(Agent):
    """Agent für Recherche-Aufgaben."""

    model = "claude-sonnet-4-20250514"
    system_prompt = """Du bist ein Recherche-Agent.
    Du suchst nach Informationen und fasst sie zusammen.
    Nutze die verfügbaren Tools systematisch."""

    @tool
    def web_search(self, query: str) -> str:
        """Suche im Web nach Informationen."""
        return search_api.search(query)

    @tool
    def read_url(self, url: str) -> str:
        """Lese den Inhalt einer Webseite."""
        return fetch_and_extract(url)

# Agent ausführen
agent = ResearchAgent()
result = agent.run("Recherchiere die neuesten Trends in erneuerbaren Energien 2026")
```

## Agent-Guardrails

Agenten, die autonom handeln, brauchen Sicherheitsmechanismen:

### 1. Token-Budget

```python
MAX_TOKENS_PER_TASK = 100_000  # Kosten-Limit

def run_agent_with_budget(task, budget=MAX_TOKENS_PER_TASK):
    total_tokens = 0
    while total_tokens < budget:
        response = call_llm(...)
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        if is_done(response):
            return response
    raise BudgetExceededError(f"Token-Budget ({budget}) überschritten")
```

### 2. Erlaubte Aktionen

```python
ALLOWED_ACTIONS = {
    "read_file": True,        # Immer erlaubt
    "write_file": "confirm",  # User muss bestätigen
    "delete_file": False,     # Nie erlaubt
    "run_command": "confirm",
    "send_email": False,
    "query_database": True,
    "modify_database": "confirm",
}
```

### 3. Sandbox

Agenten sollten in isolierten Umgebungen laufen:
- Docker-Container für Code-Ausführung
- Read-only Dateisysteme wo möglich
- Netzwerk-Beschränkungen
- Zeitlimits für einzelne Operationen

### 4. Human-in-the-Loop

Für kritische Entscheidungen: Pausiere und frage den Menschen:

```python
def agent_step(action):
    if action.risk_level == "high":
        approved = ask_human(f"Agent möchte: {action.description}\nErlauben?")
        if not approved:
            return "Aktion abgelehnt"
    return execute(action)
```

## Wann Agenten, wann nicht?

| Situation | Agent? | Warum |
|---|---|---|
| Klar definierte Aufgabe, 1 Schritt | Nein | Einfacher API-Call reicht |
| Multi-Step mit klarer Reihenfolge | Prompt-Chain | Deterministische Pipeline reicht |
| Multi-Step mit unklarer Reihenfolge | Ja | Agent entscheidet dynamisch |
| Offene Recherche-Aufgabe | Ja | Agent iteriert bis zufrieden |
| Sicherheitskritische Aufgabe | Vorsichtig | Starke Guardrails nötig |
| Echtzeit / Low-Latency | Nein | Agenten sind langsam (mehrere LLM-Calls) |

---

## Übungen

### Übung 1: ReAct-Agent
Baue einen einfachen ReAct-Agent mit 2-3 Tools (z.B. Web-Suche, Rechner, Wetter). Lass ihn eine mehrstufige Frage beantworten.

### Übung 2: MCP-Server
Schreibe einen MCP-Server für einen Anwendungsfall deiner Wahl (z.B. Zugriff auf ein lokales Dateisystem, eine SQLite-DB oder eine API).

### Übung 3: Guardrails
Implementiere Token-Budget, erlaubte Aktionen und Human-in-the-Loop für deinen Agent. Teste: Hält er sich daran?

### Übung 4: Multi-Agent
Baue ein 2-Agent-System: Ein Agent recherchiert, der andere schreibt basierend auf der Recherche. Koordiniere sie mit einem Orchestrator.
