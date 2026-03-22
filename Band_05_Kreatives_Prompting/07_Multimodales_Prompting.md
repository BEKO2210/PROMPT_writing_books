# Kapitel 7: Multimodales Prompting – Wenn Text allein nicht reicht

In den letzten drei Kapiteln hast du Text, Bilder, Musik und Video separat generiert. Dieses Kapitel bringt alles zusammen.

Multimodales Prompting bedeutet: Du arbeitest mit mehreren Modalitäten gleichzeitig. Text + Bild. Bild + Text. Audio + Text. Oder alles auf einmal.

## Was ist Multimodalität?

Modelle wie GPT-4o, Claude 3.5 und Gemini 2.0 sind multimodal – sie können mehrere Arten von Input verstehen und teilweise auch mehrere Arten von Output erzeugen.

### Input-Modalitäten (was das Modell versteht)
- **Text** → Alle großen Modelle
- **Bilder** → GPT-4o, Claude, Gemini
- **Audio** → GPT-4o (nativ), Gemini
- **Video** → Gemini (Frames), GPT-4o (begrenzt)
- **Dateien (PDF, Code, Tabellen)** → Claude, GPT-4o, Gemini

### Output-Modalitäten (was das Modell erzeugt)
- **Text** → Alle Modelle
- **Bilder** → GPT-4o (DALL-E), Gemini (Imagen)
- **Audio** → GPT-4o (Sprache)
- **Code** → Alle Modelle
- **Strukturierte Daten** → Alle Modelle

## Bild als Input: Bilder "lesen"

Die einfachste multimodale Technik: Du gibst dem Modell ein Bild und fragst etwas dazu.

### Bild analysieren

```
[Bild hochladen]

Beschreibe dieses Bild:
1. Was ist darauf zu sehen? (Objektiv)
2. Welche Stimmung vermittelt es? (Subjektiv)
3. Welche fotografischen/künstlerischen Techniken
   wurden verwendet?
4. Welche Geschichte könnte hinter diesem Bild stecken?
```

### Bild als Stil-Referenz

```
[Bild hochladen]

Analysiere den visuellen Stil dieses Bildes:
- Farbpalette (nenne die 5 dominanten Farben als Hex)
- Lichtführung
- Komposition
- Textur/Oberfläche
- Gesamtästhetik

Erstelle dann einen Prompt, mit dem ich ein ANDERES
Bild im gleichen Stil generieren kann.
Motiv des neuen Bildes: [Dein gewünschtes Motiv]
```

Das ist Gold wert. Du findest ein Bild, dessen Stil du magst, lässt den Stil analysieren und bekommst einen Prompt, um den Stil auf neue Motive anzuwenden.

### Bild zu Text (Creative Writing)

```
[Bild hochladen]

Schreibe eine Kurzgeschichte (300 Wörter), die in
diesem Bild beginnt. Die Geschichte soll sich von dem
entfernen, was man sieht – das Bild ist der Auslöser,
nicht die ganze Geschichte.

Stil: [Dein gewünschter Stil]
```

### Bild zu Code

```
[Screenshot einer Webseite/App hochladen]

Erstelle den HTML/CSS-Code, der dieses Design
nachbaut. Mobile-first, responsive.
Nutze moderne CSS (Grid, Flexbox, Custom Properties).
Keine Frameworks, nur Vanilla CSS.
```

## Audio als Input

GPT-4o und Gemini können gesprochene Sprache direkt verarbeiten:

### Transkription + Analyse

```
[Audio hochladen]

1. Transkribiere das Audio
2. Identifiziere die Sprecher
3. Fasse den Inhalt zusammen (max. 5 Sätze)
4. Wie ist der Tonfall? (sachlich, emotional, ironisch?)
5. Gibt es Hintergrundgeräusche? Wenn ja, welche?
```

### Musik analysieren

```
[Musikstück hochladen]

Analysiere diesen Song:
- Genre und Subgenre
- Geschätztes Tempo (BPM)
- Tonart
- Instrumente, die du identifizieren kannst
- Stimmung und Atmosphäre
- Vergleichbare Künstler/Songs
```

## Cross-modale Workflows

Die spannendsten Anwendungen entstehen, wenn du Modalitäten kreuzt:

### Workflow 1: Bild → Geschichte → Hörbuch

1. **Bild generieren:** Midjourney/DALL-E → Ein atmosphärisches Bild
2. **Geschichte schreiben:** Claude/GPT → Kurzgeschichte inspiriert vom Bild
3. **Vorlesen lassen:** ElevenLabs → Hörbuch-Version der Geschichte
4. **Hintergrundmusik:** Suno → Ambient-Musik passend zur Stimmung
5. **Zusammenführen:** Audacity/GarageBand → Alles zusammenmischen

### Workflow 2: Text → Song

1. **Lyrics schreiben:** Claude/GPT → Songtext
2. **Stil definieren:** Beschreibe den Sound im Detail
3. **Generieren:** Suno/Udio → Song mit Lyrics und Stil
4. **Cover-Art:** DALL-E/Midjourney → Albumcover passend zum Song

### Workflow 3: Foto → Gemälde → Geschichte

1. **Foto machen:** Dein eigenes Foto
2. **Stil transformieren:** "Verwandle dieses Foto in ein Ölgemälde im Stil der Romantik"
3. **Geschichte schreiben:** "Schreibe die Geschichte, die dieses Gemälde erzählt"

### Workflow 4: Daten → Visualisierung → Präsentation

1. **Daten analysieren:** CSV hochladen → LLM analysiert
2. **Chart generieren:** Code für Visualisierung
3. **Begleittext:** Erklärung und Interpretation
4. **Präsentationsfolien:** Design-Vorschläge

## Multimodal in einem einzigen Prompt

Moderne Modelle können mehrere Modalitäten in einem Prompt verarbeiten:

### Bild + Text → Analyse

```
[Produktfoto hochladen]
[Kundenbewertungstext einfügen]

Vergleiche, was der Kunde schreibt, mit dem, was auf
dem Produktfoto zu sehen ist. Gibt es Widersprüche?
Ist die Bewertung gerechtfertigt?
```

### Mehrere Bilder → Vergleich

```
[Bild A hochladen] [Bild B hochladen]

Vergleiche diese beiden Designs:
1. Was sind die visuellen Unterschiede?
2. Welches ist professioneller? Warum?
3. Welches spricht welche Zielgruppe an?
4. Was würdest du am schwächeren Design ändern?
```

### Dokument + Fragen

```
[PDF/Screenshot hochladen]

Beantworte basierend auf diesem Dokument:
1. [Frage 1]
2. [Frage 2]
3. [Frage 3]

Zitiere relevante Stellen aus dem Dokument.
```

## Kreative Multimodal-Projekte

### Projekt 1: Visual Novel

Eine interaktive Geschichte mit Bildern:

```
Erstelle eine Visual Novel mit 5 Szenen.

Für jede Szene:
1. Beschreibe das Bild (als Bild-Prompt)
2. Schreibe den Erzähltext (2-3 Absätze)
3. Gib dem Leser 2 Entscheidungen, die zur
   nächsten Szene führen

Setting: [Dein Setting]
Protagonist: [Dein Charakter]
```

### Projekt 2: Podcast-Episode

```
Plane eine Podcast-Episode (15 Minuten):

1. SKRIPT: Schreibe das Skript (Intro, 3 Segmente, Outro)
2. MUSIK: Beschreibe die Intro-Musik (als Musik-Prompt)
3. SOUNDEFFEKTE: Liste nötige Sound-FX
4. COVER-ART: Beschreibe das Episode-Cover (als Bild-Prompt)

Thema: [Dein Thema]
Ton: [Locker/Sachlich/Humorvoll]
```

### Projekt 3: Social Media Campaign

```
Erstelle eine 5-Post-Campaign für Instagram:

Für jeden Post:
1. BILD: Detaillierter Bild-Prompt
2. CAPTION: Instagram-Text (inkl. Hashtags)
3. STORY: Begleitende Story-Idee

Marke: [Beschreibung]
Kampagnen-Ziel: [Was soll erreicht werden?]
Zielgruppe: [Wer?]
Visuelle Identität: [Farben, Stil, Mood]
```

## Best Practices für multimodales Arbeiten

### 1. Starte mit der stärksten Modalität
Wenn du ein Bild im Kopf hast → starte mit dem Bild-Prompt. Wenn du eine Geschichte hast → starte mit dem Text. Nutze die Stärke als Anker.

### 2. Halte die Stimmung konsistent
Das größte Problem bei multimodalen Projekten: Die Teile passen nicht zusammen. Definiere die Stimmung einmal und verweise in jedem Prompt darauf.

### 3. Iteriere innerhalb der Modalität
Perfektioniere das Bild, bevor du die Musik dazu machst. Sonst iterierst du auf zwei Fronten gleichzeitig.

### 4. Nutze Cross-References
```
Dieses Bild [Upload] wurde generiert. Schreibe
einen Songtext, der die Stimmung dieses Bildes einfängt.
```

Modelle, die Bilder verstehen, können die Stimmung übersetzen – von visuell zu textlich oder musikalisch.

---

## Übungen

### Übung 1: Bild-zu-Geschichte
Nimm ein Foto (dein eigenes oder ein lizenzfreies) und lade es in ein multimodales Modell. Lass es eine Geschichte dazu schreiben. Dann: Lass es einen Bild-Prompt für eine Fortsetzung der Geschichte generieren.

### Übung 2: Cross-modaler Workflow
Wähle einen der 4 Workflows und führe ihn komplett durch. Dokumentiere jeden Schritt und das Ergebnis.

### Übung 3: Stil übertragen
Finde ein Bild, dessen Stil du magst. Lade es hoch, lass den Stil analysieren und generiere ein neues Bild in demselben Stil mit einem komplett anderen Motiv.

### Übung 4: Multi-Post-Campaign
Erstelle eine 3-Post-Social-Media-Campaign für ein Produkt oder Hobby deiner Wahl. Generiere Bilder, Texte und (wenn möglich) einen kurzen Videoclip.
