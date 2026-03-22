#!/usr/bin/env python3
"""
Web-Generator für die Reihe "Prompt Engineering Meistern"
Erzeugt eine mobile-first Lese-Webseite aus den Markdown-Kapiteln.

Verwendung:
    python3 build_web.py          # Generiert band-01/ und band-02/index.html

Autor: Belkis Aslani | Build-System v3.0
"""

import os
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

    pdf_name = f"Band_{band_nr:02d}_{config['ordner'].split('_', 2)[-1]}"

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Band {band_nr}: {config['titel']} &ndash; Prompt Engineering Meistern</title>
<meta name="description" content="{config['untertitel']} &ndash; Band {band_nr} der Buchreihe Prompt Engineering Meistern von Belkis Aslani.">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}

:root{{
--bg:#fff;--bg2:#f8f9fb;--card:#fff;
--text:#1a1a1a;--text2:#555;--text3:#888;
--accent:#2d4a7a;--accent-light:#8ab4f8;
--border:#e5e7eb;--code-bg:#f5f7fa;
--sidebar-bg:#fafbfc;
--max-w:680px;
--font:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
--font-reading:'Georgia','Liberation Serif',serif;
--font-mono:'SF Mono','Liberation Mono','Cascadia Code',monospace;
--toggle-bg:rgba(0,0,0,.06);
--toggle-text:#555;
--toggle-active-bg:linear-gradient(135deg,#2d4a7a,#4a7ab5);
--toggle-active-shadow:0 0 14px rgba(45,74,122,.4),0 0 8px rgba(138,180,248,.3) inset;
--toggle-active-text:#fff;
}}

[data-theme="dark"]{{
--bg:#0d1117;--bg2:#161b22;--card:#1c2333;
--text:#e4e8ef;--text2:#8899aa;--text3:#556677;
--accent:#8ab4f8;--accent-light:#8ab4f8;
--border:#2a3444;--code-bg:#161b22;
--sidebar-bg:#0d1117;
--toggle-bg:rgba(255,255,255,.06);
--toggle-text:#8899aa;
--toggle-active-bg:linear-gradient(135deg,#8ab4f855,#8ab4f8);
--toggle-active-shadow:0 0 14px rgba(138,180,248,.4),0 0 8px rgba(200,230,255,.3) inset;
--toggle-active-text:#fff;
}}

html{{scroll-behavior:smooth;scroll-padding-top:70px}}
body{{
font-family:var(--font);
background:var(--bg);
color:var(--text);
transition:background .3s,color .3s;
}}

/* ===== PROGRESS BAR ===== */
.progress{{
position:fixed;top:0;left:0;height:3px;
background:linear-gradient(90deg,var(--accent),var(--accent-light));
z-index:1000;width:0;transition:width .1s;
}}

/* ===== TOP BAR ===== */
.topbar{{
position:fixed;top:0;left:0;right:0;
height:56px;
background:var(--bg);
border-bottom:1px solid var(--border);
display:flex;align-items:center;
padding:0 16px;
z-index:100;
transition:background .3s,border-color .3s;
backdrop-filter:blur(12px);
background:color-mix(in srgb,var(--bg) 85%,transparent);
}}
.topbar-left{{display:flex;align-items:center;gap:12px;flex:1;min-width:0}}
.menu-btn{{
background:none;border:none;cursor:pointer;
padding:8px;color:var(--text);display:none;
}}
@media(max-width:900px){{.menu-btn{{display:block}}}}
.topbar-title{{
font-size:14px;font-weight:600;color:var(--text2);
white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}}
.topbar-title a{{color:inherit;text-decoration:none}}
.topbar-title a:hover{{color:var(--accent)}}
.topbar-actions{{display:flex;align-items:center;gap:8px}}
.btn-sm{{
font-size:12px;font-weight:600;
padding:7px 14px;border-radius:8px;
border:1px solid var(--border);
background:var(--bg2);color:var(--text);
cursor:pointer;text-decoration:none;
transition:all .2s;
display:inline-flex;align-items:center;gap:6px;
}}
.btn-sm:hover{{border-color:var(--accent);color:var(--accent)}}
.btn-sm svg{{width:14px;height:14px;fill:currentColor}}

/* ===== GLASS RADIO TOGGLE ===== */
.glass-radio-group{{
display:flex;
position:relative;
background:var(--toggle-bg);
border-radius:.6rem;
backdrop-filter:blur(12px);
box-shadow:inset 1px 1px 3px rgba(255,255,255,.12),inset -1px -1px 4px rgba(0,0,0,.15);
overflow:hidden;
width:fit-content;
height:34px;
}}
.glass-radio-group input{{display:none}}
.glass-radio-group label{{
flex:1;display:flex;align-items:center;justify-content:center;
font-size:12px;padding:0 14px;cursor:pointer;font-weight:600;
letter-spacing:.3px;color:var(--toggle-text);
position:relative;z-index:2;transition:color .3s ease-in-out;
white-space:nowrap;
}}
.glass-radio-group label:hover{{color:var(--text)}}
.glass-radio-group input:checked+label{{color:var(--toggle-active-text)}}
.glass-glider{{
position:absolute;top:0;bottom:0;width:50%;
border-radius:.6rem;z-index:1;
transition:transform .4s cubic-bezier(.37,1.95,.66,.56),background .3s,box-shadow .3s;
}}
#theme-light:checked~.glass-glider{{
transform:translateX(0);
background:var(--toggle-active-bg);
box-shadow:var(--toggle-active-shadow);
}}
#theme-dark:checked~.glass-glider{{
transform:translateX(100%);
background:var(--toggle-active-bg);
box-shadow:var(--toggle-active-shadow);
}}

/* ===== SIDEBAR ===== */
.sidebar{{
position:fixed;top:56px;left:0;bottom:0;
width:280px;
background:var(--sidebar-bg);
border-right:1px solid var(--border);
overflow-y:auto;
padding:20px 0;
z-index:90;
transition:transform .3s,background .3s,border-color .3s;
}}
@media(max-width:900px){{
.sidebar{{transform:translateX(-100%);width:300px;z-index:200;box-shadow:4px 0 30px rgba(0,0,0,.2)}}
.sidebar.open{{transform:translateX(0)}}
.overlay{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:150}}
.overlay.show{{display:block}}
}}

.sidebar-header{{
padding:0 20px 16px;
font-size:12px;
text-transform:uppercase;
letter-spacing:2px;
color:var(--text3);
font-weight:600;
}}
.toc-link{{
display:block;
padding:8px 20px 8px 24px;
font-size:14px;
color:var(--text2);
text-decoration:none;
border-left:2px solid transparent;
transition:all .2s;
line-height:1.4;
}}
.toc-link:hover{{color:var(--accent);background:var(--bg2)}}
.toc-link.active{{
color:var(--accent);
border-left-color:var(--accent);
background:var(--bg2);
font-weight:600;
}}

/* ===== MAIN CONTENT ===== */
.main{{
margin-left:280px;
padding:80px 24px 100px;
transition:margin .3s;
}}
@media(max-width:900px){{
.main{{margin-left:0}}
}}
.content{{
max-width:var(--max-w);
margin:0 auto;
}}

/* ===== TYPOGRAPHY ===== */
.chapter{{
padding-bottom:60px;
margin-bottom:40px;
border-bottom:1px solid var(--border);
}}
.chapter:last-child{{border-bottom:none}}

.chapter h1{{
font-family:var(--font);
font-size:clamp(1.6rem,4vw,2.2rem);
font-weight:800;
color:var(--text);
margin:0 0 24px;
line-height:1.15;
letter-spacing:-.02em;
}}
.chapter h2{{
font-family:var(--font);
font-size:clamp(1.2rem,3vw,1.5rem);
font-weight:700;
color:var(--text);
margin:40px 0 16px;
line-height:1.2;
}}
.chapter h3{{
font-family:var(--font);
font-size:1.1rem;
font-weight:600;
color:var(--text);
margin:32px 0 12px;
}}
.chapter h4{{
font-size:1rem;
font-weight:600;
color:var(--text2);
margin:24px 0 8px;
}}

.chapter p{{
font-family:var(--font-reading);
font-size:17px;
line-height:1.75;
margin-bottom:18px;
color:var(--text);
}}

.chapter strong{{font-weight:700}}
.chapter em{{font-style:italic}}

.chapter ul,.chapter ol{{
font-family:var(--font-reading);
font-size:17px;
line-height:1.7;
margin:12px 0 18px;
padding-left:28px;
}}
.chapter li{{margin-bottom:8px}}
.chapter li > ul,.chapter li > ol{{margin-top:6px}}

/* ===== CODE ===== */
.chapter pre{{
background:var(--code-bg);
border:1px solid var(--border);
border-radius:10px;
padding:18px 20px;
margin:20px 0;
overflow-x:auto;
font-family:var(--font-mono);
font-size:14px;
line-height:1.55;
}}
.chapter code{{
font-family:var(--font-mono);
font-size:15px;
background:var(--code-bg);
padding:2px 6px;
border-radius:5px;
color:var(--accent);
}}
.chapter pre code{{
background:none;padding:0;color:var(--text);font-size:14px;
}}

/* ===== TABLES ===== */
.chapter table{{
width:100%;border-collapse:collapse;
margin:20px 0;font-size:15px;
border-radius:8px;overflow:hidden;
}}
.chapter thead{{background:var(--accent);color:#fff}}
.chapter th{{padding:10px 14px;text-align:left;font-size:13px;font-weight:600}}
.chapter td{{
padding:10px 14px;border-bottom:1px solid var(--border);
font-family:var(--font-reading);
}}
.chapter tr:nth-child(even){{background:var(--bg2)}}

/* ===== BLOCKQUOTE ===== */
.chapter blockquote{{
border-left:3px solid var(--accent-light);
background:var(--bg2);
padding:16px 20px;
margin:20px 0;
border-radius:0 8px 8px 0;
font-style:italic;
}}
.chapter blockquote p{{margin-bottom:8px;font-size:16px}}

/* ===== HR ===== */
.chapter hr{{
border:none;
border-top:2px solid var(--border);
margin:40px 60px;
}}

/* ===== SCROLL TO TOP ===== */
.scroll-top{{
position:fixed;bottom:24px;right:24px;
width:44px;height:44px;border-radius:12px;
background:var(--accent);color:#fff;
border:none;cursor:pointer;
display:none;align-items:center;justify-content:center;
box-shadow:0 4px 20px rgba(0,0,0,.2);
z-index:50;transition:all .3s;
}}
.scroll-top:hover{{transform:translateY(-2px)}}
.scroll-top.show{{display:flex}}
.scroll-top svg{{width:20px;height:20px;fill:currentColor}}

/* ===== RESUME BANNER ===== */
.resume-banner{{
display:none;
position:fixed;bottom:80px;left:50%;transform:translateX(-50%);
background:var(--accent);color:#fff;
padding:10px 20px;border-radius:12px;
font-size:14px;font-weight:600;
cursor:pointer;z-index:60;
box-shadow:0 4px 24px rgba(0,0,0,.3);
transition:all .3s;
white-space:nowrap;
}}
.resume-banner:hover{{transform:translateX(-50%) translateY(-2px)}}
.resume-banner.show{{display:block}}

/* ===== RESPONSIVE ===== */
@media(max-width:600px){{
.chapter table{{font-size:13px}}
.chapter th,.chapter td{{padding:8px 10px}}
.chapter p{{font-size:16px}}
.chapter pre{{font-size:13px;padding:14px 16px}}
.topbar-actions .btn-sm span{{display:none}}
}}
</style>
</head>
<body>

<div class="progress" id="progress"></div>
<div class="overlay" id="overlay"></div>

<header class="topbar">
<div class="topbar-left">
<button class="menu-btn" id="menuBtn" aria-label="Menu">
<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>
</button>
<div class="topbar-title"><a href="../">Prompt Engineering Meistern</a> &middot; Band {band_nr}</div>
</div>
<div class="topbar-actions">
<a href="../output/{pdf_name}.pdf" class="btn-sm" download>
<svg viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
<span>PDF</span>
</a>
<div class="glass-radio-group" role="radiogroup" aria-label="Farbmodus">
<input type="radio" name="theme" id="theme-light" value="light">
<label for="theme-light">Hell</label>
<input type="radio" name="theme" id="theme-dark" value="dark">
<label for="theme-dark">Dunkel</label>
<div class="glass-glider"></div>
</div>
</div>
</header>

<nav class="sidebar" id="sidebar">
<div class="sidebar-header">Kapitel</div>
{toc_html}
</nav>

<main class="main">
<div class="content">
{chapters_html}
</div>
</main>

<button class="scroll-top" id="scrollTop" aria-label="Nach oben">
<svg viewBox="0 0 24 24"><path d="M12 4l-8 8h5v8h6v-8h5z"/></svg>
</button>

<div class="resume-banner" id="resumeBanner">Weiterlesen &rarr;</div>

<script>
(function(){{
var B={band_nr},K='pe-band'+B;
var html=document.documentElement;

// Theme
var stored=localStorage.getItem('theme');
var dark=stored==='dark'||(!stored&&matchMedia('(prefers-color-scheme:dark)').matches);
if(dark)html.dataset.theme='dark';
document.getElementById(dark?'theme-dark':'theme-light').checked=true;

document.querySelectorAll('.glass-radio-group input').forEach(function(r){{
r.addEventListener('change',function(){{
html.dataset.theme=this.value==='dark'?'dark':'light';
localStorage.setItem('theme',html.dataset.theme);
}});
}});

// Mobile menu
var menuBtn=document.getElementById('menuBtn');
var sidebar=document.getElementById('sidebar');
var overlay=document.getElementById('overlay');
function closeSidebar(){{sidebar.classList.remove('open');overlay.classList.remove('show')}}
menuBtn.addEventListener('click',function(){{sidebar.classList.toggle('open');overlay.classList.toggle('show')}});
overlay.addEventListener('click',closeSidebar);
document.querySelectorAll('.toc-link').forEach(function(l){{l.addEventListener('click',function(){{if(innerWidth<=900)closeSidebar()}})}});

// Progress bar + reading position save
var prog=document.getElementById('progress');
var saveTimer;
window.addEventListener('scroll',function(){{
var h=document.documentElement.scrollHeight-innerHeight;
var pct=h>0?scrollY/h:0;
prog.style.width=(pct*100)+'%';
clearTimeout(saveTimer);
saveTimer=setTimeout(function(){{
localStorage.setItem(K+'-scroll',scrollY);
// Save active chapter
var chs=document.querySelectorAll('.chapter');
for(var i=chs.length-1;i>=0;i--){{
if(chs[i].getBoundingClientRect().top<150){{
localStorage.setItem(K+'-chapter',chs[i].id);
break;
}}
}}
}},300);
}});

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
banner.addEventListener('click',function(){{
scrollTo({{top:savedScroll,behavior:'smooth'}});
banner.classList.remove('show');
}});
setTimeout(function(){{banner.classList.remove('show')}},8000);
}}

// Scroll to top
var scrollBtn=document.getElementById('scrollTop');
window.addEventListener('scroll',function(){{scrollBtn.classList.toggle('show',scrollY>600)}});
scrollBtn.addEventListener('click',function(){{scrollTo({{top:0,behavior:'smooth'}})}});

// Active TOC
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
