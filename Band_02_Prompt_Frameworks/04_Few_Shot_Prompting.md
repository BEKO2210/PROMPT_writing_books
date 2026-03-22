# Kapitel 4: Few-Shot Prompting – Muster erkennen durch mehrere Beispiele

Wenn ein Beispiel gut ist, sind mehrere besser. Zumindest meistens.

Few-Shot Prompting ist die natürliche Weiterentwicklung von One-Shot. Statt einem Beispiel gibst du dem Modell zwei, drei oder mehr. Das Modell erkennt das Muster zwischen den Beispielen und wendet es auf die neue Aufgabe an.

## Wie Few-Shot funktioniert

Das Prinzip ist simpel: Je mehr Beispiele du gibst, desto besser versteht das Modell, was du willst. Nicht weil es "klüger" wird, sondern weil es mehr Datenpunkte hat, aus denen es Muster ableiten kann.

Stell dir vor, ich sage dir: "Übersetze 'Haus' ins Klingonische." Du hast keine Ahnung. Aber wenn ich dir sage:

- Wasser → bIQ
- Feuer → qul
- Erde → tera'

Dann hast du zumindest ein Gefühl für die Sprache. Du kennst die Schreibweise, die Länge, den Stil. Du könntest raten. Und LLMs sind verdammt gut im Raten.

## Die Struktur eines Few-Shot-Prompts

```
[Aufgabenbeschreibung]

Beispiel 1:
Input: [Eingabe 1]
Output: [Ausgabe 1]

Beispiel 2:
Input: [Eingabe 2]
Output: [Ausgabe 2]

Beispiel 3:
Input: [Eingabe 3]
Output: [Ausgabe 3]

Aufgabe:
Input: [Deine Eingabe]
Output:
```

## Few-Shot in Aktion

### Beispiel 1: Sentiment-Analyse

```
Klassifiziere Kundenbewertungen als positiv, neutral oder negativ.

Beispiel 1:
Bewertung: "Absolut klasse! Schnelle Lieferung und top Qualität."
Sentiment: positiv

Beispiel 2:
Bewertung: "Ist okay, nichts Besonderes. Erfüllt seinen Zweck."
Sentiment: neutral

Beispiel 3:
Bewertung: "Totaler Reinfall. Nach einer Woche kaputt gegangen."
Sentiment: negativ

Beispiel 4:
Bewertung: "Die Lieferung hat ewig gedauert, aber das Produkt
selbst ist wirklich gut."
Sentiment: neutral

Aufgabe:
Bewertung: "Hatte Bedenken wegen der vielen negativen Bewertungen,
aber bei mir funktioniert alles einwandfrei. Preis-Leistung top."
Sentiment:
```

Beachte Beispiel 4 – eine gemischte Bewertung. Durch dieses Beispiel zeigst du dem Modell, wie es mit Ambiguität umgehen soll. Ohne dieses Beispiel hätte es vielleicht "positiv" gesagt, weil das Produkt gelobt wird. Oder "negativ", weil die Lieferung kritisiert wird. Das Beispiel kalibriert die Erwartung.

### Beispiel 2: Formatierung

```
Wandle informelle Notizen in strukturierte Meeting-Protokoll-Einträge um.

Beispiel 1:
Notiz: "müssen das budget für q3 nochmal besprechen, sarah kümmert
sich um die zahlen bis freitag"
Protokoll:
**Thema:** Q3-Budget-Review
**Beschluss:** Erneute Besprechung erforderlich
**Verantwortlich:** Sarah
**Deadline:** Freitag
**Status:** Offen

Beispiel 2:
Notiz: "website relaunch wird auf januar verschoben wegen
personalengpass, tom informiert den kunden"
Protokoll:
**Thema:** Website-Relaunch Terminverschiebung
**Beschluss:** Verschiebung auf Januar (Grund: Personalengpass)
**Verantwortlich:** Tom (Kundenkommunikation)
**Deadline:** Januar
**Status:** Verschoben

Aufgabe:
Notiz: "neue social media strategie steht, lisa und markus setzen
die erste kampagne bis ende des monats um, budget ist genehmigt"
Protokoll:
```

Hier arbeiten die Beispiele zusammen: Beispiel 1 zeigt eine offene Aufgabe, Beispiel 2 zeigt eine Verschiebung. Zusammen definieren sie das Schema vollständig.

### Beispiel 3: Kreative Konsistenz

```
Schreibe Kurzbeschreibungen für Podcast-Episoden in unserem Stil.

Beispiel 1:
Titel: "Warum Meetings meistens Zeitverschwendung sind"
Beschreibung: 47 Minuten über die Meeting-Kultur in deutschen
Unternehmen. Warum die meisten Meetings E-Mails sein sollten,
welche Meetings tatsächlich Sinn machen, und wie du deinen Chef
überzeugst, dass "kurz synchronisieren" kein Synonym für "eine
Stunde quatschen" ist.

Beispiel 2:
Titel: "Remote Work – zwei Jahre später"
Beschreibung: 52 Minuten ehrliche Bilanz. Was funktioniert hat,
was nicht, und warum die "Zurück-ins-Büro"-Debatte an der
Realität vorbeigeht. Mit echten Zahlen statt Bauchgefühl.

Aufgabe:
Titel: "KI im Arbeitsalltag – zwischen Hype und Realität"
Beschreibung:
```

Durch zwei Beispiele versteht das Modell: Dauer erwähnen, provokante Tonlage, konkret statt vage, kritisch aber nicht negativ.

## Wie viele Beispiele sind genug?

Die kurze Antwort: Zwischen 2 und 5.

Die längere Antwort:

| Anzahl | Wann sinnvoll |
|---|---|
| 2 Beispiele | Einfache Aufgaben, klares Muster |
| 3 Beispiele | Standardfall, reicht für die meisten Aufgaben |
| 4-5 Beispiele | Komplexe Aufgaben, Grenzfälle zeigen |
| 6+ Beispiele | Selten nötig, kann sogar kontraproduktiv sein |

Warum nicht mehr? Zwei Gründe:

1. **Kontextfenster:** Jedes Beispiel verbraucht Token. Bei 10 langen Beispielen ist der halbe Kontext aufgebraucht, bevor die eigentliche Aufgabe kommt.

2. **Abnehmender Grenznutzen:** Der Sprung von 0 auf 1 Beispiel ist riesig. Von 1 auf 3 ist merkbar. Von 3 auf 5 ist minimal. Von 5 auf 10 ist oft Null.

## Die Kunst der Beispielauswahl

Nicht alle Beispiele sind gleich wertvoll. Die besten Few-Shot-Sets folgen diesen Regeln:

### Regel 1: Vielfalt

Deine Beispiele sollten verschiedene Varianten der Aufgabe zeigen, nicht dreimal dasselbe.

**Schlecht:** Drei Beispiele, die alle positives Sentiment zeigen.
**Gut:** Ein positives, ein negatives, ein gemischtes Beispiel.

### Regel 2: Grenzfälle einschließen

Zeige nicht nur die einfachen Fälle. Zeige auch die schwierigen.

**Schlecht:** Nur eindeutige Beispiele.
**Gut:** Auch ein Beispiel, das ambig ist, um zu zeigen, wie das Modell damit umgehen soll.

### Regel 3: Reihenfolge beachten

Forschungen zeigen, dass die Reihenfolge der Beispiele das Ergebnis beeinflusst. Als Faustregel: Setze das Beispiel, das der aktuellen Aufgabe am ähnlichsten ist, an die letzte Position – direkt vor deine eigentliche Aufgabe.

### Regel 4: Konsistente Formatierung

Alle Beispiele müssen gleich formatiert sein. Wenn Beispiel 1 Bullet Points hat und Beispiel 2 nummerierte Listen, verwirrt das das Modell.

## Few-Shot vs. Fine-Tuning

Kurzer Ausblick für Neugierige: Few-Shot Prompting ist eine Art "Mini-Training" im Prompt selbst. Du gibst dem Modell Beispiele, es lernt daraus – aber nur für diese eine Anfrage. Beim nächsten Prompt ist alles vergessen.

Fine-Tuning dagegen verändert das Modell dauerhaft. Du trainierst es mit hunderten oder tausenden Beispielen, und es behält das Gelernte. Das ist mächtiger, aber auch aufwendiger und teurer.

Für die meisten Anwendungen reicht Few-Shot völlig aus. Fine-Tuning ist etwas für Band 7, wenn wir über Entwickler-Themen sprechen.

## Zusammenfassung

- Few-Shot = Aufgabe mit mehreren Beispielen (typischerweise 2-5)
- Ideal für Klassifikation, Formatierung und konsistente Outputs
- Die Qualität und Vielfalt der Beispiele ist entscheidend
- 3 gute Beispiele schlagen 10 mittelmäßige
- Grenzfälle in den Beispielen verbessern die Ergebnisse deutlich

---

## Übung

**Few-Shot Meisterklasse**

Erstelle einen Few-Shot-Prompt für folgende Aufgabe: Du willst, dass die KI aus unstrukturierten Tagebuch-Einträgen strukturierte Stimmungs-Logs erstellt.

1. Schreibe mindestens 3 Beispiel-Paare (Tagebuch-Eintrag → Stimmungs-Log)
2. Einer der Einträge sollte gemischte Stimmungen enthalten
3. Definiere das Format des Stimmungs-Logs selbst
4. Teste den Prompt mit einem echten (oder ausgedachten) Tagebuch-Eintrag
5. Vergleiche: Wie wäre das Ergebnis ohne Beispiele ausgefallen?

Bonus: Teste denselben Prompt einmal mit 2 Beispielen und einmal mit 4. Merkst du einen Unterschied?
