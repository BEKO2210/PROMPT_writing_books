# Kapitel 4: Programmatisches Prompting – Prompts als Code

In Kapitel 3 hast du API-Calls gemacht. Einzelne Requests, einzelne Antworten. Jetzt bauen wir Systeme: Prompt-Templates, Variablen, Pipelines, Fehlerbehandlung und Multi-Turn-Konversationen.

## Prompt-Templates

Hartcodierte Prompts sind wie hartcodierte Strings – sie funktionieren, aber sie skalieren nicht.

### Python: Prompt-Templates mit f-Strings

```python
def create_analysis_prompt(
    text: str,
    language: str = "Deutsch",
    detail_level: str = "mittel"
) -> str:
    return f"""Analysiere folgenden Text auf {language}.

TEXT:
\"\"\"
{text}
\"\"\"

DETAILGRAD: {detail_level}
- "kurz": 3 Bullet Points
- "mittel": 1 Absatz Zusammenfassung + 5 Key Findings
- "ausführlich": Vollständige Analyse mit Zitaten

Antworte auf {language}."""
```

### Fortgeschritten: Template-Klasse

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class PromptTemplate:
    system: str
    user_template: str
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 1024
    temperature: float = 0.0

    def render(self, **kwargs) -> str:
        return self.user_template.format(**kwargs)

# Templates definieren
SENTIMENT_TEMPLATE = PromptTemplate(
    system="Du bist ein Sentiment-Analyse-Experte. Antworte nur mit JSON.",
    user_template="""Analysiere das Sentiment folgender {count} Texte:

{texts}

Für jeden Text: sentiment (positiv/neutral/negativ), score (-1 bis 1), begründung (1 Satz).""",
    temperature=0.0
)

# Nutzen
prompt = SENTIMENT_TEMPLATE.render(
    count=3,
    texts="1. Super Produkt!\n2. Geht so.\n3. Nie wieder."
)
```

## Multi-Turn-Konversationen

LLM-APIs sind zustandslos. Für Konversationen musst du die History selbst verwalten:

```python
class Conversation:
    def __init__(self, client, system: str, model: str = "claude-sonnet-4-20250514"):
        self.client = client
        self.system = system
        self.model = model
        self.messages: list[dict] = []

    def send(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.system,
            messages=self.messages
        )

        assistant_message = response.content[0].text
        self.messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    def reset(self):
        self.messages = []

# Nutzung
conv = Conversation(
    client=anthropic.Anthropic(),
    system="Du bist ein Python-Tutor. Erkläre Konzepte mit Beispielen."
)

answer1 = conv.send("Was ist eine List Comprehension?")
answer2 = conv.send("Zeig mir ein komplexeres Beispiel mit Bedingung.")
# Das Modell kennt die vorherige Frage und baut darauf auf
```

## Fehlerbehandlung und Retry-Logik

APIs können fehlschlagen. Rate Limits, Timeouts, Server-Fehler. Robuster Code fängt das ab:

```python
import time
import anthropic

def call_with_retry(
    client: anthropic.Anthropic,
    max_retries: int = 3,
    **kwargs
) -> anthropic.types.Message:
    for attempt in range(max_retries):
        try:
            return client.messages.create(**kwargs)

        except anthropic.RateLimitError:
            wait = 2 ** attempt  # 1s, 2s, 4s
            print(f"Rate limit. Warte {wait}s...")
            time.sleep(wait)

        except anthropic.APITimeoutError:
            wait = 2 ** attempt
            print(f"Timeout. Warte {wait}s...")
            time.sleep(wait)

        except anthropic.APIStatusError as e:
            if e.status_code >= 500:  # Server-Fehler
                wait = 2 ** attempt
                print(f"Server error {e.status_code}. Warte {wait}s...")
                time.sleep(wait)
            else:
                raise  # Client-Fehler nicht retrien (400, 401, etc.)

    raise Exception(f"Fehlgeschlagen nach {max_retries} Versuchen")
```

## Batch-Verarbeitung

Wenn du viele Items verarbeiten musst (z.B. 1.000 Produktbeschreibungen analysieren):

```python
import asyncio
import anthropic

async def process_batch(
    items: list[str],
    prompt_template: str,
    concurrency: int = 5
) -> list[str]:
    client = anthropic.AsyncAnthropic()
    semaphore = asyncio.Semaphore(concurrency)
    results = []

    async def process_one(item: str) -> str:
        async with semaphore:
            message = await client.messages.create(
                model="claude-haiku-3-5-20241022",
                max_tokens=256,
                messages=[{
                    "role": "user",
                    "content": prompt_template.format(item=item)
                }]
            )
            return message.content[0].text

    tasks = [process_one(item) for item in items]
    results = await asyncio.gather(*tasks)
    return results

# Nutzung
items = ["Produkt A ist super", "Produkt B ist okay", ...]
results = asyncio.run(process_batch(
    items,
    "Klassifiziere das Sentiment: '{item}'. Antwort: positiv/neutral/negativ",
    concurrency=10
))
```

## Antwort-Parsing

### JSON-Parsing

```python
import json

def parse_json_response(text: str) -> dict:
    """Extrahiere JSON aus einer LLM-Antwort."""
    # Versuche direktes Parsing
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Suche nach JSON-Block in Markdown
    import re
    json_match = re.search(r'```(?:json)?\s*\n(.*?)\n```', text, re.DOTALL)
    if json_match:
        return json.loads(json_match.group(1))

    # Suche nach JSON-Objekt im Text
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        return json.loads(json_match.group(0))

    raise ValueError(f"Kein JSON gefunden in: {text[:200]}...")
```

### Besser: Structured Output nutzen (siehe Kapitel 3)

Statt JSON aus Freitext zu parsen, nutze Tool Use oder Structured Outputs. Das ist zuverlässiger.

## Prompt-Chaining programmatisch

Mehrere LLM-Calls hintereinander, wobei der Output des einen der Input des nächsten ist:

```python
async def research_and_write(topic: str) -> str:
    client = anthropic.AsyncAnthropic()

    # Schritt 1: Recherche
    research = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"Recherchiere die 5 wichtigsten Aspekte von: {topic}"
        }]
    )
    research_text = research.content[0].text

    # Schritt 2: Outline erstellen
    outline = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Basierend auf dieser Recherche:
{research_text}

Erstelle ein Outline für einen Artikel (5 Abschnitte)."""
        }]
    )
    outline_text = outline.content[0].text

    # Schritt 3: Artikel schreiben
    article = await client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": f"""Schreibe einen Artikel nach folgendem Outline:
{outline_text}

Stil: Sachlich, informativ, 800 Wörter."""
        }]
    )

    return article.content[0].text
```

## Evaluierung und Monitoring

### Prompt-Qualität messen

```python
from dataclasses import dataclass

@dataclass
class EvalResult:
    input: str
    expected: str
    actual: str
    correct: bool
    latency_ms: float
    tokens_used: int

def evaluate_prompt(
    client,
    test_cases: list[dict],  # [{"input": ..., "expected": ...}]
    prompt_template: str,
    model: str
) -> list[EvalResult]:
    results = []

    for case in test_cases:
        start = time.time()
        message = client.messages.create(
            model=model,
            max_tokens=256,
            messages=[{
                "role": "user",
                "content": prompt_template.format(**case)
            }]
        )
        latency = (time.time() - start) * 1000
        actual = message.content[0].text.strip()

        results.append(EvalResult(
            input=case["input"],
            expected=case["expected"],
            actual=actual,
            correct=actual.lower() == case["expected"].lower(),
            latency_ms=latency,
            tokens_used=message.usage.input_tokens + message.usage.output_tokens
        ))

    accuracy = sum(1 for r in results if r.correct) / len(results)
    avg_latency = sum(r.latency_ms for r in results) / len(results)
    print(f"Accuracy: {accuracy:.1%} | Avg Latency: {avg_latency:.0f}ms")

    return results
```

## Best Practices

### 1. Prompt und Code trennen
Prompts in eigene Dateien (`.txt`, `.md`, YAML) – nicht in den Code inline.

### 2. Versionierung
Prompts versionieren (in Git oder einer Prompt-Registry). A/B-Testing ermöglichen.

### 3. Logging
Jeden API-Call loggen: Input, Output, Tokens, Latenz, Modell, Timestamp. Unverzichtbar für Debugging und Kostenoptimierung.

### 4. Testfälle pflegen
Mindestens 20 Testfälle pro Prompt-Template. Bei Änderungen: Regression testen.

### 5. Graceful Degradation
Wenn die API ausfällt: Fallback auf gecachte Antworten oder ein günstigeres Modell.

---

## Übungen

### Übung 1: Template-Bibliothek
Erstelle eine PromptTemplate-Klasse und 3 Templates für verschiedene Aufgaben (Sentiment, Zusammenfassung, Übersetzung).

### Übung 2: Konversations-Manager
Implementiere eine Conversation-Klasse mit History, Token-Counting und Max-History-Länge.

### Übung 3: Batch-Verarbeitung
Verarbeite 50 Texte parallel mit asyncio. Miss die Gesamtdauer vs. sequentielle Verarbeitung.

### Übung 4: Evaluierung
Erstelle 10 Testfälle für ein Sentiment-Analyse-Template. Wie hoch ist die Accuracy?
