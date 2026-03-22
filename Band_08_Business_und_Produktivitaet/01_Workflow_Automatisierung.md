# Kapitel 1: Workflow-Automatisierung – KI als Fließband

Die größte Zeitersparnis durch KI kommt nicht von einzelnen brillanten Prompts. Sie kommt von **automatisierten Workflows** – Aufgaben, die du jede Woche machst, in eine wiederholbare Struktur zu gießen, die mit einem Klick läuft.

## Das Automatisierungs-Mindset

Bevor du einen Prompt schreibst, stell dir drei Fragen:

1. **Mache ich das regelmäßig?** (Mindestens einmal pro Woche)
2. **Folgt es einem Muster?** (Ähnliche Struktur, ähnlicher Output)
3. **Ist das Ergebnis überprüfbar?** (Du erkennst, ob es gut ist)

Wenn alle drei Ja: Automatisiere es.

### Die 80/20-Regel der KI-Produktivität

80% deiner KI-Zeitersparnis kommt von 20% deiner Aufgaben. Finde diese 20%.

Typische Kandidaten:
- Wiederkehrende E-Mails (Absagen, Follow-ups, Status-Updates)
- Berichte, die sich nur in den Zahlen unterscheiden
- Meeting-Vorbereitung und Protokolle
- Recherche-Zusammenfassungen
- Dokumentation und SOPs

## Prompt-Ketten für Workflows

Ein einzelner Prompt reicht für einfache Aufgaben. Für Workflows brauchst du **Prompt-Ketten** (siehe Band 3) – mehrere Prompts, die aufeinander aufbauen.

### Beispiel: Wöchentlicher Kundenbericht

**Schritt 1 – Daten strukturieren:**

```
Hier sind die Rohdaten dieser Woche:
[CRM-Export, Support-Tickets, Verkaufszahlen einfügen]

Extrahiere und strukturiere:
1. Neue Kunden (Anzahl, Namen, Branche)
2. Offene Support-Tickets (Anzahl, Top-3-Themen)
3. Umsatz vs. Vorwoche (Zahl + Prozent)
4. Churn-Risiko (Kunden ohne Aktivität >30 Tage)
```

**Schritt 2 – Bericht schreiben:**

```
Basierend auf diesen strukturierten Daten:
[Output von Schritt 1]

Schreibe einen Wochenbericht für das Management.
STRUKTUR: Executive Summary (3 Sätze) → KPIs (Tabelle)
→ Highlights → Risiken → Empfehlungen
TON: Sachlich, datengetrieben, max. 1 Seite
```

**Schritt 3 – E-Mail formulieren:**

```
Formuliere eine E-Mail an das Management-Team,
die den Bericht zusammenfasst.
Betreff: Max. 8 Wörter, mit der wichtigsten Zahl.
Body: 5 Sätze, die wichtigsten Punkte.
Anhang-Hinweis auf den vollständigen Bericht.
```

### Template für Prompt-Ketten

Jede Kette hat dasselbe Schema:

1. **Input-Schritt:** Rohdaten in strukturierte Form bringen
2. **Verarbeitungs-Schritt:** Analyse, Zusammenfassung, Bewertung
3. **Output-Schritt:** Finales Format (Bericht, E-Mail, Präsentation)

## Wiederkehrende Aufgaben erkennen

### Der Workflow-Audit

Führe eine Woche lang ein Protokoll: Jedes Mal, wenn du eine Aufgabe machst, die du schon mal gemacht hast, schreib sie auf. Am Ende der Woche hast du deine Automatisierungs-Kandidaten.

**Die häufigsten Workflow-Typen im Büro:**

| Workflow | Häufigkeit | Zeitersparnis |
|----------|------------|---------------|
| E-Mail-Vorlagen | Täglich | 15-30 Min/Tag |
| Meeting-Protokolle | 3-5x/Woche | 20-40 Min/Woche |
| Status-Berichte | Wöchentlich | 1-2 Std/Woche |
| Recherche-Zusammenfassungen | 2-3x/Woche | 30-60 Min/Woche |
| Dokumentation | Laufend | 1-3 Std/Woche |
| Feedback-Formulierungen | 2-3x/Woche | 15-30 Min/Woche |

**Potenzial:** 5-10 Stunden pro Woche – das ist ein ganzer Arbeitstag.

## Prompt-Templates anlegen

Ein gutes Template hat **Platzhalter** für die variablen Teile:

```
Du bist [ROLLE] bei [UNTERNEHMEN].

Aufgabe: [AUFGABE]

Kontext:
- Empfänger: [WER]
- Anlass: [WARUM]
- Ton: [WIE]

Erstelle [OUTPUT-FORMAT].

Einschränkungen:
- Max. [LÄNGE]
- Sprache: [SPRACHE]
- Wichtig: [BESONDERHEITEN]
```

Speichere deine Templates in einem Ordner, einer Notion-Datenbank oder einem Google Doc. Jedes Template braucht: **Name**, **Wann nutzen**, **Platzhalter**, **Beispiel-Output**.

## Automatisierung ohne Code

Du brauchst keine Programmierung für Business-Automatisierung. Drei Wege:

**1. Chat-Projekte:** Claude Projects, ChatGPT Custom GPTs oder Gemini Gems. Du definierst System-Prompt, Wissensbasis und häufige Aufgaben einmal – danach reicht ein kurzer Prompt.

**2. Custom Instructions:** Hinterlege deine Standard-Kontexte (Unternehmen, Rolle, Ton, Formatierung) in den Custom Instructions deines Chat-Tools. Dann musst du sie nicht bei jedem Prompt wiederholen.

**3. Makros und Shortcuts:** Viele Tools (Notion AI, Google Workspace, Microsoft Copilot) haben eingebaute KI-Funktionen. Richte Shortcuts ein für deine häufigsten Aufgaben.

## Die Automatisierungs-Falle

Nicht alles automatisieren. Drei Warnzeichen:

1. **Die Aufgabe braucht viel Kontext, der sich ständig ändert** – dann ist manuelles Prompting effizienter
2. **Das Ergebnis muss 100% korrekt sein** (Verträge, Finanzzahlen) – dann ist KI ein Entwurf, kein Endprodukt
3. **Die Aufgabe erfordert emotionale Intelligenz** (Konfliktgespräch, Krisenkommunikation) – KI kann helfen, aber nicht ersetzen

---

## Übungen

### Übung 1: Workflow-Audit
Führe eine Woche lang ein Protokoll wiederkehrender Aufgaben. Welche drei haben das größte Automatisierungs-Potenzial?

### Übung 2: Prompt-Kette bauen
Nimm eine wiederkehrende Aufgabe und baue eine 3-Schritt-Prompt-Kette (Input → Verarbeitung → Output).

### Übung 3: Template erstellen
Erstelle ein Prompt-Template mit Platzhaltern für deine häufigste E-Mail-Art. Teste es mit 3 verschiedenen Szenarien.

### Übung 4: Zeitersparnis messen
Miss die Zeit für eine Aufgabe manuell vs. mit deinem Template. Wie viel sparst du pro Durchlauf? Rechne hoch auf den Monat.
