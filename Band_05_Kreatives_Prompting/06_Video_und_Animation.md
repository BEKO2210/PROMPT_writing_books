# Kapitel 6: Video und Animation – Bewegte Bilder aus Text

Das ist das Kapitel, das in einem Jahr komplett veraltet sein könnte. Video-KI entwickelt sich so schnell, dass jeder Monat neue Möglichkeiten bringt. Was ich dir hier zeige, ist der Stand März 2026 – und es ist bereits beeindruckend.

## Die Video-KI-Landschaft (Stand 2026)

| Tool | Stärke | Limitation | Länge |
|---|---|---|---|
| **Sora** (OpenAI) | Filmqualität, Physik-Verständnis | Zugang beschränkt | bis 60s |
| **Runway Gen-3** | Vielseitig, Bild-zu-Video | Konsistenz über lange Clips | bis 18s |
| **Pika** | Schnell, einfach zu nutzen | Weniger Kontrolle | bis 10s |
| **Kling** (Kuaishou) | Bewegungsqualität, günstig | Weniger bekannt im Westen | bis 120s |
| **Stable Video** | Open Source, anpassbar | Technischer | bis 25s |
| **Veo 2** (Google) | Fotorealismus, längere Clips | Google-Ökosystem | bis 120s |

## Video-Prompts: Grundlagen

Video-Prompts sind wie Bild-Prompts plus zwei Dimensionen: Zeit und Bewegung.

### Die Bausteine

```
SZENE: [Was sieht man?]
KAMERA: [Wie bewegt sich die Kamera?]
BEWEGUNG: [Was passiert im Video?]
STIL: [Visueller Stil]
DAUER: [Wie lang?]
STIMMUNG: [Welches Gefühl?]
```

### Kamera-Vokabular

Das richtige Kamera-Vokabular macht den Unterschied zwischen "KI-Video" und "könnte ein Filmclip sein":

| Begriff | Beschreibung | Wirkung |
|---|---|---|
| Static shot | Kamera bewegt sich nicht | Ruhe, Beobachtung |
| Slow pan | Langsame horizontale Bewegung | Erkundung, Weite |
| Tracking shot | Kamera folgt einem Objekt | Dynamik, Verfolgung |
| Dolly zoom | Zoom rein + Kamera raus (oder umgekehrt) | Vertigo-Effekt, Unruhe |
| Crane shot | Kamera hebt sich nach oben | Erhabenheit, Übersicht |
| Close-up | Nahaufnahme | Intimität, Detail |
| Aerial / Drone | Von oben | Perspektive, Majestät |
| Timelapse | Zeitraffer | Vergehen der Zeit |
| Slow motion | Zeitlupe | Drama, Schönheit |

### Beispiel-Prompts

**Naturszene:**
```
Aerial drone shot über einen nebligen Bergsee bei
Sonnenaufgang. Langsamer Vorwärtsflug über das
spiegelglatte Wasser. Nadelwälder an den Ufern.
Sonnenstrahlen brechen durch die Wolkendecke.
Filmisch, 4K, warme goldene Farbtöne.
Stimmung: Ehrfurcht, Stille, Größe.
Slow motion. 10 Sekunden.
```

**Urbane Szene:**
```
Tracking shot durch eine belebte Tokio-Straße bei Nacht.
Neonlichter spiegeln sich auf nassem Asphalt.
Menschen mit Regenschirmen. Slow motion.
Kamera auf Hüfthöhe, bewegt sich gegen die
Menschenmenge. Cyberpunk-Ästhetik.
Farbpalette: Neonpink, Blau, warmes Orange.
Anamorphe Lens Flares. 8 Sekunden.
```

**Produkt-Video:**
```
Close-up einer Kaffeetasse auf einem Holztisch.
Dampf steigt langsam auf. Kamera kreist langsam um
die Tasse (360° in 6 Sekunden). Warmes Morgenlicht
von rechts. Minimalistisch, cleaner Hintergrund.
Bokeh. Werbung-Ästhetik. Slow motion.
```

## Bild-zu-Video (Image-to-Video)

Viele Video-KIs können ein Standbild zum Leben erwecken. Das ist oft kontrollierter als reines Text-zu-Video:

### Workflow

1. Generiere ein Bild mit DALL-E/Midjourney (volle Kontrolle über Komposition)
2. Nutze Runway/Pika, um das Bild zu animieren
3. Gib an, WAS sich bewegen soll

### Animations-Prompt (für Bild-zu-Video)

```
Ausgangsbild: [Dein generiertes Bild]

Animation:
- Wind bewegt die Blätter im Vordergrund
- Wolken ziehen langsam am Himmel
- Leichte Kamerabewegung nach vorne (Dolly in)
- Lichtstimmung bleibt konstant

Nicht bewegen: [Was statisch bleiben soll]
Dauer: 4 Sekunden
```

## Animation und Motion Graphics

Für abstraktere, grafische Videos:

### Logo-Animation
```
Animiere dieses Logo: [Logo-Beschreibung]

Stil: Clean, minimalistisch, professionell.
Das Logo baut sich aus geometrischen Elementen auf.
Jedes Element erscheint nacheinander.
Am Ende: Logo komplett, leichter Glanz-Effekt.
Dauer: 3 Sekunden. Schwarzer Hintergrund.
Smooth Ease-in-out Bewegungen.
```

### Infografik-Animation
```
Animiere eine Infografik:

Daten: [Zahlen/Fakten]
Stil: Flat Design, lebhafte Farben.
Animation: Balken wachsen von unten nach oben,
Zahlen zählen hoch, Icons poppen nacheinander auf.
Smooth Transitions zwischen den Datenpunkten.
Hintergrund: Weiß. Dauer: 15 Sekunden.
```

## Grenzen von Video-KI (2026)

### Was gut funktioniert:
- Landschaften und Natur
- Einfache Kamerabewegungen
- Zeitraffer und Zeitlupe
- Abstrakte und stilisierte Videos
- Kurze Clips (5-15 Sekunden)

### Was noch nicht gut funktioniert:
- **Konsistente Personen** über mehrere Clips
- **Hände und Finger** in Bewegung
- **Text im Video** (genau wie bei Bildern)
- **Lippensynchronisation** bei Gesang/Sprache
- **Physikalisch korrekte Interaktionen** (Objekte greifen, werfen)
- **Längere, zusammenhängende Videos** (>30 Sekunden mit Plot)

### Workaround: Schnitt

Die meisten professionellen KI-Videos bestehen aus mehreren kurzen Clips, die zusammengeschnitten werden. Der Workflow:

1. Plane dein Video als Storyboard (5-10 Szenen)
2. Generiere jede Szene als einzelnen Clip (5-10 Sekunden)
3. Schneide sie zusammen in CapCut, DaVinci Resolve oder iMovie
4. Füge Musik und Sound hinzu (aus Kapitel 5)

## Video für verschiedene Plattformen

### TikTok / Instagram Reels (9:16 vertikal)
```
Vertikales Format (9:16). Schneller Schnitt.
Szene 1 (2s): [Hook – muss sofort fesseln]
Szene 2 (3s): [Hauptinhalt]
Szene 3 (2s): [Payoff/Überraschung]
Dynamische Kamerabewegung. Lebhafte Farben.
Trend-Ästhetik: Schnelle Zoom-Ins, Glitch-Effekte.
```

### YouTube (16:9 horizontal)
```
Horizontales Format (16:9). Filmisch.
Establishing Shot: Weitwinkel, Setting vorstellen.
Ruhigere Schnitte, längere Einstellungen.
Professionelle Farbkorrektur. Tiefenschärfe (Bokeh).
```

### Präsentation / Corporate
```
16:9 Format. Clean, professionell.
Keine schnellen Schnitte. Sanfte Übergänge.
Corporate-Farben: [Hex-Werte].
Minimale Bewegung, Fokus auf Klarheit.
Geeignet als Hintergrund für Slides oder als Opener.
```

---

## Übungen

### Übung 1: Erster Video-Prompt
Nutze ein kostenloses Video-KI-Tool (Pika, Runway Free Tier) und generiere einen 5-Sekunden-Clip. Nutze alle Bausteine (Szene, Kamera, Bewegung, Stil).

### Übung 2: Bild-zu-Video
Generiere zuerst ein Bild mit DALL-E oder einem anderen Bild-Generator. Dann animiere es mit einer Video-KI. Wie viel Kontrolle hast du über die Animation?

### Übung 3: Storyboard
Plane ein 30-Sekunden-Video als Storyboard (6 Szenen à 5 Sekunden). Beschreibe jede Szene als Video-Prompt. Du musst sie nicht alle generieren – die Planung ist die Übung.

### Übung 4: Plattform-Anpassung
Nimm eine Szenen-Idee und formuliere sie für drei verschiedene Plattformen: TikTok (9:16, schnell), YouTube (16:9, filmisch), LinkedIn (16:9, corporate). Wie verändert sich der Prompt?
