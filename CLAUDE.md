# Prompt Engineering Meistern – 10-bandige Buchreihe

**Autor:** Belkis Aslani | **Stand:** Marz 2026

---

## Uber diese Reihe

Deutschsprachige Sachbuchreihe zu Prompt Engineering fur Large Language Models.
10 Bande, vom Anfanger bis zum Experten. Jeder Band baut auf dem vorherigen auf.

---

## Bande

| Band | Titel | Status | Themen |
|------|-------|--------|--------|
| 1 | **Grundlagen** | Fertig | KI-Grundlagen, LLMs, erste Prompts, 5 Bausteine, Fehler, Kontext, Rollen, Output-Formate, Iteration |
| 2 | **Prompt-Frameworks** | Fertig | CRAFT, RTF, RISEN; Zero-Shot, Few-Shot, One-Shot; Template-Bibliothek |
| 3 | **Fortgeschrittene Basics** | Fertig | Prompt-Chaining, Delimiter, negative Prompts, Temperatur, System-Prompts |
| 4 | **Reasoning-Techniken** | Fertig | Chain-of-Thought, Tree-of-Thought, Self-Consistency, ReAct, Meta-Prompting |
| 5 | **Kreatives Prompting** | Fertig | Storytelling, Bild-Generierung, Musik/Audio, multimodales Prompting |
| 6 | **Spezialisiertes Prompting** | Geplant | Bildung, Marketing, Datenanalyse, Wissenschaft, Recht, Medizin |
| 7 | **Prompting fur Entwickler** | Geplant | Code-Generierung, APIs, RAG, Fine-Tuning vs. Prompting |
| 8 | **Business & Produktivitat** | Geplant | Workflow-Automatisierung, E-Mail/Berichte, Team-Standards |
| 9 | **Sicherheit & Ethik** | Geplant | Prompt Injection, Bias, DSGVO, EU AI Act, Halluzinationen |
| 10 | **Die Zukunft** | Geplant | Agentic AI, autonome Agenten, Context Engineering, Automated Prompt Engineering |

---

## Projektstruktur

```
PROMPT_writing_books/
├── CLAUDE.md                       # Projektdokumentation (diese Datei)
├── build_pdf.py                    # PDF-Generator (A5, WeasyPrint)
├── build_web.py                    # Web-Generator (mobile-first HTML)
│
├── index.html                      # Webseite: Buchverzeichnis (alle Bande)
├── band-01/
│   └── index.html                  # Webseite: Leseversion Band 1
├── band-02/
│   └── index.html                  # Webseite: Leseversion Band 2
│
├── output/
│   └── Band_01_Grundlagen.pdf      # Generiertes PDF (A5)
│
├── Band_01_Grundlagen/             # Quell-Markdown Band 1
│   ├── README.md
│   ├── 00_Vorwort.md
│   ├── 01_Was_ist_KI_eigentlich.md
│   ├── 02_LLMs_verstehen.md
│   ├── 03_Dein_erster_Prompt.md
│   ├── 04_Anatomie_eines_guten_Prompts.md
│   ├── 05_Die_haeufigsten_Fehler.md
│   ├── 06_Kontext_ist_alles.md
│   ├── 07_Rollen_und_Personas.md
│   ├── 08_Output_Formate_steuern.md
│   ├── 09_Iteratives_Prompting.md
│   └── 10_Zusammenfassung_und_Ausblick.md
│
├── Band_02_Prompt_Frameworks/      # Quell-Markdown Band 2
├── Band_03_Fortgeschrittene_Basics/
├── Band_04_Chain_of_Thought/
├── Band_05_Kreatives_Prompting/
├── Band_06_Spezialisiertes_Prompting/
├── Band_07_Prompting_fuer_Entwickler/
├── Band_08_Business_und_Produktivitaet/
├── Band_09_Sicherheit_und_Ethik/
└── Band_10_Die_Zukunft/
```

---

## Build-Befehle

```bash
# PDF generieren (A5-Format)
python3 build_pdf.py                          # Band 1 (hell)
python3 build_pdf.py --band 2                 # Band 2
python3 build_pdf.py --band 1 --theme dark    # Dark-Mode-PDF
python3 build_pdf.py --band 1 --draft         # Mit Wasserzeichen

# Webseite generieren
python3 build_web.py                    # Erzeugt band-XX/index.html
```

### Abhangigkeiten

```bash
pip3 install weasyprint markdown Pygments
```

---

## PDF-Spezifikationen

| Eigenschaft | Wert |
|---|---|
| Format | A5 (148mm x 210mm) |
| Rander | Innen 18mm, Aussen 14mm, Oben 16mm, Unten 18mm |
| Schrift Text | Liberation Serif, 9.5pt |
| Schrift Uberschriften | Liberation Sans |
| Schrift Code | Liberation Mono, 7.5pt |
| Features | Titelseite, Copyright, Inhaltsverzeichnis, Seitenzahlen |
| Verkauf | Gumroad, Amazon KDP, Lulu, Epubli |

---

## Webseite

### Buchverzeichnis (`index.html`)
- Dark-Theme mit animiertem Gradient-Hintergrund
- CSS-Partikel-Animation
- Glassmorphism-Karten fur alle 10 Bande
- Responsive Grid, Card-Animations

### Leseversion (`band-01/index.html`)
- Mobile-first, Georgia-Serif fur Lesekomfort
- Dark/Light-Mode Toggle (System-Preference)
- Sticky TOC-Sidebar (Desktop) / Hamburger-Menu (Mobile)
- Lese-Fortschrittsbalken
- Active-Chapter-Tracking
- PDF-Download-Button
- Pure HTML/CSS/Vanilla JS, keine Frameworks

### GitHub Pages

GitHub Pages muss konfiguriert werden:
- **Source:** Deploy from a branch
- **Branch:** Aktueller Branch, Folder: `/ (root)`

---

## Schreibstil

- **Sprache:** Deutsch, lockerer Ton, Du-Ansprache
- **Perspektive:** Ich-Form (Belkis Aslani)
- **Zielgruppe:** Deutschsprachige Leser (Niveau steigt mit den Banden)
- **Vermeiden:** KI-Floskeln ("faszinierende Reise", "tauchen wir ein", "in der heutigen digitalen Welt")
- **Nutzen:** Personliche Anekdoten, praktische Beispiele, Ubungen am Kapitelende

---

## Dateistruktur pro Band

```
Band_XX_Name/
├── README.md           # Ubersicht und Kapitelverzeichnis
├── 00_Vorwort.md       # Vorwort
├── 01_Kapitelname.md   # Kapitel 1
├── 02_Kapitelname.md   # Kapitel 2
└── ...
```

---

## Farb-Schema

| Verwendung | Hex |
|---|---|
| Primar dunkel (Navy) | `#0a1628` |
| Primar mittel | `#1a2744` |
| Primar hell (Blau) | `#2d4a7a` |
| Akzent (Hellblau) | `#8ab4f8` |
| Akzent 2 (Turkis) | `#4ecdc4` |
| Text | `#1a1a1a` |
| Dark-Mode BG | `#0d1117` |

---

## Band 1 – Kapitelubersicht

| Kap. | Titel | Themen |
|------|-------|--------|
| 0 | Vorwort | Wer ist Belkis Aslani, warum diese Reihe |
| 1 | Was ist KI eigentlich? | Geschichte, Typen, Alltags-KI |
| 2 | LLMs verstehen | Funktionsweise, Training, Token, Modelle |
| 3 | Dein erster Prompt | Account erstellen, 10 Beispiele |
| 4 | Anatomie eines guten Prompts | 5 Bausteine, Vorher/Nachher |
| 5 | Die haufigsten Fehler | Zu vage, zu viel, Halluzinationen |
| 6 | Kontext ist alles | 5 Kontext-Kategorien, Goldener Satz |
| 7 | Rollen und Personas | 7 Rollen, Personas, Multi-Perspektiven |
| 8 | Output-Formate steuern | Listen, Tabellen, JSON, Templates |
| 9 | Iteratives Prompting | Folge-Prompts, Prompt-Protokoll |
| 10 | Zusammenfassung und Ausblick | Checkliste, Vorschau Band 2 |
