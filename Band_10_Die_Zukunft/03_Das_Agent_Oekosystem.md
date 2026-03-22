# Kapitel 3: Das Agent-Ökosystem – MCP, A2A und die Zukunft der Vernetzung

Agenten sind so gut wie ihre Werkzeuge. Ein Agent ohne Tools ist ein Chatbot. Ein Agent mit den richtigen Tools kann die Welt verändern. Und die Frage, *wie* Agenten an ihre Tools kommen, hat 2025-2026 eine Antwort bekommen: Offene Protokolle.

## MCP: Das USB-C der KI

Das **Model Context Protocol** (MCP) kennst du aus Band 7. Hier die Zusammenfassung und der aktuelle Stand:

MCP ist ein offener Standard, der definiert, wie KI-Modelle mit externen Tools, Datenquellen und Systemen kommunizieren. Im November 2024 von Anthropic eingeführt, im Dezember 2025 an die Agentic AI Foundation (AAIF) unter der Linux Foundation übergeben.

**Stand März 2026:**
- 97 Millionen monatliche SDK-Downloads (Python + TypeScript)
- Adoptiert von allen großen Anbietern: Anthropic, OpenAI, Google, Microsoft, Amazon
- Tausende MCP-Server für verschiedene Dienste verfügbar
- Enterprise-Impact: Integration von Monaten auf Wochen reduziert

### Warum MCP wichtig ist

Vor MCP: Jedes KI-Tool brauchte eigene Integrationen. Ein Claude-Plugin für Slack. Ein GPT-Plugin für Jira. Ein Gemini-Plugin für GitHub. Dreimal derselbe Code, drei verschiedene Formate.

Mit MCP: Ein MCP-Server für Slack. Funktioniert mit Claude, mit GPT, mit Gemini, mit jeder MCP-fähigen Anwendung. Einmal bauen, überall nutzen. Wie USB-C – ein Standard für alle Geräte.

### MCP-Architektur

Drei Rollen:

- **MCP Host:** Die Anwendung, die den Agenten ausführt (Claude Code, Cursor, deine App)
- **MCP Client:** Die SDK-Schicht, die die Kommunikation handhabt
- **MCP Server:** Dein Code, der Tools, Resources und Prompts exponiert

MCP-Server können **State halten** (anders als einfaches Function Calling), bieten **dynamische Tool-Discovery** (der Agent entdeckt automatisch verfügbare Tools) und exponieren nicht nur Tools, sondern auch **Resources** (Daten) und **Prompts** (Templates).

## A2A: Agent-zu-Agent-Kommunikation

MCP verbindet Agenten mit Tools. Aber was, wenn Agenten miteinander kommunizieren müssen?

Das **Agent-to-Agent Protocol** (A2A), im April 2025 von Google mit über 50 Partnern gelauncht (Atlassian, Salesforce, PayPal, SAP, ServiceNow, LangChain, Accenture, McKinsey, Deloitte), ist der nächste Schritt: Ein Standard für die Kommunikation zwischen Agenten verschiedener Hersteller. Agenten entdecken sich gegenseitig über "Agent Cards" und tauschen über einen sicheren Kanal Informationen aus.

### MCP vs. A2A

| | MCP | A2A |
|---|---|---|
| Verbindet | Agent ↔ Tool | Agent ↔ Agent |
| Analogie | Stecker und Buchse | Telefon zu Telefon |
| Fokus | Tool-Nutzung | Koordination und Delegation |
| Status | Produktionsreif | Frühe Phase |

**Praxis-Empfehlung:** Starte mit einem Agent + MCP-Tools. Multi-Agent-Koordination über A2A ist der nächste Schritt – aber für die meisten Anwendungsfälle (Stand 2026) reicht ein gut konfigurierter einzelner Agent.

## Agent-Frameworks

Wenn du Agent-Systeme bauen willst, brauchst du nicht bei Null anfangen. Frameworks nehmen dir die Basisarbeit ab:

### LangGraph

Graph-basierte Agent-Orchestrierung von LangChain. Stärken: Komplexe Workflows mit Schleifen und parallelen Branches, Checkpointing (bei Fehler in Schritt 7/10 ab Schritt 7 fortsetzen), Human-in-the-Loop Gates, LangSmith für Observability.

**Ideal für:** Enterprise-Anwendungen mit komplexen, mehrstufigen Workflows.

### CrewAI

Rollen-basierte Agenten mit Visual Editor. Du definierst "Crew Members" mit spezifischen Rollen und Fähigkeiten, die zusammenarbeiten. Seit März 2026 mit nativem MCP- und A2A-Support.

**Ideal für:** Schnelles Prototyping, wenn du in der Team-Metapher denkst ("Ein Researcher, ein Writer, ein Editor").

### OpenAI Agents SDK

Open-Source, unterstützt Handoffs zwischen Agenten, MCP-Support, funktioniert mit beliebigen Chat-Completion-APIs (nicht nur OpenAI).

**Ideal für:** Moderate Komplexität (3-5 Agenten), wenn du im OpenAI-Ökosystem bist.

### Wann kein Framework

Für einfache Workflows (1-2 Tools, lineare Abfolge): Kein Framework nötig. Direkte API-Calls sind einfacher, transparenter und wartbarer. Frameworks lohnen sich erst ab 3+ Agenten oder komplexen Abläufen mit Verzweigungen und Schleifen.

## Das Agent-Ökosystem der Zukunft

Die Vision: Ein Ökosystem, in dem Agenten verschiedener Anbieter nahtlos zusammenarbeiten. Dein persönlicher Agent delegiert an spezialisierte Agenten – einen für Reisebuchung, einen für Rechtsrecherche, einen für Code-Entwicklung – und koordiniert die Ergebnisse.

Dafür braucht es:
- **Interoperabilität** (MCP + A2A lösen das technisch)
- **Vertrauen** (Wie verifiziert Agent A, dass Agent B vertrauenswürdig ist?)
- **Abrechnung** (Wer zahlt, wenn Agent B für Agent A arbeitet?)
- **Haftung** (Wer ist verantwortlich, wenn etwas schiefgeht?)

Die technischen Probleme werden gelöst. Die sozialen und rechtlichen Fragen werden länger dauern.

## MCP-Server in der Praxis

Was kannst du heute schon mit MCP-Servern machen? Die Auswahl wächst rasant:

| MCP-Server | Was er tut |
|-----------|-----------|
| **Filesystem** | Dateien lesen/schreiben in definierten Verzeichnissen |
| **GitHub** | Issues, PRs, Repos verwalten |
| **Slack** | Nachrichten senden, Kanäle durchsuchen |
| **PostgreSQL/SQLite** | Datenbanken abfragen |
| **Google Drive** | Dokumente suchen und lesen |
| **Jira** | Tickets erstellen, Status aktualisieren |
| **Brave Search** | Web-Recherche |
| **Puppeteer** | Webseiten steuern und Screenshots machen |

Einen eigenen MCP-Server zu schreiben dauert mit dem Python-SDK (FastMCP) wenige Stunden. Die Einstiegshürde ist bewusst niedrig – Anthropic will ein Ökosystem, nicht ein Monopol.

**Die Empfehlung:** Starte mit 2-3 MCP-Servern, die deine häufigsten Datenquellen anbinden. Filesystem + Datenbank + ein Projektmanagement-Tool decken die meisten Anwendungsfälle ab.

---

## Übungen

### Übung 1: MCP-Server entdecken
Recherchiere 5 verfügbare MCP-Server, die für deine Arbeit nützlich wären. Welche Tools würdest du deinem Agenten geben?

### Übung 2: Agent-Architektur entwerfen
Zeichne eine Architektur für ein Agent-System in deinem Bereich. Welche Agenten, welche Tools, welche Datenquellen?

### Übung 3: Framework-Vergleich
Wenn du technisch bist: Baue denselben einfachen Agent einmal mit LangGraph und einmal ohne Framework. Vergleiche Aufwand und Ergebnis.

### Übung 4: Zukunftsszenario
Beschreibe ein Szenario, in dem 5 spezialisierte Agenten für dich zusammenarbeiten. Was würde sich in deinem Arbeitsalltag ändern?
