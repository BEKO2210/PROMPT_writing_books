# Kapitel 4: Programmatisches Prompting – Prompts als Code

In Kapitel 3 hast du API-Calls gemacht. Einzelne Requests, einzelne Antworten. Jetzt bauen wir Systeme: Prompt-Templates, Variablen, Pipelines, Fehlerbehandlung und Multi-Turn-Konversationen.

## Prompt-Templates

Hartcodierte Prompts sind wie hartcodierte Strings – sie funktionieren, aber sie skalieren nicht. Die Lösung: Templates mit Variablen.

Die einfachste Variante sind Python f-Strings mit einer Funktion, die `text`, `language` und `detail_level` als Parameter nimmt. Für mehr Struktur nutzt du eine `PromptTemplate`-Dataclass mit `system`, `user_template`, `model`, `max_tokens` und `temperature`. Die `render`-Methode füllt die Platzhalter:

```python
@dataclass
class PromptTemplate:
    system: str
    user_template: str
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 1024

    def render(self, **kwargs) -> str:
        return self.user_template.format(**kwargs)
```

Du definierst Templates einmal (z.B. `SENTIMENT_TEMPLATE`) und nutzt sie überall mit `.render(count=3, texts="...")`.

## Multi-Turn-Konversationen

LLM-APIs sind zustandslos. Für Konversationen verwaltest du die History selbst. Eine `Conversation`-Klasse speichert die `messages`-Liste und hängt bei jedem `send()` die User-Message an, macht den API-Call und speichert die Antwort:

```python
class Conversation:
    def __init__(self, client, system, model="claude-sonnet-4-6"):
        self.client = client
        self.system = system
        self.messages = []

    def send(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})
        response = self.client.messages.create(
            model=self.model, system=self.system,
            messages=self.messages, max_tokens=2048
        )
        text = response.content[0].text
        self.messages.append({"role": "assistant", "content": text})
        return text
```

So baut jede Antwort auf dem vorherigen Kontext auf.

## Fehlerbehandlung und Retry-Logik

APIs können fehlschlagen: Rate Limits, Timeouts, Server-Fehler. Robuster Code fängt das ab mit **Exponential Backoff** – 1s, 2s, 4s Wartezeit bei `RateLimitError` und `APITimeoutError`. Server-Fehler (500+) werden retried, Client-Fehler (400, 401) nicht. Nach `max_retries` Versuchen: Exception werfen.

## Batch-Verarbeitung

Wenn du 1.000 Items verarbeiten musst: `asyncio` mit Semaphore für kontrollierte Parallelität. Ein `AsyncAnthropic`-Client, ein Semaphore mit `concurrency=5-10`, und `asyncio.gather()` für parallele Verarbeitung. Haiku ist hier ideal – schnell und günstig.

## Antwort-Parsing

Zwei Ansätze für strukturierte Antworten:

**JSON-Parsing aus Freitext:** Ein Fallback-System – erst `json.loads()` direkt, dann nach JSON-Block in Markdown suchen, dann nach `{...}` im Text. Funktioniert, ist aber fragil.

**Besser: Structured Output** (siehe Kapitel 3). Tool Use oder Structured Outputs geben garantiert valides JSON zurück – kein Parsing nötig.

## Prompt-Chaining programmatisch

Mehrere LLM-Calls hintereinander, wobei der Output des einen der Input des nächsten ist. Beispiel: Recherche → Outline → Artikel. Drei `async`-Calls nacheinander, jeder nutzt das Ergebnis des vorherigen als Kontext.

Das Muster ist immer gleich:

1. **Schritt 1:** Breite Recherche (LLM generiert Aspekte)
2. **Schritt 2:** Struktur (LLM erstellt Outline basierend auf Schritt 1)
3. **Schritt 3:** Ausführung (LLM schreibt basierend auf Schritt 2)

## Evaluierung und Monitoring

### Prompt-Qualität messen

Ein `EvalResult`-Dataclass speichert Input, Expected, Actual, Correct-Flag, Latenz und Token-Verbrauch. Eine `evaluate_prompt`-Funktion iteriert über Testfälle, misst Latenz und Accuracy:

```
Accuracy: 87.5% | Avg Latency: 234ms
```

Mindestens 20 Testfälle pro Template. Bei Änderungen: Regression testen.

## Best Practices

1. **Prompt und Code trennen** – Prompts in eigene Dateien (`.txt`, `.md`, YAML), nicht inline
2. **Versionierung** – Prompts in Git versionieren, A/B-Testing ermöglichen
3. **Logging** – Jeden API-Call loggen: Input, Output, Tokens, Latenz, Modell, Timestamp
4. **Testfälle pflegen** – Mindestens 20 pro Template
5. **Graceful Degradation** – Bei API-Ausfall: Fallback auf Cache oder günstigeres Modell

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
