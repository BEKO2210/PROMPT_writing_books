# Kapitel 6: Kontext ist alles

Wenn es ein einziges Wort gibt, das den Unterschied zwischen einem mittelmäßigen und einem großartigen Prompt ausmacht, dann ist es: Kontext.

Ich hab das in den vorherigen Kapiteln schon mehrfach erwähnt. Aber jetzt gehen wir richtig in die Tiefe. Denn Kontext geben ist eine Kunst, die man lernen kann – und die sich sofort auszahlt.

## Warum Kontext so wichtig ist

Ein LLM hat kein Gedächtnis über Sitzungen hinweg. Es weiß nicht, wer du bist. Es weiß nicht, was du gestern gefragt hast (es sei denn, es steht noch im selben Chat). Es weiß nicht, ob du 16 oder 60 bist, ob du Arzt oder Bäcker bist, ob du Deutsch als Muttersprache sprichst oder nicht.

Wenn du fragst "Wie investiere ich mein Geld?", dann weiß das Modell nicht:
- Wie viel Geld du hast
- Wie alt du bist
- Wie risikobereit du bist
- Ob du schon Erfahrung mit Investments hast
- In welchem Land du lebst (Steuerrecht!)
- Was dein Ziel ist (Altersvorsorge? Hausbau? Urlaub?)

Ohne diese Informationen bekommst du eine Standardantwort, die für niemanden wirklich passt. Mit diesen Informationen bekommst du eine Antwort, die tatsächlich hilfreich ist.

## Die 5 Kontext-Kategorien

Ich teile Kontext in fünf Kategorien ein. Du musst nicht immer alle verwenden – aber es hilft, sie im Kopf zu haben.

### 1. Wer bist du?

Deine Rolle, dein Hintergrund, deine Erfahrung.

```
Ich bin Grundschullehrerin mit 10 Jahren Berufserfahrung...
```

```
Ich bin Student im 3. Semester Informatik...
```

```
Ich bin Geschäftsführer eines mittelständischen Unternehmens
mit 50 Mitarbeitern...
```

### 2. Was ist die Situation?

Der Hintergrund, die Umstände, das Problem.

```
...und bereite eine Elternabend-Präsentation vor, bei der es
um den Einsatz von Tablets im Unterricht geht. Manche Eltern
sind skeptisch.
```

```
...und muss morgen eine Klausur in Algorithmen und Datenstrukturen
schreiben. Ich verstehe Rekursion noch nicht richtig.
```

### 3. Wer ist die Zielgruppe?

Für wen ist das Ergebnis bestimmt?

```
Die Zielgruppe sind Eltern ohne technisches Vorwissen.
```

```
Der Text ist für mein LinkedIn-Netzwerk – hauptsächlich HR-Manager
und Recruiter.
```

```
Das soll ein internes Memo für mein Team sein.
Die kennen den Kontext schon, ich muss nicht bei null anfangen.
```

### 4. Was hast du schon versucht?

Das ist ein Kontext, den fast niemand gibt – aber der unglaublich hilfreich ist.

```
Ich habe schon versucht, das Problem mit einer For-Schleife zu lösen,
aber ich bekomme einen IndexError. Hier ist mein Code: [...]
```

```
Ich habe schon 3 verschiedene Entwürfe für die Einleitung geschrieben,
aber alle klingen zu steif. Hier ist der letzte Versuch: [...]
```

Wenn das Modell weiß, was nicht funktioniert hat, kann es dir bessere Alternativen vorschlagen.

### 5. Was ist das Ziel?

Was willst du mit dem Ergebnis machen? Was ist das große Ziel dahinter?

```
Ich brauche den Text für eine Bewerbung bei einem DAX-Konzern.
```

```
Die Analyse soll als Entscheidungsgrundlage dienen, ob wir in
einen neuen Markt eintreten.
```

```
Ich will den Prompt später als Template wiederverwenden –
er sollte also allgemein genug sein, dass ich nur die Details austauschen muss.
```

## Kontext in Aktion: Vorher und Nachher

Lass mich dir drei Beispiele zeigen, die den Unterschied deutlich machen.

### Beispiel 1: Fitness

**Ohne Kontext:**
```
Erstelle mir einen Trainingsplan.
```

*Ergebnis: Ein generischer Plan mit Kniebeugen, Liegestützen, Joggen – für irgendjemanden.*

**Mit Kontext:**
```
Erstelle mir einen Trainingsplan. Ich bin 34, männlich, 185cm, 92kg.
Ich war die letzten 2 Jahre inaktiv, hatte aber vorher Erfahrung
mit Krafttraining. Ich habe 3 Tage pro Woche jeweils 60 Minuten Zeit.
Zugang zu einem Fitnessstudio. Ziel: Wieder fit werden und 5kg abnehmen
in 3 Monaten. Ich habe leichte Knieprobleme – keine Sprungübungen bitte.
```

*Ergebnis: Ein maßgeschneiderter Plan, der deine Einschränkungen berücksichtigt.*

### Beispiel 2: Texterstellung

**Ohne Kontext:**
```
Schreib mir eine Produktbeschreibung.
```

**Mit Kontext:**
```
Schreib mir eine Produktbeschreibung für unseren neuen kabellosen
Bluetooth-Kopfhörer "SoundFlex Pro". Zielgruppe: Pendler und
Home-Office-Arbeiter, 25-45 Jahre. USP: 40 Stunden Akkulaufzeit
und aktive Geräuschunterdrückung. Preis: 89 Euro.
Ton: modern und einladend, aber nicht reißerisch.
Für unsere Website, maximal 150 Wörter.
Wir konkurrieren mit Sony und Bose – also nicht billig wirken.
```

### Beispiel 3: Problemlösung

**Ohne Kontext:**
```
Mein Team funktioniert nicht. Was soll ich tun?
```

**Mit Kontext:**
```
Ich leite ein 6-köpfiges Marketing-Team. Seit ein neuer Mitarbeiter
vor 3 Monaten dazugekommen ist, gibt es Spannungen. Zwei ältere
Teammitglieder fühlen sich übergangen, weil der Neue viele Aufgaben
direkt von der Geschäftsführung bekommt. Die Stimmung ist merklich
schlechter geworden, Deadlines werden knapp eingehalten. Ich möchte
die Situation lösen, ohne jemanden bloßzustellen. Was sind meine
Optionen?
```

Du siehst den Unterschied. Beim ersten Prompt bekommst du "Versuchen Sie, offene Kommunikation zu fördern" und ähnlichen Standardkram. Beim zweiten Prompt bekommst du eine Analyse der spezifischen Situation mit konkreten Handlungsempfehlungen.

## Wie viel Kontext ist zu viel?

Gute Frage. Kann man es übertreiben? Theoretisch ja. Wenn dein Prompt länger ist als die Antwort, die du erwartest, machst du wahrscheinlich etwas falsch.

Aber in der Praxis erlebe ich das Gegenteil: Die meisten Leute geben zu wenig Kontext, nicht zu viel. Mein Rat: Lieber eine Information zu viel als eine zu wenig. Das Modell ignoriert, was es nicht braucht. Aber es kann nicht erraten, was du nicht sagst.

Eine Ausnahme: Sensible Daten. Gib keine Passwörter, Kreditkartennummern, vertrauliche Firmendaten oder persönliche Informationen ein, die du nicht in der Cloud haben willst. Die Daten werden von den Anbietern verarbeitet – wie genau, steht in deren Datenschutzerklärung. Im Zweifel: anonymisiere.

## Der "Goldene Satz" – ein Trick, den ich oft benutze

Wenn ich nicht weiß, wie viel Kontext ich geben soll, starte ich mit einem "Goldenen Satz". Das ist ein einzelner Satz, der die wichtigste Kontextinformation enthält.

```
Ich bin Lehrer an einer Berufsschule und unterrichte Jugendliche
zwischen 16 und 18 Jahren.
```

Dieser eine Satz verändert jede Antwort. Das Modell passt automatisch Sprache, Komplexität und Beispiele an.

Probier es aus: Stell eine beliebige Frage einmal ohne und einmal mit dem Goldenen Satz davor. Der Unterschied ist oft verblüffend.

## Das Wichtigste aus diesem Kapitel

- Kontext ist der wichtigste Baustein eines guten Prompts
- 5 Kontext-Kategorien: Wer bist du, Situation, Zielgruppe, was hast du versucht, was ist das Ziel
- Lieber zu viel Kontext als zu wenig
- Sensible Daten anonymisieren oder weglassen
- Der "Goldene Satz" – ein Satz Kontext kann alles verändern

---

## Übung

**Nimm 3 einfache Prompts und füge Kontext hinzu.**

Hier sind drei bewusst kontextlose Prompts:

1. "Wie lerne ich besser?"
2. "Schreib mir einen Brief."
3. "Was soll ich beruflich machen?"

Für jeden Prompt:
- Überlege dir eine konkrete Person mit einer konkreten Situation
- Füge mindestens 3 der 5 Kontext-Kategorien hinzu
- Teste beide Versionen (ohne und mit Kontext) in einem LLM
- Vergleiche die Ergebnisse

Bonus: Versuche den "Goldenen Satz" – finde für jedes Szenario den einen Satz, der den größten Unterschied macht.
