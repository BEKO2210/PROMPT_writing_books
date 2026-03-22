# Kapitel 3: Zero-Shot Chain-of-Thought – Fünf Wörter, die alles verändern

Im letzten Kapitel hast du die klassische CoT-Methode kennengelernt: Du gibst dem Modell Beispiele mit Denkschritten (Few-Shot CoT). Das funktioniert hervorragend, ist aber aufwendig. Du musst für jede neue Aufgabe ein passendes Beispiel schreiben.

Zero-Shot CoT macht das überflüssig. Stattdessen brauchst du nur einen einzigen Satz.

## Die Entdeckung

2022 veröffentlichten Kojma et al. ein Paper mit dem Titel "Large Language Models are Zero-Shot Reasoners". Ihre Entdeckung war verblüffend einfach:

Wenn du an das Ende deines Prompts die Worte **"Let's think step by step"** anfügst – oder auf Deutsch: **"Denke Schritt für Schritt"** – verbessern sich die Ergebnisse bei Reasoning-Aufgaben dramatisch. Ohne ein einziges Beispiel. Ohne vorgegebene Schritte. Nur durch diesen einen Satz.

Die Forscher testeten es auf zwölf verschiedenen Benchmarks. Bei manchen stieg die Genauigkeit um über 40 Prozentpunkte. Fünf Wörter. 40 Prozentpunkte. Das ist keine inkrementelle Verbesserung – das ist ein Durchbruch.

## Warum funktioniert das?

Erinnere dich an Band 2, Kapitel über Zero-Shot Prompting: Zero-Shot bedeutet, dass du dem Modell keine Beispiele gibst. Das Modell muss aus seiner Trainingsdata und deiner Anweisung allein die richtige Antwort finden.

"Denke Schritt für Schritt" aktiviert einen bestimmten "Modus" im Modell. Während des Trainings hat das Modell Millionen von Texten gesehen, in denen Probleme Schritt für Schritt gelöst werden – Lehrbücher, Tutorials, Forenbeiträge, wissenschaftliche Arbeiten. Diese Phrase triggert das Modell, ein ähnliches Muster zu reproduzieren.

Es ist kein Zauberspruch. Es ist eine Anweisung, die das Modell in einen bestimmten Ausgabemodus versetzt – weg von "direkte Antwort" hin zu "ausführlicher Denkprozess".

## Die besten Zero-Shot-CoT-Trigger

"Denke Schritt für Schritt" ist die bekannteste Formulierung, aber nicht die einzige. Hier sind die effektivsten Varianten, die ich getestet habe:

### Die Klassiker

| Trigger | Wann besonders gut |
|---|---|
| "Denke Schritt für Schritt." | Allrounder, funktioniert fast immer |
| "Lass uns das Schritt für Schritt durchgehen." | Etwas natürlicher, gleiche Wirkung |
| "Erkläre deinen Denkprozess." | Wenn du den Weg zur Lösung verstehen willst |
| "Zeige deine Arbeit." | Mathematik und Berechnungen |
| "Überlege sorgfältig, bevor du antwortest." | Wenn Genauigkeit wichtiger ist als Geschwindigkeit |
| "Analysiere das systematisch." | Für analytische Aufgaben |

### Die Spezialisten

| Trigger | Wann besonders gut |
|---|---|
| "Bevor du antwortest: Was sind die relevanten Fakten?" | Faktbasierte Aufgaben |
| "Denke laut nach." | Wenn du den internen Monolog sehen willst |
| "Geh von den Grundlagen aus und arbeite dich vor." | Komplexe Themen, die Basiswissen brauchen |
| "Welche Annahmen machst du? Prüfe sie zuerst." | Wenn Annahmen gefährlich sein können |
| "Bevor du eine Lösung gibst: Was könnte schiefgehen?" | Risikobewertung |

### Die Power-Kombinationen

Manchmal reicht ein einzelner Trigger nicht. Hier sind Kombinationen, die ich regelmäßig nutze:

**Für Analyse:**
```
Denke Schritt für Schritt. Nenne zuerst deine Annahmen,
dann deine Analyse, dann dein Ergebnis.
```

**Für Entscheidungen:**
```
Überlege sorgfältig. Betrachte mindestens drei Perspektiven,
bevor du eine Empfehlung gibst.
```

**Für Problemlösung:**
```
Bevor du eine Lösung vorschlägst: Definiere das Problem präzise.
Dann liste mögliche Ursachen auf. Dann löse es.
```

## Vergleich: Zero-Shot CoT vs. Few-Shot CoT

Wann nimmst du was? Hier ist mein Entscheidungsrahmen:

### Zero-Shot CoT wählen, wenn:
- Du eine **schnelle Verbesserung** brauchst ohne viel Aufwand
- Die Aufgabe **standardmäßig** ist (Mathe, Logik, Analyse)
- Du **kein passendes Beispiel** parat hast
- Du **experimentierst** und verschiedene Ansätze testen willst
- Die Aufgabe **einmalig** ist und du keinen Template-Prompt brauchst

### Few-Shot CoT wählen, wenn:
- Du einen **bestimmten Denkstil** durchsetzen willst
- Die Aufgabe **ungewöhnlich** ist und das Modell Orientierung braucht
- Du **konsistente Ergebnisse** über viele ähnliche Aufgaben brauchst
- Du **sehr spezifische Schritte** brauchst, die das Modell nicht von allein nehmen würde
- Die Aufgabe **domänenspezifisch** ist (Recht, Medizin, Finanzen)

### Der direkte Vergleich

Dieselbe Aufgabe, drei Ansätze:

**Aufgabe:** "Maria ist älter als Tom. Tom ist älter als Sarah. Lisa ist jünger als Sarah. Wer ist am ältesten?"

**Ohne CoT:**
```
Maria ist älter als Tom. Tom ist älter als Sarah.
Lisa ist jünger als Sarah. Wer ist am ältesten?
```
→ Modell antwortet: "Maria." (Richtig, aber ohne Erklärung. Bei komplexeren Varianten steigt die Fehlerrate.)

**Zero-Shot CoT:**
```
Maria ist älter als Tom. Tom ist älter als Sarah.
Lisa ist jünger als Sarah. Wer ist am ältesten?

Denke Schritt für Schritt.
```
→ Modell antwortet:
```
Schritt 1: Maria > Tom (Maria ist älter als Tom)
Schritt 2: Tom > Sarah (Tom ist älter als Sarah)
Schritt 3: Sarah > Lisa (Lisa ist jünger als Sarah)
Schritt 4: Reihenfolge: Maria > Tom > Sarah > Lisa
Schritt 5: Maria ist am ältesten.
```

**Few-Shot CoT:**
```
Beispiel:
Alex ist größer als Ben. Ben ist größer als Chris.
Wer ist am größten?
Denkprozess: Alex > Ben > Chris. Also ist Alex am größten.
Antwort: Alex.

Aufgabe:
Maria ist älter als Tom. Tom ist älter als Sarah.
Lisa ist jünger als Sarah. Wer ist am ältesten?
Denkprozess:
```
→ Modell folgt dem Beispiel-Format exakt.

Bei dieser einfachen Aufgabe sind alle drei Ansätze korrekt. Der Unterschied zeigt sich bei schwierigeren Aufgaben – und dort gewinnt Few-Shot CoT knapp vor Zero-Shot CoT.

## Zero-Shot CoT in der Praxis: Sechs Anwendungsfälle

### 1. Schnelle Alltagsanalysen

```
Mein Auto verbraucht 7 Liter auf 100 km. Ich fahre täglich
35 km zur Arbeit und zurück. Benzin kostet 1,85 Euro.
Wie viel gebe ich pro Monat (22 Arbeitstage) für den
Arbeitsweg aus?

Rechne Schritt für Schritt.
```

Das Modell rechnet transparent: 35 km × 22 = 770 km → 770 ÷ 100 × 7 = 53,9 Liter → 53,9 × 1,85 = 99,72 Euro.

### 2. Entscheidungshilfe

```
Ich überlege, ob ich meinen Job kündigen soll. Aktuell
verdiene ich 55.000 Euro brutto, habe aber eine Zusage
für 65.000 Euro bei einem Startup. Das Startup ist seit
2 Jahren am Markt und hat 15 Mitarbeiter.

Analysiere das systematisch. Welche Faktoren sollte ich
berücksichtigen?
```

Das Modell geht systematisch durch: Gehaltsdifferenz, Jobsicherheit, Startup-Risiken, Karriereperspektiven, Work-Life-Balance, Branche des Startups, finanzielle Rücklagen.

### 3. Textverständnis vertiefen

```
Lies folgenden Absatz und beantworte die Frage:

"Die Inflation in der Eurozone lag im Januar 2026 bei 2,8%.
Die EZB hielt den Leitzins bei 3,15%. Analysten erwarten
eine Zinssenkung im zweiten Quartal, sofern die Kerninflation
unter 2,5% fällt."

Frage: Warum könnte die EZB den Zins senken – und warum
könnte sie es nicht tun?

Denke sorgfältig nach und betrachte beide Seiten.
```

### 4. E-Mail-Entwürfe verbessern

```
Ich möchte meinem Chef schreiben, dass ich ab nächsten Monat
remote arbeiten möchte. Er ist eher konservativ. Ich habe
gute Leistungen.

Bevor du die E-Mail schreibst: Überlege, welche Einwände
er haben könnte und wie du sie in der E-Mail vorwegnimmst.
Dann schreib die E-Mail.
```

Das "Bevor du schreibst: Überlege" ist der Schlüssel. Es zwingt das Modell, erst zu denken und dann zu schreiben.

### 5. Lernhilfe

```
Erkläre mir den Unterschied zwischen TCP und UDP.

Geh von den Grundlagen aus: Was ist ein Netzwerkprotokoll?
Dann erkläre beide Protokolle. Dann vergleiche sie.
Am Ende: Gib mir eine Eselsbrücke, die ich mir merken kann.
```

### 6. Faktencheck

```
Behauptung: "Deutschland hat mehr Einwohner als Frankreich
und Italien zusammen."

Bevor du die Behauptung bewertest: Nenne die aktuellen
Einwohnerzahlen aller drei Länder. Dann rechne.
Dann urteile.
```

Hier bewirkt der Zero-Shot-CoT-Trigger, dass das Modell nicht sofort "Falsch!" sagt, sondern erst die Zahlen prüft. Das reduziert Fehler – und du siehst, ob das Modell mit den richtigen Zahlen arbeitet (und kannst Halluzinationen erkennen).

## Fortgeschrittene Zero-Shot-CoT-Strategien

### Strategie 1: Zweistufiges Zero-Shot CoT

Statt einem Trigger nutzt du zwei in Folge:

**Stufe 1:**
```
[Deine Aufgabe]

Bevor du antwortest: Liste die wichtigsten Fakten und
Überlegungen auf.
```

**Stufe 2 (Folge-Prompt):**
```
Gut. Basierend auf deiner Analyse: Was ist deine
finale Empfehlung? Fasse sie in 3 Sätzen zusammen.
```

Das trennt Analyse und Zusammenfassung in zwei Schritte. Das Modell hat in Stufe 2 seine eigene Analyse als zusätzlichen Kontext.

### Strategie 2: Negatives Zero-Shot CoT

Statt dem Modell zu sagen, was es tun soll, sagst du, was es NICHT tun soll:

```
[Deine Aufgabe]

Antworte NICHT sofort. Denke zuerst nach.
Gib keine Standardantworten. Hinterfrage deine
erste Intuition.
```

Das klingt ungewöhnlich, funktioniert aber erstaunlich gut. Es bremst das Modell und zwingt es, seinen ersten Impuls zu überdenken.

### Strategie 3: Perspektiv-CoT

```
[Deine Aufgabe]

Betrachte das Problem aus drei Perspektiven:
1. Die eines Optimisten
2. Die eines Skeptikers
3. Die eines neutralen Analysten

Dann: Welche Perspektive ist am überzeugendsten?
```

Das ist Zero-Shot CoT plus Multi-Perspektiven (kennst du aus Band 1, Kapitel 7). Die Kombination ist mächtig.

### Strategie 4: Constraint-Check CoT

```
[Deine Aufgabe]

Bevor du antwortest:
- Welche Informationen FEHLEN dir, um sicher zu antworten?
- Welche ANNAHMEN musst du treffen?
- Wie SICHER bist du dir bei deiner Antwort (in Prozent)?

Dann antworte.
```

Das ist Gold wert. Erstens macht es dem Modell bewusst, wo es unsicher ist. Zweitens gibt es dir Transparenz – wenn das Modell sagt "70% sicher", weißt du, dass du gegenprüfen solltest.

## Häufige Fehler bei Zero-Shot CoT

### Fehler 1: Zu viele Trigger gleichzeitig

```
Denke Schritt für Schritt. Zeige deinen Denkprozess.
Erkläre dein Reasoning. Überlege sorgfältig. Nimm dir
Zeit. Sei gründlich.
```

Das ist Overkill. Einer oder zwei Trigger reichen. Mehr führt zu aufgeblähten Antworten ohne Mehrwert.

### Fehler 2: CoT-Trigger ohne klare Aufgabe

```
Ich bin unsicher wegen meiner Karriere. Denke Schritt für Schritt.
```

"Denke Schritt für Schritt" braucht ein konkretes Problem, über das nachgedacht werden kann. Vage Aussagen + CoT-Trigger = vage Analyse mit Schritt-für-Schritt-Formatierung.

### Fehler 3: CoT-Trigger bei Chat-Modellen vergessen

Chat-Modelle wie ChatGPT, Claude oder Gemini reagieren stärker auf den CoT-Trigger als die API-Versionen. Aber auch bei Chat-Modellen musst du den Trigger explizit setzen. "Bestimmt denkt das Modell schon von allein nach" ist ein Trugschluss.

### Fehler 4: Auf Deutsch vs. Englisch

Ein Praxis-Tipp: "Think step by step" und "Denke Schritt für Schritt" funktionieren beide. Bei den meisten Modellen ist die englische Variante minimal besser, weil die Trainingsdaten überwiegend englisch sind. Aber der Unterschied ist klein – bleib bei Deutsch, wenn du deutsche Antworten willst.

## Die "Let me think"-Technik

Eine Variante, die ich persönlich oft nutze und die nirgendwo in den Papers steht:

```
[Deine Aufgabe]

Nimm dir einen Moment. Was fällt dir auf? Was ist hier
die eigentliche Herausforderung? Dann löse es.
```

Statt "Denke Schritt für Schritt" (was eine Struktur vorgibt) sage ich dem Modell: "Orientiere dich erst." Das führt zu natürlicheren Denkprozessen, die manchmal Aspekte beleuchten, die eine vorgegebene Schrittfolge verpasst hätte.

Ist das wissenschaftlich validiert? Nein. Funktioniert es in der Praxis? Ja. Prompting ist oft mehr Handwerk als Wissenschaft.

---

## Übungen

### Übung 1: Trigger-Vergleich
Nimm folgende Aufgabe und teste sie mit 5 verschiedenen Zero-Shot-CoT-Triggern:

"Ein Projekt hat 12 Aufgaben. 3 Personen arbeiten daran. Jede Aufgabe dauert 2 Tage. Manche Aufgaben hängen voneinander ab: Aufgabe 4 braucht Aufgabe 1 und 2. Aufgabe 8 braucht Aufgabe 5. Aufgabe 12 braucht alle anderen. Wie schnell kann das Projekt minimal fertig werden?"

Welcher Trigger liefert die beste Antwort? Dokumentiere die Unterschiede.

### Übung 2: Eigene Trigger entwickeln
Entwickle drei eigene Zero-Shot-CoT-Trigger für deinen Arbeitsbereich. Teste sie mit jeweils 3 Aufgaben. Welcher funktioniert am besten?

### Übung 3: Constraint-Check testen
Nutze die Constraint-Check-Strategie bei einer Aufgabe, bei der du die richtige Antwort kennst. Hat das Modell die fehlenden Informationen korrekt identifiziert? Wie hoch war seine Selbsteinschätzung?

### Übung 4: Zero-Shot vs. Few-Shot
Nimm eine mittelschwere Aufgabe aus deinem Alltag. Löse sie einmal mit Zero-Shot CoT und einmal mit Few-Shot CoT (schreib dir ein Beispiel). Vergleiche:
- Qualität der Antwort
- Zeitaufwand für den Prompt
- Konsistenz (teste jeweils 3x)

Wann lohnt sich der Mehraufwand von Few-Shot?
