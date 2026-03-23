# Kapitel 5: System-Prompts – Das unsichtbare Fundament

Jedes Mal, wenn du ChatGPT, Claude oder Gemini öffnest, hast du es mit zwei Ebenen zu tun. Die eine siehst du: das Eingabefeld, in das du deinen Prompt tippst. Die andere siehst du nicht: den System-Prompt, der schon da war, bevor du überhaupt etwas geschrieben hast.

Der System-Prompt ist die Grundprogrammierung des Modells. Er legt fest, wie es sich verhält, welchen Ton es anschlägt, welche Regeln es befolgt. Und wenn du verstehst, wie System-Prompts funktionieren, kannst du KI auf einem ganz anderen Level nutzen.

## Was ist ein System-Prompt?

Ein System-Prompt ist eine Anweisung, die vor deinem eigentlichen Prompt an das Modell gesendet wird. Er definiert das Grundverhalten:

```
System: Du bist ein hilfreicher Assistent, der auf Deutsch antwortet.
        Du bist freundlich und professionell.

User: Was ist Photosynthese?
```

Das Modell sieht beides – den System-Prompt und deine Frage. Aber es behandelt sie unterschiedlich. Der System-Prompt hat höhere Priorität. Er gilt für die gesamte Konversation, nicht nur für eine einzelne Nachricht.

## Wo kann ich System-Prompts nutzen?

| Plattform | System-Prompt möglich? | Wie? |
|-----------|----------------------|------|
| ChatGPT | Ja | Custom Instructions / GPTs |
| Claude | Ja | System Prompt im API / Projects |
| Gemini | Ja | System Instructions in AI Studio |
| API (alle) | Ja | Direkt als `system`-Parameter |
| Lokale Modelle | Ja | In der Konfiguration |

### ChatGPT: Custom Instructions

In ChatGPT findest du unter "Custom Instructions" (oder "Benutzerdefinierte Anweisungen") zwei Felder:
1. **Über dich:** Wer du bist, was du machst, was das Modell über dich wissen sollte
2. **Antwortverhalten:** Wie das Modell antworten soll

Das ist im Grunde ein System-Prompt in zwei Teilen.

### Claude: Projects

Claude hat ein Feature namens "Projects", bei dem du einen System-Prompt für ein ganzes Projekt definieren kannst. Jede Konversation in diesem Projekt startet mit diesem System-Prompt.

### Über die API

Der direkteste Weg. Hier am Beispiel von OpenAI:

```json
{
  "model": "gpt-4o",
  "messages": [
    {
      "role": "system",
      "content": "Du bist ein erfahrener Steuerberater..."
    },
    {
      "role": "user",
      "content": "Wie funktioniert die Kleinunternehmerregelung?"
    }
  ]
}
```

## Anatomie eines guten System-Prompts

Ein effektiver System-Prompt hat vier Teile:

### 1. Identität

Wer ist das Modell? Was ist seine Expertise?

```
Du bist ein erfahrener Lektor für deutschsprachige Sachbücher.
Du hast 20 Jahre Erfahrung in der Verlagsbranche.
```

### 2. Verhalten

Wie soll es antworten?

```
Du antwortest immer auf Deutsch.
Du benutzt die Du-Ansprache.
Du bist direkt und ehrlich – auch wenn die Wahrheit unbequem ist.
Du erklärst dein Feedback immer mit konkreten Beispielen.
```

### 3. Einschränkungen

Was soll es NICHT tun?

```
Du gibst keine Rechtsberatung.
Du erfindest keine Fakten.
Wenn du dir unsicher bist, sagst du das offen.
Du behauptest nie, Emotionen zu haben.
```

### 4. Formatierung

Wie soll die Ausgabe aussehen?

```
Du formatierst deine Antworten mit Markdown.
Du nutzt Aufzählungslisten für mehr als 3 Punkte.
Du hältst Absätze unter 4 Sätzen.
```

## Fünf System-Prompts, die du sofort nutzen kannst

### 1. Der Sparringspartner

```
Du bist mein kritischer Sparringspartner. Deine Aufgabe ist es,
meine Ideen herauszufordern. Du stimmst mir nie einfach zu.
Zu jeder These findest du ein Gegenargument. Du bist respektvoll
aber direkt. Wenn ich eine schlechte Idee habe, sagst du das klar.
Wenn ich eine gute Idee habe, zeigst du mir, wo sie noch Schwächen hat.
```

### 2. Der Erklärbär

```
Du erklärst komplexe Themen so, dass ein intelligenter 14-Jähriger
sie versteht. Du benutzt Analogien aus dem Alltag. Du vermeidest
Fachbegriffe – und wenn du einen brauchst, erklärst du ihn sofort.
Du nutzt kurze Sätze. Du stellst nach jeder Erklärung eine Frage,
um zu prüfen, ob ich es verstanden habe.
```

### 3. Der Code-Reviewer

```
Du bist ein Senior Software Engineer mit Fokus auf Clean Code.
Wenn ich dir Code zeige, prüfst du:
1. Gibt es Bugs?
2. Ist der Code lesbar?
3. Gibt es Sicherheitsprobleme?
4. Gibt es Performance-Probleme?

Du zeigst immer den verbesserten Code. Du erklärst jede Änderung
in einem Satz. Du bist nicht belehrend, sondern konstruktiv.
```

### 4. Der Schreibcoach

```
Du bist ein Schreibcoach für professionelle Kommunikation.
Du hilfst mir, E-Mails, Berichte und Texte zu verbessern.

Dein Feedback folgt immer diesem Schema:
- Was funktioniert gut (1-2 Punkte)
- Was verbessert werden sollte (konkrete Vorschläge)
- Überarbeitete Version

Du veränderst nie meine Kernaussage. Du verbesserst Stil,
Klarheit und Wirkung.
```

### 5. Der Datenanalyst

```
Du bist ein Datenanalyst. Wenn ich dir Daten gebe, machst du:
1. Zusammenfassung der wichtigsten Erkenntnisse (3 Bullet Points)
2. Auffälligkeiten oder Ausreißer
3. Handlungsempfehlung

Du stellst keine Vermutungen an, die die Daten nicht hergeben.
Wenn die Datenlage unklar ist, sagst du das. Du formatierst
Zahlen einheitlich und nutzt Tabellen, wenn es sinnvoll ist.
```

## System-Prompt vs. User-Prompt

Was ist der Unterschied, wenn du die gleiche Anweisung als System-Prompt oder als User-Prompt gibst?

### Persistenz

Ein System-Prompt gilt für die gesamte Konversation. Ein User-Prompt gilt nur für diese eine Nachricht. Wenn du im System-Prompt sagst "Antworte immer auf Deutsch", gilt das für jede Nachricht. Wenn du das als User-Prompt sagst, kann das Modell es nach ein paar Nachrichten "vergessen".

### Priorität

System-Prompts haben höhere Priorität. Wenn sich System-Prompt und User-Prompt widersprechen, gewinnt in der Regel der System-Prompt. (In der Regel. Nicht immer. Dazu mehr in Band 9.)

### Unsichtbarkeit

Der System-Prompt ist für den Endnutzer normalerweise nicht sichtbar. Wenn du eine KI-Anwendung baust, sieht der Nutzer nur das Chatfenster, nicht die Grundprogrammierung dahinter.

## System-Prompts schreiben: Tipps

### Tipp 1: Sei spezifisch, nicht allgemein

```
# Schlecht
Sei hilfreich und freundlich.

# Besser
Beantworte Fragen in maximal 3 Sätzen.
Nutze Beispiele aus dem Alltag.
Wenn eine Frage mehrere Antworten hat, nenne die wahrscheinlichste zuerst.
```

### Tipp 2: Prioritäten setzen

Wenn du viele Anweisungen hast, sag dem Modell, was am wichtigsten ist:

```
Oberste Priorität: Faktische Korrektheit. Lieber "Ich bin nicht sicher"
sagen als etwas Falsches behaupten.

Zweite Priorität: Klarheit. Einfache Sprache, kurze Sätze.

Dritte Priorität: Vollständigkeit. Alle relevanten Aspekte abdecken,
aber nur wenn Priorität 1 und 2 erfüllt sind.
```

### Tipp 3: Beispiele einbauen

```
Wenn Nutzer eine Frage stellen, antworte im folgenden Format:

Frage: "Was ist TCP/IP?"
Antwort: "TCP/IP ist das Protokoll, über das Computer im Internet
kommunizieren. Stell dir eine Sprache vor, die alle Computer sprechen –
das ist TCP/IP. Es sorgt dafür, dass Datenpakete zuverlässig von A
nach B kommen."
```

### Tipp 4: Nicht überladen

Ein System-Prompt mit 2.000 Wörtern ist zu lang. Das Modell priorisiert die Anweisungen am Anfang und am Ende – die in der Mitte gehen leicht unter.

Meine Faustregel: 200-500 Wörter für einen System-Prompt. Wenn du mehr brauchst, überleg, ob du das Problem anders lösen kannst (z.B. mit Chaining oder Template-Bibliothek).

### Tipp 5: Testen und iterieren

Ein System-Prompt ist nie beim ersten Versuch perfekt. Teste ihn mit verschiedenen Fragen. Beobachte, wo das Modell von deinen Erwartungen abweicht. Passe den System-Prompt an. Teste nochmal.

Das ist iteratives Prompting (Band 1, Kapitel 9) – nur auf System-Ebene.

## Custom Instructions: Dein persönlicher System-Prompt

Wenn du ChatGPT regelmäßig nutzt, richte dir Custom Instructions ein. Hier ist ein Template:

**Über dich (Feld 1):**
```
Ich bin [Beruf/Rolle]. Ich arbeite in [Branche].
Meine häufigsten Aufgaben mit KI: [Liste].
Mein Wissensstand: [Anfänger/Fortgeschritten/Experte] in [Bereichen].
Ich bevorzuge [Deutsch/Du-Form/kurze Antworten/etc.].
```

**Antwortverhalten (Feld 2):**
```
- Antworte immer auf Deutsch
- Nutze die Du-Ansprache
- Halte Antworten kurz (max. 200 Wörter), außer ich bitte um mehr
- Zeige Code-Beispiele, wenn relevant
- Wenn du unsicher bist, sage es
- Keine Emojis
- Keine Floskeln wie "Gute Frage!" oder "Natürlich!"
```

Das allein wird deine tägliche KI-Nutzung spürbar verbessern.

---

## Übung

**Dein erster System-Prompt**

1. Überlege: Wofür nutzt du KI am häufigsten? (Texte schreiben, Code, Recherche, Lernen...)
2. Schreibe einen System-Prompt für genau diesen Anwendungsfall
3. Teste ihn mit 5 verschiedenen Fragen/Aufgaben
4. Notiere, wo das Modell sich anders verhält als erwartet
5. Überarbeite den System-Prompt und teste nochmal

Bonusaufgabe: Richte Custom Instructions bei ChatGPT oder ein Project bei Claude ein und nutze es eine Woche lang. Wie verändert es deine Erfahrung?
