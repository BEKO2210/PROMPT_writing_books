# Vorwort

Sechs Bände lang warst du Endnutzer. Du hast in Chat-Fenster getippt, Ergebnisse gelesen, iteriert. Gut so – das ist die Grundlage.

Aber jetzt bist du bereit für den nächsten Schritt: KI nicht nur nutzen, sondern einbauen. In deine Software. In deine Workflows. In deine Produkte.

## Was diesen Band anders macht

In den Bänden 1 bis 6 ging es darum, wie du mit KI *kommunizierst*. In Band 7 geht es darum, wie du KI *programmierst*.

Das ist ein fundamentaler Unterschied:

- Du schreibst nicht mehr einzelne Prompts – du baust Systeme, die tausende Prompts automatisch generieren und verarbeiten.
- Du copy-pastest keine Antworten mehr – du verarbeitest strukturierte API-Responses in deinem Code.
- Du wartest nicht mehr auf Ergebnisse – du baust Pipelines, die asynchron, parallel und skalierbar arbeiten.
- Du promptest nicht mehr allein – du baust Agenten, die Tools nutzen, Entscheidungen treffen und selbstständig handeln.

Willkommen in der Welt des programmatischen Promptings.

## Was du brauchst

Technische Voraussetzungen für diesen Band:

- **Grundlegende Programmierkenntnisse** – Python oder JavaScript. Du musst kein Senior Developer sein, aber du solltest wissen, was eine Funktion, eine Variable und ein API-Call ist.
- **Ein Terminal/Kommandozeile** – Du wirst Befehle ausführen.
- **API-Zugang** – Mindestens einen API-Key von Anthropic (Claude), OpenAI oder Google (Gemini). Kostenlose Tiers reichen für die Übungen.
- **Eine Entwicklungsumgebung** – VS Code, Cursor, oder ein beliebiger Editor.
- **Neugier** – Weil die Landschaft sich schnell bewegt und du experimentieren musst.

Wenn du nicht programmierst: Lies trotzdem die Kapitel über Code-Generierung (Kapitel 1-2) und das Konzept-Kapitel über Context Engineering (Kapitel 9). Der Rest ist für Entwickler.

## Was dich erwartet

**Code-Generierung** – Nicht "Schreib mir eine Funktion", sondern: Wie du KI für Architekturentscheidungen, Code-Reviews, Refactoring und Test-Generierung nutzt. Von der Einzelfunktion zum Gesamtsystem.

**Agentic Coding Tools** – Cursor, GitHub Copilot, Claude Code, Windsurf, Cline, Aider. Was können sie? Wie unterscheiden sie sich? Und: Wie promptest du innerhalb dieser Tools optimal?

**Die LLM-APIs** – Anthropic, OpenAI, Google, Open Source. Preise, Modelle, Features. Structured Output, Vision, Streaming, Caching. Alles, was du als Entwickler wissen musst.

**Programmatisches Prompting** – Prompt-Templates, Variablen, Antwortverarbeitung, Fehlerbehandlung, Retry-Logik. Mit echtem Code in Python und TypeScript.

**RAG (Retrieval Augmented Generation)** – Deine eigenen Daten in die KI bringen. Embeddings, Vektor-Datenbanken, Chunking-Strategien. Das Fundament jeder ernsthaften KI-Anwendung.

**Tool Use und Function Calling** – KI, die nicht nur Text generiert, sondern Funktionen aufruft: Datenbanken abfragen, APIs ansprechen, Dateien bearbeiten. Die Brücke zwischen Text und Aktion.

**Agentische Systeme** – KI-Agenten, die planen, handeln und iterieren. MCP (Model Context Protocol), Multi-Step-Agents, Orchestrierung. Der aktuellste und spannendste Bereich.

**Fine-Tuning vs. Prompting** – Wann reicht gutes Prompting? Wann lohnt sich Fine-Tuning? Die Entscheidungsmatrix mit konkreten Kosten-Nutzen-Analysen.

**Context Engineering** – Der Nachfolger von Prompt Engineering. Wie du den gesamten Kontext eines LLM-Aufrufs designst – nicht nur den Prompt, sondern System-Prompts, Tool-Definitionen, Retrieval-Ergebnisse, Konversationshistorie und Caching.

## Die KI-Entwickler-Landschaft 2026

Bevor wir einsteigen, ein Überblick über den Stand der Dinge:

| Bereich | Stand 2024 | Stand 2026 |
|---|---|---|
| Code-Assistenten | GitHub Copilot dominiert | Dutzende Tools, agentic by default |
| APIs | Text rein, Text raus | Multimodal, Tool Use, Structured Output |
| RAG | Experimentell, komplex | Standard-Pattern, viele Frameworks |
| Agenten | Demo-Stage, fragil | Produktionsreif für definierte Workflows |
| Fine-Tuning | Teuer, komplex | Günstiger, aber Prompting oft ausreichend |
| Context Engineering | Buzzword | Etablierte Disziplin |
| Open Source | Llama 2, Mixtral | Llama 4, DeepSeek-V3, Qwen 3 |

Die Entwicklung in den letzten zwei Jahren war exponentiell. Was 2024 als Research-Paper existierte, ist 2026 ein npm-Paket. Was 2024 ein Startup war, ist 2026 ein Feature von VS Code.

Dieses Buch gibt dir das Wissen, um in dieser Landschaft nicht nur mitzuschwimmen, sondern zu navigieren.

Los geht's. Wir bauen.

*Belkis Aslani, März 2026*
