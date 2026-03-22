# Kapitel 3: Negative Prompts – Sagen, was du NICHT willst

Manchmal ist es einfacher zu sagen, was du nicht willst, als zu beschreiben, was du willst.

Stell dir vor, du bestellst beim Friseur. Du könntest sagen: "Ich möchte einen mittellangen Stufenschnitt mit leichter Texturierung, natürlichem Fall und Volumen im Deckhaar." Oder du sagst: "Nicht zu kurz, kein Pony, keine Stufen, die abstehen." Beide Ansätze führen zum Ziel – aber der zweite ist manchmal schneller und klarer.

Das gleiche Prinzip funktioniert bei Prompts.

## Was sind negative Prompts?

Negative Prompts sind Anweisungen, die dem Modell sagen, was es vermeiden soll. Statt zu beschreiben, was du willst, beschreibst du, was du nicht willst.

```
Schreibe einen Blogartikel über Produktivität.

NICHT verwenden:
- Keine Aufzählungslisten
- Keine Zitate von berühmten Persönlichkeiten
- Keine Floskeln wie "in der heutigen schnelllebigen Welt"
- Keine Tipps, die mit "Steh früh auf" anfangen
```

Das Modell weiß jetzt genau, was es vermeiden soll. Und oft ist das Ergebnis besser, als wenn du versuchst, den gewünschten Stil positiv zu beschreiben.

## Warum negative Prompts funktionieren

### 1. Sie eliminieren vorhersagbares Verhalten

LLMs haben Muster. Bei bestimmten Themen produzieren sie fast immer die gleichen Phrasen, die gleichen Strukturen, die gleichen Beispiele. Ein negativer Prompt durchbricht diese Muster.

Wenn du sagst: "Schreib über Zeitmanagement", bekommst du mit 80-prozentiger Wahrscheinlichkeit etwas über die Eisenhower-Matrix und "Iss den Frosch zuerst". Sagst du: "Schreib über Zeitmanagement, aber erwähne weder die Eisenhower-Matrix noch 'Eat the Frog'", zwingt das Modell, kreativer zu werden.

### 2. Sie sind präziser als positive Beschreibungen

"Schreibe sachlich" kann vieles bedeuten. "Kein Ausrufezeichen, keine rhetorischen Fragen, keine emotionalen Adjektive" ist glasklar.

### 3. Sie fangen bekannte Probleme ab

Du weißt aus Erfahrung, welche Fehler das Modell bei bestimmten Aufgaben macht. Negative Prompts lassen dich diese Fehler proaktiv verhindern.

## Kategorien negativer Prompts

### Ton und Stil

```
Schreibe eine Unternehmenspräsentation.

Vermeide:
- Marketing-Sprech ("revolutionär", "einzigartig", "Synergien")
- Passive Konstruktionen
- Sätze über 20 Wörter
- Buzzwords ohne Erklärung
```

### Inhalt

```
Erkläre Machine Learning für Anfänger.

Nicht verwenden:
- Keine mathematischen Formeln
- Keine Fachbegriffe ohne Erklärung
- Kein Vergleich mit dem menschlichen Gehirn
- Nicht erwähnen: Terminator, Skynet, Roboter-Übernahme
```

### Format und Struktur

```
Schreibe einen Erfahrungsbericht.

Nicht:
- Keine Aufzählungen oder Bullet Points
- Keine Zwischenüberschriften
- Keine Einleitung à la "In diesem Artikel..."
- Kein Fazit-Absatz mit "Zusammenfassend..."
```

### Verhalten

```
Beantworte die folgende Fachfrage.

Regeln:
- Sage nicht "Gute Frage!"
- Beginne die Antwort nicht mit "Natürlich!"
- Wenn du dir unsicher bist, sage es direkt statt zu raten
- Keine unnötigen Disclaimer wie "Es ist wichtig zu beachten..."
```

## Die Kombination: Positiv + Negativ

Die stärksten Prompts kombinieren positive und negative Anweisungen:

```
### Aufgabe
Schreibe eine Willkommens-E-Mail für neue Newsletter-Abonnenten.

### Do's (machen)
- Persönliche Ansprache mit "du"
- Konkreten Nutzen in den ersten 2 Sätzen
- Einen klaren nächsten Schritt (CTA)
- Maximal 100 Wörter

### Don'ts (vermeiden)
- Kein "Vielen Dank für deine Anmeldung" als ersten Satz
- Keine Aufzählung aller Newsletter-Themen
- Kein Link zu Social Media
- Keine Emojis
```

Die Do's sagen, wohin es gehen soll. Die Don'ts verhindern, dass das Modell in seine Standard-Muster fällt. Zusammen geben sie einen präzisen Korridor vor.

## Negative Prompts bei Textbearbeitung

Besonders mächtig sind negative Prompts, wenn du bestehende Texte überarbeiten lässt:

```
Überarbeite den folgenden Text.

Behalte bei:
- Den Inhalt und alle Fakten
- Die Struktur (Absätze, Reihenfolge)
- Den informellen Ton

Ändere nicht:
- Fachbegriffe nicht vereinfachen
- Zahlen nicht runden
- Keine neuen Informationen hinzufügen
- Keine Absätze zusammenlegen oder aufteilen

Verbessere:
- Grammatik und Rechtschreibung
- Satzfluss
- Wortwiederholungen

"""
[Text einfügen]
"""
```

Durch die klare "Ändere nicht"-Liste weiß das Modell genau, wo die Grenzen sind. Ohne diese Einschränkungen würde es oft zu viel "verbessern" und den Charakter des Textes verändern.

## Wie viele negative Anweisungen sind zu viel?

Gute Frage. Meine Faustregel:

- **3–5 negative Anweisungen:** Ideal. Fokussiert und klar.
- **6–8:** Noch okay, wenn die Aufgabe komplex ist.
- **Mehr als 8:** Du versuchst wahrscheinlich, zu viel zu kontrollieren. Überleg, ob du stattdessen positive Anweisungen nutzen kannst.

Ein Prompt, der nur aus Verboten besteht, ist wie eine Straße, die nur aus Schildern mit "Hier nicht lang" besteht. Irgendwann weiß niemand mehr, wo es eigentlich hingehen soll.

## Das Spezifitäts-Prinzip

Negative Prompts funktionieren am besten, wenn sie spezifisch sind:

```
# Zu vage
Kein schlechter Schreibstil.

# Besser
Keine Passivsätze.
Keine Sätze über 25 Wörter.
Keine Nominalisierungen (statt "die Durchführung" → "durchführen").
```

```
# Zu vage
Nicht zu formell.

# Besser
Kein "Sie", stattdessen "du".
Keine Konjunktiv-II-Formen ("würde", "könnte").
Keine lateinischen Fachbegriffe.
```

Je konkreter das Verbot, desto zuverlässiger wird es befolgt.

## Negative Prompts für Bildgenerierung

Auch bei Bild-KIs wie DALL-E oder Midjourney funktionieren negative Prompts – dort sogar besonders gut. Aber das ist Thema von Band 5 (Kreatives Prompting). Hier nur ein kurzer Vorgeschmack:

```
Ein Porträtfoto einer Geschäftsfrau in einem modernen Büro.

Negative prompt: cartoon, illustration, anime, deformed hands,
blurry, low quality, text, watermark, oversaturated
```

Die negative Anweisung verhindert die häufigsten Probleme bei KI-generierten Bildern.

## Praxisbeispiel: Ein ganzer Workflow

Aufgabe: Du brauchst einen LinkedIn-Post über eine Branchenkonferenz, die du besucht hast.

```
Schreibe einen LinkedIn-Post über meinen Besuch auf der
Tech-Konferenz "Digital Summit 2026" in Berlin.

### Inhalt einbauen
- 3 wichtigste Erkenntnisse (ich erfinde sie, du formulierst sie aus)
- 1. KI verändert nicht Jobs, sondern Aufgaben innerhalb von Jobs
- 2. Die beste KI-Strategie beginnt mit einem konkreten Problem, nicht mit Technologie
- 3. Interdisziplinäre Teams liefern bessere KI-Projekte ab als reine Tech-Teams

### Nicht verwenden
- Kein "Ich bin so dankbar für diese Erfahrung"
- Kein "Key Takeaways" oder "Learnings" als Buzzwords
- Keine Hashtag-Flut am Ende (maximal 3)
- Kein "Agree? 👇" oder ähnliche Engagement-Bait-Fragen
- Keine Emojis am Anfang jeder Zeile
- Nicht mit "Wow" oder "Mind-blowing" anfangen

### Format
- Maximal 150 Wörter
- Erster Satz: eine provokante oder überraschende Aussage
- Kurze Absätze (2-3 Sätze)
```

Das Ergebnis wird ein Post sein, der nicht nach den 1.000 anderen LinkedIn-Konferenz-Posts klingt. Weil die negativen Prompts genau die Klischees verhindern, die LLMs bei "LinkedIn-Post" standardmäßig produzieren.

---

## Übung

**Die "Was ich nicht will"-Liste**

1. Nimm eine Aufgabe, die du regelmäßig mit KI erledigst (E-Mails schreiben, Texte zusammenfassen, Ideen generieren)
2. Schreibe den Prompt einmal nur mit positiven Anweisungen
3. Schreibe ihn nochmal nur mit negativen Anweisungen
4. Schreibe eine dritte Version, die beides kombiniert
5. Teste alle drei Versionen und vergleiche die Ergebnisse

Notiere: Welche Version hat das beste Ergebnis geliefert? Bei welcher Version warst du am überraschtesten vom Output?
