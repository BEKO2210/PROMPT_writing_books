# Kapitel 9: Context Engineering – Die Evolution des Prompt Engineering

Prompt Engineering war Band 1. Context Engineering ist Band 7.

Der Unterschied: Prompt Engineering optimiert den Text, den du an ein LLM schickst. Context Engineering optimiert *alles*, was das Modell sieht – System-Prompt, Tools, Retrieval-Ergebnisse, Konversationshistorie, Caching, und wie all diese Teile zusammenspielen.

Andrej Karpathy brachte es auf den Punkt: *"Das LLM ist eine CPU, das Context Window ist RAM, und dein Job ist es, das Betriebssystem zu sein – den Arbeitsspeicher mit genau dem richtigen Code und den richtigen Daten für jede Aufgabe zu laden."*

## Was ist Context Engineering?

Jeder API-Call an ein LLM hat fünf Kontextschichten:

1. **System-Prompt** – Rolle, Verhalten, Regeln, Output-Format
2. **Tool-Definitionen** – Verfügbare Tools mit Beschreibungen
3. **Retrieval-Kontext (RAG)** – Relevante Dokumente und Suchergebnisse
4. **Konversationshistorie** – Bisherige Messages und Tool-Ergebnisse
5. **Aktuelle Nachricht** – Der User-Prompt

Context Engineering optimiert jede dieser Schichten – und ihr Zusammenspiel.

## Schicht 1: System-Prompt Engineering

### Die Anatomie eines Produktions-System-Prompts

Ein produktionsreifer System-Prompt hat fünf Abschnitte:

- **Rolle:** Wer bist du, für welches Unternehmen, welche Expertise
- **Verhalten:** Sprache, Ton, Stil, Verbote
- **Fähigkeiten:** Welche Tools, was kannst du, was NICHT
- **Dynamischer Kontext:** Datum, User-Info, aktuelle Promotions, bekannte Probleme (per Variable eingefügt)
- **Output-Format:** Länge, Struktur, Formatierung

### System-Prompt-Patterns

**Identity + Constraints:** Wer bist du → Was kannst du → Was NICHT.

**Dynamic Context:** Kontext, der sich bei jedem Call ändert – Datum, User-Name, Plan, offene Tickets. Per f-String oder Template eingefügt.

**Graduated Response:** Für einfache Fragen kurz antworten, für komplexe strukturiert, für unbekannte weiterleiten.

## Schicht 2: Tool-Kontext-Optimierung

Die Beschreibungen deiner Tools sind Teil des Kontexts – und sie beeinflussen stark, wie gut das Modell die Tools nutzt.

- **Schlecht:** `"Sucht Dinge"`
- **Gut:** `"Durchsucht die interne Wissensdatenbank von TechCorp. Enthält: Produktdokumentation, FAQ, Troubleshooting. Enthält NICHT: Kundendaten, Finanzdaten. Nutze dieses Tool BEVOR du Produktfragen beantwortest."`

Die Investition in gute Tool-Beschreibungen zahlt sich mehr aus als fast jede andere Optimierung.

## Schicht 3: RAG-Kontext-Optimierung

### Kontext-Reihenfolge

LLMs haben ein "Lost in the Middle"-Problem: Accuracy ist am höchsten, wenn relevante Information am **Anfang** oder **Ende** des Kontexts steht. Über 30% Accuracy-Verlust für Informationen in der Mitte. Strategie: Relevantestes an den Anfang UND ans Ende.

### Kontext-Kompression

Zu viel Kontext ist schlechter als zu wenig. Forschung zeigt, dass LLM-Reasoning ab ~3.000 Tokens degradiert. Sweet Spot für Prompts: 150-300 Wörter. Bei langen Dokumenten: Vorher mit einem schnellen Modell (Haiku) zusammenfassen.

## Schicht 4: Konversationshistorie managen

Lange Konversationen sprengen das Kontext-Fenster. Zwei Strategien:

**Trimmen:** Älteste Messages entfernen, System-Prompt behalten. Einfach, aber Kontext geht verloren.

**Zusammenfassen:** Alte Messages durch eine Zusammenfassung ersetzen. Behält den Kontext, braucht einen Extra-LLM-Call.

Die beste Lösung ist oft eine Kombination: System-Prompt + Zusammenfassung der älteren History + die letzten 4-6 Messages vollständig.

Anthropics **Compaction API** (beta) macht das serverseitig – du gibst ihr die volle History, sie gibt dir eine komprimierte Version zurück.

## Schicht 5: Prompt Caching

Anthropics Prompt Caching spart bis zu 90% auf wiederholt genutzte Kontexte. Alles, was sich zwischen Calls nicht ändert (System-Prompt, Tool-Definitionen, Konversations-Prefix), markierst du mit `cache_control`. Beim ersten Call wird gecacht, alle weiteren Calls lesen aus dem Cache.

### Was cachen?

| Kontext-Teil | Cachen? | Warum |
|---|---|---|
| System-Prompt | Immer | Ändert sich selten |
| Tool-Definitionen | Immer | Ändert sich nie |
| RAG-Dokumente | Manchmal | Nur bei wiederholt gleichen Docs |
| Konversationshistorie | Ja | Prefix bleibt gleich |
| User-Prompt | Nein | Ändert sich bei jedem Call |

## Context Engineering Checkliste

Für jeden produktionsreifen LLM-Call prüfe:

**System-Prompt:** Rolle klar? Fähigkeiten und Grenzen explizit? Dynamischer Kontext eingefügt? Output-Format spezifiziert? Gecacht?

**Tools:** Beschreibungen detailliert? Beispiele enthalten? Negative Beispiele ("NICHT für...")? Gecacht?

**RAG:** Relevante Chunks (nicht zu viele)? Reranking? Quellen referenzierbar? Reihenfolge optimiert?

**History:** Getrimmt oder zusammengefasst? Token-Budget eingehalten? Prefix gecacht?

**Prompt:** Klar und eindeutig? Alle nötigen Infos? Nicht zu lang?

## Von Prompt Engineering zu Context Engineering

| Prompt Engineering | Context Engineering |
|---|---|
| "Wie schreibe ich den Prompt?" | "Wie designe ich den gesamten Kontext?" |
| Einzelner Text-Input | System + Tools + RAG + History + Prompt |
| Statisch | Dynamisch (pro User, pro Anfrage) |
| Trial and Error | Systematisch, messbar, versioniert |
| Ein Skill | Eine Disziplin |

Performance-Gewinne kommen zunehmend nicht von besseren Modellen, sondern von smarterem Kontext. Context Engineering ist die Zukunft. Wer nur Prompts schreibt, schöpft 20% des Potenzials aus. Wer den gesamten Kontext designt, schöpft 100% aus.

---

## Übungen

### Übung 1: System-Prompt Audit
Nimm einen bestehenden System-Prompt und prüfe ihn gegen die Checkliste. Was fehlt?

### Übung 2: Caching implementieren
Implementiere Prompt Caching für einen Anwendungsfall mit langem System-Prompt. Miss den Kostenunterschied.

### Übung 3: Konversationsmanager
Baue einen ConversationManager mit Zusammenfassungs-Strategie. Behält das Modell den Kontext?

### Übung 4: Full Context Design
Designe den kompletten Kontext für einen produktionsreifen Chatbot: System-Prompt, Tools, RAG, History-Management, Caching.
