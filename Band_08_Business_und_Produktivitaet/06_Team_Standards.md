# Kapitel 6: Team-Standards für Prompting – KI als Teamfähigkeit

Wenn nur du KI nutzt, sparst du Zeit. Wenn dein ganzes Team KI nutzt – mit Standards – multipliziert sich der Effekt. Aber ohne Standards wird es chaotisch: Jeder promptet anders, die Ergebnisqualität schwankt, und niemand lernt von den anderen.

## Warum Team-Standards?

Drei Probleme ohne Standards:

1. **Qualitätsschwankungen:** Der eine Kollege bekommt brillante Ergebnisse, der andere Müll – weil er den Prompt anders formuliert
2. **Wissensinseln:** Jeder entwickelt eigene Tricks, aber niemand teilt sie
3. **Datenschutz-Risiken:** Jemand kopiert Kundendaten in ChatGPT, ohne nachzudenken

## Der Prompt-Style-Guide

Wie ein Code-Style-Guide für Entwickler – nur für Prompts.

### Inhalt eines Prompt-Style-Guides

**1. Erlaubte Tools:** Welche KI-Tools darf das Team nutzen? (Welche sind für sensible Daten zugelassen, welche nur für allgemeine Aufgaben?)

**2. Datenschutz-Regeln:**
- Welche Daten dürfen in KI-Tools eingegeben werden?
- Welche NIEMALS? (Kundendaten, Personaldaten, Finanzdaten, Passwörter)
- Gibt es freigegebene Enterprise-Versionen?

**3. Prompt-Struktur:** Einheitliches Format für alle Team-Prompts:

```
ROLLE: [Wer soll die KI sein?]
AUFGABE: [Was soll sie tun?]
KONTEXT: [Hintergrund-Informationen]
FORMAT: [Wie soll das Ergebnis aussehen?]
EINSCHRÄNKUNGEN: [Was soll sie NICHT tun?]
```

**4. Qualitätsregeln:**
- Jedes KI-Ergebnis wird von einem Menschen geprüft
- Zahlen und Fakten werden verifiziert
- KI-generierte Texte werden vor dem Versand personalisiert
- Bei externen Texten: KI-Nutzung kennzeichnen (wenn verlangt)

**5. Do's und Don'ts:**

| Do | Don't |
|---|---|
| Kontext geben | "Schreib mir was über X" |
| Ergebnis prüfen | Blind kopieren |
| Templates teilen | Jeder für sich |
| Feedback an KI geben | Beim ersten Ergebnis aufhören |
| Sensible Daten anonymisieren | Echtdaten einfügen |

## Die Prompt-Bibliothek

Eine zentrale Sammlung getesteter Prompt-Templates für wiederkehrende Aufgaben.

### Aufbau der Bibliothek

Für jedes Template:

- **Name:** Eindeutig, beschreibend (z.B. "Kunden-Follow-up nach Angebot")
- **Kategorie:** E-Mail / Bericht / Planung / Analyse / Kreativ
- **Wann nutzen:** In welcher Situation?
- **Platzhalter:** Was muss eingefügt werden?
- **Beispiel-Input:** Ein konkretes Beispiel
- **Beispiel-Output:** Was kommt raus?
- **Getestet von:** Wer hat es getestet und für gut befunden?
- **Letztes Update:** Wann zuletzt geprüft?

### Wo speichern?

- **Notion-Datenbank** – Filterbar, durchsuchbar, Tags
- **Google Sheets** – Einfach, kollaborativ, niedrige Einstiegshürde
- **Confluence/Wiki** – Für größere Teams mit bestehender Doku-Infrastruktur
- **Dedizierte Tools** – PromptLayer, Promptbase, eigene Lösungen

### Bibliothek aktuell halten

Templates veralten. Modelle werden besser, Workflows ändern sich. Einmal pro Quartal: Review aller Templates. Welche funktionieren noch? Welche brauchen Updates? Welche sind überflüssig?

## KI-Onboarding für neue Mitarbeiter

Neue Teammitglieder brauchen KI-Onboarding – genauso wie Tool-Onboarding.

### Onboarding-Plan für KI

**Tag 1:** KI-Grundlagen (Welche Tools nutzen wir? Was darf rein, was nicht?)
**Woche 1:** Prompt-Bibliothek zeigen, 3-5 Templates ausprobieren
**Woche 2:** Eigene Workflows identifizieren und erste Templates anpassen
**Monat 1:** Feedback-Runde – was funktioniert, was nicht?

### KI-Champion im Team

Bestimme eine Person als KI-Champion. Sie ist verantwortlich für:
- Prompt-Bibliothek pflegen
- Neue Techniken evaluieren und teilen
- KI-Office-Hours (30 Min pro Woche, Fragen beantworten)
- Datenschutz-Compliance sicherstellen

## Prompt-Reviews

Wie Code-Reviews – nur für Prompts:

*"Hier ist ein Prompt-Template, das mein Kollege erstellt hat: [Prompt]. Bewerte: (1) Ist die Aufgabe klar? (2) Sind genug Kontext-Informationen vorhanden? (3) Ist das Output-Format spezifiziert? (4) Gibt es Datenschutz-Bedenken? (5) Ist es wiederverwendbar? Verbesserungsvorschläge?"*

## Messbare Ergebnisse

### KI-ROI messen

Einfacher als du denkst:

1. **Zeitersparnis pro Aufgabe:** Manuell vs. KI-gestützt messen
2. **Qualität:** Sind die Ergebnisse besser, gleich oder schlechter?
3. **Adoption:** Wie viele Teammitglieder nutzen die Templates regelmäßig?
4. **Kostenersparnis:** Zeitersparnis × Stundensatz = €€€

### Beispielrechnung

5 Teammitglieder × 3 Stunden/Woche Zeitersparnis × 50€/Stunde × 48 Wochen = **36.000€/Jahr**

Das ist konservativ gerechnet. Und die Qualitätsverbesserung ist da noch nicht eingepreist.

---

## Übungen

### Übung 1: Prompt-Style-Guide erstellen
Erstelle einen Prompt-Style-Guide für dein Team. Definiere Datenschutz-Regeln, Prompt-Struktur und Do's/Don'ts.

### Übung 2: Prompt-Bibliothek starten
Erstelle die ersten 5 Templates für die häufigsten Aufgaben deines Teams. Dokumentiere sie vollständig.

### Übung 3: KI-Onboarding
Erstelle einen KI-Onboarding-Plan für neue Mitarbeiter in deinem Team.

### Übung 4: ROI berechnen
Miss die Zeitersparnis für 3 Aufgaben (manuell vs. KI). Rechne auf das Jahr hoch.
