# Prompt Engineering Meistern – 10-bändige Buchreihe

**Autor:** Belkis Aslani | **Stand:** März 2026

## Über diese Reihe

Eine deutschsprachige Sachbuchreihe zum Thema Prompt Engineering für Large Language Models. 10 Bände, vom absoluten Anfänger bis zum Experten. Jeder Band baut auf dem vorherigen auf.

---

## Bände im Überblick

### Anfänger (Band 1-3)

| Band | Titel | Status | Beschreibung |
|------|-------|--------|-------------|
| 1 | **Grundlagen** | ✅ Fertig | Was ist KI, wie funktionieren LLMs, erste Prompts schreiben, häufige Fehler vermeiden, Kontext und Rollen nutzen, Output-Formate steuern, iterativ verbessern |
| 2 | **Prompt-Frameworks** | 📝 Geplant | CRAFT, RTF, RISEN Frameworks; Zero-Shot, Few-Shot, One-Shot; Template-Bibliothek aufbauen |
| 3 | **Fortgeschrittene Basics** | 📝 Geplant | Prompt-Chaining, Delimiter, negative Prompts, Temperatur/Parameter, LLM-Vergleich, System-Prompts |

### Fortgeschritten (Band 4-6)

| Band | Titel | Status | Beschreibung |
|------|-------|--------|-------------|
| 4 | **Reasoning-Techniken** | 📝 Geplant | Chain-of-Thought, Tree-of-Thought, Self-Consistency, ReAct, Meta-Prompting |
| 5 | **Kreatives Prompting** | 📝 Geplant | Storytelling, kreatives Schreiben, Bild-Generierung, Musik/Audio, multimodales Prompting |
| 6 | **Spezialisiertes Prompting** | 📝 Geplant | Branchenspezifisch: Bildung, Marketing, Datenanalyse, Wissenschaft, Recht, Medizin |

### Profi (Band 7-9)

| Band | Titel | Status | Beschreibung |
|------|-------|--------|-------------|
| 7 | **Prompting für Entwickler** | 📝 Geplant | Code-Generierung, APIs, Python/JS, RAG, Fine-Tuning vs. Prompting, automatisierte Optimierung |
| 8 | **Business & Produktivität** | 📝 Geplant | Workflow-Automatisierung, E-Mail/Berichte, Entscheidungsunterstützung, Team-Standards |
| 9 | **Sicherheit & Ethik** | 📝 Geplant | Prompt Injection, Scaffolding, Bias, DSGVO, EU AI Act, Halluzinationen |

### Experte (Band 10)

| Band | Titel | Status | Beschreibung |
|------|-------|--------|-------------|
| 10 | **Die Zukunft** | 📝 Geplant | Agentic AI, autonome Agenten, Context Engineering, multimodales Prompting, Automated Prompt Engineering |

---

## Projektstruktur

```
PROMPT_writing_books/
├── CLAUDE.md                    # Diese Datei – Projekt-Übersicht
├── build_pdf.py                 # PDF-Generator (WeasyPrint, A5-Format)
├── build_web.py                 # Web-Generator (HTML/CSS/JS)
├── index.html                   # Redirect → docs/index.html
│
├── Band_01_Grundlagen/          # Markdown-Quelldateien Band 1
│   ├── README.md
│   ├── 00_Vorwort.md
│   ├── 01_Was_ist_KI_eigentlich.md
│   └── ...
├── Band_02_Prompt_Frameworks/   # (geplant)
│   └── ...
├── ...                          # Band 03-10 (geplant)
│
├── output/                      # Generierte PDFs
│   ├── Band_01_Grundlagen.pdf
│   └── Band_01_Grundlagen.html  # Debug-HTML
│
└── docs/                        # Webseite (GitHub Pages kompatibel)
    ├── index.html               # Buchverzeichnis (alle 10 Bände)
    └── band-01/
        └── index.html           # Web-Leseversion Band 1
```

## Build-Befehle

### PDF generieren
```bash
python3 build_pdf.py                    # Band 1 (Standard), A5-Format
python3 build_pdf.py --band 1           # Explizit Band 1
python3 build_pdf.py --band 1 --draft   # Mit ENTWURF-Wasserzeichen
```

### Webseite generieren
```bash
python3 build_web.py                    # Generiert docs/ Verzeichnis
```

## PDF-Spezifikationen

- **Format:** A5 (148mm × 210mm)
- **Ränder:** Innen 18mm (Bindung), Außen 14mm, Oben 16mm, Unten 18mm
- **Schrift:** Liberation Serif (Text), Liberation Sans (Überschriften), Liberation Mono (Code)
- **Schriftgröße:** 9.5pt (A5-optimiert)
- **Features:** Titelseite, Copyright, Inhaltsverzeichnis, Seitenzahlen, Kapitel-Seitenumbrüche
- **Verkaufsplattformen:** Gumroad, Amazon KDP, Lulu, Epubli

## Webseite-Spezifikationen

- **Verzeichnis (docs/index.html):** Dark-Theme, animierter Gradient, Glassmorphism-Karten für alle 10 Bände
- **Leseversion (docs/band-XX/):** Mobile-first, Dark/Light-Mode, Lese-Fortschrittsbalken, sticky TOC
- **Technologie:** Pure HTML/CSS/Vanilla JS, keine Frameworks
- **Kompatibel mit:** GitHub Pages, Netlify, Vercel, statisches Hosting

## Schreibstil-Leitfaden

- **Sprache:** Deutsch, lockerer Ton, Du-Ansprache
- **Perspektive:** Ich-Form (Belkis Aslani)
- **Zielgruppe:** Deutschsprachige Leser ohne bis mit Vorwissen (je nach Band)
- **Vermeiden:** KI-typische Floskeln ("faszinierende Reise", "tauchen wir ein", "in der heutigen digitalen Welt")
- **Nutzen:** Persönliche Anekdoten, praktische Beispiele, Übungen am Kapitelende, variierende Satzlängen

## Dateistruktur pro Band

```
Band_XX_Name/
├── README.md           # Übersicht und Kapitelverzeichnis
├── 00_Vorwort.md       # Vorwort
├── 01_Kapitelname.md   # Kapitel 1
├── 02_Kapitelname.md   # Kapitel 2
└── ...
```

## Band 1 – Inhalt (Referenz)

Band 1 enthält 10 Kapitel + Vorwort:
- **Vorwort:** Wer ist Belkis Aslani, warum diese Buchreihe
- **Kap. 1:** Was ist KI eigentlich? (Geschichte, Typen, Alltags-KI)
- **Kap. 2:** LLMs verstehen (Funktionsweise, Training, Token, die wichtigsten Modelle)
- **Kap. 3:** Dein erster Prompt (Account erstellen, loslegen, 10 Beispiele)
- **Kap. 4:** Anatomie eines guten Prompts (5 Bausteine, Vorher/Nachher)
- **Kap. 5:** Die häufigsten Fehler (zu vage, zu viel, keine Rolle, Halluzinationen)
- **Kap. 6:** Kontext ist alles (Hintergrund geben, Zielgruppe definieren)
- **Kap. 7:** Rollen und Personas (Rollen zuweisen, Experten vs. kreative Personas)
- **Kap. 8:** Output-Formate steuern (Listen, Tabellen, JSON, Länge, Tonalität)
- **Kap. 9:** Iteratives Prompting (Verfeinern, Feedback, Prompt-Protokoll)
- **Kap. 10:** Zusammenfassung und Ausblick (Checkliste, Vorschau Band 2)

## Abhängigkeiten

```bash
pip3 install weasyprint markdown Pygments
```

## Farb-Schema

| Verwendung | Farbe | Hex |
|---|---|---|
| Primär dunkel | Navy | `#0a1628` |
| Primär mittel | Dunkelblau | `#1a2744` |
| Primär hell | Blau | `#2d4a7a` |
| Akzent | Hellblau | `#8ab4f8` |
| Text | Fast-Schwarz | `#1a1a1a` |
| Hintergrund hell | Weiß | `#ffffff` |
| Hintergrund dunkel | GitHub Dark | `#0d1117` |
