# Kapitel 4: Temperatur und Parameter – Die Regler hinter den Kulissen

Bis jetzt hast du immer die Standardeinstellungen deines LLMs benutzt. Du tippst einen Prompt, drückst Enter, bekommst eine Antwort. Was im Hintergrund passiert, war dir egal.

Ab jetzt nicht mehr.

Hinter jedem LLM stecken Parameter, die du einstellen kannst. Sie bestimmen, wie kreativ oder wie vorhersagbar die Antwort ausfällt. Wie lang sie wird. Wie viel Variation du bekommst.

Diese Parameter zu verstehen, ist der Unterschied zwischen "ich benutze KI" und "ich beherrsche KI".

## Wo stelle ich Parameter ein?

Erstmal die schlechte Nachricht: In den normalen Chat-Oberflächen (ChatGPT, Claude.ai, Gemini) kannst du die meisten Parameter nicht direkt einstellen. Die Anbieter wählen Standardwerte, die für die meisten Nutzer funktionieren.

Die gute Nachricht: Es gibt andere Wege.

- **API-Zugang** – Über die Programmierschnittstelle hast du volle Kontrolle über alle Parameter. Das ist das Thema von Band 7.
- **Playground/Studio** – OpenAI Playground, Google AI Studio, Anthropic Console bieten eine Benutzeroberfläche mit Reglern.
- **Drittanbieter-Tools** – Apps wie TypingMind, OpenRouter oder Poe lassen dich Parameter einstellen, ohne Code zu schreiben.

Für dieses Kapitel nutze ich Google AI Studio als Beispiel, weil es kostenlos ist und alle wichtigen Parameter zeigt. Aber die Konzepte gelten für alle Modelle.

## Temperatur: Der wichtigste Parameter

Die Temperatur bestimmt, wie "zufällig" die Antwort des Modells ist.

### Wie es technisch funktioniert

Wenn ein LLM den nächsten Token (das nächste Wort) vorhersagt, berechnet es für jedes mögliche Wort eine Wahrscheinlichkeit:

```
"Die Hauptstadt von Frankreich ist ___"

Paris:    92%
Lyon:      3%
Marseille: 2%
Berlin:    0.5%
Pizza:     0.001%
```

Die Temperatur bestimmt, wie strikt das Modell der Wahrscheinlichkeitsverteilung folgt:

- **Temperatur 0:** Das Modell nimmt IMMER das wahrscheinlichste Wort. Ergebnis: vorhersagbar, konsistent, manchmal steif.
- **Temperatur 1:** Das Modell folgt der Wahrscheinlichkeitsverteilung. Paris wird meistens gewählt, aber Lyon hat auch eine Chance.
- **Temperatur 2:** Die Verteilung wird geglättet. Auch weniger wahrscheinliche Wörter bekommen eine realistische Chance. Ergebnis: kreativ, überraschend, manchmal unsinnig.

### Die Temperatur-Skala

| Wert | Verhalten | Geeignet für |
|------|-----------|-------------|
| 0 | Deterministisch, immer gleich | Fakten, Code, Mathematik |
| 0.1–0.3 | Sehr konsistent, minimale Variation | Zusammenfassungen, Übersetzungen |
| 0.4–0.6 | Ausgewogen | Allgemeine Texte, E-Mails |
| 0.7–0.9 | Kreativ, variabel | Brainstorming, Storytelling |
| 1.0–1.5 | Sehr kreativ, unvorhersagbar | Gedichte, kreative Experimente |
| 1.5+ | Chaotisch | Fast nie sinnvoll |

### Temperatur in der Praxis

**Aufgabe: Firmen-Slogan generieren**

Bei Temperatur 0.2 bekommst du:
```
"TechCorp – Innovation für Ihre Zukunft"
```
Solide. Vorhersagbar. Langweilig.

Bei Temperatur 0.8 bekommst du:
```
"TechCorp – Weil 'geht nicht' keine Option ist"
```
Kreativer. Unerwarteter. Vielleicht genau richtig.

Bei Temperatur 1.5 bekommst du:
```
"TechCorp – Deine Neuronen tanzen Breakdance im Quantenregen"
```
Äh. Zu viel.

### Mein Temperatur-Cheat-Sheet

- **Code schreiben:** 0
- **Fakten abfragen:** 0
- **E-Mails formulieren:** 0.3–0.5
- **Blogartikel schreiben:** 0.5–0.7
- **Brainstorming:** 0.8–1.0
- **Kreatives Schreiben:** 0.7–0.9
- **Verrückte Ideen:** 1.0–1.2

## Top-P: Die Alternative zur Temperatur

Top-P (auch "Nucleus Sampling" genannt) ist ein anderer Weg, die Kreativität zu steuern. Statt die gesamte Wahrscheinlichkeitsverteilung zu verändern, begrenzt Top-P die Auswahl auf die wahrscheinlichsten Wörter.

### Wie es funktioniert

Top-P = 0.1 bedeutet: Das Modell wählt nur aus den Wörtern, die zusammen 10% der Wahrscheinlichkeit ausmachen. Bei unserem Beispiel:

```
"Die Hauptstadt von Frankreich ist ___"

Top-P 0.1 → Nur "Paris" zur Auswahl (92% > 10%)
Top-P 0.5 → "Paris" (92%)
Top-P 0.95 → "Paris", "Lyon", "Marseille" (zusammen ~97%)
```

### Temperatur vs. Top-P

| | Temperatur | Top-P |
|---|---|---|
| Was es macht | Verändert die Verteilung | Begrenzt die Auswahl |
| Niedrig | Konservativ, vorhersagbar | Nur Top-Kandidaten |
| Hoch | Kreativ, chaotisch | Breite Auswahl |
| Standard | 1.0 | 1.0 |

**Wichtige Regel:** Verändere nie beide gleichzeitig. Wähle entweder Temperatur ODER Top-P. Wenn du beide gleichzeitig anpasst, beeinflussen sie sich gegenseitig auf unvorhersehbare Weise.

Die meisten Experten empfehlen: Bleib bei Temperatur und lass Top-P auf dem Standard. Temperatur ist intuitiver und einfacher zu kontrollieren.

## Max Tokens: Wie lang darf die Antwort sein?

Max Tokens begrenzt die Länge der Antwort. Ein Token ist ungefähr ¾ eines Wortes (im Deutschen etwas weniger, weil deutsche Wörter tendenziell länger sind).

```
Max Tokens 50  → ca. 35-40 Wörter
Max Tokens 200 → ca. 150 Wörter
Max Tokens 1000 → ca. 750 Wörter
Max Tokens 4000 → ca. 3000 Wörter
```

### Wann Max Tokens setzen?

- **Zusammenfassungen:** Begrenze auf 200-300 Tokens für knappe Zusammenfassungen
- **Kurze Antworten:** 50-100 Tokens erzwingen Prägnanz
- **Kostenoptimierung:** Bei API-Nutzung zahlst du pro Token

**Achtung:** Wenn die Antwort länger wäre als dein Limit, wird sie einfach abgeschnitten – mitten im Satz. Das Modell beendet seinen Gedanken nicht sauber. Setze Max Tokens also lieber etwas höher als zu niedrig, oder nutze stattdessen eine Anweisung im Prompt: "Antworte in maximal 100 Wörtern."

## Frequency Penalty und Presence Penalty

Diese zwei Parameter kontrollieren Wiederholungen.

### Frequency Penalty (Häufigkeitsstrafe)

Bestraft Wörter, die bereits häufig in der Antwort vorkommen. Je höher der Wert, desto weniger Wiederholungen.

- **0:** Keine Strafe. Das Modell wiederholt sich frei.
- **0.5:** Moderate Strafe. Weniger "und dann... und dann... und dann..."
- **1.0:** Starke Strafe. Erzwingt Wortvielfalt.
- **2.0:** Extrem. Das Modell vermeidet sogar sinnvolle Wiederholungen.

### Presence Penalty (Anwesenheitsstrafe)

Ähnlich, aber subtiler. Bestraft Wörter, die überhaupt schon in der Antwort vorkommen – egal wie oft. Ermutigt das Modell, über neue Themen zu sprechen.

- **0:** Keine Strafe.
- **0.5:** Leichter Drang zu neuen Themen.
- **1.0:** Starker Drang, Neues einzubringen.

### Wann welche Penalty?

| Situation | Frequency Penalty | Presence Penalty |
|-----------|-------------------|------------------|
| Normaler Text | 0–0.3 | 0 |
| Kreatives Schreiben | 0.3–0.7 | 0.3–0.5 |
| Brainstorming | 0.5 | 0.8–1.0 |
| Technischer Text | 0 | 0 |

Für technische Texte willst du KEINE Penalties. Wenn ein Fachbegriff zehn Mal vorkommt, soll er zehn Mal vorkommen. Wortvielfalt auf Kosten von Präzision ist hier kontraproduktiv.

## Stop Sequences: Wann das Modell aufhören soll

Stop Sequences sind Zeichenfolgen, bei denen das Modell sofort aufhört zu generieren.

```
Stop sequence: ["###", "Ende", "\n\n"]
```

Das Modell stoppt, sobald es eine dieser Zeichenfolgen generiert.

**Nützlich für:**
- Einzelne Antworten ohne Nachsatz: Stop bei `"\n\n"`
- Strukturierte Outputs: Stop bei `"###"` nach dem ersten Abschnitt
- Rollenspiele: Stop beim Sprecher-Wechsel

## Parameter-Profile für typische Aufgaben

Hier meine getesteten Einstellungen für häufige Anwendungen:

### Profil: "Faktentreu"
```
Temperatur: 0
Top-P: 1
Max Tokens: 500
Frequency Penalty: 0
Presence Penalty: 0
```
Für: Code, Übersetzungen, Fakten-Recherche

### Profil: "Businesstext"
```
Temperatur: 0.4
Top-P: 1
Max Tokens: 1000
Frequency Penalty: 0.3
Presence Penalty: 0
```
Für: E-Mails, Berichte, Präsentationen

### Profil: "Kreativ"
```
Temperatur: 0.8
Top-P: 1
Max Tokens: 2000
Frequency Penalty: 0.5
Presence Penalty: 0.3
```
Für: Blogartikel, Stories, Marketing-Texte

### Profil: "Brainstorming"
```
Temperatur: 1.0
Top-P: 1
Max Tokens: 1500
Frequency Penalty: 0.5
Presence Penalty: 0.8
```
Für: Ideenfindung, unkonventionelle Ansätze

## Der häufigste Anfängerfehler

Der häufigste Fehler: Temperatur hochdrehen in der Hoffnung auf "bessere" Ergebnisse. Mehr Kreativität ≠ besser. Es bedeutet nur mehr Variation.

Für 90% aller Aufgaben sind die Standardeinstellungen gut genug. Fang immer mit den Standards an und ändere einen Parameter nach dem anderen. Nie zwei gleichzeitig. Sonst weißt du nicht, welche Änderung welchen Effekt hatte.

---

## Übung

**Parameter-Experiment**

1. Geh zu Google AI Studio (aistudio.google.com) – es ist kostenlos
2. Wähle ein Modell (z.B. Gemini 2.0 Flash)
3. Gib diesen Prompt ein: "Schreibe einen Eröffnungssatz für einen Krimi, der in Hamburg spielt."
4. Generiere den Satz mit Temperatur 0, 0.5, 0.8 und 1.2 – jeweils 3 Mal
5. Notiere die Unterschiede:
   - Wie stark variieren die Ergebnisse bei gleicher Temperatur?
   - Ab welcher Temperatur wird es "zu kreativ"?
   - Welche Temperatur liefert die besten Ergebnisse für DIESE Aufgabe?

Bonusaufgabe: Wiederhole das Experiment mit einem Fakten-Prompt ("Was ist die Hauptstadt von Frankreich?") und beobachte den Unterschied.
