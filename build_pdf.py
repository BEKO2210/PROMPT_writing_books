#!/usr/bin/env python3
"""
PDF-Buchgenerator für die Reihe "Prompt Engineering Meistern"
Erzeugt ein verkaufsfertiges PDF aus den Markdown-Kapiteln.

Verwendung:
    python3 build_pdf.py                    # Band 1 (Standard)
    python3 build_pdf.py --band 2           # Band 2
    python3 build_pdf.py --band 1 --draft   # Entwurfsmodus (mit Wasserzeichen)

Autor: Belkis Aslani | Build-System v1.0
"""

import argparse
import os
import re
import sys
from pathlib import Path

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from weasyprint import HTML

# ─────────────────────────────────────────────────
# Konfiguration
# ─────────────────────────────────────────────────

BAND_CONFIG = {
    1: {
        "ordner": "Band_01_Grundlagen",
        "titel": "Grundlagen",
        "untertitel": "Dein Einstieg in die Welt der KI-Kommunikation",
        "dateien": [
            "00_Vorwort.md",
            "01_Was_ist_KI_eigentlich.md",
            "02_LLMs_verstehen.md",
            "03_Dein_erster_Prompt.md",
            "04_Anatomie_eines_guten_Prompts.md",
            "05_Die_haeufigsten_Fehler.md",
            "06_Kontext_ist_alles.md",
            "07_Rollen_und_Personas.md",
            "08_Output_Formate_steuern.md",
            "09_Iteratives_Prompting.md",
            "10_Zusammenfassung_und_Ausblick.md",
        ],
    },
}

AUTOR = "Belkis Aslani"
REIHE = "Prompt Engineering Meistern"
JAHR = "2026"
AUFLAGE = "1. Auflage"

# ─────────────────────────────────────────────────
# CSS: Professionelles Buchdesign
# ─────────────────────────────────────────────────

def get_book_css():
    """CSS für ein verkaufsfertiges Buchformat (6×9 Zoll / 15,24×22,86 cm)."""
    return """
/* ============================================
   BUCHFORMAT: 6×9 Zoll (Standard für Gumroad/Amazon KDP)
   Ränder: Innen 2cm (Bindung), Außen 1.8cm, Oben 2cm, Unten 2.2cm
   ============================================ */

@page {
    size: 15.24cm 22.86cm;  /* 6×9 Zoll */
    margin-top: 2cm;
    margin-bottom: 2.2cm;
    margin-inside: 2cm;     /* Bundsteg (Innenseite) */
    margin-outside: 1.8cm;

    @bottom-center {
        content: counter(page);
        font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
        font-size: 9pt;
        color: #555;
    }
}

/* Erste Seite jedes Kapitels: keine Seitenzahl */
@page chapter-start {
    @bottom-center { content: none; }
}

/* Titelseiten: keine Seitenzahl, keine Ränder-Extras */
@page title-page {
    margin: 0;
    @bottom-center { content: none; }
}

@page copyright-page {
    @bottom-center { content: none; }
}

@page toc-page {
    @bottom-center { content: none; }
}

/* ============================================
   TYPOGRAFIE
   ============================================ */

body {
    font-family: 'Liberation Serif', 'DejaVu Serif', 'FreeSerif', serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #1a1a1a;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
    orphans: 3;
    widows: 3;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

/* ============================================
   TITELSEITE
   ============================================ */

.title-page {
    page: title-page;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    text-align: center;
    padding: 3cm 2cm;
    background: linear-gradient(180deg, #0a1628 0%, #1a2744 40%, #2d4a7a 100%);
    color: white;
}

.title-page .reihe {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 11pt;
    text-transform: uppercase;
    letter-spacing: 4pt;
    color: #8ab4f8;
    margin-bottom: 1.5cm;
    font-weight: 400;
}

.title-page .band-nummer {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 14pt;
    color: #8ab4f8;
    letter-spacing: 2pt;
    margin-bottom: 0.8cm;
    text-transform: uppercase;
}

.title-page .haupttitel {
    font-family: 'Liberation Serif', 'DejaVu Serif', serif;
    font-size: 32pt;
    font-weight: bold;
    line-height: 1.2;
    margin-bottom: 0.6cm;
    color: #ffffff;
}

.title-page .untertitel {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 13pt;
    font-weight: 300;
    color: #c8ddf8;
    margin-bottom: 2.5cm;
    line-height: 1.4;
}

.title-page .autor {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 16pt;
    letter-spacing: 2pt;
    color: #ffffff;
    margin-bottom: 0.3cm;
}

.title-page .trennlinie {
    width: 4cm;
    height: 2px;
    background: #8ab4f8;
    margin: 0.8cm auto;
}

.title-page .jahr {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 10pt;
    color: #8ab4f8;
    letter-spacing: 1pt;
}

/* ============================================
   RÜCKSEITE TITELSEITE (Copyright)
   ============================================ */

.copyright-page {
    page: copyright-page;
    page-break-before: always;
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 8.5pt;
    color: #555;
    line-height: 1.6;
    padding-top: 60%;
}

.copyright-page p {
    margin-bottom: 0.4cm;
    text-align: left;
}

/* ============================================
   INHALTSVERZEICHNIS
   ============================================ */

.toc-page {
    page: toc-page;
    page-break-before: always;
}

.toc-page h2 {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 20pt;
    color: #1a2744;
    border-bottom: 2px solid #2d4a7a;
    padding-bottom: 0.3cm;
    margin-bottom: 1cm;
    text-align: left;
}

.toc-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.toc-list li {
    padding: 0.3cm 0;
    border-bottom: 1px dotted #ccc;
    font-size: 11pt;
    line-height: 1.4;
}

.toc-list li.vorwort {
    font-style: italic;
    color: #555;
}

.toc-list .toc-nummer {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-weight: bold;
    color: #2d4a7a;
    display: inline-block;
    width: 1.2cm;
}

/* ============================================
   KAPITEL-ÜBERSCHRIFTEN
   ============================================ */

h1 {
    page: chapter-start;
    page-break-before: always;
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 24pt;
    font-weight: bold;
    color: #1a2744;
    margin-top: 3cm;
    margin-bottom: 1cm;
    line-height: 1.2;
    border-bottom: 3px solid #2d4a7a;
    padding-bottom: 0.5cm;
    text-align: left;
}

/* Erstes h1 (Vorwort) soll keinen Seitenumbruch erzwingen */
.chapter-content:first-of-type h1 {
    page-break-before: always;
}

h2 {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 16pt;
    font-weight: bold;
    color: #2d4a7a;
    margin-top: 1.2cm;
    margin-bottom: 0.5cm;
    line-height: 1.3;
}

h3 {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 13pt;
    font-weight: bold;
    color: #3d5a8a;
    margin-top: 0.8cm;
    margin-bottom: 0.4cm;
}

h4 {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-size: 11pt;
    font-weight: bold;
    color: #4a6a9a;
    margin-top: 0.6cm;
    margin-bottom: 0.3cm;
}

/* ============================================
   ABSÄTZE UND TEXT
   ============================================ */

p {
    margin-bottom: 0.4cm;
    text-indent: 0;
}

/* Erster Absatz nach Überschrift: kein Einzug */
h1 + p, h2 + p, h3 + p, h4 + p {
    text-indent: 0;
}

strong {
    font-weight: bold;
    color: #1a1a1a;
}

em {
    font-style: italic;
}

/* ============================================
   LISTEN
   ============================================ */

ul, ol {
    margin: 0.4cm 0;
    padding-left: 1.2cm;
}

li {
    margin-bottom: 0.2cm;
    line-height: 1.5;
}

li > ul, li > ol {
    margin-top: 0.15cm;
}

/* ============================================
   CODE-BLÖCKE
   ============================================ */

pre {
    background: #f5f7fa;
    border: 1px solid #d0d7e2;
    border-left: 4px solid #2d4a7a;
    border-radius: 4px;
    padding: 0.5cm 0.6cm;
    margin: 0.5cm 0;
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
    font-size: 9pt;
    line-height: 1.45;
    overflow-wrap: break-word;
    word-wrap: break-word;
    white-space: pre-wrap;
    page-break-inside: avoid;
}

code {
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
    font-size: 9.5pt;
    background: #f0f3f7;
    padding: 1px 4px;
    border-radius: 3px;
    color: #2d4a7a;
}

pre code {
    background: none;
    padding: 0;
    border-radius: 0;
    color: #1a1a1a;
    font-size: 9pt;
}

/* ============================================
   TABELLEN
   ============================================ */

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.6cm 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

thead {
    background: #1a2744;
    color: white;
}

th {
    font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
    font-weight: bold;
    padding: 0.3cm 0.4cm;
    text-align: left;
    font-size: 9.5pt;
}

td {
    padding: 0.25cm 0.4cm;
    border-bottom: 1px solid #e0e4ea;
    vertical-align: top;
}

tr:nth-child(even) {
    background: #f8f9fb;
}

/* ============================================
   HORIZONTALE LINIE (Übungstrenner)
   ============================================ */

hr {
    border: none;
    border-top: 2px solid #2d4a7a;
    margin: 1cm 2cm;
}

/* ============================================
   BLOCKQUOTES (für Tipps/Hinweise)
   ============================================ */

blockquote {
    border-left: 4px solid #8ab4f8;
    background: #f0f5ff;
    margin: 0.5cm 0;
    padding: 0.4cm 0.6cm;
    font-style: italic;
    color: #333;
    page-break-inside: avoid;
}

blockquote p {
    margin-bottom: 0.2cm;
}

/* ============================================
   ÜBUNGSBOX
   ============================================ */

.uebung-box {
    background: #f0f8f0;
    border: 2px solid #4a8a4a;
    border-radius: 6px;
    padding: 0.6cm;
    margin: 0.8cm 0;
    page-break-inside: avoid;
}

.uebung-box h2, .uebung-box h3 {
    color: #2d6a2d;
}

/* ============================================
   LINKS (für Print: nur Text, kein Underline)
   ============================================ */

a {
    color: #2d4a7a;
    text-decoration: none;
}

/* ============================================
   SEITENUMBRÜCHE
   ============================================ */

.page-break {
    page-break-before: always;
}

.avoid-break {
    page-break-inside: avoid;
}

/* ============================================
   WASSERZEICHEN (Entwurfsmodus)
   ============================================ */

.draft-watermark {
    position: fixed;
    top: 45%;
    left: 15%;
    font-size: 80pt;
    color: rgba(200, 0, 0, 0.08);
    transform: rotate(-45deg);
    font-family: 'Liberation Sans', sans-serif;
    font-weight: bold;
    z-index: -1;
    pointer-events: none;
}
"""


# ─────────────────────────────────────────────────
# Markdown → HTML Konvertierung
# ─────────────────────────────────────────────────

def md_to_html(md_text):
    """Konvertiert Markdown zu HTML mit allen nötigen Extensions."""
    extensions = [
        TableExtension(),
        CodeHiliteExtension(
            css_class="highlight",
            guess_lang=False,
            use_pygments=True,
        ),
        TocExtension(permalink=False),
        "markdown.extensions.fenced_code",
        "markdown.extensions.nl2br",
        "markdown.extensions.smarty",
    ]
    return markdown.markdown(md_text, extensions=extensions)


def extract_toc_entries(dateien, band_ordner):
    """Extrahiert Kapitelüberschriften für das Inhaltsverzeichnis."""
    entries = []
    for datei in dateien:
        pfad = os.path.join(band_ordner, datei)
        if not os.path.exists(pfad):
            continue
        with open(pfad, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    titel = line[2:].strip()
                    # Kapitelnummer extrahieren
                    match = re.match(r"Kapitel\s+(\d+):\s*(.*)", titel)
                    if match:
                        entries.append(
                            {"nummer": match.group(1), "titel": match.group(2)}
                        )
                    else:
                        entries.append({"nummer": None, "titel": titel})
                    break
    return entries


# ─────────────────────────────────────────────────
# HTML-Dokument zusammenbauen
# ─────────────────────────────────────────────────

def build_title_page(band_nr, config):
    """Erzeugt die Titelseite."""
    return f"""
    <div class="title-page">
        <div class="reihe">{REIHE}</div>
        <div class="band-nummer">Band {band_nr}</div>
        <div class="haupttitel">{config['titel']}</div>
        <div class="untertitel">{config['untertitel']}</div>
        <div class="trennlinie"></div>
        <div class="autor">{AUTOR}</div>
        <div class="trennlinie"></div>
        <div class="jahr">{JAHR}</div>
    </div>
    """


def build_copyright_page(band_nr, config):
    """Erzeugt die Copyright/Impressum-Seite."""
    return f"""
    <div class="copyright-page">
        <p><strong>{REIHE}</strong><br>
        Band {band_nr}: {config['titel']} – {config['untertitel']}</p>

        <p>&copy; {JAHR} {AUTOR}. Alle Rechte vorbehalten.</p>

        <p>{AUFLAGE}, März {JAHR}</p>

        <p>Dieses Werk ist urheberrechtlich geschützt. Jede Verwertung außerhalb
        der engen Grenzen des Urheberrechtsgesetzes ist ohne Zustimmung des Autors
        unzulässig und strafbar. Das gilt insbesondere für Vervielfältigungen,
        Übersetzungen, Mikroverfilmungen und die Einspeicherung und Verarbeitung
        in elektronischen Systemen.</p>

        <p>Die in diesem Buch genannten Produkt- und Firmennamen sind Marken
        der jeweiligen Eigentümer. Die Nennung erfolgt ohne Gewähr der freien
        Verwendbarkeit.</p>

        <p>Satz und Layout: Eigensatz des Autors<br>
        Umschlaggestaltung: Belkis Aslani</p>

        <p>Kontakt: prompt-engineering-meistern@belkisaslani.com</p>
    </div>
    """


def build_toc_page(entries):
    """Erzeugt das Inhaltsverzeichnis."""
    items = []
    for entry in entries:
        if entry["nummer"]:
            items.append(
                f'<li><span class="toc-nummer">{entry["nummer"]}</span>'
                f'{entry["titel"]}</li>'
            )
        else:
            items.append(f'<li class="vorwort">{entry["titel"]}</li>')

    return f"""
    <div class="toc-page">
        <h2>Inhaltsverzeichnis</h2>
        <ul class="toc-list">
            {"".join(items)}
        </ul>
    </div>
    """


def build_chapter_html(md_text):
    """Konvertiert ein Markdown-Kapitel zu HTML mit Wrapper."""
    html_content = md_to_html(md_text)
    return f'<div class="chapter-content">{html_content}</div>'


def build_full_html(band_nr, config, band_ordner, draft=False):
    """Baut das komplette HTML-Dokument zusammen."""
    # Titelseite
    title_page = build_title_page(band_nr, config)

    # Copyright-Seite
    copyright_page = build_copyright_page(band_nr, config)

    # Kapitelüberschriften für Inhaltsverzeichnis sammeln
    toc_entries = extract_toc_entries(config["dateien"], band_ordner)
    toc_page = build_toc_page(toc_entries)

    # Kapitel-Inhalte laden und konvertieren
    chapters_html = []
    for datei in config["dateien"]:
        pfad = os.path.join(band_ordner, datei)
        if not os.path.exists(pfad):
            print(f"  WARNUNG: {pfad} nicht gefunden, überspringe.")
            continue
        with open(pfad, "r", encoding="utf-8") as f:
            md_text = f.read()
        chapters_html.append(build_chapter_html(md_text))
        print(f"  ✓ {datei}")

    # Wasserzeichen für Entwurf
    watermark = '<div class="draft-watermark">ENTWURF</div>' if draft else ""

    # Alles zusammensetzen
    css = get_book_css()
    full_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="utf-8">
    <title>{REIHE} – Band {band_nr}: {config['titel']}</title>
    <style>{css}</style>
</head>
<body>
    {watermark}
    {title_page}
    {copyright_page}
    {toc_page}
    {"".join(chapters_html)}
</body>
</html>"""

    return full_html


# ─────────────────────────────────────────────────
# PDF erzeugen
# ─────────────────────────────────────────────────

def generate_pdf(band_nr, draft=False):
    """Hauptfunktion: Erzeugt das PDF für einen Band."""
    if band_nr not in BAND_CONFIG:
        print(f"FEHLER: Band {band_nr} ist noch nicht konfiguriert.")
        print(f"Verfügbare Bände: {list(BAND_CONFIG.keys())}")
        sys.exit(1)

    config = BAND_CONFIG[band_nr]
    script_dir = Path(__file__).parent.resolve()
    band_ordner = script_dir / config["ordner"]

    if not band_ordner.exists():
        print(f"FEHLER: Ordner {band_ordner} nicht gefunden.")
        sys.exit(1)

    # Output-Verzeichnis
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)

    suffix = "_ENTWURF" if draft else ""
    output_pdf = output_dir / f"Band_{band_nr:02d}_{config['titel']}{suffix}.pdf"
    output_html = output_dir / f"Band_{band_nr:02d}_{config['titel']}{suffix}.html"

    print(f"\n{'='*60}")
    print(f"  PDF-Buchgenerator | {REIHE}")
    print(f"  Band {band_nr}: {config['titel']}")
    print(f"  Modus: {'ENTWURF' if draft else 'VERKAUFSFERTIG'}")
    print(f"{'='*60}\n")

    # HTML zusammenbauen
    print("Kapitel werden verarbeitet:")
    full_html = build_full_html(band_nr, config, str(band_ordner), draft)

    # HTML speichern (für Debugging)
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"\n  HTML gespeichert: {output_html}")

    # PDF erzeugen
    print(f"  PDF wird generiert...")
    HTML(string=full_html, base_url=str(script_dir)).write_pdf(str(output_pdf))

    # Dateigröße
    size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"\n  ✓ PDF erfolgreich erstellt: {output_pdf}")
    print(f"  ✓ Dateigröße: {size_mb:.2f} MB")

    # Seitenanzahl schätzen (grob)
    total_words = 0
    for datei in config["dateien"]:
        pfad = os.path.join(str(band_ordner), datei)
        if os.path.exists(pfad):
            with open(pfad, "r", encoding="utf-8") as f:
                total_words += len(f.read().split())
    print(f"  ✓ Geschätzte Wortanzahl: ~{total_words:,}")
    print(f"  ✓ Format: 6×9 Zoll (15,24 × 22,86 cm)")
    print(f"  ✓ Geeignet für: Gumroad, Amazon KDP, Lulu, Epubli")

    print(f"\n{'='*60}")
    print(f"  Fertig! Die PDF liegt unter:")
    print(f"  {output_pdf}")
    print(f"{'='*60}\n")

    return str(output_pdf)


# ─────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="PDF-Buchgenerator für 'Prompt Engineering Meistern'"
    )
    parser.add_argument(
        "--band", type=int, default=1, help="Bandnummer (Standard: 1)"
    )
    parser.add_argument(
        "--draft",
        action="store_true",
        help="Entwurfsmodus mit Wasserzeichen",
    )
    args = parser.parse_args()

    generate_pdf(args.band, args.draft)
