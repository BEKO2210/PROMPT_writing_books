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

Das Grundmuster ist eine Schleife: **Planen → Handeln → Beobachten → Bewerten → (Wiederholen oder Fertig)**. In der Literatur heißt das **ReAct** (Reason + Act).

```
ZIEL (User-Input)
    ↓
PLANEN (LLM denkt) ←──────┐
    ↓                       │
HANDELN (Tool nutzen)      │
    ↓                       │
BEOBACHTEN (Ergebnis)      │
    ↓                       │
BEWERTEN ── Ziel erreicht? ─┘
    ↓ Ja
ANTWORT
```

## Der einfachste Agent: ReAct-Loop

Der ReAct-Loop ist im Kern der Tool-Use-Loop aus Kapitel 6 – nur mit einem System-Prompt, der dem Modell sagt: *"Arbeite Schritt für Schritt. Überlege, was du als Nächstes tun musst. Nutze ein Tool. Beobachte das Ergebnis. Entscheide: fertig oder weitermachen?"*

Plus ein `max_steps`-Parameter als Sicherheitsnetz gegen Endlosschleifen. Bei jedem Schritt wird geloggt, welches Tool aufgerufen wird – so siehst du, wie der Agent "denkt".

## MCP – Model Context Protocol

MCP (Model Context Protocol) ist der offene Standard für die Verbindung von Agenten mit externen Systemen. Im November 2024 von Anthropic eingeführt, im Dezember 2025 an die Linux Foundation übergeben. Stand März 2026: 97 Millionen monatliche SDK-Downloads, adoptiert von Anthropic, OpenAI, Google, Microsoft und Amazon.

### Was MCP löst

Ohne MCP schreibst du für jedes externe System (Datenbank, GitHub, Slack, Jira) eigenen Integrations-Code. Mit MCP definierst du einmal einen MCP-Server – und jeder MCP-fähige Client (Claude Code, Cursor, deine App) kann ihn nutzen.

### MCP-Architektur

Drei Komponenten: **MCP Host** (Claude, Cursor, deine App), **MCP Client** (SDK) und **MCP Server** (dein Code). Der Server exponiert drei Dinge: **Tools** (Funktionen, die der Agent aufrufen kann), **Resources** (Daten, die der Agent lesen kann) und **Prompts** (vordefinierte Prompt-Templates).

### MCP vs. Function Calling

MCP-Server halten State über Aufrufe hinweg, bieten dynamische Tool-Discovery (Agent erkennt automatisch verfügbare Tools) und exponieren Resources – das ist reicher als stateless Function Calling.

### Einen MCP-Server schreiben

Mit dem Python SDK (`FastMCP`) sind es wenige Zeilen:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Firmen-Server")

@mcp.tool()
def search_knowledge_base(query: str, max_results: int = 5) -> str:
    """Durchsucht die interne Wissensdatenbank."""
    results = db.search(query, limit=max_results)
    return json.dumps(results)

@mcp.resource("file://docs/{path}")
def read_document(path: str) -> str:
    """Liest ein Dokument aus dem Docs-Verzeichnis."""
    return (Path("docs") / path).read_text()

mcp.run()
```

In der Claude-Code-Konfiguration (`settings.json`) registrierst du den Server mit `command` und `args`. Dann kann der Agent automatisch deine Wissensdatenbank durchsuchen.

## Multi-Agent-Systeme

Für komplexe Aufgaben: Mehrere spezialisierte Agenten, die zusammenarbeiten.

### Orchestrator-Pattern

Ein Orchestrator analysiert die Aufgabe, erstellt einen Plan mit Teilaufgaben und delegiert an Spezialisten (Research-Agent, Coding-Agent, Review-Agent). Am Ende führt ein Synthese-Agent die Ergebnisse zusammen.

### Supervisor-Pattern

Ein Supervisor wählt dynamisch den nächsten Agent und überwacht den Fortschritt. Im Gegensatz zum Orchestrator ist der Plan nicht statisch – der Supervisor entscheidet bei jedem Schritt neu, basierend auf den bisherigen Ergebnissen.

### Agent-Frameworks

| Framework | Stärke | Ideal für |
|-----------|--------|-----------|
| **LangGraph** | Graph-basiert, Checkpointing | Komplexe Workflows mit Schleifen |
| **CrewAI** | Rollen-basierte Agents, Visual Editor | Schnelles Prototyping |
| **OpenAI Agents SDK** | Open-Source, MCP-Support | Moderate Komplexität |

**Praxis-Empfehlung:** Für einfache Workflows (1-2 Tools) brauchst du kein Framework – direkte API-Calls reichen. Framework erst ab 3+ Agents oder komplexen Abläufen.

## Agent-Guardrails

Agenten, die autonom handeln, brauchen Sicherheitsmechanismen:

### 1. Token-Budget
Setze ein maximales Token-Limit pro Aufgabe. Wenn überschritten: Stoppe den Agent und melde den Fehler.

### 2. Erlaubte Aktionen
Definiere pro Tool eine Sicherheitsstufe: `read_file` immer erlaubt, `write_file` nur mit Bestätigung, `delete_file` nie, `send_email` nie.

### 3. Sandbox
Agenten sollten in isolierten Umgebungen laufen: Docker-Container, Read-only Dateisysteme, Netzwerk-Beschränkungen, Zeitlimits.

### 4. Human-in-the-Loop
Für kritische Entscheidungen: Pausiere und frage den Menschen.

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
Baue einen einfachen ReAct-Agent mit 2-3 Tools. Lass ihn eine mehrstufige Frage beantworten.

### Übung 2: MCP-Server
Schreibe einen MCP-Server für einen Anwendungsfall deiner Wahl (z.B. SQLite-DB oder lokale API).

### Übung 3: Guardrails
Implementiere Token-Budget, erlaubte Aktionen und Human-in-the-Loop. Teste: Hält er sich daran?

### Übung 4: Multi-Agent
Baue ein 2-Agent-System: Einer recherchiert, der andere schreibt. Koordiniere sie mit einem Orchestrator.
