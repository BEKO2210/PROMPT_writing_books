# Kapitel 4: Bild-Generierung – Von der Idee zum Bild

Text war gestern. Jetzt malen wir.

Bild-Generierung ist der Bereich, in dem KI-Kreativität am sichtbarsten geworden ist. DALL-E, Midjourney, Stable Diffusion, Flux, Adobe Firefly – in den letzten drei Jahren ist eine ganze Industrie entstanden. Und die Qualität ist von "lustige Verzerrungen" zu "ist das ein Foto?" gesprungen.

In diesem Kapitel lernst du, wie du Bild-Prompts schreibst, die mehr produzieren als generische Stock-Fotos.

## Die Bild-KI-Landschaft (Stand 2026)

| Tool | Stärke | Schwäche | Zugang |
|---|---|---|---|
| **Midjourney** | Ästhetik, Kunststile | Wenig Kontrolle über Details | Discord / Web |
| **DALL-E 3** | Textverstehen, Integration mit ChatGPT | Weniger künstlerisch | ChatGPT Plus / API |
| **Stable Diffusion** | Vollständige Kontrolle, Open Source | Technischer, Lernkurve | Lokal / Online |
| **Flux** | Fotorealismus, Schnelligkeit | Neueres Ökosystem | API / Online |
| **Adobe Firefly** | Ethische Trainingsdaten, Photoshop-Integration | Weniger kreativ | Adobe Creative Cloud |
| **Imagen 3** | Textverstehen, Google-Integration | Beschränkter Zugang | Google AI Studio |

Welches Tool du nutzt, ist weniger wichtig als *wie* du deine Prompts schreibst. Die Grundprinzipien gelten überall.

## Die Anatomie eines Bild-Prompts

Ein guter Bild-Prompt besteht aus fünf Bausteinen:

### 1. Subjekt (Was?)
Was soll auf dem Bild zu sehen sein?
- "Eine Frau mit rotem Mantel"
- "Ein verlassener Bahnhof"
- "Eine Katze, die Klavier spielt"

### 2. Stil (Wie?)
Wie soll es aussehen?
- "Ölgemälde", "Aquarell", "Fotorealistisch"
- "Im Stil der Renaissance", "Cyberpunk-Ästhetik"
- "Minimalistisch", "Hyperdetailliert"

### 3. Komposition (Wo im Bild?)
Wie ist das Bild aufgebaut?
- "Nahaufnahme", "Totale", "Vogelperspektive"
- "Symmetrisch", "Rule of Thirds"
- "Vordergrund: X, Hintergrund: Y"

### 4. Beleuchtung (Welches Licht?)
Licht macht oder bricht ein Bild.
- "Goldene Stunde", "Gegenlicht", "Studioblitz"
- "Diffuses Tageslicht", "Kerzenschein"
- "Neonlicht", "Mondlicht"

### 5. Atmosphäre (Welches Gefühl?)
Die Stimmung des Bildes.
- "Melancholisch", "Fröhlich", "Bedrohlich"
- "Verträumt", "Dramatisch", "Intim"
- "Nostalgisch", "Futuristisch"

### Der vollständige Bild-Prompt

```
[SUBJEKT], [STIL], [KOMPOSITION],
[BELEUCHTUNG], [ATMOSPHÄRE]
```

### Beispiel

**Schlecht:**
```
Ein Wald
```

**Gut:**
```
Dichter Nadelwald im Nebel, Ölgemälde im Stil der
Romantik, Blick von einem Waldweg nach vorne,
diffuses Morgenlicht das durch die Baumkronen bricht,
mysteriöse und stille Atmosphäre
```

**Sehr gut:**
```
Ein schmaler Waldweg verschwindet im Nebel eines dichten
Nadelwaldes. Ölgemälde-Stil, inspiriert von Caspar David
Friedrich. Perspektive: Betrachter steht am Anfang des Weges.
Diffuses Morgenlicht, Sonnenstrahlen brechen durch das
Blätterdach. Farbpalette: Dunkelgrün, Moosbraun, goldenes
Licht. Stimmung: Ehrfürchtig, still, als würde der Wald
ein Geheimnis hüten. Hyperdetailliert.
```

## Stil-Vokabular

Das richtige Wort macht den Unterschied. Hier ist dein Stil-Wörterbuch:

### Kunstrichtungen
| Begriff | Ergebnis |
|---|---|
| Impressionismus | Weich, lichtdurchflutet, Pinselstriche sichtbar |
| Art Nouveau / Jugendstil | Organische Linien, florale Muster, elegant |
| Bauhaus | Geometrisch, minimalistisch, primäre Farben |
| Pop Art | Kräftige Farben, Comic-Ästhetik, Wiederholung |
| Ukiyo-e | Japanischer Holzschnitt-Stil, flache Flächen |
| Art Déco | Geometrisch, luxuriös, Gold, Symmetrie |

### Fotografie-Begriffe
| Begriff | Ergebnis |
|---|---|
| Bokeh | Verschwommener Hintergrund, scharfes Subjekt |
| Long Exposure | Fließendes Wasser, Lichtspuren |
| Tilt-Shift | Miniatureffekt, selektive Schärfe |
| High Key | Hell, wenig Schatten, luftig |
| Low Key | Dunkel, dramatisch, Chiaroscuro |
| Film Grain | Körnig, analog, Retro-Feeling |

### Render-Begriffe (für 3D/Digital)
| Begriff | Ergebnis |
|---|---|
| Octane Render | Hyperrealistisch, perfekte Beleuchtung |
| Unreal Engine | Gaming-Ästhetik, dynamisch |
| Isometric | 3D-Schrägansicht, technisch |
| Voxel Art | Pixelig, Minecraft-artig |
| Wireframe | Nur Drahtgitter, technisch |
| Ray Tracing | Perfekte Reflektionen und Lichtbrechung |

## Negative Prompts für Bilder

Du kennst negative Prompts aus Band 3. Bei Bildern sind sie besonders wichtig:

```
Negative Prompt: Verschwommene Hände, deformierte Finger,
extra Gliedmaßen, Text im Bild, Wasserzeichen,
schlechte Anatomie, verzerrte Gesichter,
niedriger Detailgrad
```

### Die häufigsten Bild-Probleme und ihre Negativ-Prompts

| Problem | Negativ-Prompt |
|---|---|
| Verzerrte Hände | "deformed hands, extra fingers, bad anatomy" |
| Unscharfes Bild | "blurry, low quality, low resolution" |
| Ungewollter Text | "text, watermark, signature, labels" |
| Zu viel auf dem Bild | "cluttered, busy background, too many elements" |
| Unheimliche Gesichter | "uncanny valley, distorted face, asymmetric eyes" |

## Fortgeschrittene Bild-Techniken

### Technik 1: Referenz-Stacking

Statt einem Stil kombinierst du mehrere Referenzen:

```
Eine futuristische Bibliothek.
Die Architektur von Zaha Hadid,
die Farbpalette von Wes Anderson,
die Beleuchtung eines Vermeer-Gemäldes.
Fotorealistisch, 8K, Weitwinkel.
```

Das erzeugt Bilder, die in keinem einzelnen Stil existieren – sondern in einer neuen Kombination. Das ist echte KI-Kreativität.

### Technik 2: Mood Board als Prompt

```
Erstelle ein Bild, das diese Stimmung einfängt:

Ein Sonntagnachmittag im November.
Der Geruch von frisch gebackenem Brot.
Regen an der Fensterscheibe.
Ein Buch, das du nie zu Ende gelesen hast.
Wollsocken.
Die Art Licht, die alles weich macht.

Stil: Fotografie, leicht überbelichtet, warme Töne.
Keine Person im Bild. Nur Gegenstände und Atmosphäre.
```

Du beschreibst keine Szene, sondern ein Gefühl. Und die KI übersetzt es in ein Bild. Die Ergebnisse sind oft überraschend gut.

### Technik 3: Der Negativ-Raum

```
Ein einzelner roter Regenschirm auf einer riesigen,
leeren, regennassen Betonfläche.
90% des Bildes ist leerer Raum.
Minimalistisch. Der Regenschirm ist klein, aber
der Fokus. Farbpalette: Grau, Dunkelgrau, ein
einziges kräftiges Rot.
```

Negativer Raum (leere Fläche) ist ein mächtiges Stilmittel, das KI-Generatoren gut umsetzen können.

### Technik 4: Zeitliche Schichtung

```
Ein Gebäude, das drei Epochen gleichzeitig zeigt:
- Linke Seite: Mittelalter (Fachwerk, Strohdach)
- Mitte: Industrialisierung (Backstein, Rauch)
- Rechte Seite: Zukunft (Glas, schwebende Elemente)

Der Übergang ist fließend, als würde die Zeit
durch das Gebäude fließen.
Stil: Concept Art, Filmqualität.
```

### Technik 5: Text-zu-Bild-zu-Text

Ein kreativer Workflow:
1. Beschreibe ein Bild in Worten (dein Prompt)
2. Lass es generieren
3. Beschreibe das generierte Bild in neuen Worten
4. Lass ein neues Bild generieren

Jede Iteration entfernt sich weiter vom Original – wie ein visuelles "Stille Post". Die Ergebnisse sind oft unerwartet kreativ.

## Bild-Prompts für spezifische Anwendungen

### Social Media Content

```
Instagram-Post-Bild für ein Café.
Flache Latte Art in einer keramischen Tasse,
rustikaler Holztisch, Pflanze unscharf im Hintergrund.
Natürliches Fensterlicht von links, warme Töne.
Draufsicht (Flatlay). Platz für Text oben im Bild.
Instagram-Ästhetik: clean, warm, einladend.
```

### Buchcover

```
Buchcover für einen psychologischen Thriller.
Titel: "Der letzte Gast"
Eine einzelne Tür am Ende eines langen,
leeren Hotelflurs. Teppich mit Muster.
Warmes, aber beunruhigendes Licht unter der Tür.
Stil: Fotorealistisch, leicht entsättigt.
Farbpalette: Bernstein, Dunkelbraun, ein Hauch Rot.
Platz für Titel oben und Autorname unten.
```

### Präsentationen und Infografiken

```
Abstrakte Illustration für eine Unternehmenspräsentation
zum Thema "Digitale Transformation".
Keine Klischees (keine Zahnräder, keine Glühbirnen).
Stattdessen: Organische Formen, die sich in geometrische
verwandeln. Farbpalette: Unternehmensblau (#2d4a7a),
Weiß, ein Akzent in Türkis.
Stil: Flach, modern, corporate aber nicht langweilig.
Weißer Hintergrund. Geeignet für 16:9-Slides.
```

## Iteration bei Bildern

Das erste Ergebnis ist selten perfekt. So iterierst du:

### Methode 1: Variationen
```
Das gefällt mir, aber:
- Mach den Himmel dramatischer
- Weniger Elemente im Vordergrund
- Wärmere Farbpalette
```

### Methode 2: Inpainting
Viele Tools erlauben es, nur einen Teil des Bildes neu zu generieren. Nutze das für:
- Gesichter korrigieren
- Hintergrund ändern
- Details hinzufügen

### Methode 3: Upscaling + Detail
```
[Gleiches Bild], aber in höherer Auflösung.
Zusätzliche Details: [spezifische Details, die
du sehen möchtest]
```

## Häufige Fehler bei Bild-Prompts

### Fehler 1: Zu viele Elemente
"Eine Stadt mit Bergen und einem See und einem Boot und einer Burg und einem Drachen und einem Regenbogen und..."
→ Je mehr Elemente, desto chaotischer. Fokussiere auf 2-3 Hauptelemente.

### Fehler 2: Widersprüchliche Anweisungen
"Fotorealistisch, im Stil eines Aquarells" – das geht nicht beides.

### Fehler 3: Keine Beleuchtungsangabe
Beleuchtung ist der wichtigste Faktor für die Stimmung. Ohne Angabe wählt das Modell generisches "Studio-Licht".

### Fehler 4: Text im Bild
KI kann (noch) keinen sauberen Text rendern. Wenn du Text im Bild brauchst, füge ihn nachträglich mit Canva oder Photoshop ein.

---

## Übungen

### Übung 1: Die fünf Bausteine
Generiere ein Bild nur mit dem Subjekt ("Ein Leuchtturm"). Dann füge nacheinander Stil, Komposition, Beleuchtung und Atmosphäre hinzu. Vergleiche alle 5 Versionen.

### Übung 2: Referenz-Stacking
Kombiniere drei Stilreferenzen, die normalerweise nicht zusammengehören (z.B. "japanischer Holzschnitt + Cyberpunk + Pastellfarben"). Was entsteht?

### Übung 3: Mood Board
Beschreibe ein Gefühl, nicht eine Szene. Lass die KI es als Bild umsetzen. Trifft es die Stimmung?

### Übung 4: Iterieren
Generiere ein Bild und verbessere es in 3 Iterationen. Dokumentiere, was du in jeder Runde geändert hast und wie sich das Ergebnis verbessert hat.
