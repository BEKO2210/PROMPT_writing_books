# Kapitel 2: Autonome Agenten in der Praxis – Was heute schon funktioniert

Kapitel 1 war die Theorie. Jetzt die Praxis: Welche Agenten gibt es 2026, was können sie, und wie nutzt du sie?

## Coding-Agenten: Die Vorreiter

Coding war der erste Bereich, in dem Agenten wirklich funktioniert haben. Der Grund: Code ist testbar. Ein Agent kann Code schreiben, Tests laufen lassen, sehen ob sie bestehen, und wenn nicht, den Code fixen. Die Feedback-Schleife ist klar und automatisierbar.

### Claude Code

Anthropics Terminal-nativer Coding-Agent. Arbeitet direkt in deinem Git-Repository, versteht den Kontext deiner Codebasis (bis zu 1M Tokens), kann Dateien lesen und schreiben, Tests ausführen, Git-Operationen durchführen und über MCP-Server auf externe Tools zugreifen.

**Was ihn besonders macht:** Tiefe Integration ins Entwickler-Ökosystem. Kein IDE-Plugin, sondern ein eigenständiges Tool, das im Terminal lebt – da, wo Entwickler arbeiten. Claude Code erreichte 1 Milliarde Dollar Jahresumsatz (ARR) schneller als ChatGPT und steht im März 2026 bei **2,5 Milliarden Dollar ARR** – mehr als die Hälfte von Anthropics Enterprise-Umsatz.

Seit Februar 2026: **Agent Teams** – Multi-Agent-Koordination. Ein Lead-Agent spawnt Teammates, jeder mit eigener Session und eigenem Kontextfenster. Kommunikation über JSON-Inbox-Dateien. Reduziert die Arbeitszeit um 3-5x bei parallelisierbarer Arbeit.

In Umfragen 2026 wird Claude Code als "most loved" AI Coding Tool von 46% der Befragten genannt.

### Cursor

Der IDE-native Ansatz. Cursor ist ein Fork von VS Code mit eingebauter KI. Marktführer im Bereich AI-IDEs mit über 360.000 zahlenden Nutzern und über 500 Mio. Dollar Jahresumsatz (Stand 2026). Über 90% der Entwickler bei Salesforce nutzen Cursor.

**Cloud Agents (Februar 2026):** Völlig autonome Agenten auf isolierten Linux-VMs. Schreiben Code, testen ihn, nehmen Video-Demos auf und liefern Merge-ready Pull Requests. 30% von Cursors eigenen gemergten PRs werden von diesen Agenten erstellt. BugBot findet Bugs in PRs und spawnt automatisch Cloud-Agenten zur Reparatur – über 35% der Fixes werden ohne Änderung gemergt.

### GitHub Copilot

15 Millionen Entwickler nutzen Copilot. Der Agent Mode ermöglicht mehrstufige Aufgaben: nicht nur Code-Vervollständigung, sondern Feature-Implementierung über mehrere Dateien. Enterprise-Features wie Audit-Trails und Compliance (SOC 2) machen es für große Unternehmen attraktiv.

### Devin

Der "KI-Software-Engineer" von Cognition. Kann Stunden bis Tage autonom an Aufgaben arbeiten – deutlich längere Autonomie als die meisten Konkurrenten. Setzt eigene Entwicklungsumgebungen auf, navigiert Webseiten, debuggt.

**Die Realität:** Beeindruckend für klar definierte, abgegrenzte Aufgaben. Preis von 500$/Monat auf 20$/Monat + 2,25$ pro "Agent Compute Unit" gesenkt – deutlich zugänglicher. Bei ambigen oder kreativen Aufgaben noch unzuverlässig. Sicherheitsforscher fanden Schwachstellen (siehe Band 9).

### Aider

Open-Source, terminal-basiert, Git-nativ. Funktioniert mit jedem LLM (Claude, GPT, lokale Modelle). Bring-Your-Own-Model-Ansatz. Typische Kosten: 5-30$/Monat. Ideal für Entwickler, die maximale Kontrolle und Transparenz wollen.

### Die Benchmark-Realität

Wie gut sind Coding-Agenten wirklich? SWE-bench (ein Benchmark für reale GitHub-Issues) gibt eine Orientierung:
- Claude Opus 4.6: 80,8% – kann 4 von 5 echten GitHub-Issues lösen
- GPT-5.2 (xhigh): 89% auf LiveCodeBench
- Claude Sonnet 4.5: 77-82% – das beste Preis-Leistungsverhältnis

Aber Benchmarks sind nicht die Realität. In der Praxis hängt die Qualität vom Kontext ab: Wie gut ist die Codebasis dokumentiert? Wie klar ist die Aufgabe? Wie komplex sind die Abhängigkeiten? Ein Agent, der auf einem sauberen Open-Source-Projekt brilliert, kann an einer verwinkelten Enterprise-Codebasis scheitern.

## Die Empfehlung für 2026

Kein einzelnes Tool ist das Beste für alles. Die Praxis-Empfehlung:

- **Cursor** oder **Windsurf** als tägliche IDE mit KI-Integration
- **Claude Code** für schwierige Probleme, große Refactorings und Automatisierung
- **GitHub Copilot** als günstiges Safety-Net für Completions
- **Aider** wenn du Open Source und volle Kontrolle bevorzugst

## Business-Agenten

### E-Mail-Agenten

Agenten, die deinen Posteingang managen: E-Mails klassifizieren, priorisieren, Entwürfe für Antworten erstellen, Follow-ups erinnern. Microsoft Copilot in Outlook und Google Gemini in Gmail sind die bekanntesten Vertreter.

### Recherche-Agenten

Perplexity AI, Claude mit Web-Search, ChatGPT mit Browsing – Agenten, die Informationen aus dem Web zusammentragen, bewerten und zusammenfassen. Die Herausforderung bleibt Quellenqualität.

### Workflow-Agenten

Tools wie Zapier AI, Make (ehemals Integromat) und n8n integrieren KI in bestehende Workflows: Wenn eine E-Mail eingeht → KI klassifiziert sie → leitet sie an die richtige Person → erstellt ein Ticket → sendet eine Bestätigung. Ohne Code.

## Computer-Use-Agenten

Die neueste Entwicklung: Agenten, die einen Computer bedienen können – wie ein Mensch. Sie sehen den Bildschirm (Screenshots), klicken auf Buttons, tippen Text, navigieren durch Webseiten und Anwendungen.

**Anthropic Computer Use:** Claude kann einen Desktop steuern. Screenshots machen, Mausbewegungen und Klicks ausführen, Text eingeben. Funktional für einfache bis mittlere Workflows.

**OpenAI Operator/ChatGPT Agent:** Gestartet Januar 2025, im Juli 2025 in ChatGPT integriert. Erreichte 38,1% auf OSWorld, 58,1% auf WebArena und 87% auf WebVoyager. Kann Reisen buchen, Restaurants reservieren, online einkaufen – automatisch.

**Warum das wichtig ist:** Nicht jede Software hat eine API. Computer Use ermöglicht Agenten, mit *jeder* Software zu arbeiten – auch mit Legacy-Systemen, die nie für KI-Integration gedacht waren. Das ist der letzte Baustein für universelle Automatisierung.

## Die Grenzen (Stand 2026)

Agenten sind beeindruckend, aber nicht allwissend:

1. **Lange Aufgaben:** Je länger ein Agent autonom arbeitet, desto wahrscheinlicher akkumulieren sich kleine Fehler zu großen Problemen.
2. **Ambiguität:** Agenten brauchen klare Ziele. "Mach das irgendwie besser" funktioniert nicht.
3. **Unbekanntes Terrain:** Agenten sind gut in Aufgaben, die ähnlich wie ihre Trainingsdaten sind. Bei völlig neuen Problemen stolpern sie.
4. **Kosten:** Ein Agent, der 100 LLM-Calls macht, kostet 100x so viel wie ein einzelner Call. Token-Budgets sind wichtig.
5. **Sicherheit:** Mehr Autonomie = mehr Angriffsfläche (Band 9). Jeder neue Tool-Zugang ist ein potenzielles Sicherheitsrisiko.

---

## Übungen

### Übung 1: Coding-Agent testen
Probiere einen Coding-Agenten (Claude Code, Cursor Agent, Copilot Agent Mode) an einem echten Projekt. Wie viel kannst du delegieren?

### Übung 2: Workflow automatisieren
Nimm einen wiederkehrenden Workflow und automatisiere ihn mit einem No-Code-Tool (Zapier AI, Make). Wie lange brauchst du für das Setup vs. die manuelle Ausführung?

### Übung 3: Computer Use beobachten
Teste Computer Use (wenn verfügbar) an einer einfachen Web-Aufgabe. Wo funktioniert es gut? Wo scheitert es?

### Übung 4: Agent-Kosten berechnen
Lass einen Agenten eine mittlere Aufgabe ausführen. Zähle die LLM-Calls und berechne die Kosten. Lohnt es sich vs. manuelle Arbeit?
