# Kapitel 3: Die LLM-APIs – Dein Zugang zur KI-Power

Bisher hast du KI über Chat-Interfaces genutzt. Jetzt nutzt du sie programmatisch – über APIs. Das bedeutet: Du schickst HTTP-Requests und bekommst strukturierte Responses. Automatisiert. Skalierbar. Integriert in deine Software.

## Die großen Drei (und die Challenger)

### Anthropic (Claude)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| Claude Opus 4 | 200K | Reasoning, komplexe Aufgaben, Code | $15 / $75 |
| Claude Sonnet 4 | 200K | Bestes Preis-Leistung, schnell, gut in Code | $3 / $15 |
| Claude Haiku 3.5 | 200K | Schnell, günstig, einfache Aufgaben | $0.80 / $4 |

**Besondere Features:**
- **Extended Thinking** – Das Modell "denkt nach" bevor es antwortet (Chain-of-Thought intern). Ideal für komplexe Aufgaben.
- **Tool Use** – Natives Function Calling mit JSON-Schema-Definitionen.
- **Computer Use** – Claude kann einen Computer steuern (Screenshots, Klicks, Tippen).
- **Prompt Caching** – Wiederholt genutzte Prompt-Teile werden gecacht (90% günstiger).
- **Batches API** – Massenhaft Requests mit 50% Rabatt (24h SLA).
- **Vision** – Bilder und PDFs als Input.
- **Citationen** – Claude kann Quellenangaben in Dokumenten referenzieren.

### OpenAI (GPT)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| GPT-4.1 | 1M | Coding, Instruction Following | $2 / $8 |
| GPT-4o | 128K | Multimodal (Text + Bild + Audio) | $2.50 / $10 |
| o3 | 200K | Deep Reasoning, Mathematik | $10 / $40 |
| o4-mini | 200K | Schnelles Reasoning | $1.10 / $4.40 |
| GPT-4o-mini | 128K | Günstig, schnell, gutes Allround | $0.15 / $0.60 |

**Besondere Features:**
- **Structured Outputs** – Garantiert valides JSON nach JSON-Schema.
- **Function Calling** – Nativ, parallel (mehrere Tools gleichzeitig).
- **Realtime API** – Audio-Input und -Output in Echtzeit.
- **Assistants API** – Persistente Threads mit Code Interpreter und File Search.
- **Fine-tuning** – Für GPT-4o-mini und GPT-4o verfügbar.

### Google (Gemini)

| Modell | Kontext | Stärke | Input / Output (pro 1M Token) |
|---|---|---|---|
| Gemini 2.5 Pro | 1M | Reasoning, riesiger Kontext | $1.25-$2.50 / $10-$15 |
| Gemini 2.5 Flash | 1M | Schnell, günstig, Thinking-Budget | $0.15-$0.60 / $0.60-$3.50 |
| Gemini 2.0 Flash | 1M | Multimodal, Agentic | Kostenloser Tier verfügbar |

**Besondere Features:**
- **1M Token Kontext** – Gesamte Codebases in einem Request.
- **Grounding mit Google Search** – Modell kann googeln.
- **Code Execution** – Führt Python-Code in Sandbox aus.
- **Thinking Budget** – Steuere, wie viel das Modell "nachdenken" soll.

### Open Source / Alternative

| Modell | Parameter | Stärke | Zugang |
|---|---|---|---|
| Llama 4 (Meta) | Scout: 17B aktiv (109B gesamt), Maverick: 17B aktiv (400B gesamt) | Multimodal, Open Source | Lokal / Together / Groq |
| DeepSeek-V3 | 685B (37B aktiv) | Coding, Reasoning, günstig | API / Lokal |
| DeepSeek-R1 | 685B | Reasoning (o1-Level) | API / Lokal |
| Qwen 3 | Diverse | Multimodal, mehrsprachig | API / Lokal |
| Mistral Large 2 | 123B | Europa, mehrsprachig, Code | API / Lokal |
| Codestral | 22B | Speziell für Code | API / Lokal |

## Dein erster API-Call

### Python (Anthropic SDK)

```python
import anthropic

client = anthropic.Anthropic()  # ANTHROPIC_API_KEY aus Env

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Erkläre mir in 3 Sätzen, was eine API ist."
        }
    ]
)

print(message.content[0].text)
```

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI()  # OPENAI_API_KEY aus Env

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Erkläre mir in 3 Sätzen, was eine API ist."}
    ]
)

print(response.choices[0].message.content)
```

### TypeScript (Anthropic SDK)

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-sonnet-4-20250514",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "Erkläre mir in 3 Sätzen, was eine API ist."
    }
  ]
});

console.log(message.content[0].text);
```

## System-Prompts

System-Prompts definieren das Verhalten des Modells über die gesamte Konversation:

```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2048,
    system="""Du bist ein Senior Python Developer mit 15 Jahren Erfahrung.
Du schreibst sauberen, typisierten Python-Code nach PEP 8.
Du bevorzugst funktionale Patterns über OOP.
Du erklärst deine Designentscheidungen kurz.
Du schreibst immer Tests.""",
    messages=[
        {"role": "user", "content": "Implementiere eine Retry-Logik mit exponential backoff."}
    ]
)
```

## Streaming

Für UX-freundliche Responses – Text erscheint Wort für Wort:

```python
# Anthropic Streaming
with client.messages.stream(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Schreibe eine Kurzgeschichte."}]
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

```python
# OpenAI Streaming
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Schreibe eine Kurzgeschichte."}],
    stream=True
)
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## Structured Output

Das Modell gibt garantiert valides JSON zurück:

### Anthropic (Tool Use für strukturiertes JSON)

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    tools=[{
        "name": "analyze_sentiment",
        "description": "Analysiere das Sentiment eines Textes",
        "input_schema": {
            "type": "object",
            "properties": {
                "sentiment": {
                    "type": "string",
                    "enum": ["positiv", "neutral", "negativ"]
                },
                "confidence": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 1
                },
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "required": ["sentiment", "confidence", "keywords"]
        }
    }],
    tool_choice={"type": "tool", "name": "analyze_sentiment"},
    messages=[{
        "role": "user",
        "content": "Analysiere: 'Das neue Update ist fantastisch, aber der Preis ist zu hoch.'"
    }]
)

# Ergebnis ist garantiert valides JSON nach Schema
result = message.content[0].input
# {"sentiment": "neutral", "confidence": 0.7, "keywords": ["Update", "fantastisch", "Preis", "hoch"]}
```

## Prompt Caching (Anthropic)

Spart bis zu 90% bei wiederholten Prompts:

```python
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "Du bist ein Experte für deutsches Steuerrecht...",
            "cache_control": {"type": "ephemeral"}  # Diesen Teil cachen
        }
    ],
    messages=[{"role": "user", "content": "Wie funktioniert die Umsatzsteuervoranmeldung?"}]
)

# Beim zweiten Call mit demselben System-Prompt:
# Cache Hit → 90% günstiger für den gecachten Teil
```

## Vision (Bilder als Input)

```python
import base64

# Bild als Base64
with open("screenshot.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data
                }
            },
            {
                "type": "text",
                "text": "Erstelle den HTML/CSS-Code, der dieses Design nachbaut."
            }
        ]
    }]
)
```

## Kosten optimieren

### Strategie 1: Das richtige Modell wählen

```
Einfache Aufgaben (Klassifikation, Extraktion) → Haiku / GPT-4o-mini
Mittlere Aufgaben (Texte, Code) → Sonnet / GPT-4o
Komplexe Aufgaben (Reasoning, Architektur) → Opus / o3
```

### Strategie 2: Prompt Caching
Wiederholt genutzte System-Prompts und Kontexte cachen. Spart 90% auf gecachte Tokens.

### Strategie 3: Batches
Nicht zeitkritische Anfragen sammeln und als Batch senden. 50% günstiger.

### Strategie 4: Token-Budget
`max_tokens` auf das Minimum setzen. Nicht 4096, wenn 500 reichen.

### Strategie 5: Prompt-Optimierung
Kürzere Prompts = weniger Input-Tokens = günstiger. Unnötige Wiederholungen entfernen.

---

## Übungen

### Übung 1: Erster API-Call
Erstelle einen API-Key bei Anthropic oder OpenAI. Schreibe deinen ersten API-Call in Python oder TypeScript. Lass dir einen Witz erzählen.

### Übung 2: System-Prompt
Schreibe einen System-Prompt für einen spezialisierten Assistenten (z.B. Code-Reviewer, Übersetzer, Datenanalyst). Teste ihn mit verschiedenen User-Messages.

### Übung 3: Structured Output
Nutze Tool Use oder Structured Outputs, um das Sentiment von 10 Produktbewertungen zu analysieren. Gib das Ergebnis als JSON zurück.

### Übung 4: Kosten berechnen
Schätze die API-Kosten für ein Szenario: 1.000 Kundenanfragen pro Tag, je ~500 Input-Tokens und ~200 Output-Tokens. Vergleiche die Kosten bei Claude Sonnet, GPT-4o und Gemini Flash.
