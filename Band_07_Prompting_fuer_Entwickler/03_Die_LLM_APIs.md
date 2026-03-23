# Kapitel 3: Die LLM-APIs – Dein Zugang zur KI-Power

Bisher hast du KI über Chat-Interfaces genutzt. Jetzt nutzt du sie programmatisch – über APIs. Das bedeutet: Du schickst HTTP-Requests und bekommst strukturierte Responses. Automatisiert. Skalierbar. Integriert in deine Software.

## Die großen Drei (und die Challenger)

### Anthropic (Claude)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| Claude Opus 4.6 | 200K (1M beta) | #1 Reasoning, 80.8% SWE-bench, Code | $15 / $75 |
| Claude Sonnet 4.5 | 200K | Bestes Preis-Leistung, 77-82% SWE-bench | $3 / $15 |
| Claude Haiku 4.5 | 200K | Schnell, günstig, agentic Loops | $0.25 / $1.25 |

**Besondere Features:**
- **Extended Thinking** – Das Modell "denkt nach" bevor es antwortet. Steuerbar über `effort`-Parameter. Thinking-Tokens als Output abgerechnet.
- **Tool Use** – Natives Function Calling mit JSON-Schema. Plus: Web Search, Code Execution, Computer Use, programmatic Tool Calling.
- **Prompt Caching** – Wiederholt genutzte Prompt-Teile werden gecacht (90% günstiger).
- **Batches API** – Massenhaft Requests mit 50% Rabatt (24h SLA).
- **Vision** – Bilder, PDFs, Charts, Diagramme als Input.
- **Compaction API** (beta) – Server-seitige Kontext-Zusammenfassung für endlose Konversationen.
- **1M Token Context Window** (beta für Opus 4.6).

### OpenAI (GPT)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| GPT-5.2 (xhigh) | 1M | #1 Coding-Benchmarks (89% LiveCodeBench) | $1.75 / $14 |
| GPT-5 mini | 200K | Schnell, günstig, starkes Allround | $0.25 / $2 |
| GPT-5 nano | 128K | Ultra-günstig, Edge-Deployment | $0.05 / $0.40 |
| GPT-4o | 128K | Multimodal (Text + Bild + Audio) | $2.50 / $10 |
| o3 | 200K | Deep Reasoning, Mathematik | $10 / $40 |

**Besondere Features:**
- **Responses API** – Ersetzt Chat Completions für neue Projekte. Agentic by default.
- **Structured Outputs** – Garantiert valides JSON mit `strict: true`.
- **Agents SDK** – Open-Source Multi-Agent-Orchestrierung mit MCP-Support.
- **Realtime API** – Audio-Input und -Output in Echtzeit.

### Google (Gemini)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| Gemini 3.1 Pro | 1M | Reasoning, Cross-Language | $2 / $12 |
| Gemini 3 Flash | 1M | Schnell, günstig | $0.50 / $3 |
| Gemini 2.5 Pro | 1M | Bewährt, riesiger Kontext | $1.25 / $10 |
| Gemini 2.0 Flash-Lite | 1M | Ultra-günstig | $0.075 / $0.30 |

**Besondere Features:** 1M Token Kontext, großzügigstes Free Tier (1.000 Anfragen/Tag kostenlos), Code Execution in Sandbox, Thinking Budget, nativer MCP-Support.

### Open Source / Alternative

| Modell | Parameter | Stärke | Zugang |
|---|---|---|---|
| Llama 4 (Meta) | Scout 17B aktiv / Maverick 400B | Multimodal, Open Source | Lokal / Together / Groq |
| DeepSeek-V3.2 | 685B (37B aktiv) | Coding, Reasoning, $0.28/1M In | API / Lokal |
| Qwen 3 | Diverse | Multimodal, mehrsprachig | API / Lokal |
| Mistral Large 2 | 123B | Europa, mehrsprachig | API / Lokal |

## Dein erster API-Call

Die Grundstruktur ist bei allen Anbietern ähnlich: Client erstellen, Modell wählen, Nachricht senden:

```python
import anthropic

client = anthropic.Anthropic()  # ANTHROPIC_API_KEY aus Env
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Was ist eine API?"}]
)
print(message.content[0].text)
```

Bei OpenAI sieht es fast identisch aus – `from openai import OpenAI`, `client.chat.completions.create()`, Ergebnis in `response.choices[0].message.content`. Die SDKs für TypeScript folgen demselben Muster.

## System-Prompts

System-Prompts definieren das Verhalten des Modells über die gesamte Konversation. Bei Anthropic ein `system`-Parameter, bei OpenAI eine Message mit `role: "system"`:

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    system="Du bist ein Senior Python Developer. PEP 8, typisiert, Tests.",
    messages=[{"role": "user", "content": "Implementiere Retry-Logik."}]
)
```

## Streaming

Für UX-freundliche Responses – Text erscheint Wort für Wort. Bei Anthropic: `client.messages.stream()` mit einem Context Manager und `stream.text_stream`. Bei OpenAI: `stream=True` als Parameter und Iteration über `chunk.choices[0].delta.content`.

## Structured Output

Das Modell gibt garantiert valides JSON zurück. Bei Anthropic nutzt du **Tool Use** – du definierst ein JSON-Schema als Tool, und das Ergebnis kommt als validiertes JSON:

```python
message = client.messages.create(
    model="claude-sonnet-4-6",
    tools=[{
        "name": "analyze_sentiment",
        "description": "Analysiere das Sentiment",
        "input_schema": {
            "type": "object",
            "properties": {
                "sentiment": {"type": "string", "enum": ["positiv", "neutral", "negativ"]},
                "confidence": {"type": "number"}
            },
            "required": ["sentiment", "confidence"]
        }
    }],
    tool_choice={"type": "tool", "name": "analyze_sentiment"},
    messages=[{"role": "user", "content": "Analysiere: 'Super Produkt, aber zu teuer.'"}]
)
result = message.content[0].input  # Valides JSON nach Schema
```

Bei OpenAI: `response_format` mit `type: "json_schema"` und `strict: true`.

## Prompt Caching

Spart bis zu 90% bei wiederholten Prompts. Bei Anthropic fügst du `cache_control: {"type": "ephemeral"}` zu System-Prompt-Blöcken hinzu. Beim zweiten Call mit demselben System-Prompt trifft der Cache – 90% günstiger für den gecachten Teil.

## Vision (Bilder als Input)

Bilder als Base64 oder URL in den Content-Array einfügen. Das Modell kann Screenshots, Diagramme, PDFs analysieren und z.B. HTML/CSS-Code daraus generieren.

## Kosten optimieren

Fünf Strategien, die zusammen bis zu 95% sparen:

1. **Richtiges Modell:** Einfache Aufgaben → Haiku/nano, Mittlere → Sonnet/mini, Komplexe → Opus/o3
2. **Prompt Caching:** 90% Ersparnis auf wiederholt genutzte Kontexte
3. **Batches:** Nicht zeitkritische Anfragen sammeln, 50% Rabatt
4. **Token-Budget:** `max_tokens` auf das Minimum setzen
5. **Prompt-Optimierung:** Kürzere Prompts = weniger Input-Tokens

**Preisentwicklung:** LLM-API-Preise sind zwischen Anfang 2025 und Anfang 2026 um ca. 80% gefallen. Die Preise pro Token sinken kontinuierlich.

---

## Übungen

### Übung 1: Erster API-Call
Erstelle einen API-Key bei Anthropic oder OpenAI. Schreibe deinen ersten API-Call in Python oder TypeScript.

### Übung 2: System-Prompt
Schreibe einen System-Prompt für einen spezialisierten Assistenten. Teste ihn mit verschiedenen User-Messages.

### Übung 3: Structured Output
Nutze Tool Use, um das Sentiment von 10 Produktbewertungen als JSON zu analysieren.

### Übung 4: Kosten berechnen
Schätze die API-Kosten für 1.000 Anfragen/Tag bei ~500 Input + ~200 Output Tokens. Vergleiche Claude Sonnet, GPT-5 mini und Gemini Flash.
