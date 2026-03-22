#!/usr/bin/env python3
"""
Web-Generator für die Reihe "Prompt Engineering Meistern"
Erzeugt mobile-first Lese-Webseiten aus den Markdown-Kapiteln.

Verwendung:
    python3 build_web.py          # Generiert band-01/ und band-02/index.html

Autor: Belkis Aslani | Build-System v4.0 (Production)
"""

import re
from pathlib import Path

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension

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
    2: {
        "ordner": "Band_02_Prompt_Frameworks",
        "titel": "Prompt-Frameworks",
        "untertitel": "Strukturiert zum perfekten Prompt",
        "dateien": [
            "00_Vorwort.md",
            "01_Warum_Frameworks.md",
            "02_Zero_Shot_Prompting.md",
            "03_One_Shot_Prompting.md",
            "04_Few_Shot_Prompting.md",
            "05_Das_CRAFT_Framework.md",
            "06_Das_RTF_Framework.md",
            "07_Das_RISEN_Framework.md",
            "08_Frameworks_vergleichen.md",
            "09_Template_Bibliothek.md",
            "10_Zusammenfassung_und_Ausblick.md",
        ],
    },
}

BASE_URL = "https://beko2210.github.io/PROMPT_writing_books"


def md_to_html(md_text):
    extensions = [
        TableExtension(),
        CodeHiliteExtension(css_class="highlight", guess_lang=False, use_pygments=True),
        TocExtension(permalink=False),
        "markdown.extensions.fenced_code",
        "markdown.extensions.smarty",
    ]
    return markdown.markdown(md_text, extensions=extensions)


def extract_chapter_title(md_text):
    for line in md_text.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return "Kapitel"


def build_band_page(band_nr, config):
    script_dir = Path(__file__).parent.resolve()
    band_ordner = script_dir / config["ordner"]

    chapters = []
    toc_items = []

    for i, datei in enumerate(config["dateien"]):
        pfad = band_ordner / datei
        if not pfad.exists():
            continue
        md_text = pfad.read_text(encoding="utf-8")
        title = extract_chapter_title(md_text)
        slug = f"ch-{i}"
        html = md_to_html(md_text)
        chapters.append({"slug": slug, "title": title, "html": html})

        short = title
        m = re.match(r"Kapitel\s+\d+:\s*(.*)", title)
        if m:
            short = m.group(1)
        toc_items.append({"slug": slug, "title": short, "full": title})

    toc_html = "\n".join(
        f'<a href="#{t["slug"]}" class="toc-link" data-target="{t["slug"]}">{t["title"]}</a>'
        for t in toc_items
    )

    chapters_html = "\n".join(
        f'<section class="chapter" id="{ch["slug"]}">\n{ch["html"]}\n</section>'
        for ch in chapters
    )

    pdf_name = f"Band_{band_nr:02d}_{config['titel']}"
    page_url = f"{BASE_URL}/band-{band_nr:02d}/"

    return f"""<!DOCTYPE html>
<html lang="de" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Band {band_nr}: {config['titel']} &ndash; Prompt Engineering Meistern</title>
<meta name="description" content="{config['untertitel']} &ndash; Band {band_nr} der Buchreihe Prompt Engineering Meistern von Belkis Aslani. Kostenlos online lesen.">
<meta name="author" content="Belkis Aslani">
<meta name="theme-color" content="#0a1628" media="(prefers-color-scheme:dark)">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme:light)">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{page_url}">
<link rel="manifest" href="../manifest.json">
<link rel="icon" href="../icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../icon-192.png">
<meta property="og:type" content="book">
<meta property="og:title" content="Band {band_nr}: {config['titel']} &ndash; Prompt Engineering Meistern">
<meta property="og:description" content="{config['untertitel']}. Kostenlos online lesen.">
<meta property="og:url" content="{page_url}">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="Prompt Engineering Meistern">
<meta property="og:image" content="{BASE_URL}/icon-512.png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Band {band_nr}: {config['titel']}">
<meta name="twitter:description" content="{config['untertitel']}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Book","name":"Prompt Engineering Meistern – Band {band_nr}: {config['titel']}","author":{{"@type":"Person","name":"Belkis Aslani"}},"bookEdition":"1. Auflage","inLanguage":"de","url":"{page_url}","isPartOf":{{"@type":"BookSeries","name":"Prompt Engineering Meistern"}}}}
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
--bg:#fff;--bg2:#f8f9fb;--card:#fff;
--text:#1a1a1a;--text2:#555;--text3:#888;
--accent:#2d4a7a;--accent-light:#8ab4f8;
--border:#e5e7eb;--code-bg:#f5f7fa;
--sidebar-bg:#fafbfc;--max-w:680px;
--font:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
--font-reading:'Georgia','Liberation Serif',serif;
--font-mono:'SF Mono','Liberation Mono','Cascadia Code',monospace;
}}
[data-theme="dark"]{{
--bg:#0d1117;--bg2:#161b22;--card:#1c2333;
--text:#e4e8ef;--text2:#8899aa;--text3:#556677;
--accent:#8ab4f8;--accent-light:#8ab4f8;
--border:#2a3444;--code-bg:#161b22;--sidebar-bg:#0d1117;
}}
html{{scroll-behavior:smooth;scroll-padding-top:70px}}
body{{font-family:var(--font);background:var(--bg);color:var(--text);transition:background .3s,color .3s}}

/* Progress */
.progress{{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--accent),var(--accent-light));z-index:1000;width:0;transition:width .15s}}

/* Topbar */
.topbar{{
position:fixed;top:0;left:0;right:0;height:56px;
border-bottom:1px solid var(--border);display:flex;align-items:center;
padding:0 16px;z-index:100;transition:background .3s,border-color .3s;
backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
background:color-mix(in srgb,var(--bg) 85%,transparent);
}}
.topbar-left{{display:flex;align-items:center;gap:12px;flex:1;min-width:0}}
.menu-btn{{background:none;border:none;cursor:pointer;padding:8px;color:var(--text);display:none}}
@media(max-width:900px){{.menu-btn{{display:block}}}}
.topbar-title{{font-size:14px;font-weight:600;color:var(--text2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.topbar-title a{{color:inherit;text-decoration:none}}
.topbar-title a:hover{{color:var(--accent)}}
.topbar-actions{{display:flex;align-items:center;gap:8px}}
.btn-sm{{
font-size:12px;font-weight:600;padding:7px 14px;border-radius:8px;
border:1px solid var(--border);background:var(--bg2);color:var(--text);
cursor:pointer;text-decoration:none;transition:all .2s;
display:inline-flex;align-items:center;gap:6px;
}}
.btn-sm:hover{{border-color:var(--accent);color:var(--accent)}}
.btn-sm svg{{width:14px;height:14px;fill:currentColor}}

/* Sun/Moon Toggle */
.switch{{position:relative;display:inline-block;width:54px;height:30px}}
.switch input{{opacity:0;width:0;height:0;position:absolute}}
.tm-slider{{position:absolute;cursor:pointer;inset:0;background:#2196f3;transition:.4s;overflow:hidden;border-radius:30px}}
.sun-moon{{position:absolute;height:22px;width:22px;left:4px;bottom:4px;background:yellow;transition:.4s;border-radius:50%}}
.switch input:checked+.tm-slider{{background:#111827}}
.switch input:checked+.tm-slider .sun-moon{{transform:translateX(24px);background:#e2e8f0;animation:smRotate .6s ease-in-out both}}
@keyframes smRotate{{0%{{transform:translateX(24px) rotate(0)}}100%{{transform:translateX(24px) rotate(360deg)}}}}
.moon-dot{{opacity:0;transition:.4s;fill:#94a3b8;position:absolute;z-index:4}}
.switch input:checked+.tm-slider .moon-dot{{opacity:1}}
.md1{{left:9px;top:3px;width:5px;height:5px}}.md2{{left:2px;top:9px;width:8px;height:8px}}.md3{{left:14px;top:16px;width:3px;height:3px}}
.light-ray{{position:absolute;z-index:-1;fill:white;opacity:.1}}
.lr1{{left:-7px;top:-7px;width:36px;height:36px}}.lr2{{left:-50%;top:-50%;width:44px;height:44px}}.lr3{{left:-14px;top:-14px;width:50px;height:50px}}
.cloud-l,.cloud-d{{position:absolute;animation:cMv 6s infinite}}
.cloud-l{{fill:#eee}}.cloud-d{{fill:#ccc;animation-delay:1s}}
.c1{{left:26px;top:13px;width:34px}}.c2{{left:38px;top:8px;width:17px}}.c3{{left:15px;top:20px;width:26px}}
.c4{{left:30px;top:15px;width:34px}}.c5{{left:42px;top:11px;width:17px}}.c6{{left:18px;top:22px;width:26px}}
@keyframes cMv{{0%,100%{{transform:translateX(0)}}40%{{transform:translateX(3px)}}80%{{transform:translateX(-3px)}}}}
.stars{{transform:translateY(-28px);opacity:0;transition:.4s}}
.star{{fill:white;position:absolute;transition:.4s;animation:stTw 2s infinite}}
.switch input:checked+.tm-slider .stars{{transform:translateY(0);opacity:1}}
.s1{{width:16px;top:2px;left:3px;animation-delay:.3s}}.s2{{width:5px;top:14px;left:3px}}
.s3{{width:10px;top:17px;left:9px;animation-delay:.6s}}.s4{{width:14px;top:0;left:15px;animation-delay:1.3s}}
@keyframes stTw{{0%,100%{{transform:scale(1)}}40%{{transform:scale(1.2)}}80%{{transform:scale(.8)}}}}

/* Sidebar */
.sidebar{{
position:fixed;top:56px;left:0;bottom:0;width:280px;
background:var(--sidebar-bg);border-right:1px solid var(--border);
overflow-y:auto;padding:20px 0;z-index:90;
transition:transform .3s,background .3s,border-color .3s;
}}
@media(max-width:900px){{
.sidebar{{transform:translateX(-100%);width:300px;z-index:200;box-shadow:4px 0 30px rgba(0,0,0,.2)}}
.sidebar.open{{transform:translateX(0)}}
.overlay{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:150}}
.overlay.show{{display:block}}
}}
.sidebar-header{{padding:0 20px 16px;font-size:12px;text-transform:uppercase;letter-spacing:2px;color:var(--text3);font-weight:600}}
.toc-link{{
display:block;padding:8px 20px 8px 24px;font-size:14px;color:var(--text2);
text-decoration:none;border-left:2px solid transparent;transition:all .2s;line-height:1.4;
}}
.toc-link:hover{{color:var(--accent);background:var(--bg2)}}
.toc-link.active{{color:var(--accent);border-left-color:var(--accent);background:var(--bg2);font-weight:600}}

/* Main */
.main{{margin-left:280px;padding:80px 24px 100px;transition:margin .3s}}
@media(max-width:900px){{.main{{margin-left:0}}}}
.content{{max-width:var(--max-w);margin:0 auto}}

/* Typography */
.chapter{{padding-bottom:60px;margin-bottom:40px;border-bottom:1px solid var(--border)}}
.chapter:last-child{{border-bottom:none}}
.chapter h1{{font-family:var(--font);font-size:clamp(1.6rem,4vw,2.2rem);font-weight:800;color:var(--text);margin:0 0 24px;line-height:1.15;letter-spacing:-.02em}}
.chapter h2{{font-family:var(--font);font-size:clamp(1.2rem,3vw,1.5rem);font-weight:700;color:var(--text);margin:40px 0 16px;line-height:1.2}}
.chapter h3{{font-family:var(--font);font-size:1.1rem;font-weight:600;color:var(--text);margin:32px 0 12px}}
.chapter h4{{font-size:1rem;font-weight:600;color:var(--text2);margin:24px 0 8px}}
.chapter p{{font-family:var(--font-reading);font-size:17px;line-height:1.75;margin-bottom:18px;color:var(--text)}}
.chapter strong{{font-weight:700}}.chapter em{{font-style:italic}}
.chapter ul,.chapter ol{{font-family:var(--font-reading);font-size:17px;line-height:1.7;margin:12px 0 18px;padding-left:28px}}
.chapter li{{margin-bottom:8px}}.chapter li>ul,.chapter li>ol{{margin-top:6px}}

/* Code */
.chapter pre{{background:var(--code-bg);border:1px solid var(--border);border-radius:10px;padding:18px 20px;margin:20px 0;overflow-x:auto;font-family:var(--font-mono);font-size:14px;line-height:1.55}}
.chapter code{{font-family:var(--font-mono);font-size:15px;background:var(--code-bg);padding:2px 6px;border-radius:5px;color:var(--accent)}}
.chapter pre code{{background:none;padding:0;color:var(--text);font-size:14px}}

/* Tables */
.chapter table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:15px;border-radius:8px;overflow:hidden}}
.chapter thead{{background:var(--accent);color:#fff}}
.chapter th{{padding:10px 14px;text-align:left;font-size:13px;font-weight:600}}
.chapter td{{padding:10px 14px;border-bottom:1px solid var(--border);font-family:var(--font-reading)}}
.chapter tr:nth-child(even){{background:var(--bg2)}}

/* Blockquote */
.chapter blockquote{{border-left:3px solid var(--accent-light);background:var(--bg2);padding:16px 20px;margin:20px 0;border-radius:0 8px 8px 0;font-style:italic}}
.chapter blockquote p{{margin-bottom:8px;font-size:16px}}

/* HR */
.chapter hr{{border:none;border-top:2px solid var(--border);margin:40px 60px}}

/* Scroll to top */
.scroll-top{{
position:fixed;bottom:24px;right:24px;width:44px;height:44px;border-radius:12px;
background:var(--accent);color:#fff;border:none;cursor:pointer;
display:none;align-items:center;justify-content:center;
box-shadow:0 4px 20px rgba(0,0,0,.2);z-index:50;transition:all .3s;
}}
.scroll-top:hover{{transform:translateY(-2px)}}
.scroll-top.show{{display:flex}}
.scroll-top svg{{width:20px;height:20px;fill:currentColor}}

/* Fullscreen / Focus Mode */
.focus-btn{{
background:none;border:1px solid var(--border);width:34px;height:34px;
border-radius:8px;cursor:pointer;color:var(--text);
display:inline-flex;align-items:center;justify-content:center;transition:all .2s;
}}
.focus-btn:hover{{border-color:var(--accent);color:var(--accent)}}
.focus-btn svg{{width:16px;height:16px;fill:currentColor}}
body.focus-mode .topbar{{transform:translateY(-100%)}}
body.focus-mode .sidebar{{transform:translateX(-100%)}}
body.focus-mode .main{{margin-left:0;padding-top:40px}}
body.focus-mode .scroll-top,.body.focus-mode .resume-banner{{display:none!important}}
body.focus-mode .progress{{opacity:0}}
body.focus-mode .focus-exit{{display:flex}}
.focus-exit{{
display:none;position:fixed;top:16px;right:16px;z-index:200;
background:var(--bg);border:1px solid var(--border);border-radius:10px;
padding:8px 16px;font-size:13px;font-weight:600;color:var(--text2);
cursor:pointer;align-items:center;gap:6px;
box-shadow:0 4px 20px rgba(0,0,0,.15);transition:all .2s;
}}
.focus-exit:hover{{color:var(--accent);border-color:var(--accent)}}
.focus-exit kbd{{
background:var(--bg2);border:1px solid var(--border);border-radius:4px;
padding:1px 6px;font-size:11px;font-family:var(--font-mono);
}}

/* Resume banner */
.resume-banner{{
display:none;position:fixed;bottom:80px;left:50%;transform:translateX(-50%);
background:var(--accent);color:#fff;padding:10px 20px;border-radius:12px;
font-size:14px;font-weight:600;cursor:pointer;z-index:60;
box-shadow:0 4px 24px rgba(0,0,0,.3);transition:all .3s;white-space:nowrap;
}}
.resume-banner:hover{{transform:translateX(-50%) translateY(-2px)}}
.resume-banner.show{{display:block}}

/* Update toast */
.update-toast{{
display:none;position:fixed;bottom:24px;left:50%;transform:translateX(-50%);
background:var(--card);border:1px solid var(--border);border-radius:16px;
padding:20px 24px;z-index:999;max-width:420px;width:calc(100% - 32px);
box-shadow:0 12px 40px rgba(0,0,0,.4);
}}
.update-toast.show{{display:block;animation:toastIn .4s ease}}
@keyframes toastIn{{from{{opacity:0;transform:translateX(-50%) translateY(20px)}}to{{opacity:1;transform:translateX(-50%) translateY(0)}}}}
.update-toast h3{{font-size:15px;color:var(--text);margin-bottom:8px}}
.update-toast ul{{padding-left:18px;margin:8px 0 14px;font-size:13px;color:var(--text2);line-height:1.6}}
.update-toast .ver{{font-size:12px;color:var(--accent);margin-bottom:6px;letter-spacing:1px}}
.update-toast button{{background:var(--accent);color:#fff;border:none;border-radius:8px;padding:8px 20px;font-size:13px;font-weight:600;cursor:pointer;width:100%}}
.update-toast button:hover{{opacity:.9}}

/* Responsive */
@media(max-width:600px){{
.chapter table{{font-size:13px}}.chapter th,.chapter td{{padding:8px 10px}}
.chapter p{{font-size:16px}}.chapter pre{{font-size:13px;padding:14px 16px}}
.topbar-actions .btn-sm span{{display:none}}
}}
</style>
</head>
<body>
<div class="progress" id="progress" role="progressbar" aria-label="Lesefortschritt"></div>
<div class="overlay" id="overlay"></div>

<header class="topbar">
<div class="topbar-left">
<button class="menu-btn" id="menuBtn" type="button" aria-label="Inhaltsverzeichnis &ouml;ffnen" aria-expanded="false" aria-controls="sidebar">
<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>
</button>
<div class="topbar-title"><a href="../">Prompt Engineering Meistern</a> &middot; Band {band_nr}</div>
</div>
<div class="topbar-actions">
<a href="../output/{pdf_name}.pdf" class="btn-sm" download aria-label="PDF herunterladen">
<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
<span>PDF</span>
</a>
<button class="focus-btn" id="focusBtn" type="button" aria-label="Vollbild-Lesemodus">
<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/></svg>
</button>
<label class="switch" aria-label="Farbmodus umschalten">
<input id="themeInput" type="checkbox" role="switch" aria-label="Dark Mode">
<div class="tm-slider">
<div class="sun-moon">
<svg class="moon-dot md1" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="moon-dot md2" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="moon-dot md3" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="light-ray lr1" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="light-ray lr2" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="light-ray lr3" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-d c1" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-d c2" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-d c3" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-l c4" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-l c5" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
<svg class="cloud-l c6" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="50"/></svg>
</div>
<div class="stars">
<svg class="star s1" viewBox="0 0 20 20" aria-hidden="true"><path d="M0 10C10 10 10 10 0 10 10 10 10 10 10 20 10 10 10 10 20 10 10 10 10 10 10 0 10 10 10 10 0 10Z"/></svg>
<svg class="star s2" viewBox="0 0 20 20" aria-hidden="true"><path d="M0 10C10 10 10 10 0 10 10 10 10 10 10 20 10 10 10 10 20 10 10 10 10 10 10 0 10 10 10 10 0 10Z"/></svg>
<svg class="star s3" viewBox="0 0 20 20" aria-hidden="true"><path d="M0 10C10 10 10 10 0 10 10 10 10 10 10 20 10 10 10 10 20 10 10 10 10 10 10 0 10 10 10 10 0 10Z"/></svg>
<svg class="star s4" viewBox="0 0 20 20" aria-hidden="true"><path d="M0 10C10 10 10 10 0 10 10 10 10 10 10 20 10 10 10 10 20 10 10 10 10 10 10 0 10 10 10 10 0 10Z"/></svg>
</div>
</div>
</label>
</div>
</header>

<nav class="sidebar" id="sidebar" aria-label="Inhaltsverzeichnis">
<div class="sidebar-header">Kapitel</div>
{toc_html}
</nav>

<main class="main" id="main">
<article class="content">
{chapters_html}
</article>
</main>

<button class="scroll-top" id="scrollTop" type="button" aria-label="Nach oben scrollen">
<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l-8 8h5v8h6v-8h5z"/></svg>
</button>

<div class="resume-banner" id="resumeBanner" role="button" tabindex="0" aria-label="Weiterlesen">Weiterlesen &rarr;</div>

<div class="update-toast" id="updateToast" role="alert" aria-live="polite">
<div class="ver" id="toastVer"></div>
<h3>Neues Update!</h3>
<ul id="toastChanges"></ul>
<button id="toastClose" type="button">Verstanden</button>
</div>

<button class="focus-exit" id="focusExit" type="button" aria-label="Lesemodus beenden">Lesemodus beenden <kbd>Esc</kbd></button>

<script>
(function(){{
var B={band_nr},K='pe-band'+B;
var html=document.documentElement;

// Theme
var stored=localStorage.getItem('theme');
var dark=stored==='dark'||(!stored&&matchMedia('(prefers-color-scheme:dark)').matches);
var themeInput=document.getElementById('themeInput');
if(dark){{html.dataset.theme='dark';themeInput.checked=true;}}
themeInput.addEventListener('change',function(){{
html.dataset.theme=this.checked?'dark':'light';
localStorage.setItem('theme',html.dataset.theme);
}});

// Mobile menu
var menuBtn=document.getElementById('menuBtn');
var sidebar=document.getElementById('sidebar');
var overlay=document.getElementById('overlay');
function closeSidebar(){{sidebar.classList.remove('open');overlay.classList.remove('show');menuBtn.setAttribute('aria-expanded','false')}}
menuBtn.addEventListener('click',function(){{
var open=sidebar.classList.toggle('open');
overlay.classList.toggle('show');
menuBtn.setAttribute('aria-expanded',open?'true':'false');
}});
overlay.addEventListener('click',closeSidebar);
document.querySelectorAll('.toc-link').forEach(function(l){{l.addEventListener('click',function(){{if(innerWidth<=900)closeSidebar()}})}});

// Progress bar + reading position save
var prog=document.getElementById('progress');
var saveTimer;
function onScroll(){{
var h=document.documentElement.scrollHeight-innerHeight;
var pct=h>0?scrollY/h:0;
prog.style.width=(pct*100)+'%';
// Scroll to top button
scrollBtn.classList.toggle('show',scrollY>600);
clearTimeout(saveTimer);
saveTimer=setTimeout(function(){{
localStorage.setItem(K+'-scroll',scrollY);
var chs=document.querySelectorAll('.chapter');
for(var i=chs.length-1;i>=0;i--){{
if(chs[i].getBoundingClientRect().top<150){{
localStorage.setItem(K+'-chapter',chs[i].id);
break;
}}
}}
}},300);
}}
window.addEventListener('scroll',onScroll,{{passive:true}});

// Resume reading position
var savedScroll=parseInt(localStorage.getItem(K+'-scroll'),10);
var savedChapter=localStorage.getItem(K+'-chapter');
if(savedScroll>300&&savedChapter){{
var banner=document.getElementById('resumeBanner');
var chEl=document.getElementById(savedChapter);
if(chEl){{
var chTitle=chEl.querySelector('h1');
banner.textContent=(chTitle?chTitle.textContent:'Weiterlesen')+' \u2192';
}}
banner.classList.add('show');
function doResume(){{scrollTo({{top:savedScroll,behavior:'smooth'}});banner.classList.remove('show')}}
banner.addEventListener('click',doResume);
banner.addEventListener('keydown',function(e){{if(e.key==='Enter')doResume()}});
setTimeout(function(){{banner.classList.remove('show')}},8000);
}}

// Scroll to top
var scrollBtn=document.getElementById('scrollTop');
scrollBtn.addEventListener('click',function(){{scrollTo({{top:0,behavior:'smooth'}})}});

// Active TOC tracking
var chapters=document.querySelectorAll('.chapter');
var links=document.querySelectorAll('.toc-link');
var observer=new IntersectionObserver(function(entries){{
entries.forEach(function(e){{
if(e.isIntersecting){{
links.forEach(function(l){{l.classList.remove('active')}});
var active=document.querySelector('.toc-link[data-target="'+e.target.id+'"]');
if(active)active.classList.add('active');
}}
}});
}},{{rootMargin:'-80px 0px -60% 0px'}});
chapters.forEach(function(ch){{observer.observe(ch)}});

// Focus / Fullscreen reading mode
var focusBtn=document.getElementById('focusBtn');
var focusExit=document.getElementById('focusExit');
function toggleFocus(on){{
var entering=typeof on==='boolean'?on:!document.body.classList.contains('focus-mode');
document.body.classList.toggle('focus-mode',entering);
if(entering)closeSidebar();
}}
focusBtn.addEventListener('click',function(){{toggleFocus(true)}});
focusExit.addEventListener('click',function(){{toggleFocus(false)}});
document.addEventListener('keydown',function(e){{
if(e.key==='Escape'&&document.body.classList.contains('focus-mode'))toggleFocus(false);
}});

// Service Worker + Version popup
if('serviceWorker' in navigator){{
navigator.serviceWorker.register('../sw.js').then(function(){{
setTimeout(function(){{
var lastVer=localStorage.getItem('pe-app-version');
fetch('../version.json?t='+Date.now()).then(function(r){{return r.json()}}).then(function(data){{
if(lastVer&&lastVer!==data.version){{
var toast=document.getElementById('updateToast');
document.getElementById('toastVer').textContent='Version '+data.version;
var ul=document.getElementById('toastChanges');ul.innerHTML='';
data.changes.forEach(function(c){{var li=document.createElement('li');li.textContent=c;ul.appendChild(li)}});
toast.classList.add('show');
document.getElementById('toastClose').addEventListener('click',function(){{toast.classList.remove('show');localStorage.setItem('pe-app-version',data.version)}});
}}else{{localStorage.setItem('pe-app-version',data.version)}}
}}).catch(function(){{}});
}},1000);
}});
}}
}})();
</script>
</body>
</html>"""


def main():
    script_dir = Path(__file__).parent.resolve()

    for band_nr, config in BAND_CONFIG.items():
        out_dir = script_dir / f"band-{band_nr:02d}"
        out_dir.mkdir(parents=True, exist_ok=True)

        html = build_band_page(band_nr, config)
        out_file = out_dir / "index.html"
        out_file.write_text(html, encoding="utf-8")
        print(f"  Band {band_nr}: {out_file}")

    print("\nWebseiten generiert!")


if __name__ == "__main__":
    main()
