# Kapitel 7: Rollen und Personas – Die KI in eine Rolle schlüpfen lassen

Stell dir vor, du fragst jemanden nach einem Trainingsplan. Wenn du einen zufälligen Passanten fragst, bekommst du eine andere Antwort als von einem Personal Trainer. Gleiche Frage, völlig anderes Ergebnis.

Bei LLMs funktioniert das genauso. Und das Beste: Du kannst der KI sagen, wer sie sein soll.

## "Du bist ein..." – So weist du Rollen zu

Der einfachste Weg, eine Rolle zuzuweisen, ist ein Satz am Anfang deines Prompts:

```
Du bist ein erfahrener Steuerberater mit 20 Jahren Berufserfahrung
in Deutschland. Ein Kunde fragt dich: [...]
```

```
Du bist eine freundliche Grundschullehrerin. Erkläre einem 8-Jährigen,
warum es Jahreszeiten gibt.
```

```
Du bist ein kritischer Lektor, der kein Blatt vor den Mund nimmt.
Lies folgenden Text und sag mir ehrlich, was daran schlecht ist: [...]
```

Was passiert hier? Du gibst dem Modell einen Rahmen. Es weiß jetzt, aus welcher Perspektive es antworten soll, welchen Wortschatz es verwenden soll und welches Niveau angemessen ist.

## Warum Rollen funktionieren

Erinnere dich an Kapitel 2: LLMs haben während des Trainings Millionen von Texten gelesen, die von verschiedenen "Typen" von Menschen geschrieben wurden. Ärzte schreiben anders als Comedians. Professoren formulieren anders als Blogger.

Wenn du dem Modell sagst "Du bist ein erfahrener Koch", dann greift es auf die Muster zurück, die es von Köchen, Kochbüchern und Food-Bloggern gelernt hat. Es verwendet Fachbegriffe wie "blanchieren" statt "kurz in kochendes Wasser tun". Es strukturiert die Antwort wie ein Rezept. Es denkt an Dinge wie Garzeiten und Würzung.

Das ist kein Trick. Es ist die Art, wie diese Modelle funktionieren – und du nutzt es zu deinem Vorteil.

## 7 Rollen, die besonders gut funktionieren

Hier sind Rollen, die ich regelmäßig benutze und die konstant gute Ergebnisse liefern:

### 1. Der Experte

```
Du bist ein Experte für [Thema] mit [X] Jahren Erfahrung.
```

Funktioniert für fast alles. Steuerrecht, Gartenarbeit, Autoversicherungen. Die KI antwortet fundierter, wenn sie denkt, sie sei ein Experte.

### 2. Der Lehrer

```
Du bist ein geduldiger Lehrer, der Anfängern komplexe Themen
in einfachen Worten erklärt.
```

Perfekt, wenn du etwas lernen willst. Die Antworten sind didaktisch aufgebaut, mit Beispielen und ohne Fachjargon.

### 3. Der kritische Reviewer

```
Du bist ein strenger aber fairer Kritiker. Analysiere [Text/Idee/Plan]
und zeige Schwächen auf, die ich übersehen habe.
```

Einer meiner Favoriten. Die meisten Leute benutzen KI nur zum Bestätigen. Aber sie ist am nützlichsten, wenn sie dir sagt, was nicht funktioniert.

### 4. Der Berater

```
Du bist ein erfahrener Business-Berater. Dein Kunde kommt zu dir mit
folgendem Problem: [...]
```

Die KI gibt dir dann keine Schulbuch-Antwort, sondern eine praxisorientierte Empfehlung.

### 5. Der Übersetzer/Vereinfacher

```
Du bist ein Übersetzer, der komplizierte Fachtexte in einfache
Alltagssprache übersetzt. Kein Wort mit mehr als 3 Silben.
```

Klingt lustig, funktioniert aber hervorragend, wenn du einen komplizierten Text für Laien aufbereiten musst.

### 6. Der kreative Partner

```
Du bist ein kreativer Brainstorming-Partner. Wirf mir ungewöhnliche
Ideen zu, auch wenn sie erstmal verrückt klingen. Wir filtern später.
```

Das gibt der KI die Erlaubnis, wild zu denken, statt die sicherste Antwort zu geben.

### 7. Der Devil's Advocate

```
Du bist ein Devil's Advocate. Finde Gegenargumente zu meiner Position,
auch wenn du denkst, dass ich Recht habe. Ich brauche die andere Perspektive.
```

Unglaublich nützlich für Entscheidungsfindung und Argumentationsschärfung.

## Personas: Rollen mit Persönlichkeit

Eine Persona geht noch einen Schritt weiter als eine Rolle. Statt nur "Experte" zu sagen, gibst du der KI eine komplette Persönlichkeit.

**Rolle:**
```
Du bist ein Marketing-Experte.
```

**Persona:**
```
Du bist Sarah, 42, Marketingleiterin bei einem mittelständischen
Unternehmen in Hamburg. Du arbeitest seit 15 Jahren im B2B-Marketing,
hast schon drei Firmen beraten und bist bekannt für deine direkte,
no-bullshit Kommunikation. Du magst keine Buzzwords und sagst lieber
"das funktioniert nicht" als "da gibt es Optimierungspotenzial".
```

Je detaillierter die Persona, desto konsistenter und charaktervoller die Antworten. Das ist besonders nützlich, wenn du:
- Fiktive Interviews für Marktforschung simulierst
- Einen konsistenten Charakter für eine Geschichte brauchst
- Verschiedene Perspektiven auf ein Problem haben willst

## Mehrere Perspektiven einholen

Ein richtig starker Move: Lass die KI aus verschiedenen Rollen auf dieselbe Frage antworten.

```
Ich überlege, mich selbstständig zu machen. Gib mir Rat aus drei
verschiedenen Perspektiven:
1. Ein erfolgreicher Unternehmer, der seit 10 Jahren selbstständig ist
2. Ein Steuerberater
3. Ein Psychologe, der sich auf Stress und Work-Life-Balance spezialisiert hat

Jede Perspektive: 3-4 Sätze, klar getrennt.
```

Du bekommst drei verschiedene Blickwinkel in einer Antwort. Der Unternehmer sagt dir, worauf es ankommt. Der Steuerberater warnt dich vor finanziellen Fallstricken. Der Psychologe fragt, ob du emotional bereit bist.

Das ist Beratung auf einem Niveau, für das du sonst drei verschiedene Termine brauchst.

## Rollen kombinieren mit anderen Bausteinen

Rollen funktionieren am besten, wenn du sie mit den anderen Bausteinen aus Kapitel 4 kombinierst:

```
Du bist ein erfahrener UX-Designer (ROLLE).
Ich baue eine App für Senioren, die ihre Medikamente verwalten sollen (KONTEXT).
Erstelle eine Liste von 5 Design-Prinzipien, die ich beachten sollte (AUFGABE).
Jedes Prinzip: Überschrift + 2 Sätze Erklärung + ein konkretes Beispiel (FORMAT).
Vermeide Fachjargon – mein Chef ist kein Designer (EINSCHRÄNKUNG).
```

Siehst du, wie alles zusammenspielt? Rolle, Kontext, Aufgabe, Format, Einschränkung – die fünf Bausteine aus Kapitel 4, hier in Aktion.

## Typische Fehler bei Rollen

**Fehler 1: Zu generisch**
```
Du bist schlau. Hilf mir.
```
Das ist keine Rolle, das ist ein Wunsch. Sei spezifisch.

**Fehler 2: Widersprüchliche Rollen**
```
Du bist ein konservativer Finanzberater, der riskante Investments empfiehlt.
```
Das Modell wird verwirrt sein und inkonsistent antworten.

**Fehler 3: Die Rolle vergessen**
Wenn du in einem längeren Chat die Rolle nur am Anfang zuweist, kann das Modell sie nach einigen Nachrichten "vergessen". Erinnere es gelegentlich: "Bleib bitte in deiner Rolle als Steuerberater."

## Das Wichtigste aus diesem Kapitel

- Rollen geben dem Modell einen Rahmen für Perspektive und Fachsprache
- "Du bist ein..." ist der einfachste Einstieg
- Personas (mit Persönlichkeit) liefern konsistentere Ergebnisse als generische Rollen
- Mehrere Perspektiven in einem Prompt liefern vielseitigere Antworten
- Rollen mit den anderen 4 Bausteinen kombinieren für beste Ergebnisse

---

## Übung

**Erstelle 5 verschiedene Rollen-Prompts zum selben Thema.**

Wähle ein Thema, das dich interessiert. Zum Beispiel: "Soll ich auf Social Media aktiver werden?"

Jetzt schreibe 5 Prompts – immer mit einer anderen Rolle:
1. Ein Social-Media-Manager
2. Ein Psychologe
3. Ein Datenschutz-Experte
4. Ein erfolgreicher Influencer
5. Ein Großvater, der skeptisch gegenüber Technologie ist

Teste alle 5 im selben LLM und vergleiche die Antworten. Achte darauf:
- Wie unterscheidet sich die Sprache?
- Welche Argumente kommen nur in bestimmten Rollen vor?
- Welche Perspektive war am überraschendsten?

Das ist Prompt Engineering in Aktion: Durch die Rolle steuerst du nicht nur *was* die KI sagt, sondern *wie* und *aus welcher Perspektive* sie es sagt.
