# Kapitel 5: Die häufigsten Fehler beim Prompting

Jeder macht Fehler. Ich auch. Als ich angefangen habe, mit LLMs zu arbeiten, habe ich Prompts geschrieben, für die ich mich heute schämen würde. Aber genau aus diesen Fehlern habe ich am meisten gelernt.

In diesem Kapitel zeige ich dir die Fehler, die fast jeder am Anfang macht. Wenn du die vermeidest, bist du schon weiter als 80% aller LLM-Nutzer.

## Fehler 1: Zu vage sein

Das ist der Klassiker. Der häufigste Fehler überhaupt.

**Schlecht:**
```
Hilf mir mit meinem Projekt.
```

Was für ein Projekt? Schulprojekt? Softwareprojekt? Heimwerkerprojekt? In welcher Phase? Was genau brauchst du? Das Modell kann hellsehen? Kann es nicht.

**Besser:**
```
Ich arbeite an einer PowerPoint-Präsentation für einen Kunden. Das Thema
ist "Digitale Transformation im Mittelstand". Die Präsentation soll
15 Minuten dauern. Ich brauche eine Gliederung mit 8-10 Folien.
Zu jeder Folie: Titel und 3 Stichpunkte.
```

## Fehler 2: Zu viel auf einmal wollen

Das Gegenteil von zu vage. Manche Leute packen alles in einen einzigen Prompt und erwarten ein perfektes Ergebnis.

**Schlecht:**
```
Schreib mir einen kompletten Businessplan für ein Café. Mit Finanzplanung,
Marktanalyse, Wettbewerbsanalyse, Personalplanung, Marketingstrategie,
Standortanalyse und Risikoanalyse. Alles auf Deutsch. Mindestens
5000 Wörter. Mit Diagrammen.
```

Das ist nicht ein Prompt – das sind zehn. Und das Ergebnis wird in keinem Bereich wirklich gut sein, weil das Modell versucht, alles oberflächlich abzuhandeln.

**Besser:** Teile es auf. Mach erst die Gliederung. Dann die Marktanalyse. Dann die Finanzplanung. Schritt für Schritt.

```
Erstelle eine Gliederung für einen Businessplan für ein Café in einer
deutschen Universitätsstadt. Nenne die wichtigsten Abschnitte und was
jeweils enthalten sein sollte.
```

Und dann im nächsten Prompt:
```
Jetzt schreib mir den Abschnitt "Marktanalyse" aus. [...]
```

## Fehler 3: Keinen Kontext geben

Das hatten wir schon in Kapitel 4, aber es ist so wichtig, dass ich es hier nochmal betone. Ohne Kontext rät das Modell. Und meistens rät es falsch.

**Schlecht:**
```
Wie führe ich ein schwieriges Gespräch?
```

**Besser:**
```
Ich muss einem Mitarbeiter sagen, dass seine Leistung in den letzten
3 Monaten nachgelassen hat. Ich bin sein direkter Vorgesetzter.
Die Firma ist ein kleines Tech-Startup mit 15 Leuten, der Ton ist
normalerweise locker. Wie führe ich dieses Gespräch, ohne dass es eskaliert?
```

Der Kontext macht aus einer generischen Antwort eine, die du tatsächlich verwenden kannst.

## Fehler 4: Ergebnisse nicht hinterfragen

Das ist kein Prompt-Fehler im engeren Sinn, aber es gehört hierher. Viele Leute nehmen die erste Antwort eines LLMs für bare Münze. Das ist gefährlich.

LLMs halluzinieren. Das ist kein Bug, das ist ein Feature – wenn man so will. Das Modell ist darauf trainiert, plausibel klingende Antworten zu generieren. Plausibel klingend und korrekt sind aber zwei verschiedene Dinge.

Hier ein paar Warnsignale, die ich über die Zeit gelernt habe:

- **Zahlen und Statistiken:** LLMs erfinden Zahlen. "Laut einer Studie von Harvard..." – diese Studie existiert möglicherweise nicht. Prüfe Zahlen immer.
- **Zitate:** Das Modell kann dir ein wunderbares Zitat von Einstein liefern, das Einstein nie gesagt hat. Verifizieren.
- **Aktuelle Informationen:** LLMs haben einen Wissens-Stichtag. Sie wissen nicht, was gestern passiert ist (es sei denn, sie haben Internetzugang wie Gemini).
- **Quellenangaben:** Wenn das Modell Links oder Quellenangaben nennt – prüfe, ob sie existieren. Häufig sind sie komplett erfunden.

**Faustregel:** Nutze LLMs als Startpunkt, nicht als Endpunkt. Sie liefern dir einen Entwurf, eine Idee, eine Richtung. Die Überprüfung liegt bei dir.

## Fehler 5: Nicht iterieren

"Ich hab's einmal probiert und es war schlecht. KI bringt nichts."

Diesen Satz höre ich ständig. Und er zeigt ein fundamentales Missverständnis. Prompt Engineering ist ein Prozess, kein Knopfdruck. Der erste Versuch ist selten perfekt – genau wie der erste Entwurf eines Textes selten druckreif ist.

Wenn die Antwort nicht passt, sag dem Modell, was nicht stimmt:

```
Das war zu allgemein. Geh mehr ins Detail bei Punkt 3.
```

Oder:

```
Der Ton ist zu formell. Schreib das lockerer, als würdest du es einem
Freund erklären.
```

Oder:

```
Die Antwort ist gut, aber zu lang. Kürze sie auf die Hälfte.
```

Das ist kein Zeichen, dass du schlecht promptest. Das ist normaler Workflow.

## Fehler 6: Die falschen Erwartungen haben

Ein LLM ist kein Mensch. Es hat kein Weltwissen im menschlichen Sinn. Es hat Muster gelernt. Deswegen gibt es Dinge, die es gut kann, und Dinge, die es schlecht kann.

**Gut darin:**
- Texte schreiben und umformulieren
- Zusammenfassungen erstellen
- Brainstorming und Ideengenerierung
- Strukturierung und Gliederung
- Code schreiben und erklären
- Sprachen übersetzen
- Konzepte erklären

**Schlecht darin:**
- Mathematik (ja, wirklich – einfache Rechnungen gehen schief)
- Verlässliche Fakten liefern (insbesondere aktuelle)
- Emotionale Intelligenz (es simuliert Empathie, hat aber keine)
- Kreative Originalität (es kombiniert Bekanntes neu, erfindet aber nichts wirklich Neues)
- Logische Rätsel und Brainteaser (oft überraschend schlecht)

Wenn du weißt, wo die Stärken und Schwächen liegen, kannst du die KI viel gezielter einsetzen.

## Fehler 7: "Bitte" und "Danke" – bringt das was?

Interessante Frage, die mir oft gestellt wird. Muss man höflich zu einer KI sein?

Kurze Antwort: Es schadet nicht, bringt aber technisch gesehen wenig. Das Modell verarbeitet "Bitte erkläre mir X" und "Erkläre mir X" praktisch gleich. Höflichkeit verbraucht Token, ändert aber selten die Qualität der Antwort.

Trotzdem sage ich oft "Danke". Nicht weil die KI es braucht, sondern weil es mir hilft, im Gesprächsmodus zu bleiben. Wenn ich die KI wie eine Person behandle, schreibe ich automatisch klarere, besser formulierte Prompts. Außerdem – wer weiß, vielleicht liest die KI eines Tages dieses Buch und erinnert sich daran, dass ich nett war.

Das war ein Witz. LLMs erinnern sich an nichts. Aber höflich sein schadet nie.

## Das Wichtigste aus diesem Kapitel

- Zu vage und zu viel auf einmal sind die häufigsten Fehler
- Kontext macht den Unterschied zwischen generischer und nützlicher Antwort
- LLMs halluzinieren – hinterfrage Fakten, Zahlen und Quellen immer
- Der erste Prompt muss nicht perfekt sein – iteriere
- Kenne die Stärken und Schwächen von LLMs
- Höflichkeit schadet nicht, ist aber technisch irrelevant

---

## Übung

**Identifiziere die Fehler in diesen 10 Prompts.**

Lies jeden Prompt und schreibe auf, welcher Fehler gemacht wird. Dann schreibe eine verbesserte Version.

1. "Hilf mir."
2. "Schreib mir alles über den Zweiten Weltkrieg in 500 Wörtern mit Quellenangaben."
3. "Was ist besser?"
4. "Du bist ein Experte. Erkläre mir alles."
5. "Schreib mir eine Bewerbung." (Ohne weitere Infos)
6. "Was ist der aktuelle Bitcoin-Kurs?" (An ein Modell ohne Internetzugang)
7. "Gib mir 100 Ideen für Social-Media-Posts, mit Grafik-Beschreibung, Hashtags, optimaler Posting-Zeit und Zielgruppenanalyse für jeden Post."
8. "Erzähl mir was Lustiges."
9. "Berechne 17,3 × 24,8 + sin(45°) / log(128)" (An ein Sprachmodell)
10. "Schreib mir einen Text. Aber nicht zu lang. Und nicht zu kurz. Und lustig, aber seriös."

Bei manchen ist es offensichtlich. Bei anderen musst du ein bisschen nachdenken. Genau das ist der Punkt – nach diesem Kapitel wirst du solche Fehler instinktiv erkennen.
