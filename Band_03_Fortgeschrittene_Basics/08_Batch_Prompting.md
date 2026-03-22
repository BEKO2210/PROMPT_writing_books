# Kapitel 8: Batch-Prompting – Mehrere Aufgaben auf einen Schlag

Du hast 20 Kundenbewertungen und willst jede einzeln analysieren. Du könntest 20 Prompts schreiben. Oder du machst es in einem.

Batch-Prompting bedeutet: Du gibst dem Modell mehrere Aufgaben gleichzeitig. Das spart Zeit, spart Tokens und – wenn du es richtig machst – liefert konsistentere Ergebnisse.

## Was ist Batch-Prompting?

Statt:
```
Prompt 1: Analysiere Bewertung 1
Prompt 2: Analysiere Bewertung 2
Prompt 3: Analysiere Bewertung 3
...
```

Machst du:
```
Analysiere die folgenden 5 Bewertungen.
Gib für jede an: Sentiment (positiv/neutral/negativ),
Hauptthema, Handlungsbedarf (ja/nein).

Bewertung 1: """..."""
Bewertung 2: """..."""
Bewertung 3: """..."""
Bewertung 4: """..."""
Bewertung 5: """..."""
```

Ein Prompt, fünf Ergebnisse.

## Wann Batch-Prompting sinnvoll ist

**Geeignet:**
- Gleiche Aufgabe auf verschiedene Inputs anwenden (Bewertungen analysieren, E-Mails kategorisieren, Texte zusammenfassen)
- Listen erstellen (10 Blogtitel, 5 Slogans, 8 Interviewfragen)
- Daten transformieren (CSV-Daten in Tabelle, mehrere Texte übersetzen)
- Vergleiche anstellen (3 Produkte nebeneinander bewerten)

**Nicht geeignet:**
- Jede Aufgabe braucht individuellen Kontext
- Die Aufgaben sind komplex und voneinander unabhängig
- Du brauchst für jede Aufgabe Höchstqualität (dann lieber einzeln)
- Die Gesamtdatenmenge sprengt das Kontext-Fenster

## Batch-Prompting-Muster

### Muster 1: Gleiche Aufgabe, verschiedene Inputs

```
Übersetze die folgenden 5 Sätze ins Englische.
Nummeriere die Übersetzungen entsprechend.

1. "Der frühe Vogel fängt den Wurm."
2. "Übung macht den Meister."
3. "Wer rastet, der rostet."
4. "Aller Anfang ist schwer."
5. "Ohne Fleiß kein Preis."
```

### Muster 2: Verschiedene Varianten einer Aufgabe

```
Schreibe 5 verschiedene Betreffzeilen für eine E-Mail,
die Kunden über einen Serverausfall informiert.

Variante 1: Sachlich-informativ
Variante 2: Entschuldigend
Variante 3: Lösungsorientiert
Variante 4: Kurz und knapp (max. 5 Wörter)
Variante 5: Mit Zeitangabe
```

### Muster 3: Daten strukturiert verarbeiten

```
Ich gebe dir eine Liste von Kundenfeedback-Einträgen.
Erstelle eine Tabelle mit folgenden Spalten:

| Nr. | Sentiment | Kategorie | Kernaussage | Priorität |

Kategorien: Produkt, Lieferung, Service, Preis, Sonstiges
Priorität: Hoch (negativ + häufig), Mittel, Niedrig

Feedback:
1. "Tolles Produkt, aber die Lieferung hat 2 Wochen gedauert."
2. "Kundenservice war super, hat mir sofort geholfen."
3. "Für den Preis hatte ich mehr erwartet. Qualität ist okay."
4. "Seit dem letzten Update stürzt die App ständig ab."
5. "Bin seit 3 Jahren Kunde und immer zufrieden."
6. "Rücksendung war ein Albtraum. 4 Wochen auf Erstattung gewartet."
7. "Gutes Preis-Leistungs-Verhältnis."
8. "Die neue Funktion ist genial! Genau das hat gefehlt."
```

### Muster 4: Parallele Perspektiven

```
Bewerte die folgende Geschäftsidee aus 4 verschiedenen Perspektiven:

Geschäftsidee: "Ein Abo-Service für nachhaltige Büromaterialien,
geliefert an kleine Unternehmen."

Perspektive 1 - Investor: Marktpotential, Skalierbarkeit, ROI
Perspektive 2 - Kunde: Nutzen, Preis, Convenience
Perspektive 3 - Wettbewerb: Differenzierung, Markteintrittsbarrieren
Perspektive 4 - Operations: Logistik, Lieferkette, Herausforderungen

Für jede Perspektive: 3 Stärken, 2 Risiken, 1 Empfehlung.
```

## Die Batch-Größe: Wie viel auf einmal?

Meine Erfahrungswerte:

| Aufgabenkomplexität | Optimale Batch-Größe |
|---------------------|---------------------|
| Einfach (Übersetzen, Kategorisieren) | 10–20 Items |
| Mittel (Zusammenfassen, Analysieren) | 5–10 Items |
| Komplex (Bewerten, Erstellen) | 3–5 Items |

Warum nicht mehr? Weil die Qualität sinkt. Bei 30 Bewertungen in einem Prompt werden die letzten oberflächlicher analysiert als die ersten. Das Modell wird "müde" – nicht wirklich, aber der Effekt ist ähnlich.

Meine Faustregel: Lieber 3 Batches à 10 Items als 1 Batch à 30 Items.

## Output-Format bei Batches

Bei Batch-Prompting ist ein klares Output-Format besonders wichtig. Ohne Format bekommst du einen Textblock, in dem die Ergebnisse ineinander übergehen.

### Nummerierte Listen

```
Gib die Ergebnisse als nummerierte Liste.
Format pro Eintrag:

[Nummer]. [Ergebnis]
   Bewertung: [Positiv/Negativ/Neutral]
   Kommentar: [1 Satz]
```

### Tabellen

```
Gib die Ergebnisse als Markdown-Tabelle.
Spalten: Nr. | Input | Output | Anmerkung
```

### JSON (für Entwickler)

```
Gib die Ergebnisse als JSON-Array.
Format pro Eintrag:
{"id": 1, "input": "...", "result": "...", "category": "..."}
```

## Fehler beim Batch-Prompting

### Fehler 1: Kein einheitliches Format

Wenn du nicht sagst, wie die Ausgabe aussehen soll, bekommst du bei 10 Items möglicherweise 10 verschiedene Formate. Item 1 als Fließtext, Item 5 als Liste, Item 8 als Tabelle.

Lösung: Format VORHER definieren und ein Beispiel geben.

### Fehler 2: Zu große Batches

20+ komplexe Items in einem Prompt. Die Qualität der letzten Items wird schlechter.

Lösung: Batch aufteilen. Qualität vor Effizienz.

### Fehler 3: Ungleiche Inputs

Wenn deine Items sehr unterschiedlich lang oder komplex sind, kann das Modell den kürzeren Items weniger Aufmerksamkeit schenken.

Lösung: Gruppiere ähnlich komplexe Items zusammen.

### Fehler 4: Keine Nummerierung

Ohne Nummerierung weißt du bei der Ausgabe nicht, welches Ergebnis zu welchem Input gehört. Besonders bei langen Listen.

Lösung: Immer nummerieren. Input UND Output.

## Batch-Prompting vs. Prompt-Chaining

Wann was?

| | Batch-Prompting | Prompt-Chaining |
|---|---|---|
| Aufgabentyp | Gleiche Aufgabe, verschiedene Inputs | Verschiedene Aufgaben, ein Input |
| Ziel | Effizienz | Qualität |
| Wann | "Mach das mit allen" | "Mach erst das, dann das" |
| Beispiel | 10 Texte zusammenfassen | 1 Text: recherchieren → analysieren → schreiben |

Du kannst beides kombinieren: Prompt-Chaining als Gesamtstruktur, und in einem Schritt Batch-Prompting für mehrere Items.

```
Schritt 1 (Einzelprompt): Definiere Bewertungskriterien
Schritt 2 (Batch): Bewerte 10 Produkte nach diesen Kriterien
Schritt 3 (Einzelprompt): Erstelle ein Ranking mit Empfehlung
```

## Praxisbeispiel: Wöchentliches Team-Reporting

Du bekommst jeden Freitag 5 Statusberichte von deinem Team. Statt jeden einzeln zusammenzufassen:

```
Ich gebe dir 5 Statusberichte meiner Teammitglieder.
Erstelle daraus einen Gesamtbericht für die Geschäftsführung.

Format:
1. Executive Summary (3 Sätze)
2. Tabelle: Teammitglied | Hauptergebnis | Status (🟢🟡🔴) | Blocker
3. Top-3-Risiken für nächste Woche
4. Empfohlene Maßnahmen

<bericht_1>
[Statusbericht Person 1]
</bericht_1>

<bericht_2>
[Statusbericht Person 2]
</bericht_2>

<bericht_3>
[Statusbericht Person 3]
</bericht_3>

<bericht_4>
[Statusbericht Person 4]
</bericht_4>

<bericht_5>
[Statusbericht Person 5]
</bericht_5>
```

Ein Prompt. Fünf Berichte rein, ein Management-Summary raus. Jeden Freitag in 2 Minuten statt 30.

---

## Übung

**Batch-Prompting in der Praxis**

1. Sammle 5-10 gleichartige Texte (E-Mails, Bewertungen, Nachrichtenartikel – was immer du griffbereit hast)
2. Definiere eine Analyse-Aufgabe (z.B. "Kategorisiere nach Thema und Stimmung")
3. Erstelle einen Batch-Prompt mit klarem Output-Format
4. Teste mit der gesamten Batch
5. Teste dann jedes Item einzeln mit dem gleichen Prompt
6. Vergleiche: Qualitätsunterschied? Zeitersparnis?

Bonusaufgabe: Finde die optimale Batch-Größe für deine Aufgabe, indem du mit 3, 5 und 10 Items testest.
