# Kapitel 3: Dein erster Prompt

Genug Theorie. Jetzt wird's praktisch.

In diesem Kapitel schreibst du deinen ersten Prompt. Und deinen zweiten. Und deinen zehnten. Am Ende wirst du ein Gefühl dafür haben, was passiert, wenn du mit einem LLM sprichst – und was nicht.

## Was ist ein Prompt überhaupt?

Ein Prompt ist die Eingabe, die du einem LLM gibst. Das kann eine Frage sein, eine Anweisung, eine Bitte – oder alles zusammen. Im Grunde ist es das, was du in das Textfeld tippst.

Das Wort kommt aus dem Englischen und bedeutet so viel wie "Anstoß" oder "Aufforderung". Du stößt die KI an, etwas zu tun.

Ein paar Beispiele für Prompts:

- "Was ist die Hauptstadt von Kanada?"
- "Schreib mir eine Einkaufsliste für ein italienisches Abendessen."
- "Fasse diesen Text in drei Sätzen zusammen: [Text]"
- "Du bist ein erfahrener Fitness-Trainer. Erstelle mir einen Trainingsplan für Anfänger."

Alles davon sind Prompts. Der erste ist simpel. Der letzte ist schon deutlich raffinierter. In den nächsten Kapiteln lernst du, warum – und wie du selbst solche Prompts baust.

## Account erstellen – so geht's

Falls du noch keinen Account hast, hier die schnellste Route:

### Option A: ChatGPT (OpenAI)
1. Geh auf chat.openai.com
2. Klick auf "Registrieren"
3. E-Mail, Passwort, fertig
4. Die kostenlose Version (GPT-4o mini) reicht für den Anfang

### Option B: Claude (Anthropic)
1. Geh auf claude.ai
2. Registriere dich mit E-Mail oder Google-Account
3. Die kostenlose Version gibt dir Zugang zum aktuellen Standard-Modell

### Option C: Gemini (Google)
1. Geh auf gemini.google.com
2. Melde dich mit deinem Google-Account an
3. Kostenlos nutzbar

Ich empfehle dir, mindestens zwei davon auszuprobieren. Für dieses Buch ist es egal, welches Modell du benutzt – die Prinzipien funktionieren bei allen.

## Dein allererster Prompt

Öffne dein bevorzugtes LLM und tippe Folgendes ein:

```
Erkläre mir, was Prompt Engineering ist.
```

Das war's. Drück Enter. Lies die Antwort.

War das jetzt ein guter Prompt? Naja, er funktioniert. Du bekommst eine Antwort. Aber er ist auch ziemlich vage. Das Modell weiß nicht, wer du bist, was du schon weißt oder wie detailliert die Antwort sein soll.

Jetzt probier diesen hier:

```
Ich bin Anfänger und habe noch nie mit KI gearbeitet. Erkläre mir in einfachen Worten, was Prompt Engineering ist. Verwende ein Alltagsbeispiel, um es anschaulich zu machen. Maximal 200 Wörter.
```

Merkst du den Unterschied in der Antwort? Der zweite Prompt gibt dem Modell viel mehr Informationen:
- **Wer du bist:** Anfänger ohne Vorwissen
- **Was du willst:** Erklärung von Prompt Engineering
- **Wie du es willst:** Einfache Worte, Alltagsbeispiel
- **Wie lang:** Maximal 200 Wörter

Das ist im Kern schon Prompt Engineering: Dem Modell genug Informationen geben, damit es dir genau das liefert, was du brauchst.

## 10 Prompts zum Ausprobieren

Hier sind zehn Prompts, die du jetzt direkt testen kannst. Ich habe sie nach Schwierigkeit sortiert – von simpel bis schon ziemlich clever:

**1. Die einfache Frage**
```
Was ist der Unterschied zwischen Wetter und Klima?
```

**2. Die Zusammenfassung**
```
Fasse die Handlung von "Der Herr der Ringe" in 5 Sätzen zusammen.
```

**3. Die Liste**
```
Gib mir 7 Tipps, wie ich morgens schneller wach werde.
```

**4. Die Übersetzung**
```
Übersetze folgenden Satz ins Englische, Französische und Spanische:
"Ich hätte gerne einen Tisch für zwei Personen."
```

**5. Die Analyse**
```
Was sind die Vor- und Nachteile von Homeoffice? Erstelle eine Tabelle mit je 5 Punkten.
```

**6. Die kreative Aufgabe**
```
Schreib mir ein kurzes Gedicht über Montagmorgen. Es soll humorvoll sein.
```

**7. Die Rollenaufgabe**
```
Du bist ein Ernährungsberater. Was sollte ich frühstücken, wenn ich mich gesund ernähren will, aber morgens wenig Zeit habe?
```

**8. Die Vergleichsaufgabe**
```
Vergleiche Python und JavaScript für Anfänger. Was ist leichter zu lernen und warum? Antworte in maximal 150 Wörtern.
```

**9. Die Schritt-für-Schritt-Anleitung**
```
Erkläre mir Schritt für Schritt, wie ich eine Pressemitteilung schreibe. Gib mir für jeden Schritt ein konkretes Beispiel.
```

**10. Die komplexe Aufgabe**
```
Ich möchte eine Geburtstagsparty für 20 Personen planen. Budget: 500 Euro.
Die Gäste sind zwischen 25 und 35 Jahre alt. Es soll ein Motto geben.
Erstelle mir einen vollständigen Plan mit Motto-Vorschlag, Einkaufsliste,
Zeitplan und Deko-Ideen.
```

Probier alle zehn aus. Achte darauf, wie sich die Antworten verändern, je detaillierter dein Prompt wird. Bei Prompt 1 bis 3 bekommst du kurze, allgemeine Antworten. Bei Prompt 9 und 10 bekommst du ausführliche, strukturierte Ergebnisse.

## Was ein Prompt ist – und was er nicht ist

Ein Prompt ist **kein Google-Suchbegriff**. Das ist einer der häufigsten Fehler, den Anfänger machen. Bei Google tippst du "beste Restaurants Berlin" ein und bekommst eine Liste von Webseiten. Bei einem LLM kannst du viel mehr tun:

```
Ich suche ein Restaurant in Berlin-Mitte für ein Geschäftsessen.
Es sollte gehobene Küche sein, aber nicht zu steif. Mein Gast ist
Vegetarier. Budget: 80-120 Euro pro Person. Schlage mir 3 Optionen
vor und erkläre, warum sie passen.
```

Das hier würde bei Google nicht funktionieren. Bei einem LLM schon. Weil du dem Modell Kontext, Einschränkungen und ein klares Ziel gibst.

Ein Prompt ist auch **kein Befehl an einen dummen Computer**. Du musst nicht in einer bestimmten Syntax schreiben. Du musst keine speziellen Kommandos kennen. Schreib einfach, was du willst – als würdest du mit einem sehr geduldigen, sehr belese­nen Assistenten reden.

Und ein Prompt ist **kein einmaliger Versuch**. Wenn die Antwort nicht passt, schreib eine Folgenachricht. "Das ist mir zu technisch, erkläre es einfacher." Oder "Gib mir mehr Details zu Punkt 3." Das Gespräch geht weiter. Genau das macht LLMs so mächtig – du kannst nachbohren, korrigieren und verfeinern.

## Das Wichtigste aus diesem Kapitel

- Ein Prompt ist deine Eingabe an ein LLM – Frage, Anweisung oder beides
- Je mehr Kontext und Details du gibst, desto besser die Antwort
- Prompts sind kein Google-Suchbegriff – du kannst viel komplexere Anfragen stellen
- Der erste Prompt muss nicht perfekt sein – du kannst immer nachbessern

---

## Übung

**Schreibe 5 eigene Prompts und beobachte die Ergebnisse.**

Denk an Dinge, die dich in deinem Alltag beschäftigen. Dein Job, dein Hobby, dein nächster Urlaub, ein Problem, das du gerade hast. Schreib zu jedem Thema einen Prompt und teste ihn.

Achte besonders auf:
- Wie ausführlich ist die Antwort?
- Entspricht sie dem, was du erwartet hast?
- Was hättest du anders formulieren können?

Schreib dir die Ergebnisse auf. In den nächsten Kapiteln wirst du lernen, wie du diese Prompts systematisch verbessern kannst.
