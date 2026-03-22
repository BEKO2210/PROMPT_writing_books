# Kapitel 8: Kreative Frameworks – Systematisch kreativ sein

"Kreativität lässt sich nicht erzwingen." Stimmt. Aber man kann ihr den Weg ebnen.

In Band 2 hast du Prompt-Frameworks wie CRAFT, RTF und RISEN kennengelernt – strukturierte Ansätze für gute Prompts. Dieses Kapitel überträgt bewährte Kreativitätstechniken in die Welt der KI-Prompts.

## Warum Frameworks für Kreativität?

Kreativität fühlt sich an wie Magie. Aber Forscher wissen seit Jahrzehnten: Kreativität folgt Mustern. Man kann diese Muster nutzen, um systematisch auf neue Ideen zu kommen.

Das gilt für Menschen. Und es gilt für KI.

Ohne Framework fragt man: "Gib mir eine kreative Idee für X." Das Ergebnis ist meistens die naheliegendste Idee – die erste, auf die jeder kommen würde.

Mit Framework fragt man gezielt aus ungewöhnlichen Richtungen. Und da werden die Ideen spannend.

## Framework 1: SCAMPER

SCAMPER ist ein Kreativitäts-Klassiker. Es steht für sieben Denkoperationen, die du auf jedes Thema, Produkt oder Konzept anwenden kannst:

| Buchstabe | Operation | Frage |
|---|---|---|
| **S** | Substitute (Ersetzen) | Was kann ich durch etwas anderes ersetzen? |
| **C** | Combine (Kombinieren) | Was kann ich mit etwas anderem verbinden? |
| **A** | Adapt (Anpassen) | Was kann ich aus einem anderen Kontext übernehmen? |
| **M** | Modify (Verändern) | Was kann ich vergrößern, verkleinern, übertreiben? |
| **P** | Put to other use (Umnutzen) | Wofür könnte es sonst noch verwendet werden? |
| **E** | Eliminate (Weglassen) | Was kann ich weglassen oder vereinfachen? |
| **R** | Reverse (Umkehren) | Was passiert, wenn ich es umdrehe? |

### Der SCAMPER-Prompt

```
Ich habe folgendes [Produkt/Konzept/Projekt]:
[Beschreibung]

Wende SCAMPER an und generiere für jede Operation
mindestens 2 konkrete Ideen:

S – SUBSTITUTE: Was ersetzen?
C – COMBINE: Womit verbinden?
A – ADAPT: Was aus anderen Bereichen übernehmen?
M – MODIFY: Was vergrößern/verkleinern/übertreiben?
P – PUT TO OTHER USE: Wofür sonst nutzen?
E – ELIMINATE: Was weglassen?
R – REVERSE: Was umdrehen?

Bewerte am Ende: Welche 3 Ideen haben das meiste Potenzial?
```

### Beispiel

```
Ich habe folgendes Produkt:
Eine App für Meal Planning (Wochenplan für Mahlzeiten).

Wende SCAMPER an...
```

**Mögliche Ergebnisse:**
- **S:** Ersetze Rezepte durch Zutaten → Die App schlägt keine Gerichte vor, sondern Zutatenkombinationen
- **C:** Kombiniere mit Fitness-Tracking → Mahlzeiten, die auf das heutige Workout abgestimmt sind
- **A:** Übernimm das Tinder-Prinzip → Swipe durch Gerichte: links nein, rechts ja → KI lernt Vorlieben
- **M:** Verkleinere auf 1 Mahlzeit → Nur das Abendessen planen, aber dafür perfekt
- **P:** Nutze es für Restaurants → Restaurants planen ihre Wochenkarte mit der App
- **E:** Eliminiere die Planung → Die App bestellt direkt die Zutaten, ohne dass du den Plan siehst
- **R:** Umkehren: Statt "Was koche ich?" → "Was mache ich mit dem, was ich habe?"

## Framework 2: Die Sechs Hüte (De Bono)

Edward de Bonos "Six Thinking Hats" teilt Denken in sechs Perspektiven auf:

| Hut | Farbe | Perspektive |
|---|---|---|
| Weiß | Fakten | Welche Daten und Informationen haben wir? |
| Rot | Emotionen | Wie fühlt sich das an? Bauchgefühl? |
| Schwarz | Kritik | Was kann schiefgehen? Risiken? |
| Gelb | Optimismus | Was sind die Chancen? Best Case? |
| Grün | Kreativität | Welche neuen Ideen gibt es? |
| Blau | Prozess | Wie gehen wir vor? Was ist der nächste Schritt? |

### Der Sechs-Hüte-Prompt

```
Thema: [Dein Thema/Idee/Problem]

Analysiere das Thema aus allen 6 Perspektiven
(De Bonos Sechs Hüte):

🤍 WEISS (Fakten): Was wissen wir? Was nicht?
❤️ ROT (Emotion): Wie fühlt sich das an?
   Erste Reaktion? Bauchgefühl?
🖤 SCHWARZ (Kritik): Was kann schiefgehen?
   Schwächen? Risiken?
💛 GELB (Optimismus): Was sind die Chancen?
   Best-Case-Szenario?
💚 GRÜN (Kreativität): Welche ungewöhnlichen
   Ansätze gibt es? Verrückte Ideen?
💙 BLAU (Prozess): Was ist der beste nächste Schritt?
   Wie entscheiden wir?

Am Ende: Synthese aus allen 6 Perspektiven.
```

## Framework 3: Random Input (Zufalls-Stimulus)

Die Idee: Verbinde dein Problem mit einem zufälligen Wort, Bild oder Konzept. Die erzwungene Verbindung erzeugt unerwartete Ideen.

### Der Random-Input-Prompt

```
Mein kreatives Problem: [Beschreibung]

Verbinde es mit diesen 5 zufälligen Wörtern und generiere
für jedes eine kreative Lösung:

1. Aquarium
2. Briefmarke
3. Vulkan
4. Schlüsselbund
5. Wolke

Für jedes Wort: Wie könnte eine Verbindung zwischen
dem Wort und meinem Problem zu einer Lösung führen?
Denke lateral, nicht logisch.
```

### Beispiel

```
Mein Problem: Ich brauche eine kreative Einladung
für eine Firmenfeier.

Verbinde mit: "Aquarium"

→ Idee: Einladung als Flasche, die "im Meer gefunden" wurde.
Einladungstext als handgeschriebene Flaschenpost. Farbpalette
in Meeresblau und Sand. Motto der Feier: "Abtauchen."
```

## Framework 4: Perspektivwechsel (Morphologischer Kasten)

Du variierst systematisch die Parameter eines kreativen Problems:

### Der Morphologische Prompt

```
Kreatives Projekt: [Beschreibung]

Variiere systematisch diese Parameter:

| Parameter | Option A | Option B | Option C |
|---|---|---|---|
| Zielgruppe | Kinder | Senioren | Außerirdische |
| Medium | Video | Plakat | Performance |
| Tonalität | Lustig | Düster | Sachlich |
| Ort | Unter Wasser | Im All | In einer Küche |
| Zeitraum | 1920er | Heute | 3000 n.Chr. |

Wähle eine ungewöhnliche Kombination aus jeder Spalte
und entwickle daraus eine konkrete Idee.

Zum Beispiel: Kinder + Performance + Düster + Im All + 1920er
→ Was wird daraus?
```

## Framework 5: "Was wäre wenn?" (Hypothetisches Denken)

```
Ausgangspunkt: [Dein Thema/Produkt/Idee]

Beantworte diese "Was wäre wenn?"-Fragen und
entwickle aus jeder Antwort eine Idee:

1. Was wäre, wenn es kostenlos wäre?
2. Was wäre, wenn es nur 1 Minute dauern dürfte?
3. Was wäre, wenn es von einem Kind bedient
   werden müsste?
4. Was wäre, wenn das Gegenteil die Lösung wäre?
5. Was wäre, wenn es physisch nicht existieren dürfte?
6. Was wäre, wenn es nur durch Zusammenarbeit
   funktionieren würde?
7. Was wäre, wenn es in 100 Jahren noch relevant
   sein müsste?
```

## Framework 6: Mind Mapping mit KI

```
Zentrales Thema: [Dein Thema]

Erstelle eine Mind Map mit 3 Ebenen:

EBENE 1: 5 Hauptäste (die wichtigsten Aspekte)
EBENE 2: Je 3 Unteräste pro Hauptast
EBENE 3: Je 2 konkrete Ideen pro Unterast

Formatiere es als Textstruktur:

📌 [Thema]
├── [Hauptast 1]
│   ├── [Unterast 1.1]
│   │   ├── Idee 1.1.1
│   │   └── Idee 1.1.2
│   ├── [Unterast 1.2]
│   │   ├── Idee 1.2.1
│   │   └── Idee 1.2.2
│   └── [Unterast 1.3]
│       ├── Idee 1.3.1
│       └── Idee 1.3.2
├── [Hauptast 2]
│   ...

Am Ende: Markiere die 5 überraschendsten Ideen.
```

## Framework 7: Die Provokation (Po)

Eine Technik von Edward de Bono: Formuliere eine bewusst absurde Aussage und nutze sie als Sprungbrett für echte Ideen.

```
Mein Thema: [Dein Thema]

Formuliere 5 bewusst absurde Behauptungen (Provokationen)
zu diesem Thema:

Beispiel für "Restaurant":
PO: "Das Restaurant hat keine Speisekarte"
PO: "Die Gäste kochen selbst"
PO: "Man bezahlt, wie viel man will"
PO: "Das Restaurant hat keine Wände"
PO: "Man isst im Dunkeln"

Für jede Provokation: Welche ECHTE, umsetzbare Idee
steckt dahinter? (z.B. "Man isst im Dunkeln" → Dinner
in the Dark → gibt es tatsächlich als Konzept!)
```

## Frameworks kombinieren

Die stärksten Ergebnisse kommen aus der Kombination:

### SCAMPER + Sechs Hüte

```
1. Nutze SCAMPER, um 7 Ideen zu generieren
2. Wähle die 3 besten
3. Bewerte jede mit den 6 Hüten
4. Die Idee, die bei allen Hüten gut abschneidet, gewinnt
```

### Random Input + Was wäre wenn

```
1. Verbinde dein Problem mit einem zufälligen Wort
2. Stelle "Was wäre wenn?"-Fragen zur entstandenen Idee
3. Die Antworten sind deine kreativen Ansätze
```

### Mind Map + Provokation

```
1. Erstelle eine Mind Map zu deinem Thema
2. Für jeden Hauptast: Formuliere eine Provokation
3. Entwickle aus den Provokationen neue Unteräste
```

## Wann welches Framework?

| Situation | Framework |
|---|---|
| Bestehendes Produkt verbessern | SCAMPER |
| Neue Perspektiven finden | Sechs Hüte |
| Kreative Blockade durchbrechen | Random Input |
| Systematisch alle Möglichkeiten erkunden | Morphologischer Kasten |
| Annahmen hinterfragen | Was wäre wenn? |
| Komplexes Thema strukturieren | Mind Map |
| Radikal neue Richtungen finden | Provokation |

---

## Übungen

### Übung 1: SCAMPER in Aktion
Wähle ein Alltagsprodukt (Regenschirm, Kaffeemaschine, Rucksack). Wende SCAMPER an. Welche Idee hat das meiste Potenzial?

### Übung 2: Sechs Hüte für eine Entscheidung
Nimm eine aktuelle Entscheidung (beruflich oder privat) und analysiere sie mit den Sechs Hüten. Hat der rote Hut (Emotion) etwas gezeigt, das die anderen übersehen haben?

### Übung 3: Random Input
Öffne ein Wörterbuch auf einer zufälligen Seite. Nimm das erste Wort, das du siehst. Verbinde es mit einem kreativen Problem, das du gerade hast. Was entsteht?

### Übung 4: Framework-Kombination
Wähle zwei Frameworks und kombiniere sie für ein kreatives Projekt deiner Wahl. Dokumentiere den Prozess und das Ergebnis.
