# Kapitel 5: Multimodales Prompting – Text + Bild + Audio + Video

In Band 5 hast du kreatives Prompting mit Bildern und Musik kennengelernt. Das war 2025. Seitdem hat sich die multimodale KI rasant weiterentwickelt. Die Modelle von 2026 können nicht nur Text generieren – sie sehen, hören, sprechen und erstellen visuelle Inhalte auf einem Niveau, das vor zwei Jahren Science Fiction war.

## Was "multimodal" heute bedeutet

### Input: Was Modelle verstehen

| Modalität | Was sie verstehen | Beispiel |
|-----------|-------------------|---------|
| **Text** | Alle Sprachen, Code, Formeln | Standard |
| **Bilder** | Fotos, Screenshots, Diagramme, Handschrift | "Beschreibe dieses Bild" |
| **PDFs** | Dokumente mit Layout und Grafiken | "Fasse dieses PDF zusammen" |
| **Audio** | Sprache, Musik, Umgebungsgeräusche | "Transkribiere dieses Meeting" |
| **Video** | Szenen, Aktionen, zeitliche Abfolgen | "Was passiert in diesem Video?" |

### Output: Was Modelle generieren

| Modalität | Stand 2026 | Tools/Modelle |
|-----------|-----------|---------------|
| **Text** | Exzellent | Alle LLMs |
| **Bilder** | Sehr gut | DALL-E 3, Midjourney, Stable Diffusion, Imagen 3 |
| **Audio/Sprache** | Gut-Sehr gut | OpenAI TTS/Voice, ElevenLabs, Suno |
| **Video** | Gut (kurz) | Sora, Runway, Kling, Veo |
| **Code** | Exzellent | Alle Coding-LLMs |
| **3D** | Frühe Phase | Point-E, Meshy, Tripo |

## Bild-Verständnis (Vision)

### Was 2026-Modelle in Bildern erkennen

Nicht nur "Das ist eine Katze." Sondern:

- **Screenshots analysieren:** "Erstelle den HTML/CSS-Code für dieses Design"
- **Diagramme verstehen:** "Erkläre diese Architektur" (aus einem Whiteboard-Foto)
- **Handschrift lesen:** Notizen, Post-its, Formulare
- **Daten extrahieren:** Tabellen, Charts, Grafiken → strukturierte Daten
- **Fehler finden:** "Was ist falsch in diesem UI-Screenshot?"
- **Vergleichen:** "Was hat sich zwischen Version A und Version B geändert?"

### Vision-Prompt-Techniken

**Sei spezifisch darin, was du sehen willst:**
- Schlecht: *"Was ist auf diesem Bild?"*
- Gut: *"Analysiere dieses Dashboard-Screenshot. Welche KPIs sind im roten Bereich? Welche Trends erkennst du?"*

**Kombiniere Bild + Text für präzisere Ergebnisse:**
- *"Hier ist ein Foto meines Serverraums. Markiere alle Kabel, die nicht ordentlich verlegt sind."*
- *"Hier ist eine Handskizze meiner App-Idee. Erstelle daraus ein Wireframe in Figma-Qualität."*

**Multi-Image-Vergleich:**
- *"Hier sind Screenshots meiner Website vor und nach dem Redesign. Liste alle Unterschiede auf."*

## Audio und Sprache

### Sprach-Interaktion

OpenAIs Advanced Voice Mode hat gezeigt, was möglich ist: Natürliche, flüssige Gespräche mit KI. Unterbrechungen werden verstanden, emotionaler Tonfall wird erkannt, die Antworten klingen menschlich.

Das verändert die Art, wie wir mit KI interagieren. Statt zu tippen, sprechen wir. Das ist nicht nur bequemer – es ist natürlicher und ermöglicht neue Anwendungsfälle:

- **Echtzeit-Übersetzer:** Gespräche in Echtzeit übersetzen
- **Meeting-Assistent:** Live im Meeting zuhören, Notizen machen, Fragen beantworten
- **Sprachgesteuerter Agent:** "Hey Claude, buche mir einen Flug nach Berlin für nächsten Dienstag"
- **Lern-Partner:** Fremdsprachen mit einem KI-Tutor üben, der Aussprache korrigiert

### Audio-Analyse

Modelle können Audio analysieren:
- Transkripte aus Meetings, Interviews, Podcasts
- Sentiment-Analyse aus Stimmlagen
- Musik analysieren und beschreiben
- Umgebungsgeräusche identifizieren

## Video

### Was möglich ist

**Kurze Videos generieren (5-60 Sekunden):** Sora (OpenAI), Runway, Kling, Veo (Google). Die Qualität ist 2026 beeindruckend für kurze Clips – Produktdemos, Social-Media-Content, Konzeptvisualisierungen.

**Videos verstehen:** Gemini kann Videos als Input nehmen und Fragen dazu beantworten: "Was passiert in Minute 3?" oder "Fasse die wichtigsten Punkte dieses 30-Minuten-Vortrags zusammen."

### Limitationen

- Längere Videos (>1 Minute) sind qualitativ noch inkonsistent
- Physik und menschliche Hände sind immer noch problematisch
- Die Kosten sind hoch – ein 10-Sekunden-Video kann mehrere Dollar kosten
- Kontrolle über das Ergebnis ist begrenzt – du bekommst nicht immer, was du dir vorstellst

## Multimodales Prompting in der Praxis

### Anwendungsfall 1: Dokumentenanalyse

Statt Texte aus PDFs zu extrahieren (fehleranfällig), gibst du das PDF als Bild an die KI. Sie versteht Layout, Tabellen, Grafiken und Zusammenhänge – besser als reine Textextraktion.

### Anwendungsfall 2: Prototyping

Skizziere auf Papier → fotografiere → KI generiert Wireframe → KI generiert Code. Vom Napkin-Sketch zum funktionierenden Prototyp in Minuten.

### Anwendungsfall 3: Content-Erstellung

Ein einziger Prompt kann eine Multi-Format-Content-Strategie starten: Blogpost schreiben → Zusammenfassung für Social Media → Bild-Vorschlag für Header → Video-Skript für kurzes Erklärvideo.

### Anwendungsfall 4: Qualitätskontrolle

Fotos von Produkten, Baustellen, Serverräumen analysieren lassen. KI erkennt Mängel, fehlende Teile, Abweichungen vom Standard.

### Anwendungsfall 5: Barrierefreiheit

Multimodale KI hat das Potenzial, Barrierefreiheit fundamental zu verbessern:
- **Blinde und sehbehinderte Nutzer:** KI beschreibt, was auf dem Bildschirm ist – in Echtzeit, per Sprache
- **Gehörlose Nutzer:** Echtzeit-Transkription von Gesprächen und Meetings
- **Sprachbarrieren:** Echtzeit-Übersetzung in Audio und Text gleichzeitig
- **Kognitive Einschränkungen:** Komplexe Informationen vereinfachen und in verschiedenen Formaten darstellen

Das ist nicht nur eine technische Möglichkeit – es ist eine moralische Verpflichtung. Multimodale KI kann Millionen Menschen den Zugang zu Informationen und Kommunikation ermöglichen, der ihnen bisher verwehrt war.

### Anwendungsfall 6: Bildung

Ein Lehrer, der in Band 6 die Bildungs-Prompts gelernt hat, kann jetzt:
- Handschriftliche Schülerarbeiten fotografieren und automatisch bewerten lassen
- Unterrichtsvideos zusammenfassen und Key-Learnings extrahieren
- Interaktive Lernmaterialien erstellen, die Text, Bild und Audio kombinieren
- Schüler-Präsentationen per Video analysieren und Feedback geben

## Die Zukunft: Native Multimodalität

Heutige Modelle verarbeiten verschiedene Modalitäten oft noch getrennt: Ein Modul für Text, ein Modul für Bilder, ein Modul für Audio. Die nächste Generation wird **nativ multimodal** sein – alles wird im selben Modell verarbeitet, nahtlos und gleichzeitig.

Das bedeutet: Du wirst einem Agenten ein Video zeigen, eine Sprachfrage stellen und als Antwort einen Mix aus Text, Bildern und Sprache bekommen – fließend und integriert.

---

## Übungen

### Übung 1: Bild-Analyse
Mache ein Foto von deinem Arbeitsplatz und lass es analysieren. Was erkennt die KI? Was überrascht dich?

### Übung 2: Screenshot-zu-Code
Mache einen Screenshot einer Webseite und lass den HTML/CSS-Code generieren. Wie nah kommt die KI ans Original?

### Übung 3: Voice-Interaktion
Wenn verfügbar: Führe ein 5-Minuten-Gespräch mit einer KI per Sprache. Wie unterscheidet sich das Erlebnis vom Tippen?

### Übung 4: Multi-Format-Content
Nimm einen Blogpost und lass ihn in 4 Formate umwandeln: Social Media Post, Präsentationsfolie, Newsletter-Snippet und Video-Skript.
