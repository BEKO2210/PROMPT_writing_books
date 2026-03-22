# Kapitel 7: Prompt-Debugging – Wenn der Prompt nicht funktioniert

Dein Prompt funktioniert nicht. Das Ergebnis ist falsch, zu lang, am Thema vorbei oder einfach schlecht. Was jetzt?

Die meisten Leute machen eine von zwei Sachen: Entweder sie schreiben den Prompt komplett neu. Oder sie fügen noch mehr Anweisungen hinzu, in der Hoffnung, dass es dadurch besser wird.

Beides ist meistens der falsche Ansatz.

Was du brauchst, ist Debugging. Systematisches Fehlersuchen. Genau wie ein Programmierer nicht sein ganzes Programm neu schreibt, wenn ein Bug auftaucht, solltest du nicht deinen ganzen Prompt über den Haufen werfen.

## Das 5-Schritte-Debugging-System

### Schritt 1: Das Problem benennen

Bevor du irgendetwas änderst, formuliere das Problem in einem Satz:

- "Das Modell ignoriert meine Formatvorgabe."
- "Die Antwort ist zu allgemein, ich brauche spezifische Beispiele."
- "Das Modell erfindet Fakten."
- "Der Ton ist zu formell, obwohl ich 'locker' gesagt habe."

Ein klar benanntes Problem ist ein halb gelöstes Problem.

### Schritt 2: Den Prompt zerlegen

Schau dir deinen Prompt an und identifiziere die einzelnen Bestandteile:

```
Aufgabe:       Was soll das Modell tun?
Kontext:       Welche Hintergrundinformationen hast du gegeben?
Format:        Welches Ausgabeformat hast du verlangt?
Ton:           Welchen Stil hast du definiert?
Einschränkungen: Was soll das Modell NICHT tun?
Beispiele:     Hast du Beispiele gegeben?
```

Welcher Teil verursacht das Problem? Meistens ist es einer – nicht alle.

### Schritt 3: Hypothese aufstellen

Basierend auf Schritt 1 und 2, rate, was schiefläuft:

- "Ich glaube, meine Aufgabe ist zu vage."
- "Ich glaube, mein Kontext widerspricht meiner Aufgabe."
- "Ich glaube, ich habe zu viele Einschränkungen."

### Schritt 4: Einen Parameter ändern

Ändere genau EINE Sache. Nicht zwei, nicht drei. Eine.

- Vage Aufgabe? → Mach sie spezifischer.
- Fehlender Kontext? → Füge Kontext hinzu.
- Zu viele Einschränkungen? → Entferne eine.

### Schritt 5: Testen und vergleichen

Teste den veränderten Prompt. Ist das Ergebnis besser? Dann war deine Hypothese richtig. Ist es gleich oder schlechter? Mach die Änderung rückgängig und probiere eine andere Hypothese.

## Die häufigsten Prompt-Probleme und ihre Lösungen

### Problem: "Das Ergebnis ist zu allgemein"

**Ursache:** Zu wenig Kontext oder zu vage Aufgabe.

```
# Schlecht
Schreib einen Text über Marketing.

# Besser
Schreib einen 300-Wörter-Text über Content-Marketing-Strategien
für B2B-SaaS-Startups mit weniger als 10 Mitarbeitern.
Fokus: LinkedIn und Blogartikel. Zielgruppe: CTOs mittelständischer Unternehmen.
```

**Faustregel:** Wenn dein Prompt weniger als 2 Sätze hat und die Aufgabe komplex ist, fehlt wahrscheinlich Kontext.

### Problem: "Das Modell ignoriert Teile meiner Anweisung"

**Ursache:** Zu viele Anweisungen, schlechte Strukturierung, oder das Kontext-Fenster ist voll.

**Lösung 1: Priorisiere.** Welche Anweisung ist am wichtigsten? Stelle sie an den Anfang.

**Lösung 2: Strukturiere mit Delimitern.**
```
### Aufgabe
[Die eine Sache, die gemacht werden soll]

### Formatregeln (WICHTIG)
[Die Regeln, die nicht ignoriert werden dürfen]

### Stilregeln
[Ton und Formulierung]
```

**Lösung 3: Wiederhole die wichtigste Anweisung am Ende.**
```
[Gesamter Prompt]

Zur Erinnerung: Die Antwort MUSS als Tabelle formatiert sein.
```

### Problem: "Das Modell erfindet Fakten"

**Ursache:** Das Modell "halluziniert" – es generiert plausibel klingende, aber falsche Informationen.

**Lösung 1:** Sag es explizit.
```
Wenn du dir bei einer Information nicht sicher bist, schreibe
"[nicht verifiziert]" dahinter. Erfinde keine Zahlen, Daten oder Quellen.
```

**Lösung 2:** Begrenze den Wissensbereich.
```
Beantworte die Frage ausschließlich basierend auf dem folgenden Text.
Nutze KEIN externes Wissen.

"""
[Text einfügen]
"""
```

**Lösung 3:** Fordere Quellenangaben.
```
Nenne für jede Behauptung die Quelle. Wenn du keine Quelle hast,
kennzeichne die Aussage als "eigene Einschätzung".
```

### Problem: "Der Ton stimmt nicht"

**Ursache:** Tonbeschreibungen wie "locker" oder "professionell" sind subjektiv. Was für dich locker ist, kann für das Modell etwas anderes bedeuten.

**Lösung: Zeig statt beschreiben.**
```
# Statt
Schreibe locker.

# Besser
Schreibe so, als würdest du einem Freund in einer WhatsApp-Nachricht
etwas erklären. Kurze Sätze. Du-Form. Keine Fachbegriffe.
Beispiel für den gewünschten Ton:
"Hey, weißt du was? Das ist gar nicht so kompliziert.
Pass auf, ich erklär's dir kurz."
```

### Problem: "Die Antwort ist zu lang"

**Ursache:** Du hast keine Längenbegrenzung angegeben, oder die Begrenzung ist unklar.

```
# Wenig effektiv
Fass dich kurz.

# Effektiver
Antworte in maximal 3 Sätzen.

# Am effektivsten
Antworte in genau 3 Bullet Points. Jeder Bullet Point maximal 15 Wörter.
```

Zahlen sind immer besser als Adjektive. "Kurz" ist subjektiv. "3 Sätze" ist messbar.

### Problem: "Das Ergebnis ist immer gleich"

**Ursache:** Temperatur zu niedrig, oder der Prompt lässt keinen Spielraum.

**Lösung 1:** Temperatur erhöhen (wenn möglich).

**Lösung 2:** Explizit um Variation bitten.
```
Gib mir 5 verschiedene Versionen. Jede Version soll einen
anderen Ansatz verfolgen. Variiere: Perspektive, Einstieg, Tonalität.
```

**Lösung 3:** Constraints lockern.
```
# Statt
Schreib eine Einleitung, die mit einer Frage beginnt.

# Besser
Schreib eine Einleitung. Du kannst mit einer Frage, einer
überraschenden Statistik oder einer kurzen Anekdote beginnen.
```

## Die Prompt-Debugging-Checkliste

Wenn ein Prompt nicht funktioniert, gehe diese Checkliste durch:

- [ ] **Ist die Aufgabe klar?** Könnte ein Mensch mit diesen Anweisungen das Gewünschte liefern?
- [ ] **Fehlt Kontext?** Weiß das Modell, für wen, warum und in welchem Zusammenhang?
- [ ] **Ist das Format definiert?** Weiß das Modell, wie die Antwort aussehen soll?
- [ ] **Gibt es Widersprüche?** Widersprechen sich verschiedene Teile deines Prompts?
- [ ] **Ist der Prompt zu lang?** Mehr ist nicht immer mehr. Kürze Redundanzen.
- [ ] **Fehlt ein Beispiel?** Ein gutes Beispiel sagt mehr als 100 Wörter Erklärung.
- [ ] **Sind die Einschränkungen zu streng?** Zu viele Don'ts lassen keinen Raum.
- [ ] **Ist das Kontext-Fenster voll?** Bei langen Konversationen: neue Konversation starten.

## Die Subtraktionsmethode

Manchmal ist das Problem nicht, dass etwas fehlt – sondern dass zu viel da ist. In dem Fall hilft die Subtraktionsmethode:

1. Nimm deinen nicht-funktionierenden Prompt
2. Entferne die Hälfte der Anweisungen
3. Teste
4. Wenn es besser ist: Die entfernten Anweisungen haben gestört
5. Wenn es schlechter ist: Füge sie zurück und entferne die andere Hälfte

So findest du die problematische Anweisung durch Ausschluss. Das ist effizienter als wild herumzuändern.

## A/B-Testing für Prompts

Wenn du regelmäßig ähnliche Aufgaben erledigst, lohnt sich systematisches A/B-Testing:

```
Version A:
"Fasse diesen Text in 3 Sätzen zusammen."

Version B:
"Lies den folgenden Text. Identifiziere die Kernaussage und
die zwei wichtigsten Nebenargumente. Formuliere eine Zusammenfassung
in genau 3 Sätzen."
```

Teste beide Versionen mit 5 verschiedenen Texten. Welche Version liefert konsistent bessere Ergebnisse? Die gewinnt. Und wird dein neues Template.

## Prompt-Protokoll reloaded

In Band 1 habe ich das Prompt-Protokoll eingeführt. Jetzt wird es zum Debugging-Tool.

Erweitere dein Protokoll um diese Spalten:

| Datum | Prompt | Ergebnis | Problem | Hypothese | Änderung | Besser? |
|-------|--------|----------|---------|-----------|----------|---------|
| 22.03 | [Prompt] | Zu allgemein | Kein Kontext | Mehr Kontext | Zielgruppe ergänzt | Ja |

Drei Spalten mehr. Aber sie machen den Unterschied zwischen ziellosem Herumprobieren und systematischer Verbesserung.

---

## Übung

**Debug-Challenge**

Hier ist ein absichtlich schlechter Prompt:

```
Schreib was über Hunde. Es soll gut sein und nicht zu lang
aber auch nicht zu kurz und irgendwie professionell aber nicht
zu steif und mit Fakten aber nicht langweilig.
```

1. Identifiziere alle Probleme (Hinweis: Es sind mindestens 5)
2. Schreibe eine verbesserte Version
3. Teste beide Versionen und vergleiche
4. Dokumentiere den Prozess in deinem Prompt-Protokoll

Bonusaufgabe: Nimm deinen schlechtesten Prompt der letzten Woche und wende das 5-Schritte-System darauf an.
