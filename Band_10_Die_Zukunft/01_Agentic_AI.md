# Kapitel 1: Agentic AI – Von Chatbots zu Agenten, die handeln

Die erste Generation von KI-Anwendungen war reaktiv: Du fragst, KI antwortet. Eine Eingabe, eine Ausgabe. Fertig. Das war 2023.

Die zweite Generation ist proaktiv: KI plant, handelt, beobachtet, passt an und iteriert – über Minuten, Stunden oder Tage. Du gibst ein Ziel, nicht eine Frage. Und die KI findet den Weg zum Ziel selbstständig.

Das ist Agentic AI. Und es verändert alles.

## Was ist ein Agent?

In Band 7 hast du den ReAct-Loop kennengelernt: Planen → Handeln → Beobachten → Bewerten → Wiederholen. Ein Agent ist ein LLM mit Zugang zu Tools und einem Ziel, das diesen Loop autonom durchläuft.

Der entscheidende Unterschied zum Chatbot:

| | Chatbot | Agent |
|---|---|---|
| Interaktion | Frage → Antwort | Ziel → Ergebnis |
| Schritte | 1 | 10-1.000+ |
| Autonomie | Keine | Hoch |
| Tools | Keine oder wenige | Viele, selbst gewählt |
| Dauer | Sekunden | Minuten bis Stunden |
| Fehlerbehandlung | Keine | Retry, alternative Pfade |

## Warum 2026 das Jahr der Agenten ist

Drei Entwicklungen kamen zusammen:

**1. Bessere Modelle:** Claude Opus 4.6, GPT-5.2, Gemini 3 Pro – die Modelle von 2026 machen weniger Fehler, folgen Anweisungen besser und können komplexere Pläne ausführen. Die Halluzinationsrate bei Frontier-Modellen liegt unter 2% für Standard-Tasks.

**2. Infrastruktur:** MCP (Model Context Protocol) hat das Tool-Problem gelöst. Statt für jedes Tool eigene Integrationen zu schreiben, gibt es ein universelles Protokoll. 97 Millionen monatliche SDK-Downloads. Unterstützt von Anthropic, OpenAI, Google, Microsoft und Amazon.

**3. Kontextfenster:** 200K-1M Tokens bedeuten, dass Agenten genug "Arbeitsgedächtnis" haben, um komplexe, mehrstufige Aufgaben zu bewältigen, ohne den Faden zu verlieren.

## Agent-Typen

### Der Tool-Agent

Die einfachste Form. Ein LLM mit Zugang zu klar definierten Tools. Beispiel: Ein Kundenservice-Agent, der Bestellungen nachschlagen, Rückgaben einleiten und Tickets erstellen kann. Er entscheidet bei jeder Nutzeranfrage, welches Tool er braucht.

### Der Workflow-Agent

Führt mehrstufige Workflows aus. Beispiel: "Erstelle einen Monatsbericht" → Agent sammelt Daten aus 3 Quellen, analysiert sie, erstellt den Bericht, formatiert ihn, schickt ihn an die Stakeholder. 10+ Schritte, vollautomatisch.

### Der Coding-Agent

Der am weitesten fortgeschrittene Typ. Coding-Agenten wie Claude Code, Cursor, Devin und Codex können ganze Features implementieren: Code schreiben, Tests laufen lassen, Fehler fixen, Commits machen – über hunderte Dateien hinweg.

### Der Recherche-Agent

Durchsucht das Web, liest Dokumente, extrahiert Informationen, fasst zusammen und synthetisiert. Kann Stunden an Recherche in Minuten erledigen. Die Herausforderung: Quellenqualität und Halluzinationen (Band 9).

### Der Multi-Agent-Schwarm

Mehrere spezialisierte Agenten, die zusammenarbeiten. Ein Orchestrator-Agent teilt die Aufgabe auf, delegiert an Spezialisten (Recherche-Agent, Code-Agent, Review-Agent) und führt die Ergebnisse zusammen. Die Königsklasse der agentic Systeme.

## Wie du mit Agenten arbeitest

### Das Ziel definieren, nicht den Weg

Bei Chatbots sagst du: "Schreibe mir eine Funktion, die X tut."
Bei Agenten sagst du: "Implementiere Feature X. Schreibe Tests. Stelle sicher, dass alle bestehenden Tests bestehen."

Der Agent findet den Weg selbst. Deine Aufgabe ist, das Ziel klar zu definieren, die Erfolgskriterien zu nennen und die Grenzen zu setzen.

### Guardrails setzen

Aus Band 9 weißt du: Autonome Systeme brauchen Sicherheitsmechanismen. Für Agenten besonders wichtig:

- **Token-Budget:** Maximale Kosten pro Aufgabe
- **Schritt-Limit:** Maximale Anzahl Schritte (verhindert Endlosschleifen)
- **Erlaubte Aktionen:** Whitelist von Tools und Operationen
- **Human-in-the-Loop:** Pausiere bei kritischen Entscheidungen
- **Rollback-Fähigkeit:** Alles rückgängig machen können

### Ergebnisse prüfen

Agenten sind nicht perfekt. Sie können in Sackgassen laufen, falsche Annahmen treffen oder subtile Fehler einbauen. **Prüfe das Ergebnis, nicht nur ob es "fertig" ist.** Besonders bei Code: Nicht nur ob es kompiliert, sondern ob es korrekt ist.

## Die Zukunft der Agenten

### Kurzfristig (2026-2027)

- Agenten werden zum Standard-Tool für Entwickler
- Einfache Büro-Agenten (E-Mail, Kalender, Dokumentation) werden massentauglich
- Enterprise-Agenten für spezifische Workflows (HR, Finanzen, Legal)

### Mittelfristig (2027-2028)

- Multi-Agent-Systeme, die wie Teams arbeiten
- Agenten, die über Tage und Wochen an Projekten arbeiten
- Agent-zu-Agent-Kommunikation wird Standard (A2A-Protokoll)
- Agenten mit "Gedächtnis" über Projekte hinweg
- Persönliche Agenten, die deinen Kalender, deine E-Mails und deine Aufgaben kennen

### Langfristig (2028+)

- KI-Wissenschaftler, die eigenständig Hypothesen aufstellen, Experimente designen und Ergebnisse interpretieren
- Agenten, die Unternehmen gründen und betreiben – von der Marktanalyse über die Produktentwicklung bis zum Marketing
- Persönliche KI-Assistenten, die dein gesamtes digitales Leben kennen und managen

Ob alle diese Vorhersagen eintreten, weiß niemand. Aber die Richtung ist klar: Mehr Autonomie, mehr Fähigkeiten, mehr Integration.

## Wie du dich vorbereitest

Die wichtigste Fähigkeit im Zeitalter der Agenten ist nicht mehr "Wie schreibe ich einen guten Prompt?" sondern **"Wie definiere ich ein gutes Ziel?"**

Das klingt trivial. Ist es nicht. Ein gutes Ziel für einen Agenten hat:

- **Klare Erfolgskriterien:** Nicht "Mach es besser" sondern "Erhöhe die Test-Abdeckung auf 80%"
- **Definierte Grenzen:** Was darf der Agent tun, was nicht?
- **Messbare Ergebnisse:** Woran erkennst du, dass der Agent fertig ist?
- **Kontext:** Welche Informationen braucht der Agent, um das Ziel zu erreichen?

Das sind die Prompting-Prinzipien aus Band 1-3 – angewandt auf ein autonomes System statt auf eine einzelne Frage. Alles, was du gelernt hast, bleibt relevant. Es wird nur eine Abstraktionsebene höher.

---

## Übungen

### Übung 1: Agent vs. Chatbot
Nimm 3 Aufgaben, die du aktuell mit einem Chatbot erledigst. Welche davon wären als Agent besser? Warum?

### Übung 2: Ziel-Definition
Formuliere ein Ziel für einen hypothetischen Agent. Definiere Erfolgskriterien, Grenzen und Guardrails.

### Übung 3: Agenten beobachten
Nutze Claude Code oder ein ähnliches Tool im Agenten-Modus. Beobachte: Wie viele Schritte braucht der Agent? Wo macht er Fehler? Wo überrascht er dich?

### Übung 4: Multi-Agent-Szenario
Entwirf ein Multi-Agent-System für einen Workflow in deinem Unternehmen. Welche Spezialisten bräuchtest du?
