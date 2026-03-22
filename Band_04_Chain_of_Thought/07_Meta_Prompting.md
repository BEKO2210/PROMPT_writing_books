# Kapitel 7: Meta-Prompting – Prompts, die Prompts verbessern

Stell dir vor, du könntest einem Koch sagen: "Bewerte dein eigenes Rezept und verbessere es." Genau das macht Meta-Prompting – nur mit Prompts.

## Die Idee

Meta-Prompting ist Prompting auf einer höheren Ebene. Statt dem Modell eine Aufgabe zu geben, gibst du ihm die Aufgabe, seinen eigenen Prompt (oder seine eigene Antwort) zu analysieren und zu verbessern.

Das klingt nach Zirkelschluss, funktioniert aber erstaunlich gut. LLMs sind oft besser darin, die Qualität eines Textes zu bewerten, als ihn beim ersten Versuch perfekt zu schreiben. Diese Asymmetrie nutzt Meta-Prompting aus.

## Die drei Formen von Meta-Prompting

### Form 1: Prompt-Optimierung
Das Modell verbessert deinen Prompt, bevor es ihn ausführt.

### Form 2: Antwort-Verbesserung
Das Modell bewertet seine eigene Antwort und liefert eine bessere Version.

### Form 3: Aufgaben-Dekomposition
Das Modell zerlegt eine komplexe Aufgabe in Unteraufgaben und bearbeitet jede einzeln.

## Form 1: Prompt-Optimierung

Du gibst dem Modell deinen Prompt und bittest es, den Prompt zuerst zu verbessern.

### Das Grundmuster

```
Ich möchte folgenden Prompt an ein LLM schicken:

"""
[Dein Original-Prompt]
"""

Bevor du den Prompt ausführst:
1. Analysiere den Prompt: Was ist gut? Was fehlt?
   Was ist unklar?
2. Schreibe eine verbesserte Version des Prompts
3. Erkläre, was du geändert hast und warum
4. Führe dann den verbesserten Prompt aus
```

### Beispiel

```
Ich möchte folgenden Prompt an ein LLM schicken:

"""
Schreib mir was über gesunde Ernährung.
"""

Bevor du den Prompt ausführst:
1. Analysiere den Prompt: Was ist gut? Was fehlt?
2. Schreibe eine verbesserte Version
3. Erkläre die Änderungen
4. Führe den verbesserten Prompt aus
```

**Mögliches Ergebnis:**

```
ANALYSE:
- Zu vage: Was genau über gesunde Ernährung?
- Keine Zielgruppe: Für wen? Sportler? Büroarbeiter? Kinder?
- Kein Format: Artikel? Liste? Ernährungsplan?
- Keine Länge: 100 Wörter? 1.000 Wörter?
- Kein Ton: Wissenschaftlich? Locker? Motivierend?

VERBESSERTER PROMPT:
"Schreib einen lockeren, motivierenden Blogartikel (ca. 600 Wörter)
über gesunde Ernährung für Büroarbeiter, die wenig Zeit zum Kochen
haben. Fokus auf: Meal Prep, schnelle Rezepte, gesunde Snacks
fürs Büro. Vermeide Diät-Dogmen und belehrenden Ton. Duze den Leser."

ÄNDERUNGEN:
1. Zielgruppe ergänzt (Büroarbeiter)
2. Format definiert (Blogartikel, 600 Wörter)
3. Ton festgelegt (locker, motivierend)
4. Fokus eingeschränkt (3 konkrete Themen)
5. Negative Anweisung ergänzt (kein belehrender Ton)

AUSFÜHRUNG:
[Der Artikel basierend auf dem verbesserten Prompt]
```

Siehst du, was passiert ist? Das Modell hat alle Schwächen deines Prompts erkannt und behoben – genau die Dinge, die wir in Band 1 und 2 gelernt haben (Bausteine, Kontext, Ton). Das Modell kennt die Best Practices und kann sie auf deinen Prompt anwenden.

## Form 2: Antwort-Verbesserung

Das Modell gibt eine Antwort, reflektiert darüber und verbessert sie.

### Einzel-Prompt-Methode

```
Aufgabe: [Deine Aufgabe]

Gib zuerst eine Antwort (Entwurf).
Dann bewerte deinen eigenen Entwurf:
- Was ist gut?
- Was fehlt?
- Was könnte besser sein?
Dann: Gib eine verbesserte Finalversion.
```

### Zwei-Prompt-Methode

**Prompt 1:**
```
[Deine Aufgabe]
```
→ Modell gibt Antwort.

**Prompt 2:**
```
Hier ist deine vorherige Antwort:
"""
[Antwort einfügen]
"""

Bewerte sie kritisch:
1. Ist sie vollständig?
2. Ist sie korrekt?
3. Ist sie gut strukturiert?
4. Was würdest du ändern?

Dann: Schreibe eine verbesserte Version.
```

Die Zwei-Prompt-Methode ist aufwendiger, aber oft besser, weil der zweite Prompt mit frischen "Augen" auf die Antwort schaut.

### Beispiel: E-Mail verbessern

**Prompt 1:**
```
Schreib eine E-Mail an meinen Vermieter. Ich möchte eine
Mietminderung, weil seit 3 Wochen die Heizung im Wohnzimmer
nicht funktioniert. Ich habe am 1.3. den Mangel gemeldet.
```

**Prompt 2:**
```
Bewerte diese E-Mail:

"""
[Die generierte E-Mail]
"""

Prüfe:
1. Ist der Ton angemessen? (sachlich, aber bestimmt)
2. Sind alle rechtlich relevanten Punkte enthalten?
   (Mangelmeldung, Frist, Minderungsquote)
3. Fehlen wichtige Informationen?
4. Ist die Struktur klar?

Schreibe eine verbesserte Version.
```

## Form 3: Aufgaben-Dekomposition

Das Modell zerlegt eine komplexe Aufgabe selbst in Teilaufgaben.

### Das Grundmuster

```
Aufgabe: [Komplexe Aufgabe]

Bevor du anfängst:
1. Zerlege diese Aufgabe in 3-5 Teilaufgaben
2. Sortiere sie in die richtige Reihenfolge
3. Bearbeite dann jede Teilaufgabe einzeln
4. Fasse am Ende alles zusammen
```

### Beispiel

```
Aufgabe: Erstelle ein Konzept für einen Online-Kurs
zum Thema "Persönliche Finanzen für Berufseinsteiger".

Bevor du anfängst:
1. Zerlege das in die nötigen Teilaufgaben
2. Ordne sie logisch
3. Bearbeite jede einzeln
4. Fasse am Ende zusammen
```

**Mögliches Ergebnis:**

```
TEILAUFGABEN:
1. Zielgruppe definieren (Wer? Welches Wissen? Welche Probleme?)
2. Lernziele formulieren (Was können die Teilnehmer danach?)
3. Curriculum entwickeln (Module, Reihenfolge, Inhalte)
4. Format und Didaktik festlegen (Video, Text, Übungen)
5. Marktpositionierung (USP, Preis, Vergleich mit Konkurrenz)

TEILAUFGABE 1: Zielgruppe...
[Ausführliche Bearbeitung]

TEILAUFGABE 2: Lernziele...
[Ausführliche Bearbeitung]

...

ZUSAMMENFASSUNG:
[Kompaktes Gesamtkonzept]
```

Das Modell hat die Aufgabe besser zerlegt, als die meisten Menschen es tun würden. Es hat die Teilaufgaben in einer logischen Reihenfolge sortiert (Zielgruppe vor Curriculum, weil das Curriculum von der Zielgruppe abhängt).

## Der Meta-Prompt-Generator

Mein Lieblings-Meta-Prompt. Er macht aus jeder vagen Idee einen scharfen Prompt:

```
Ich habe folgende Aufgabe, bin mir aber nicht sicher,
wie ich sie als Prompt formulieren soll:

"""
[Deine vage Aufgabe/Idee]
"""

Erstelle einen optimalen Prompt für diese Aufgabe.
Der Prompt soll enthalten:
- Klare Rolle (wer soll das Modell sein?)
- Präzise Aufgabe (was genau soll es tun?)
- Kontext (was muss es wissen?)
- Format (wie soll die Antwort aussehen?)
- Einschränkungen (was soll es NICHT tun?)

Zeige mir den fertigen Prompt, den ich direkt
kopieren und verwenden kann.
```

### Beispiel

**Input:**
```
Ich habe folgende Aufgabe, bin mir aber nicht sicher,
wie ich sie als Prompt formulieren soll:

"""
Ich will irgendwas mit Newsletter machen
"""

Erstelle einen optimalen Prompt für diese Aufgabe.
```

**Output:**
```
GENERIERTER PROMPT:

Du bist ein erfahrener Content-Stratege mit Fokus auf
E-Mail-Marketing.

Entwickle ein Newsletter-Konzept mit folgenden Punkten:

1. ZIELGRUPPE: Für wen ist der Newsletter? (Ich brauche
   hier noch Input von dir – beantworte: Was ist dein
   Thema/deine Branche?)

2. STRATEGIE:
   - Frequenz (wöchentlich/zweiwöchentlich/monatlich)
   - Inhaltsmix (Formate, Rubriken)
   - Ziel (Traffic, Sales, Branding?)

3. ERSTE 5 AUSGABEN:
   - Betreffzeile
   - Inhaltsskizze (3-4 Bullet Points)
   - Call-to-Action

4. WACHSTUMSSTRATEGIE:
   - Wie gewinne ich die ersten 100 Subscriber?
   - Welche Tools brauche ich?

Format: Strukturiert mit Überschriften.
Ton: Praxisnah, keine Marketing-Floskeln.
```

Aus "irgendwas mit Newsletter" wurde ein professioneller, strukturierter Prompt. Das ist die Magie von Meta-Prompting.

## Fortgeschrittene Meta-Techniken

### Technik 1: Iteratives Meta-Prompting

Drei Runden Verbesserung:

```
Runde 1: Beantworte die Aufgabe (Entwurf 1)
Runde 2: Kritisiere Entwurf 1 und erstelle Entwurf 2
Runde 3: Kritisiere Entwurf 2 und erstelle die finale Version

Aufgabe: [Deine Aufgabe]
```

Jede Runde verbessert die vorherige. Diminishing Returns setzen typischerweise nach 2-3 Runden ein.

### Technik 2: Perspektiv-Meta-Prompting

```
Aufgabe: [Deine Aufgabe]

Schritt 1: Beantworte die Aufgabe
Schritt 2: Lass einen Kritiker die Antwort bewerten
Schritt 3: Lass einen Praktiker Verbesserungen vorschlagen
Schritt 4: Schreibe die finale Version unter
Berücksichtigung beider Feedbacks
```

### Technik 3: Socratic Meta-Prompting

Das Modell stellt sich selbst Fragen:

```
Aufgabe: [Deine Aufgabe]

Bevor du antwortest:
1. Stelle 5 klärende Fragen, die du bräuchtest,
   um die beste Antwort zu geben
2. Beantworte die Fragen selbst (basierend auf
   dem verfügbaren Kontext)
3. Dann: Gib die Antwort, die diese Klärung berücksichtigt
```

### Technik 4: Adversarial Meta-Prompting

Das Modell argumentiert gegen sich selbst:

```
Aufgabe: [Deine Aufgabe/These/Empfehlung]

Phase 1: Verteidige die Position (stärkste Argumente dafür)
Phase 2: Greife die Position an (stärkste Argumente dagegen)
Phase 3: Synthese (was bleibt nach beiden Runden?)
Phase 4: Finale Einschätzung
```

Das ist besonders wertvoll für Entscheidungsfindung und Meinungsbildung.

## Meta-Prompting im Arbeitsalltag

### Template-Erstellung

```
Ich brauche ein Prompt-Template für folgende wiederkehrende
Aufgabe: [Beschreibe die Aufgabe]

Erstelle ein Template mit Platzhaltern [IN GROSSBUCHSTABEN],
das ich jedes Mal nur ausfüllen muss.
Optimiere das Template für maximale Ergebnisqualität.
Erkläre, warum du jeden Teil so formuliert hast.
```

### Meeting-Vor- und Nachbereitung

```
Ich habe in 1 Stunde ein Meeting zum Thema "[THEMA]".
Teilnehmer: [LISTE].
Mein Ziel: [WAS ICH ERREICHEN WILL].

Bevor du mir Tipps gibst:
1. Welche Fragen sollte ICH mir stellen, um gut vorbereitet zu sein?
2. Beantworte diese Fragen basierend auf meinem Kontext
3. Dann: Gib mir einen konkreten Plan für das Meeting
```

### Präsentationsstruktur

```
Ich muss eine 15-minütige Präsentation halten:
Thema: [THEMA]
Zielgruppe: [WER HÖRT ZU]
Ziel: [WAS SOLL DAS PUBLIKUM DANACH DENKEN/TUN]

Bevor du die Struktur erstellst:
1. Was sind die 3 häufigsten Fehler bei Präsentationen
   zu diesem Thema?
2. Wie vermeide ich sie?
3. Dann: Erstelle die Präsentationsstruktur
```

## Wann Meta-Prompting nutzen?

### Ideal bei:
- **Ersten Entwürfen** – Wenn du weißt, dass der erste Versuch nicht perfekt sein wird
- **Wichtigen Dokumenten** – E-Mails an den Chef, Bewerbungen, Verträge
- **Komplexen Aufgaben** – Wenn du nicht sicher bist, ob du alles bedacht hast
- **Prompt-Entwicklung** – Wenn du Prompts für wiederkehrende Aufgaben baust
- **Kreativ-Iterationen** – Texte, Konzepte, Strategien verbessern

### Nicht nötig bei:
- **Einfachen, klaren Aufgaben** – "Übersetze X" braucht kein Meta-Prompting
- **Zeitkritischen Aufgaben** – Meta-Prompting kostet Zeit und Tokens
- **Faktenfragen** – "Wann wurde X gegründet?" profitiert nicht von Meta-Reflexion

## Häufige Fehler

### Fehler 1: Endlose Iterationsschleifen
```
Verbessere die Antwort.
→ Jetzt verbessere diese Verbesserung.
→ Und jetzt verbessere das nochmal.
→ ...
```
Nach 2-3 Runden sinkt der Mehrwert. Manchmal wird es sogar schlechter (Over-Editing). Setze ein Limit.

### Fehler 2: Unkritische Selbstbewertung
Das Modell neigt dazu, seine eigene Arbeit zu mild zu bewerten:
```
"Mein Entwurf ist insgesamt gut, nur kleine Verbesserungen nötig."
```
Gegenmaßnahme: Fordere harte Kritik explizit:
```
Sei ein strenger Kritiker. Finde mindestens 3 echte Schwächen.
Keine Schmeicheleien.
```

### Fehler 3: Form über Inhalt
Meta-Prompting kann dazu führen, dass die Antwort "polierter" wird, ohne inhaltlich besser zu sein. Achte auf Substanz, nicht nur auf Stil.

---

## Übungen

### Übung 1: Meta-Prompt-Generator
Nimm 3 vage Aufgaben aus deinem Alltag und füttere sie durch den Meta-Prompt-Generator. Vergleiche die generierten Prompts mit dem, was du selbst geschrieben hättest. Was ist besser?

### Übung 2: Dreifach-Iteration
Wähle eine wichtige Schreibaufgabe (z.B. Bewerbungsanschreiben, Projektvorschlag). Nutze das iterative Meta-Prompting (3 Runden). Vergleiche Entwurf 1 mit der Finalversion. Wie viel besser ist die Finalversion?

### Übung 3: Adversarial Meta-Prompting
Teste eine kontroverse These mit der Adversarial-Technik:
"Remote-Arbeit ist produktiver als Büroarbeit."
Hat die Synthese (Phase 3) deine Meinung verändert?

### Übung 4: Socratic Meta-Prompting
Nutze die Socratic-Technik für eine Entscheidung, die du gerade triffst. Welche Fragen hat das Modell sich gestellt, die du selbst nicht gestellt hättest?
