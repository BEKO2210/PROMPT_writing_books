# Kapitel 2: Storytelling mit KI – Geschichten, die fesseln

"Schreib mir eine Geschichte über einen Drachen." Das kann jeder prompten. Das Ergebnis? Generisch. Vorhersagbar. Langweilig.

Dieses Kapitel zeigt dir, wie du aus "schreib mir eine Geschichte" ein echtes Storytelling-Werkzeug machst.

## Warum die meisten KI-Geschichten schlecht sind

Drei Gründe:

1. **Zu vage Prompts.** "Schreib eine Geschichte" ist wie "Koch mir was". Klar, du bekommst etwas. Aber ob es dir schmeckt, ist Zufall.

2. **Keine Struktur.** Gute Geschichten haben einen Spannungsbogen. KI produziert ohne Anleitung oft Aufzählungen von Ereignissen statt einer Story mit Dramaturgie.

3. **KI-Standardsprache.** Jedes LLM hat stilistische Muster, die es bevorzugt. "Die Sonne tauchte den Horizont in ein goldenes Licht." "Ein Lächeln umspielte ihre Lippen." "Sie wusste, dass nichts mehr so sein würde wie zuvor." Du erkennst den KI-Sound sofort.

Die gute Nachricht: Alle drei Probleme lassen sich lösen. Mit den richtigen Prompts.

## Die fünf Elemente einer guten Geschichte

Bevor wir prompten, müssen wir wissen, was eine gute Geschichte ausmacht. Das gilt für menschliche und KI-generierte Storys gleichermaßen:

### 1. Protagonist mit Tiefe
Nicht "ein Mann", sondern ein Mensch mit Wünschen, Ängsten und Widersprüchen. Der Protagonist muss wollen – und etwas muss ihm im Weg stehen.

### 2. Konflikt
Ohne Konflikt keine Geschichte. Extern (Protagonist vs. Welt) oder intern (Protagonist vs. sich selbst). Idealerweise beides.

### 3. Spannungsbogen
Setup → steigende Spannung → Höhepunkt → Auflösung. Das muss nicht linear sein, aber die Elemente müssen da sein.

### 4. Stimme
Jede Geschichte braucht eine eigene Stimme – den Ton, der sie von anderen unterscheidet. Lakonisch? Poetisch? Zynisch? Kindlich?

### 5. Ein Ende, das etwas auslöst
Nicht "und sie lebten glücklich bis an ihr Ende." Sondern ein Ende, das den Leser zum Nachdenken bringt, überrascht oder emotional berührt.

## Der Story-Prompt: Grundmuster

Hier ist mein Basis-Prompt für Geschichten, der alle fünf Elemente abdeckt:

```
Schreibe eine Kurzgeschichte (ca. [LÄNGE] Wörter).

PROTAGONIST:
[Name, Alter, ein definierender Charakterzug,
ein Wunsch, eine Angst]

KONFLIKT:
[Was steht dem Protagonisten im Weg?]

SETTING:
[Ort, Zeit, Atmosphäre]

TON:
[Welche Stimmung soll die Geschichte haben?]

STRUKTUR:
[z.B. "Beginne mitten im Geschehen",
"Erzähle rückwärts", "Wechsle zwischen zwei Zeitebenen"]

ENDE:
[z.B. "Offen", "Überraschend", "Bittersüß",
"Der letzte Satz soll alles in Frage stellen"]

STILISTISCHE EINSCHRÄNKUNGEN:
[z.B. "Keine Klischees", "Kurze Sätze",
"Viel Dialog, wenig Beschreibung"]
```

### Beispiel

```
Schreibe eine Kurzgeschichte (ca. 500 Wörter).

PROTAGONIST:
Mara, 34, Chirurgin. Perfektionistin bis zur Selbstzerstörung.
Will die Kontrolle behalten – über alles. Hat Angst vor dem
Moment, in dem sie nichts mehr tun kann.

KONFLIKT:
Mara sitzt im Wartezimmer. Ihre Mutter wird operiert –
von einem Kollegen. Zum ersten Mal ist sie auf der
anderen Seite.

SETTING:
Krankenhaus-Wartezimmer, Winternacht, Neonlicht.

TON:
Still, angespannt. Wie das Ticken einer Uhr in
einem leeren Raum.

STRUKTUR:
Beginne mit einer Nahaufnahme: Maras Hände.
Die Geschichte spielt sich in ihrem Kopf ab –
Erinnerungen, Ängste, Selbstgespräche.
Nur der letzte Absatz ist in der Außenwelt.

ENDE:
Offen. Wir erfahren nicht, wie die OP ausgeht.
Aber Mara verändert sich in diesem Wartezimmer.

STILISTISCHE EINSCHRÄNKUNGEN:
Keine Rückblenden, die alles erklären. Keine
Tränen. Maras Emotion zeigt sich in dem, was sie
NICHT tut (nicht weint, nicht anruft, nicht aufsteht).
Kurze Sätze. Max 10% Dialog.
```

Vergleiche das Ergebnis mit "Schreib eine Geschichte über eine Ärztin im Wartezimmer." Der Unterschied ist Welten.

## Perspektive wählen

Die Erzählperspektive verändert alles. Derselbe Plot fühlt sich komplett anders an, je nachdem, wer erzählt.

### Ich-Perspektive
```
Erzähle die Geschichte aus Maras Perspektive in
der Ich-Form. Gegenwart. Wir sind in ihrem Kopf.
```
→ Intim, unmittelbar, subjektiv. Der Leser sieht nur, was Mara sieht.

### Dritte Person, nah
```
Erzähle aus der dritten Person, aber bleib nah bei Mara.
Wir kennen ihre Gedanken, aber haben etwas Distanz.
```
→ Der Standard für die meisten Geschichten. Flexibel.

### Ungewöhnliche Perspektiven
Hier wird es interessant:
```
Erzähle die Geschichte aus der Perspektive des Wartezimmers.
Das Wartezimmer beobachtet Mara. Es hat hunderte Menschen
kommen und gehen sehen. Es kennt das Muster: die Unruhe,
das Warten, die Erleichterung oder das Zusammenbrechen.
```

```
Erzähle die Geschichte als Aufzählung der Gegenstände,
die Mara berührt. Jeder Gegenstand erzählt ein Stück
der Geschichte.
```

```
Erzähle die Geschichte als Abfolge von Bildern –
ohne Worte wie "sie dachte" oder "sie fühlte".
Nur Beobachtungen. Kamera-Perspektive.
```

Ungewöhnliche Perspektiven sind der schnellste Weg zu originellen Geschichten. KI ist überraschend gut darin – wahrscheinlich, weil sie keine Konventionen verinnerlicht hat, die sie daran hindern.

## Dialog schreiben

Dialog ist die Achillesferse von KI-generierten Texten. Typische Probleme:
- Alle Figuren klingen gleich
- Dialog klingt nach Theaterstück, nicht nach echtem Gespräch
- Zu viel Exposition ("Wie du weißt, sind wir seit 10 Jahren verheiratet...")
- Zu perfekte, zu eloquente Sätze

### Der Dialog-Prompt

```
Schreibe einen Dialog zwischen [FIGUR A] und [FIGUR B].

FIGUR A spricht: [Beschreibung des Sprechstils –
kurze Sätze? Dialekt? Tics? Lieblingswörter?]

FIGUR B spricht: [Anderer Sprechstil]

REGELN:
- Echte Menschen reden in Fragmenten. Nicht in
  vollständigen Sätzen.
- Figuren unterbrechen sich.
- Nicht alles wird ausgesprochen. Die wichtigsten
  Dinge werden oft NICHT gesagt.
- Kein "sagte er/sie" nach jeder Zeile. Nutze
  Handlungen zwischen den Zeilen.
- Max. 3 Zeilen am Stück pro Figur.
```

### Beispiel

```
Dialog zwischen einem Vater (60, Handwerker, sagt nie
direkt, was er fühlt) und seiner Tochter (28, Akademikerin,
redet zu viel, wenn sie nervös ist).

Situation: Sie sagt ihm, dass sie ins Ausland zieht.

Vater spricht: Kurz. Fragt praktische Dinge statt
emotionale. Sagt "Hm" und "Na ja" statt ganzer Sätze.

Tochter spricht: Erklärt zu viel. Rechtfertigt sich,
obwohl niemand sie angeklagt hat. Redet schneller,
wenn die Stille zu lang wird.

Das Wichtigste wird nicht gesagt. Der Vater sagt nicht
"Ich werde dich vermissen." Die Tochter sagt nicht
"Ich brauche deine Erlaubnis." Aber beides schwingt mit.
```

Das Ergebnis wird ein Dialog sein, der sich echt anfühlt. Nicht weil die KI Menschen versteht, sondern weil du ihr genau gesagt hast, wie diese Menschen reden.

## Genre-spezifische Prompts

### Krimi/Thriller
```
Schreibe den Anfang eines Krimis (800 Wörter).

HOOK: Der erste Absatz muss eine Frage aufwerfen,
die der Leser beantwortet haben will.

ATMOSPHÄRE: Regennacht, leere Straßen, das Gefühl,
beobachtet zu werden.

PROTAGONIST: Nicht der Detektiv, sondern ein Zeuge.
Jemand, der eigentlich nichts damit zu tun hat.

TECHNIK: Zeige Details, die später wichtig werden,
aber lass den Leser sie noch nicht als Hinweise erkennen.

VERMEIDE: "Es war eine dunkle und stürmische Nacht."
Genre-Klischees. Übertriebene Brutalität.
```

### Science Fiction
```
Schreibe eine Sci-Fi-Kurzgeschichte (600 Wörter).

REGEL: Die Zukunftstechnologie ist NICHT der Plot.
Sie ist Hintergrund, wie ein Smartphone in einer
heutigen Geschichte. Der Plot ist menschlich.

WORLD-BUILDING: Zeige die Welt durch Details im Alltag,
nicht durch Erklärungen. Kein "Im Jahr 2157 hatten
die Menschen gelernt, dass..."

PROTAGONIST: Hat ein alltägliches Problem in einer
außergewöhnlichen Welt.

TON: Leise Sci-Fi, nicht Actionfilm. Mehr Arrival,
weniger Transformers.
```

### Märchen/Fabel
```
Schreibe ein modernes Märchen (400 Wörter).

SETTING: Heutige Welt, aber mit einem einzigen
magischen Element.

MORAL: Muss subtil sein. Nicht "Und die Moral von
der Geschicht..." sondern eingebettet in die Handlung.

SPRACHE: Einfach, rhythmisch, wie zum Vorlesen.
Wiederholungen sind erlaubt (Dreierstruktur wie
im klassischen Märchen).

TWIST: Das magische Element hat einen Preis.
```

## Fortgeschrittene Storytelling-Techniken

### Technik 1: Die Lücke

Das Mächtigste in einer Geschichte ist nicht das, was gesagt wird, sondern das, was fehlt.

```
Schreibe eine Geschichte, in der das Wichtigste
nie direkt erwähnt wird.

Beispiel: Eine Geschichte über Trauer, in der das
Wort "Tod" nicht vorkommt. Die Trauer zeigt sich
durch: leere Stühle, unangetastetes Essen,
Telefonate die nicht geführt werden.
```

### Technik 2: Die Zeitschleife

```
Erzähle dieselbe Szene dreimal – aber jedes Mal
aus einer anderen Perspektive. Jede Perspektive
enthüllt etwas, das die vorherige verborgen hat.
```

### Technik 3: Die Liste als Geschichte

```
Erzähle eine Geschichte als Einkaufsliste, als
To-Do-Liste oder als Browser-Verlauf. Die Geschichte
ergibt sich aus dem, was zwischen den Zeilen steht.

Beispiel: Eine Beziehung, erzählt durch die Google-
Suchanfragen einer Person über ein Jahr.
```

### Technik 4: Constraint Writing

```
Schreibe eine Geschichte mit folgender Einschränkung:
[Wähle eine]
- Nur 50 Wörter
- Jeder Satz beginnt mit dem nächsten Buchstaben des Alphabets
- Nur Dialog, keine Beschreibung
- Nur ein einziger Satz (grammatisch korrekt)
- Ohne das Wort "und"
```

Constraints klingen einschränkend, aber sie erzwingen Kreativität. Die KI muss ungewöhnliche Lösungen finden – und genau das macht die Ergebnisse interessant.

## Den KI-Sound loswerden

KI-Texte haben einen erkennbaren Sound. Hier sind die häufigsten Muster und wie du sie vermeidest:

| KI-Klischee | Gegenmaßnahme im Prompt |
|---|---|
| "Ein Lächeln umspielte ihre Lippen" | "Keine Klischee-Metaphern" |
| Zu viele Adjektive | "Maximal 1 Adjektiv pro Satz" |
| Erklärende Emotionen ("Sie war traurig") | "Zeige Emotionen durch Handlungen, nicht durch Benennung" |
| Perfekte Eloquenz | "Figuren reden wie echte Menschen – mit Fehlern, Pausen, Unterbrechungen" |
| Moralisierendes Ende | "Kein moralisches Fazit. Lass den Leser selbst urteilen" |
| "Plötzlich" als Spannungswort | "Das Wort 'plötzlich' ist verboten" |
| Zu viel Beschreibung | "Max. 20% Beschreibung, 80% Handlung und Dialog" |

Der beste Anti-KI-Sound-Prompt:
```
Schreibe wie ein Mensch, nicht wie eine KI.
Das bedeutet: Unperfekt. Mit Eigenheiten. Mit
Passagen, die nicht ganz logisch sind, aber sich
richtig anfühlen. Ohne Floskeln, ohne Klischees,
ohne den Drang, alles zu erklären.
```

## Längere Werke: Kapitel-für-Kapitel

Für Geschichten, die länger als ~1.000 Wörter sind, empfehle ich die Kapitel-Methode:

### Schritt 1: Outline erstellen
```
Erstelle ein Outline für eine Kurzgeschichte
(5.000 Wörter) mit folgender Prämisse:
[Deine Prämisse]

Für jedes Kapitel (5-7 Kapitel):
- Was passiert?
- Welche Figur steht im Fokus?
- Was verändert sich?
- Welche Frage bleibt offen (zum nächsten Kapitel)?
```

### Schritt 2: Kapitel einzeln schreiben
```
Basierend auf diesem Outline, schreibe Kapitel [X].

Vorheriges Kapitel endete mit: [Zusammenfassung]
Dieses Kapitel soll: [Ziel]
Nächstes Kapitel wird: [Vorschau]

Stil-Referenz: [Verweis auf Ton und Stimme aus
Kapitel 1, damit es konsistent bleibt]
```

### Schritt 3: Konsistenz-Check
```
Hier sind alle bisherigen Kapitel:
[Kapiteltexte oder Zusammenfassungen]

Prüfe auf Konsistenz:
- Widerspricht sich etwas?
- Ist der Ton durchgehend gleich?
- Gibt es Plot-Löcher?
- Werden alle aufgeworfenen Fragen beantwortet?
```

---

## Übungen

### Übung 1: Der volle Story-Prompt
Nutze das Grundmuster und schreibe eine Kurzgeschichte (500 Wörter) mit allen Elementen (Protagonist, Konflikt, Setting, Ton, Struktur, Ende, Stilregeln). Bist du mit dem Ergebnis zufrieden?

### Übung 2: Perspektiv-Experiment
Wähle eine einfache Szene (z.B. "Jemand wartet am Bahnhof"). Lass sie aus drei verschiedenen Perspektiven erzählen: Ich-Form, Kamera-Perspektive, und aus der Sicht des Bahnhofs selbst.

### Übung 3: Dialog-Werkstatt
Schreibe einen Dialog zwischen zwei Figuren mit gegensätzlichen Sprechstilen. Nutze den Dialog-Prompt. Prüfe: Klingen die Figuren unterschiedlich?

### Übung 4: Constraint-Challenge
Lass die KI eine Geschichte in genau 55 Wörtern erzählen. Dann in 100. Dann in 25. Welche Länge erzeugt die stärkste Wirkung?
