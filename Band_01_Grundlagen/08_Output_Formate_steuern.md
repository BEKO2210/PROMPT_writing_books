# Kapitel 8: Output-Formate steuern – Damit die KI liefert, was du brauchst

Du weißt jetzt, wie du gute Prompts schreibst, Kontext gibst und Rollen zuweist. Aber was nützt die beste Antwort, wenn sie im falschen Format kommt?

Stell dir vor, du brauchst eine Tabelle für eine Präsentation, aber die KI liefert dir einen Fließtext. Oder du willst eine kurze Zusammenfassung und bekommst einen Roman. Das passiert ständig – und es ist komplett vermeidbar.

In diesem Kapitel lernst du, wie du das Output-Format kontrollierst. Das spart dir Zeit und Nerven.

## Die wichtigsten Formate

### Listen

Listen sind das am häufigsten gewünschte Format. Es gibt zwei Varianten:

**Nummerierte Liste (wenn Reihenfolge wichtig ist):**
```
Gib mir die 5 wichtigsten Schritte, um ein LinkedIn-Profil
zu optimieren. Nummerierte Liste.
```

**Bullet Points (wenn Reihenfolge egal ist):**
```
Nenne mir die Vorteile von Remote-Arbeit. Aufzählung mit Stichpunkten.
```

### Tabellen

Tabellen sind Gold wert für Vergleiche.

```
Vergleiche ChatGPT, Claude und Gemini in einer Tabelle.
Spalten: Name, Anbieter, Stärken, Schwächen, Kosten (kostenlose Version).
```

Das Modell erstellt dir eine saubere Markdown-Tabelle, die du direkt kopieren kannst.

### Strukturierter Text mit Überschriften

```
Schreib mir einen Überblick über Projektmanagement-Methoden.
Verwende Überschriften (## für Hauptmethoden) und darunter jeweils
3-4 Sätze Beschreibung plus ein Beispiel, wann die Methode sinnvoll ist.
```

### JSON (für Entwickler und Datenverarbeitung)

```
Erstelle eine Liste von 5 fiktiven Produkten mit Name, Preis,
Kategorie und Kurzbeschreibung. Format: JSON-Array.
```

Ergebnis:
```json
[
  {
    "name": "SmartLamp X1",
    "preis": 49.99,
    "kategorie": "Smart Home",
    "beschreibung": "LED-Lampe mit App-Steuerung und 16 Millionen Farben"
  },
  ...
]
```

### Markdown

Wenn du mit Markdown arbeitest (z.B. für GitHub, Notion oder Obsidian):

```
Erstelle eine Projektdokumentation in Markdown-Format.
Verwende Überschriften, Code-Blöcke, Listen und eine Tabelle.
```

## Länge steuern

Die Länge der Antwort ist einer der einfachsten Stellschrauben – und einer der wichtigsten.

**Wortanzahl:**
```
Erkläre Quantencomputing. Maximal 100 Wörter.
```

**Satzanzahl:**
```
Fasse diesen Artikel in genau 3 Sätzen zusammen.
```

**Absatzanzahl:**
```
Schreib eine Produktbeschreibung. Genau 2 Absätze.
Erster Absatz: Was ist das Produkt?
Zweiter Absatz: Warum sollte man es kaufen?
```

**Seitenangabe:**
```
Erstelle einen Bericht über KI im Bildungswesen.
Umfang: ungefähr 2 DIN-A4-Seiten.
```

Ein Hinweis zur Genauigkeit: LLMs sind nicht super präzise bei Wortanzahlen. Wenn du "maximal 100 Wörter" sagst, bekommst du vielleicht 95 oder 115. Für die meisten Zwecke ist das nah genug. Wenn du es wirklich exakt brauchst, sag "Zähle die Wörter und schreibe die Anzahl am Ende."

## Sprache und Tonalität steuern

Das Format umfasst nicht nur die Struktur, sondern auch den Stil.

**Formell:**
```
Schreib eine E-Mail an den Vorstand. Ton: formell und professionell.
Keine Umgangssprache, keine Emojis.
```

**Locker:**
```
Schreib einen Instagram-Caption. Ton: locker, freundlich, leicht
humorvoll. Wie ein Gespräch unter Freunden.
```

**Akademisch:**
```
Verfasse einen Absatz im Stil einer wissenschaftlichen Arbeit.
Verwende Passivkonstruktionen und Fachterminologie.
Zitiere im APA-Format.
```

**Kindgerecht:**
```
Erkläre, wie eine Batterie funktioniert.
Schreib so, dass ein 7-Jähriger es versteht.
Verwende einfache Wörter und ein Alltagsbeispiel.
```

## Strukturierte Ausgaben erzwingen

Manchmal brauchst du eine ganz bestimmte Struktur. Dann gib dem Modell ein Template:

```
Analysiere die folgende Geschäftsidee. Verwende exakt diese Struktur:

**Idee:** [Kurzbeschreibung in einem Satz]
**Zielgruppe:** [Wer würde das kaufen?]
**Stärken:** [3 Bullet Points]
**Schwächen:** [3 Bullet Points]
**Nächster Schritt:** [Was sollte man als erstes tun?]
**Bewertung:** [1-10, mit Begründung in einem Satz]

Die Geschäftsidee: Eine App, die lokale Bauernhöfe mit Restaurants verbindet.
```

Das Modell füllt dein Template aus. Punkt für Punkt. Das ist besonders praktisch, wenn du mehrere Dinge nach dem gleichen Schema analysieren willst – du schickst einfach das gleiche Template mit einer anderen Idee.

## Mehrere Formate in einem Prompt

Du kannst auch verschiedene Formate kombinieren:

```
Erstelle eine Übersicht über die 3 beliebtesten Programmiersprachen
für Anfänger.

Für jede Sprache:
1. **Überschrift** mit dem Namen
2. **Kurzbeschreibung** (2 Sätze)
3. **Tabelle** mit Vor- und Nachteilen (je 3)
4. **Code-Beispiel** (Hello World)
5. **Empfehlung** in einem Satz: Für wen ist diese Sprache am besten?
```

## Praxis-Trick: Das Format vorab zeigen

Wenn du ein ganz bestimmtes Format im Kopf hast, zeig dem Modell ein Beispiel:

```
Erstelle 3 Flashcards zum Thema Fotosynthese.
Format wie in diesem Beispiel:

---
**Frage:** Was ist Fotosynthese?
**Antwort:** Der Prozess, bei dem Pflanzen Licht in Energie umwandeln.
**Merkhilfe:** Foto = Licht, Synthese = Zusammensetzen
**Schwierigkeit:** Leicht
---

Erstelle 3 weitere in diesem Format zum Thema Zellteilung.
```

Das Modell kopiert dein Format exakt. Das nennt man "Few-Shot Prompting" – du zeigst ein Beispiel und das Modell folgt dem Muster. Dazu mehr in Band 2.

## Das Wichtigste aus diesem Kapitel

- Du kannst Listen, Tabellen, JSON, Markdown und Fließtext anfordern
- Länge steuerst du über Wort-, Satz- oder Absatzanzahl
- Tonalität (formell, locker, akademisch) ist Teil des Formats
- Templates erzwingen eine konsistente Struktur
- Ein Beispiel zu zeigen ist der sicherste Weg zum gewünschten Format

---

## Übung

**Lass dir dasselbe Thema in 5 verschiedenen Formaten ausgeben.**

Wähle ein beliebiges Thema. Zum Beispiel: "Die Vorteile von regelmäßiger Bewegung."

Jetzt fordere es in diesen 5 Formaten an:
1. Eine nummerierte Liste mit 7 Punkten
2. Eine Tabelle (Vorteil | Erklärung | Wie oft pro Woche)
3. Ein kurzer Absatz (maximal 80 Wörter) im akademischen Stil
4. Ein Instagram-Post (locker, mit Emoji-Vorschlägen)
5. Ein JSON-Objekt mit den Feldern: vorteil, kategorie, evidenz

Vergleiche die Ergebnisse. Achte darauf, wie das gleiche Wissen komplett anders präsentiert wird – nur durch die Format-Anweisung.
