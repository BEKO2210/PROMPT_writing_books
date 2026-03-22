# Kapitel 4: Anatomie eines guten Prompts

Du hast jetzt deine ersten Prompts geschrieben. Manche haben gut funktioniert, andere weniger. Aber woran liegt das eigentlich? Was macht einen Prompt gut – und was macht ihn schlecht?

In diesem Kapitel zerlege ich gute Prompts in ihre Einzelteile. Danach wirst du verstehen, warum manche Prompts goldene Ergebnisse liefern und andere nur Standardbrei.

## Die 5 Bausteine eines guten Prompts

Ich hab mir angewöhnt, jeden Prompt gedanklich in fünf Bausteine aufzuteilen. Nicht jeder Prompt braucht alle fünf – aber je mehr du davon verwendest, desto präziser wird das Ergebnis.

### 1. Die Aufgabe (Was soll die KI tun?)

Das ist der offensichtlichste Teil, aber viele Leute machen es sich hier zu einfach. "Schreib mir was über Marketing" ist eine Aufgabe. Aber eine miese.

**Vage:** "Schreib mir was über Marketing."
**Besser:** "Schreib mir eine Einleitung für einen Blogartikel über E-Mail-Marketing für kleine Unternehmen."
**Noch besser:** "Schreib mir eine Einleitung (maximal 100 Wörter) für einen Blogartikel über E-Mail-Marketing für kleine Unternehmen mit weniger als 10 Mitarbeitern."

Siehst du, wie jede Version spezifischer wird? Spezifisch schlägt vage. Immer.

### 2. Der Kontext (Was muss die KI wissen?)

Kontext ist das, was die meisten Anfänger weglassen – und was den größten Unterschied macht. Das Modell weiß nicht, wer du bist, was du schon probiert hast, oder warum du die Frage stellst.

**Ohne Kontext:**
```
Wie schreibe ich eine Bewerbung?
```

**Mit Kontext:**
```
Ich bin 28, habe 3 Jahre Erfahrung als Grafikdesigner in einer Agentur
und bewerbe mich jetzt bei einem Tech-Startup als UI/UX Designer.
Wie sollte ich mein Anschreiben aufbauen?
```

Beim ersten Prompt bekommst du eine generische Antwort, die für jeden und niemanden passt. Beim zweiten bekommst du eine maßgeschneiderte Anleitung.

### 3. Das Format (Wie soll die Antwort aussehen?)

Du kannst dem Modell sagen, in welchem Format es antworten soll. Liste? Tabelle? Fließtext? Aufzählung mit Nummern? Bullet Points? Kurz oder lang?

```
Gib mir 5 Ideen für ein Firmenevent.
Format: Nummerierte Liste. Zu jeder Idee ein Satz Beschreibung und eine
grobe Kostenschätzung.
```

Ohne Formatangabe entscheidet das Modell selbst – und das Ergebnis passt dann oft nicht zu dem, was du brauchst.

### 4. Der Ton (Wie soll es klingen?)

Formell oder locker? Akademisch oder umgangssprachlich? Ernst oder humorvoll? Das alles kannst du steuern.

```
Erkläre Photosynthese. Schreib so, als würdest du es einem 10-Jährigen erklären.
```

vs.

```
Erkläre Photosynthese auf dem Niveau einer Biologie-Vorlesung im ersten Semester.
```

Gleiche Frage, komplett andere Antwort. Der Ton macht's.

### 5. Einschränkungen (Was soll die KI NICHT tun?)

Manchmal ist es genauso wichtig zu sagen, was du nicht willst.

```
Erkläre mir, wie eine Blockchain funktioniert.
Verwende keine technischen Fachbegriffe.
Keine Analogien mit Banken oder Geld.
Maximal 200 Wörter.
```

Einschränkungen sind wie Leitplanken – sie halten die Antwort auf der Spur.

## Vorher/Nachher: 5 Prompts im Vergleich

Jetzt wird's konkret. Ich zeige dir fünf Prompts in der "vorher"-Version (wie sie die meisten Leute schreiben) und in der "nachher"-Version (mit den 5 Bausteinen).

### Beispiel 1: Rezept

**Vorher:**
```
Gib mir ein Rezept.
```
*Ergebnis: Irgendein zufälliges Rezept. Vielleicht Spaghetti Bolognese, vielleicht Sushi.*

**Nachher:**
```
Gib mir ein vegetarisches Rezept für ein Abendessen unter der Woche.
Es sollte maximal 30 Minuten dauern und mit Zutaten funktionieren, die
man in jedem Supermarkt bekommt. Für 2 Personen.
Format: Zutatenliste + Schritt-für-Schritt-Anleitung.
```
*Ergebnis: Ein passendes Rezept, das du tatsächlich nachkochen kannst.*

### Beispiel 2: E-Mail

**Vorher:**
```
Schreib mir eine E-Mail an meinen Chef.
```

**Nachher:**
```
Schreib mir eine höfliche, aber bestimmte E-Mail an meinen Vorgesetzten.
Ich möchte um ein Gespräch über eine Gehaltserhöhung bitten.
Ich bin seit 2 Jahren in der Firma und habe zuletzt ein großes Projekt
erfolgreich abgeschlossen. Ton: professionell, aber nicht unterwürfig.
Länge: maximal 150 Wörter.
```

### Beispiel 3: Lernen

**Vorher:**
```
Erkläre mir Python.
```

**Nachher:**
```
Ich möchte Python lernen und habe keine Programmiererfahrung.
Erstelle mir einen Lernplan für die ersten 4 Wochen.
Pro Woche: 1 Thema, 1 kurze Erklärung, 1 praktische Übung.
Halte es einfach – keine fortgeschrittenen Konzepte.
```

### Beispiel 4: Brainstorming

**Vorher:**
```
Gib mir Geschäftsideen.
```

**Nachher:**
```
Ich lebe in einer deutschen Kleinstadt (30.000 Einwohner), habe ein Budget
von 10.000 Euro und kann 20 Stunden pro Woche investieren.
Gib mir 5 realistische Geschäftsideen, die ich nebenberuflich starten könnte.
Zu jeder Idee: Was ist es, warum könnte es funktionieren, was ist das Risiko?
```

### Beispiel 5: Texterstellung

**Vorher:**
```
Schreib mir einen Social-Media-Post.
```

**Nachher:**
```
Schreib mir einen LinkedIn-Post über die Wichtigkeit von Weiterbildung
im Bereich KI. Zielgruppe: Berufstätige zwischen 30-50.
Ton: motivierend, aber nicht aufdringlich. Kein Corporate-Sprech.
Länge: 100-150 Wörter. Inklusive einem konkreten Call-to-Action am Ende.
```

## Spezifisch vs. Vage – Warum der Unterschied so groß ist

Ich bekomme oft die Frage: "Muss ich wirklich so viele Details angeben? Das Modell ist doch intelligent genug, um zu verstehen, was ich meine."

Die Antwort ist: Nein, ist es nicht. Nicht weil es dumm wäre, sondern weil es dein Gedankenleser nicht ist.

Wenn du in ein Taxi steigst und sagst "Fahren Sie los", dann fährt der Fahrer irgendwohin. Wenn du sagst "Bitte zum Hauptbahnhof, und nehmen Sie nicht die Autobahn, da ist Stau", dann kommst du an, wo du hinwillst.

LLMs funktionieren genauso. Sie brauchen klare Anweisungen. Nicht weil sie bockig sind, sondern weil sie *alles* können – und deswegen nicht wissen, was du gerade willst, wenn du es nicht sagst.

Heißt das, dass jeder Prompt ein Roman sein muss? Nein. Für eine einfache Frage reicht eine einfache Frage. "Was ist die Hauptstadt von Australien?" braucht keinen Kontext. Aber für alles, was über eine Faktenfrage hinausgeht, gilt: Mehr Details = bessere Ergebnisse.

## Eine Faustregel, die mir immer hilft

Bevor ich einen Prompt schreibe, stelle ich mir diese Frage:

*"Wenn ich das einem sehr kompetenten Praktikanten am ersten Tag sagen würde – hätte er genug Informationen, um genau das zu liefern, was ich will?"*

Wenn die Antwort nein ist, fehlt was. Dann füge ich Kontext, Format oder Einschränkungen hinzu. Wenn die Antwort ja ist, drücke ich Enter.

## Das Wichtigste aus diesem Kapitel

- Gute Prompts haben bis zu 5 Bausteine: Aufgabe, Kontext, Format, Ton, Einschränkungen
- Nicht jeder Prompt braucht alle 5 – aber mehr ist meistens besser
- Spezifische Prompts schlagen vage Prompts in jeder Kategorie
- Stell dir die Praktikanten-Frage: Hat das Modell genug Info, um zu liefern?

---

## Übung

**Verbessere diese 5 schlechten Prompts.**

Nimm jeden der folgenden Prompts und schreibe eine verbesserte Version – mit so vielen der 5 Bausteine wie möglich.

1. "Schreib mir einen Text."
2. "Was soll ich essen?"
3. "Hilf mir bei meiner Präsentation."
4. "Erkläre mir Wirtschaft."
5. "Schreib mir eine Geschichte."

Teste sowohl die Original-Version als auch deine verbesserte Version in einem LLM deiner Wahl. Vergleiche die Ergebnisse. Du wirst den Unterschied sofort sehen.
