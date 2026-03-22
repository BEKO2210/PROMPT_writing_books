# Kapitel 9: Modelle vergleichen – Das richtige Werkzeug für den Job

Bis jetzt habe ich in dieser Reihe meistens allgemein von "LLMs" oder "dem Modell" gesprochen. Aber in der Realität hast du die Wahl. Und diese Wahl macht einen Unterschied.

GPT-4o ist nicht Claude ist nicht Gemini ist nicht Llama. Jedes Modell hat Stärken, Schwächen und Eigenheiten. Und wenn du weißt, welches Modell für welche Aufgabe am besten passt, werden deine Ergebnisse sofort besser.

## Die großen Vier (und ein paar mehr)

### OpenAI: GPT-4o und o3

**Stärken:**
- Allrounder. Gut in fast allem.
- Starke Code-Generierung
- Gute Instruktionsbefolgung
- Riesiges Ökosystem (Plugins, GPT Store, API)
- o3: Besonders stark bei Reasoning und Mathematik

**Schwächen:**
- Kann bei langen Outputs qualitativ nachlassen
- Neigt zu übertrieben höflichem Ton
- Halluziniert gelegentlich bei Fakten

**Am besten für:** Alltags-Prompting, Code, kreatives Schreiben, wenn du ein Ökosystem willst.

### Anthropic: Claude 3.5 Sonnet / Claude 4

**Stärken:**
- Exzellent bei langen Texten und Analysen
- Großes Kontext-Fenster (200.000 Tokens)
- Sehr guter Schreibstil, weniger "robotic"
- Stark bei Nuancen und komplexen Anweisungen
- Folgt Einschränkungen zuverlässig

**Schwächen:**
- Manchmal zu vorsichtig (lehnt Anfragen ab, die andere Modelle beantworten)
- Kleineres Ökosystem als OpenAI
- Kann bei sehr technischen Themen hinter GPT zurückfallen

**Am besten für:** Lange Dokumente analysieren, Texte schreiben, komplexe Prompts mit vielen Einschränkungen, Zusammenfassungen.

### Google: Gemini 2.0

**Stärken:**
- Riesiges Kontext-Fenster (1 Million Tokens)
- Integration mit Google-Diensten (Gmail, Docs, Search)
- Stark bei multimodalem Input (Bilder, Videos, Audio)
- Kostenloses AI Studio mit Parameter-Kontrolle
- Gute Faktengenauigkeit durch Zugang zu aktuellen Informationen

**Schwächen:**
- Schreibstil manchmal generisch
- Instruktionsbefolgung nicht immer auf GPT/Claude-Niveau
- Kann bei kreativen Aufgaben konservativ sein

**Am besten für:** Recherche, multimodale Aufgaben, sehr lange Dokumente, Integration mit Google-Workflow.

### Meta: Llama 3.3

**Stärken:**
- Open Source – du kannst es lokal betreiben
- Keine Daten gehen an Dritte (bei lokaler Nutzung)
- Kostenlos
- Gute Leistung für ein offenes Modell
- Anpassbar (Fine-Tuning möglich)

**Schwächen:**
- Erfordert technisches Know-how für lokale Installation
- Leistung hinter GPT-4o und Claude bei komplexen Aufgaben
- Kein eingebautes Web-Zugriff
- Weniger "poliert" in der Ausgabe

**Am besten für:** Datenschutz-sensible Aufgaben, Experimente, Entwickler, die ein Modell anpassen wollen.

### Weitere Modelle

- **Mistral** – Europäisches Modell, stark bei mehrsprachigen Aufgaben, DSGVO-konform
- **Cohere Command R** – Spezialisiert auf RAG (Retrieval-Augmented Generation) und Unternehmenslösungen
- **xAI Grok** – Zugang zu Echtzeit-Daten über X (Twitter), lockerer Ton

## Modelle vergleichen: Die Entscheidungsmatrix

### GPT-4o

| Kriterium | Bewertung |
|---|---|
| Textqualität | ★★★★☆ |
| Code | ★★★★★ |
| Faktengenauigkeit | ★★★★☆ |
| Lange Kontexte | ★★★★☆ |
| Kreativität | ★★★★★ |
| Instruktionsbefolgung | ★★★★★ |
| Datenschutz | ★★★☆☆ |
| Kosten (API) | ★★★☆☆ |
| Multimodal | ★★★★☆ |

### Claude 3.5

| Kriterium | Bewertung |
|---|---|
| Textqualität | ★★★★★ |
| Code | ★★★★☆ |
| Faktengenauigkeit | ★★★★☆ |
| Lange Kontexte | ★★★★★ |
| Kreativität | ★★★★☆ |
| Instruktionsbefolgung | ★★★★★ |
| Datenschutz | ★★★☆☆ |
| Kosten (API) | ★★★☆☆ |
| Multimodal | ★★★☆☆ |

### Gemini 2.0

| Kriterium | Bewertung |
|---|---|
| Textqualität | ★★★★☆ |
| Code | ★★★★☆ |
| Faktengenauigkeit | ★★★★★ |
| Lange Kontexte | ★★★★★ |
| Kreativität | ★★★☆☆ |
| Instruktionsbefolgung | ★★★★☆ |
| Datenschutz | ★★★☆☆ |
| Kosten (API) | ★★★★☆ |
| Multimodal | ★★★★★ |

### Llama 3.3

| Kriterium | Bewertung |
|---|---|
| Textqualität | ★★★☆☆ |
| Code | ★★★☆☆ |
| Faktengenauigkeit | ★★★☆☆ |
| Lange Kontexte | ★★★☆☆ |
| Kreativität | ★★★☆☆ |
| Instruktionsbefolgung | ★★★☆☆ |
| Datenschutz | ★★★★★ |
| Kosten (API) | ★★★★★ |
| Multimodal | ★★☆☆☆ |

## Modellwahl nach Aufgabe

### Für Texte schreiben
**Erste Wahl:** Claude
**Alternative:** GPT-4o

Claude schreibt natürlicher. Weniger "KI-typisch". Besonders bei langen Texten, Artikeln und kreativen Aufgaben. GPT-4o ist fast gleichauf und hat mehr Plugins.

### Für Code
**Erste Wahl:** GPT-4o oder Claude
**Alternative:** Gemini

Für Code-Generierung, Debugging und Code-Review sind GPT-4o und Claude die stärksten. Claude kann besonders gut große Codebasen analysieren (dank des großen Kontext-Fensters).

### Für Recherche und Fakten
**Erste Wahl:** Gemini (mit Webzugang) oder ChatGPT (mit Browsing)
**Alternative:** Perplexity (spezialisiertes Recherchetool)

Wenn du aktuelle Informationen brauchst, sind Modelle mit Webzugang klar im Vorteil.

### Für Datenanalyse
**Erste Wahl:** GPT-4o (mit Code Interpreter)
**Alternative:** Claude

GPT-4o kann mit dem Code Interpreter direkt Daten verarbeiten, Diagramme erstellen und statistische Analysen durchführen. Claude kann das analytisch auch, hat aber keinen eingebauten Code-Runner.

### Für sensible Daten
**Erste Wahl:** Llama (lokal)
**Alternative:** Claude oder GPT mit Enterprise-Vertrag

Wenn Datenschutz oberste Priorität hat: Llama lokal. Keine Daten verlassen deinen Rechner.

### Für multimodale Aufgaben
**Erste Wahl:** Gemini
**Alternative:** GPT-4o

Bilder analysieren, PDFs verstehen, Videos zusammenfassen – Gemini ist hier am vielseitigsten, besonders mit dem 1-Million-Token-Fenster.

## Gleicher Prompt, verschiedene Modelle

Lass mich dir zeigen, wie unterschiedlich Modelle auf den gleichen Prompt reagieren können.

**Prompt:**
```
Erkläre Quantencomputing in 3 Sätzen für jemanden ohne
technischen Hintergrund. Keine Analogien mit Katzen.
```

**Typisches GPT-4o-Ergebnis:**
Strukturiert, leicht zu verstehen, vielleicht einen Tick zu lang. Befolgt die "keine Katzen"-Anweisung zuverlässig.

**Typisches Claude-Ergebnis:**
Elegant formuliert, etwas kürzer, natürlicher Ton. Hält sich strikt an 3 Sätze.

**Typisches Gemini-Ergebnis:**
Faktisch korrekt, manchmal etwas trocken. Könnte die 3-Sätze-Grenze leicht überschreiten.

Die Unterschiede sind subtil, aber sie sind da. Und bei komplexeren Aufgaben werden sie deutlicher.

## Kosten im Vergleich

Wenn du die API nutzt (oder planst, es zu tun), sind die Kosten ein wichtiger Faktor:

| Modell | Input (pro 1M Tokens) | Output (pro 1M Tokens) |
|--------|----------------------|----------------------|
| GPT-4o | ~2,50 $ | ~10,00 $ |
| Claude 3.5 Sonnet | ~3,00 $ | ~15,00 $ |
| Gemini 2.0 Flash | ~0,10 $ | ~0,40 $ |
| Llama 3.3 (lokal) | 0 $ (+ Strom + Hardware) | 0 $ |

*Preise ändern sich häufig. Stand: Anfang 2026.*

Für gelegentliche Nutzung ist der Preisunterschied irrelevant. Für Anwendungen, die tausende Anfragen pro Tag verarbeiten, kann er tausende Euro pro Monat ausmachen.

**Tipp:** Nutze günstige Modelle (Gemini Flash, GPT-4o-mini) für einfache Aufgaben und die Premium-Modelle nur, wenn du die Qualität brauchst.

## Multi-Modell-Strategie

Die Profis nutzen nicht EIN Modell. Sie nutzen das richtige Modell für die richtige Aufgabe.

Mein persönlicher Workflow:
- **Schnelle Fragen und Brainstorming:** ChatGPT (GPT-4o)
- **Texte schreiben und überarbeiten:** Claude
- **Recherche mit aktuellen Daten:** Gemini oder ChatGPT mit Browsing
- **Code:** Claude oder GPT-4o (je nach Komplexität)
- **Sensible Unternehmensdaten:** Llama lokal

Du musst dir nicht sofort alle Modelle anschauen. Fang mit einem an, das du gut kennst. Und wenn du merkst, dass es bei bestimmten Aufgaben schwächelt, probiere ein anderes.

## Modelle testen: Ein Framework

Wenn du ein Modell für eine bestimmte Aufgabe bewerten willst:

1. **Definiere 5 Test-Prompts** – Typische Aufgaben, die du damit erledigen willst
2. **Teste jeden Prompt 3 Mal** – Um Variation auszuschließen
3. **Bewerte nach deinen Kriterien** – Qualität, Geschwindigkeit, Instruktionsbefolgung
4. **Vergleiche die Ergebnisse** – Nicht nach Gefühl, sondern nach deinen vordefinierten Kriterien

Das dauert eine Stunde. Aber danach weißt du, welches Modell für DEINE Aufgaben am besten funktioniert.

---

## Übung

**Modell-Vergleichstest**

1. Wähle 3 Aufgaben, die du regelmäßig mit KI erledigst
2. Teste jede Aufgabe mit mindestens 2 verschiedenen Modellen (kostenlose Versionen reichen)
3. Bewerte jedes Ergebnis auf einer Skala von 1-5 nach:
   - Qualität des Ergebnisses
   - Wie gut die Anweisungen befolgt wurden
   - Wie nützlich das Ergebnis in der Praxis ist
4. Erstelle deine persönliche Empfehlung: Welches Modell für welche Aufgabe?

Tipp: Nutze für den Test den gleichen Prompt bei allen Modellen. So ist der Vergleich fair.
