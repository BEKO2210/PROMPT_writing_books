# Kapitel 4: Context Engineering – Die Evolution des Prompt Engineering

In Band 7 hast du Context Engineering als Technik kennengelernt – wie du System-Prompts, Tools, RAG-Kontext, History und Caching optimierst. In Band 10 betrachten wir es als **Disziplin** – die Disziplin, die Prompt Engineering ablöst. Oder genauer: die es erweitert.

## Von Prompt Engineering zu Context Engineering

Andrej Karpathy (ehemals OpenAI, Tesla) brachte den Unterschied im Juni 2025 auf den Punkt:

*"Der Begriff 'Prompt Engineering' verharmlost, was wir eigentlich tun. Das LLM ist eine CPU, das Context Window ist RAM, und dein Job ist es, das Betriebssystem zu sein – den Arbeitsspeicher mit genau dem richtigen Code und den richtigen Daten für jede Aufgabe zu laden."*

**Prompt Engineering** fragt: Wie schreibe ich den Prompt?
**Context Engineering** fragt: Wie designe ich alles, was das Modell sieht?

| Prompt Engineering | Context Engineering |
|---|---|
| Ein Text | Ein System |
| Statisch | Dynamisch (ändert sich pro User, pro Anfrage) |
| Manuell | Automatisiert (Pipelines) |
| Trial and Error | Systematisch, messbar, versioniert |
| Ein Skill | Eine Disziplin |

## Die fünf Kontextschichten

Jeder LLM-Call hat fünf Schichten, die zusammen den Kontext bilden:

### 1. System-Prompt (Identität)

Wer ist das Modell? Was kann es? Was darf es nicht? Welcher Ton? Welches Format?

Der System-Prompt ist der stabilste Teil – er ändert sich selten. Deshalb ist er ideal zum Cachen (90% Ersparnis bei Anthropic).

**2026-Trend:** System-Prompts werden länger und komplexer. Produktionssysteme haben System-Prompts von 5.000-50.000 Tokens – mit dynamischen Teilen (aktuelles Datum, User-Infos, bekannte Probleme).

### 2. Tool-Definitionen (Fähigkeiten)

Welche Tools hat das Modell? Die Beschreibungen sind Teil des Kontexts und beeinflussen stark, wie gut das Modell die Tools nutzt.

**2026-Trend:** Dynamische Tool-Discovery über MCP. Der Agent entdeckt automatisch, welche Tools verfügbar sind, statt eine feste Liste zu haben.

### 3. Retrieval-Kontext (Wissen)

RAG-Chunks, Suchergebnisse, Dokumente. Das Wissen, das das Modell für diese spezifische Anfrage braucht.

**2026-Trend:** Hybrid Search (Vektor + Keyword) ist Pflicht. Reranking ist der höchste ROI-Upgrade. Contextual Retrieval (Kontext-Sätze vor jedem Chunk) verbessert die Ergebnisse um 20-50%.

### 4. Konversationshistorie (Gedächtnis)

Bisherige Messages, Tool-Ergebnisse, Zusammenfassungen alter Konversationen.

**2026-Trend:** Compaction APIs (Anthropic) und automatische History-Zusammenfassung. Statt die History zu kürzen, wird sie intelligent komprimiert – das Modell behält den Kontext, aber in weniger Tokens.

### 5. Aktuelle Nachricht (Aufgabe)

Der User-Prompt. Paradoxerweise der kleinste Teil des Kontexts – aber der, auf den wir uns in Band 1-6 konzentriert haben.

## Das "Lost in the Middle"-Problem

Forschung zeigt: LLMs haben eine U-förmige Aufmerksamkeitskurve. Informationen am **Anfang** und am **Ende** des Kontexts werden am besten verarbeitet. Informationen in der **Mitte** werden bis zu 30% häufiger übersehen.

**Konsequenz für Context Engineering:**
- Kritische Anweisungen an den Anfang (System-Prompt)
- Kritische Informationen ans Ende (direkt vor dem User-Prompt)
- Nie wichtige Dinge nur in der Mitte platzieren

## Context Pipelines

In Produktion wird der Kontext nicht manuell zusammengestellt. Er wird durch **Pipelines** automatisch aufgebaut:

1. **System-Prompt laden** (aus Konfiguration, mit dynamischen Variablen)
2. **Tools registrieren** (über MCP Discovery)
3. **Relevante Dokumente abrufen** (RAG-Pipeline: Suche → Reranking → Top-K)
4. **History komprimieren** (alte Messages zusammenfassen, Prefix cachen)
5. **User-Prompt einfügen**
6. **An LLM senden**

Diese Pipeline läuft bei jedem Request. Jede Schicht ist optimierbar, testbar und versionierbar.

## Prompt-Optimierung wird Teil von Context Engineering

Was in Band 1-6 "den Prompt verbessern" hieß, ist jetzt Teil eines größeren Systems. Du optimierst nicht mehr einzelne Prompts – du optimierst die gesamte Pipeline:

- Welche Chunks werden retrieved? (RAG-Qualität)
- Wie wird die History zusammengefasst? (Kontext-Effizienz)
- Welche Tools sind verfügbar? (Agent-Fähigkeiten)
- Wie teuer ist der Call? (Token-Budget)
- Wie schnell ist die Antwort? (Latenz)

## Was bedeutet das für dich?

Wenn du nur Chat-Prompts schreibst: Prompt Engineering reicht. Du brauchst kein Context Engineering für "Schreib mir eine E-Mail."

Wenn du KI-Systeme baust (Chatbots, Agenten, RAG-Pipelines): Context Engineering ist dein Job. Nicht "Wie schreibe ich den Prompt?" sondern "Wie designe ich den gesamten Kontext – dynamisch, effizient und zuverlässig?"

Die gute Nachricht: Alles, was du in Band 1-9 gelernt hast, ist die Grundlage. Context Engineering baut darauf auf – es macht es systematischer, automatisierter und skalierbarer.

## Die Zukunft von Context Engineering

Gartner definiert Context Engineering als eine der wichtigsten KI-Disziplinen für 2026-2027 und empfiehlt Unternehmen, einen "Context Engineering Lead" zu ernennen – eine Person, die für die Kuratierung und Governance von KI-Kontexten verantwortlich ist.

Die Disziplin hat sich klar geteilt:

**Casual Prompting:** Kann jeder, die Modelle werden besser im Verstehen von Absichten. Du tippst eine Frage, die KI versteht, was du meinst. Hier brauchst du kein Context Engineering – Band 1-3 reichen.

**Production Context Engineering:** Eine echte Engineering-Fähigkeit. Automatisierte Pipelines, die System-Prompts, Dialog-Historie, Echtzeit-Daten, Dokumente und externe Tools aggregieren, filtern und im Kontext-Fenster formatieren. Hier wird die Zukunft entschieden.

Forschung zeigt: Performance-Gewinne kommen zunehmend nicht von besseren Modellen, sondern von smarterem Kontext. Die Modelle sind bereits sehr gut. Der Kontext, den sie bekommen, ist oft der Flaschenhals.

**Prompts kurz halten:** Forschung zeigt, dass LLM-Reasoning ab ~3.000 Tokens degradiert. Der Sweet Spot für den eigentlichen Prompt: 150-300 Wörter. Der Rest des Kontextfensters gehört System-Prompt, Tools, RAG und History – nicht dem User-Prompt.

---

## Übungen

### Übung 1: Kontext-Audit
Nimm einen produktiven LLM-Call (Chatbot, Agent) und analysiere alle 5 Kontextschichten. Wo wird Kontext verschwendet? Wo fehlt er?

### Übung 2: Lost-in-the-Middle-Test
Platziere eine wichtige Information absichtlich in der Mitte eines langen Kontexts. Findet das Modell sie? Verschiebe sie an den Anfang oder das Ende. Ändert sich das Ergebnis?

### Übung 3: Pipeline skizzieren
Skizziere eine Context Pipeline für einen konkreten Use Case. Welche Datenquellen? Welche Optimierungen?

### Übung 4: Caching-Strategie
Identifiziere in einem bestehenden System die Teile, die gecacht werden könnten. Berechne die potenzielle Kostenersparnis.
