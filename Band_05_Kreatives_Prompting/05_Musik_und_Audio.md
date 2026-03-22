# Kapitel 5: Musik und Audio – KI hören lassen

Von Text zu Bildern zu... Musik? Ja. Und es ist weiter, als du denkst.

2024 hat KI-generierte Musik einen Wendepunkt erreicht. Tools wie Suno und Udio produzieren Songs, die klingen, als kämen sie aus einem professionellen Studio. Nicht perfekt, aber gut genug, um auf Spotify nicht sofort als KI erkannt zu werden.

In diesem Kapitel lernst du, wie du KI-Musik, Soundeffekte und Sprache promptest.

## Die Audio-KI-Landschaft (Stand 2026)

| Tool | Kann | Prompt-Typ | Kosten |
|---|---|---|---|
| **Suno** | Vollständige Songs mit Gesang | Text-Prompt | Freemium |
| **Udio** | Songs, hohe Audioqualität | Text-Prompt | Freemium |
| **Stable Audio** | Instrumentalmusik, Sound FX | Text-Prompt | Freemium |
| **ElevenLabs** | Text-to-Speech, Voice Cloning | Text + Stimme | Abo |
| **AIVA** | Klassische Musik, Filmmusik | Parameter + Text | Freemium |
| **Soundraw** | Lizenzfreie Hintergrundmusik | GUI + Parameter | Abo |
| **MusicLM** (Google) | Musik aus Beschreibungen | Text-Prompt | Research |

## Musik-Prompts schreiben

Musik-Prompts funktionieren anders als Text-Prompts. Du beschreibst nicht WAS gespielt wird (Note für Note), sondern WIE es klingen soll.

### Die Bausteine eines Musik-Prompts

```
GENRE: [Pop/Rock/Jazz/Klassik/Electronic/HipHop/...]
STIMMUNG: [Fröhlich/Melancholisch/Episch/Entspannt/...]
TEMPO: [Langsam/Mittel/Schnell oder BPM-Angabe]
INSTRUMENTE: [Klavier/Gitarre/Streicher/Synths/...]
GESANG: [Männlich/Weiblich/Keiner/Chor]
REFERENZ: [Klingt wie X trifft auf Y]
```

### Beispiele: Von schlecht zu gut

**Schlecht:**
```
Mach mir ein Lied.
```

**Besser:**
```
Ein fröhlicher Pop-Song mit Klavier und akustischer Gitarre.
```

**Gut:**
```
Ein melancholischer Indie-Folk-Song. Akustische Gitarre
(Fingerpicking), leises Klavier, sanftes Schlagzeug.
Weiblicher Gesang, verletzlich und nah. Tempo: 85 BPM.
Stimmung wie ein Spaziergang durch einen herbstlichen
Park, wenn die Blätter fallen und du an jemanden denkst,
den du vermisst.
```

**Sehr gut (für Suno/Udio):**
```
[Genre: Indie Folk / Acoustic]
[Tempo: 85 BPM]
[Mood: Melancholic, nostalgic, intimate]
[Instruments: Fingerpicked acoustic guitar, soft piano,
brushed drums, subtle cello]
[Vocals: Female, breathy, close-mic, emotionally restrained]
[Production: Lo-fi warmth, slight vinyl crackle,
room reverb, intimate recording]
[Structure: Verse - Chorus - Verse - Bridge - Chorus - Outro]
[Reference: Iron & Wine meets Bon Iver's acoustic side]
```

## Song-Texte (Lyrics) generieren

Viele Musik-KIs akzeptieren auch Lyrics. Die kannst du separat mit einem LLM schreiben:

### Der Lyric-Prompt

```
Schreibe den Text für einen [GENRE]-Song.

THEMA: [Worum geht es?]
STIMMUNG: [Wie fühlt sich der Song an?]
PERSPEKTIVE: [Wer singt? An wen?]

STRUKTUR:
Vers 1 (4 Zeilen)
Chorus (4 Zeilen – einprägsam, wiederholbar)
Vers 2 (4 Zeilen)
Chorus
Bridge (2-4 Zeilen – emotionaler Höhepunkt)
Chorus (mit Variation)

REGELN:
- Chorus muss nach einmal Hören hängenbleiben
- Verse erzählen, Chorus fasst zusammen
- Keine Klischee-Reime erzwingen – lieber unreiner
  Reim oder kein Reim als "Herz/Schmerz"
- Jede Zeile muss singbar sein (teste: Lies sie laut)
```

### Beispiel

```
Schreibe den Text für einen Indie-Pop-Song.

THEMA: Die letzte Nacht in der alten Wohnung,
bevor man umzieht.
STIMMUNG: Bittersüß. Abschied, aber auch Aufbruch.
PERSPEKTIVE: Ich-Form. An die Wohnung gerichtet.

STRUKTUR: Vers – Chorus – Vers – Chorus – Bridge – Chorus
SPRACHE: Deutsch
REGELN:
- Konkrete Bilder (die Delle in der Wand, der
  Fleck auf dem Teppich) statt abstrakte Emotionen
- Chorus: Max. 4 Zeilen, einfach, emotional
- Kein "auf Wiedersehen" – zeige den Abschied,
  sag ihn nicht
```

## Soundeffekte und Ambient

Nicht nur Musik – auch Soundeffekte und Atmosphären lassen sich generieren:

### Sound-Design-Prompt

```
Erstelle einen Soundeffekt:
[Beschreibung des Klangs]

Beispiele:
- "Das Geräusch einer rostigen Tür, die sich
  langsam in einer leeren Kathedrale öffnet"
- "Regen auf einem Blechdach, nah, mit
  gelegentlichem Donner in der Ferne"
- "Das Surren und Klicken eines alten Computers,
  der hochfährt – 1990er-Ästhetik"
```

### Ambient-Atmosphären

```
Erstelle eine 2-minütige Ambient-Atmosphäre:

Setting: Japanischer Garten bei Nacht.
Elemente:
- Leichter Wind in Bambusblättern
- Wasser, das in ein Steinbecken tropft (Shishi-odoshi)
- Ferne Grillen
- Sehr leise Windspiele
- Keine Musik, nur Naturklänge

Stimmung: Meditativ, beruhigend, zeitlos.
```

## Voice und Text-to-Speech

ElevenLabs und ähnliche Tools können Stimmen erzeugen, die kaum von echten Menschen zu unterscheiden sind.

### Voice-Prompt

```
Sprich folgenden Text in folgender Stimme:

STIMME: [Männlich/Weiblich, Alter, Charakter]
TON: [Warm/Autoritär/Freundlich/Sachlich]
GESCHWINDIGKEIT: [Langsam/Normal/Schnell]
EMOTION: [Neutral/Begeistert/Ruhig/Traurig]
ANWENDUNG: [Podcast/Hörbuch/Werbung/Meditation]

TEXT:
"[Dein Text]"
```

### Anwendungen für Text-to-Speech

| Anwendung | Stimm-Empfehlung |
|---|---|
| Hörbuch | Warm, variabel, lebhaft |
| Podcast-Intro | Klar, freundlich, mittlere Geschwindigkeit |
| Erklär-Video | Sachlich, deutlich, etwas langsamer |
| Meditation | Tief, langsam, beruhigend |
| Werbung | Energisch, überzeugend, mit Pausen |

## Musik für verschiedene Zwecke

### Hintergrundmusik für Videos

```
Hintergrundmusik für ein YouTube-Tutorial (Tech).
Genre: Lo-fi Electronic / Chillhop.
Tempo: 80-90 BPM.
Stimmung: Entspannt, fokussiert, nicht ablenkend.
Keine Vocals. Leise, im Hintergrund bleibend.
Instrumente: Soft Synths, sanftes Piano,
gedämpfte Drums. 3 Minuten.
```

### Podcast-Jingle

```
Podcast-Intro-Jingle (10 Sekunden).
Genre: Akustik-Pop.
Stimmung: Freundlich, einladend, professionell.
Struktur: Kurzer melodischer Hook, endet mit
einem klaren Abschluss (kein Fade-Out).
Instrumente: Ukulele, Fingersnaps, leichter Bass.
```

### Meditations-Musik

```
Meditationsmusik (15 Minuten).
Genre: Ambient / Drone.
Tempo: Kein spürbarer Beat.
Elemente: Weiche Synth-Pads, Naturklänge (Wasser),
gelegentliche Klangschale. Sanfte Übergänge.
Keine Überraschungen. Fließend.
```

## KI-Musik und Urheberrecht

Noch wichtiger als bei Bildern: Musik und Urheberrecht.

### Was du wissen musst:
- **Kommerziell nutzbar?** Abhängig vom Tool und Plan. Suno Pro erlaubt kommerzielle Nutzung. Kostenlose Pläne meistens nicht.
- **Klingt wie [Künstler]?** Riskant. Wenn ein Song zu nah an einem existierenden Song klingt, drohen Klagen – egal ob KI oder Mensch.
- **GEMA/Streaming?** KI-generierte Musik kann auf Spotify und Apple Music veröffentlicht werden, aber die Plattformen verschärfen ihre Regeln.
- **Trainingsdaten?** Suno und Udio wurden wegen der Verwendung urheberrechtlich geschützter Musik verklagt. Die Rechtslage entwickelt sich.

### Mein Rat:
- Nutze KI-Musik für persönliche Projekte, Hintergrundmusik und Prototypen.
- Für kommerzielle Nutzung: Lies die Lizenzbedingungen. Nutze Tools mit klarer kommerzieller Lizenz.
- Vermeide explizite Kopien ("klingt genau wie [Song X]").
- Wenn du ernsthaft Musik machen willst: KI als Ausgangspunkt, dann eigene Bearbeitung und Produktion.

## Qualität beurteilen

Wie erkennst du gute KI-Musik? Meine Checkliste:

- [ ] Klingt der Song "fertig" oder wie ein Demo?
- [ ] Ist der Gesang verständlich und natürlich?
- [ ] Gibt es eine erkennbare Struktur (Vers, Chorus)?
- [ ] Passt das Ende oder bricht der Song einfach ab?
- [ ] Klingt es wie ein Genre oder wie "KI-Einheitsbrei"?
- [ ] Würdest du es freiwillig nochmal anhören?

Wenn du bei den meisten Punkten "Ja" sagst, hast du einen guten Prompt geschrieben.

---

## Übungen

### Übung 1: Erster Song
Nutze Suno oder Udio (kostenlose Version) und generiere deinen ersten Song. Nutze das vollständige Prompt-Format (Genre, Stimmung, Tempo, Instrumente, Gesang, Referenz).

### Übung 2: Lyrics + Musik
Schreibe zuerst Lyrics mit einem LLM (Claude, ChatGPT). Dann generiere die Musik dazu mit einer Musik-KI. Passen Lyrics und Musik zusammen?

### Übung 3: Hintergrundmusik
Generiere Hintergrundmusik für ein konkretes Projekt (Video, Podcast, Präsentation). Funktioniert sie im Kontext?

### Übung 4: Ambient-Experiment
Erstelle eine 2-minütige Ambient-Atmosphäre für einen Ort deiner Wahl. Schließe die Augen und höre zu. Bist du "dort"?
