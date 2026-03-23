# Kapitel 9: Iteratives Prompting – Warum der erste Versuch selten reicht

Ich muss dir was sagen, das viele Prompt-Engineering-Anfänger nicht hören wollen: Dein erster Prompt wird fast nie perfekt sein. Und das ist völlig in Ordnung.

Die besten Ergebnisse entstehen nicht durch einen einzigen genialen Prompt. Sie entstehen durch einen Prozess: Schreiben, Ergebnis lesen, korrigieren, verfeinern, nochmal probieren. Genau wie ein Bildhauer nicht mit einem einzigen Hammerschlag eine Statue formt, formst du dein Ergebnis Schritt für Schritt.

Das nennt sich iteratives Prompting. Und es ist die vielleicht wichtigste Fähigkeit, die du in diesem Buch lernst.

## Warum der erste Prompt selten perfekt ist

Drei Gründe:

**1. Du weißt nicht immer, was du willst**
Klingt komisch, ist aber wahr. Oft merkst du erst, wenn du die Antwort siehst, dass du eigentlich etwas anderes wolltest. Das ist kein Versagen – das ist ein normaler Denkprozess. Die erste Antwort hilft dir, dein eigenes Ziel zu schärfen.

**2. Du kannst nicht alles im Voraus bedenken**
Selbst mit den 5 Bausteinen aus Kapitel 4 vergisst du manchmal einen wichtigen Kontext. Oder du merkst, dass der Ton nicht stimmt. Oder die Länge passt nicht. Kein Problem – dafür gibt es Folgeprompts.

**3. LLMs interpretieren anders als du denkst**
Du schreibst "kurz", aber dein "kurz" sind 3 Sätze und das "kurz" des Modells sind 3 Absätze. Oder du schreibst "professionell" und meinst "freundlich-businesslike", aber das Modell versteht "steif und distanziert". Missverständnisse passieren – und du korrigierst sie im Dialog.

## Die Kunst des Folge-Prompts

Ein Folge-Prompt ist dein Werkzeug, um die Antwort zu verfeinern. Hier sind die häufigsten Situationen und was du schreiben kannst:

### Die Antwort ist zu lang

```
Das ist zu ausführlich. Kürze es auf die Hälfte und behalte nur
die wichtigsten Punkte.
```

Oder noch präziser:

```
Kürze den Text auf maximal 100 Wörter. Behalte Punkt 1, 3 und 5.
Die anderen können weg.
```

### Die Antwort ist zu oberflächlich

```
Gut als Überblick, aber geh bei Punkt 2 und 4 mehr ins Detail.
Ich brauche konkrete Beispiele und Zahlen.
```

### Der Ton stimmt nicht

```
Das klingt zu formell. Schreib es um – lockerer, als würdest du es
einem Freund bei einem Kaffee erklären. Keine Fachbegriffe.
```

### Die Antwort geht in die falsche Richtung

```
Das geht an meiner Frage vorbei. Ich meinte nicht [X], sondern [Y].
Lass uns nochmal von vorn anfangen: [Klarstellung]
```

### Du willst einen bestimmten Teil vertiefen

```
Punkt 3 ist sehr interessant. Kannst du dazu mehr schreiben?
Speziell: Welche konkreten Schritte müsste ich unternehmen?
```

### Du willst das Format ändern

```
Gut, aber mach daraus eine Tabelle statt Fließtext.
Spalten: Schritt, Beschreibung, Zeitaufwand, benötigte Ressourcen.
```

## Ein vollständiges Beispiel: 5 Iterationen

Lass mich dir zeigen, wie ein iterativer Prozess in der Praxis aussieht. Ich wollte neulich einen LinkedIn-Post über KI im Bildungswesen schreiben.

**Iteration 1:**
```
Schreib mir einen LinkedIn-Post über KI im Bildungswesen.
```
*Ergebnis: Generisch, lang, voller Buzzwords. Nicht brauchbar.*

**Iteration 2:**
```
Das ist mir zu generisch und zu lang. Ich möchte einen konkreten
Aspekt: Wie Lehrer KI als Werkzeug nutzen können. Maximal 150 Wörter.
Kein Buzzword-Bingo.
```
*Ergebnis: Besser. Fokussierter. Aber immer noch etwas langweilig.*

**Iteration 3:**
```
Der Inhalt stimmt jetzt, aber der Einstieg ist schwach. Starte mit
einer konkreten Szene oder einem Beispiel, nicht mit einer allgemeinen
Aussage. Und der Schluss braucht einen konkreten Call-to-Action.
```
*Ergebnis: Guter Einstieg, besserer Schluss. Fast da.*

**Iteration 4:**
```
Gut! Aber Satz 3 ist zu lang – teile ihn in zwei kürzere Sätze auf.
Und ersetze "transformieren" durch ein normaleres Wort.
```
*Ergebnis: Fast perfekt.*

**Iteration 5:**
```
Letzter Feinschliff: Füge nach dem zweiten Absatz eine Leerzeile ein
und setze einen kurzen Satz in Klammern, der eine persönliche Meinung
einbringt. So wirkt es authentischer.
```
*Ergebnis: Fertig. Ein Post, den ich veröffentlichen kann.*

Fünf Iterationen. Der erste Versuch war meh. Der fünfte war gut. So funktioniert iteratives Prompting.

## Das Prompt-Protokoll

Hier kommt ein Tipp, der dich langfristig besser macht: Führe ein Prompt-Protokoll.

Was ist das? Eine Sammlung deiner besten Prompts. Schreib dir die Prompts auf, die besonders gut funktioniert haben – inklusive der Iterationen, die nötig waren, um dahin zu kommen.

Das klingt nach Mehraufwand, und am Anfang ist es das auch. Aber nach ein paar Wochen hast du eine persönliche Prompt-Bibliothek, auf die du immer zurückgreifen kannst. Du musst das Rad nicht jedes Mal neu erfinden.

Ich mache das mit einer einfachen Textdatei. Andere benutzen Notion, Obsidian oder Google Docs. Das Tool ist egal – Hauptsache, du machst es.

Ein Eintrag in meinem Protokoll sieht so aus:

```
Datum: 15.03.2026
Zweck: LinkedIn-Post über KI im Bildungswesen
Modell: Claude 4 Sonnet
Iterationen: 5

Finaler Prompt:
"Du bist ein Bildungsexperte, der auf LinkedIn aktiv ist.
Schreib einen Post (maximal 150 Wörter) darüber, wie Lehrer
KI als Werkzeug im Unterricht nutzen können. Starte mit einer
konkreten Szene aus dem Schulalltag. Kein Buzzword-Bingo, kein
Corporate-Sprech. Inklusive einem konkreten Call-to-Action am Ende.
Ton: enthusiastisch aber realistisch."

Notizen: Erster Versuch war zu generisch. Key Learning:
Immer einen konkreten Aspekt wählen statt ein breites Thema.
```

## Aus Fehlern lernen

Jede schlechte Antwort ist eine Lektion. Wenn das Modell nicht liefert, was du willst, liegt das fast immer am Prompt – nicht am Modell.

Frag dich:
- War ich spezifisch genug?
- Fehlte Kontext?
- Hätte eine Rolle geholfen?
- War das gewünschte Format klar?
- Habe ich zu viel auf einmal verlangt?

Meistens liegt es an einem dieser Punkte. Und wenn du den Fehler erkennst, wird dein nächster Prompt besser. Prompt Engineering ist eine Fähigkeit, die mit jedem Versuch wächst.

## Wann du aufhören solltest zu iterieren

Auch das ist eine berechtigte Frage. Iteratives Prompting heißt nicht, dass du endlos hin und her korrigieren sollst. Irgendwann gibt es Diminishing Returns – die Verbesserungen werden kleiner und der Aufwand größer.

Meine Faustregel: Wenn du nach 5-7 Iterationen nicht da bist, wo du hinwillst, dann ist das Modell für diese Aufgabe nicht das richtige Werkzeug. Oder du musst deinen Ansatz komplett ändern – nicht nur einzelne Wörter austauschen.

Manchmal ist es effizienter, den ganzen Prompt zu löschen und von vorn anzufangen, als eine schlechte Antwort durch 20 Korrekturen zu retten.

## Das Wichtigste aus diesem Kapitel

- Der erste Prompt muss nicht perfekt sein – iteriere
- Folge-Prompts sind dein Werkzeug zur Verfeinerung
- Sei spezifisch in deinen Korrekturen ("Satz 3 kürzen", nicht "mach es besser")
- Führe ein Prompt-Protokoll für langfristiges Lernen
- Nach 5-7 Iterationen: Entweder passt es oder du brauchst einen neuen Ansatz

---

## Übung

**Starte mit einem einfachen Prompt und verbessere ihn in 5 Iterationen.**

1. Wähle ein Thema, das dich interessiert
2. Schreib einen bewusst einfachen, vagen ersten Prompt
3. Lies die Antwort und notiere, was nicht passt
4. Schreib einen Folge-Prompt, der genau eine Sache verbessert
5. Wiederhole Schritt 3 und 4 noch dreimal (insgesamt 5 Iterationen)
6. Vergleiche die erste und die letzte Antwort

Schreib dir den finalen Prompt auf – er kommt in dein Prompt-Protokoll.

Bonus-Übung: Versuche dieselbe Aufgabe, aber schreibe direkt einen detaillierten Prompt (ohne Iteration). Vergleiche, ob das Ergebnis besser oder schlechter ist als nach 5 Iterationen. Du wirst überrascht sein, wie oft der iterative Weg gewinnt.
