# Kapitel 8: Fine-Tuning vs. Prompting – Die Entscheidungsmatrix

"Sollte ich das Modell fine-tunen?" Diese Frage höre ich ständig. Und die Antwort ist fast immer: Nein. Zumindest nicht zuerst.

Fine-Tuning ist mächtig. Aber es ist teuer, komplex und oft unnötig. In den meisten Fällen erreichst du mit gutem Prompting, RAG und Tool Use dasselbe Ergebnis – schneller und günstiger.

Dieses Kapitel zeigt dir, wann welcher Ansatz der richtige ist.

## Die Optionen im Überblick

```
EINFACHHEIT                                KOMPLEXITÄT
    │                                          │
    ▼                                          ▼
Prompt      Few-Shot     RAG      Fine-Tuning    Eigenes
Engineering  Prompting   Pipeline  (bestehend)   Modell trainieren
    │           │           │          │              │
Minuten     Stunden      Tage     Wochen          Monate
    │           │           │          │              │
$0           $0.01       $100      $1.000+        $100.000+
```

## Wann reicht Prompting?

| Anforderung | Prompting reicht? |
|---|---|
| Ton/Stil anpassen | ✅ Ja – System-Prompt mit Beispielen |
| Fachsprache verwenden | ✅ Ja – Fachbegriffe im Prompt erklären |
| Ausgabe-Format steuern | ✅ Ja – Structured Output / Tool Use |
| Auf eigene Daten zugreifen | ✅ Ja – RAG |
| Eigene Tools nutzen | ✅ Ja – Function Calling |
| Komplexe Reasoning-Aufgaben | ✅ Ja – Chain-of-Thought, Extended Thinking |
| 95%+ Accuracy bei Klassifikation | ⚠️ Vielleicht – Few-Shot oft ausreichend |
| Spezifische Domäne (Jura, Medizin) | ⚠️ Vielleicht – RAG + spezialisierter Prompt |
| Eigene "Stimme" / Brand Voice | ⚠️ Vielleicht – System-Prompt + Beispiele |
| Extrem hohe Konsistenz | ❌ Vielleicht Fine-Tuning nötig |
| Latenz-kritisch (jede ms zählt) | ❌ Fine-Tuning auf kleinem Modell |
| Offline-Betrieb | ❌ Eigenes/lokales Modell nötig |

## Wann Fine-Tuning?

Fine-Tuning ist sinnvoll, wenn:

1. **Konsistenz über tausende Anfragen** – Du brauchst exakt dasselbe Format, denselben Stil, immer. Nicht "meistens", sondern "immer".

2. **Latenz** – Du willst ein kleines, schnelles Modell, das eine spezifische Aufgabe so gut kann wie ein großes.

3. **Kosten bei Volumen** – 1 Million Requests/Tag: Ein fine-getuntes GPT-4o-mini ist günstiger als ein Prompt mit 2000 Token Kontext bei Sonnet.

4. **Spezifisches Verhalten** – Das Modell soll Dinge tun, die schwer per Prompt zu beschreiben sind (z.B. einen sehr spezifischen Coding-Style).

5. **Datenschutz** – Deine Trainingsdaten bleiben bei dir (lokales Fine-Tuning mit Open Source).

## Fine-Tuning-Optionen (Stand 2026)

### Cloud-basiert

| Anbieter | Modell | Methode | Kosten (Training) | Kosten (Inference) |
|---|---|---|---|---|
| OpenAI | GPT-4o-mini | Supervised FT | $3.00 / 1M Token | $0.30 / 1M Token (out) |
| OpenAI | GPT-4o | Supervised FT | $25.00 / 1M Token | $3.75 / 1M Token (out) |
| Google | Gemini Flash | Supervised FT | Variabel | Reduziert vs. Base |
| Together AI | Llama, Mistral etc. | LoRA, Full FT | Ab $0.50/Stunde GPU | Pay-per-token |
| Fireworks AI | Diverse Open Source | LoRA | Ab $0.50/Stunde GPU | Pay-per-token |

### Lokal

| Tool | Methode | Stärke |
|---|---|---|
| **Unsloth** | QLoRA | 2x schneller, 60% weniger VRAM, Open Source |
| **Axolotl** | LoRA, QLoRA, Full FT | Flexibel, viele Modelle |
| **Hugging Face TRL** | SFT, DPO, RLHF | Standard-Framework |
| **MLX** (Apple) | LoRA | Optimiert für Apple Silicon |
| **Ollama + Modelfile** | Basis-Anpassung | Einfachster Einstieg |

## Fine-Tuning: Der Prozess

### Schritt 1: Trainingsdaten erstellen

```json
// Format: JSONL (eine Zeile pro Beispiel)
{"messages": [
    {"role": "system", "content": "Du bist ein Support-Bot für TechCorp."},
    {"role": "user", "content": "Wie setze ich mein Passwort zurück?"},
    {"role": "assistant", "content": "Gehe auf techcorp.de/passwort, klicke auf 'Passwort vergessen', gib deine E-Mail ein. Du erhältst innerhalb von 5 Minuten einen Reset-Link."}
]}
{"messages": [
    {"role": "system", "content": "Du bist ein Support-Bot für TechCorp."},
    {"role": "user", "content": "Wie kündige ich mein Abo?"},
    {"role": "assistant", "content": "Gehe zu Einstellungen > Abo > Kündigen. Die Kündigung wird zum Ende des aktuellen Abrechnungszeitraums wirksam. Du behältst bis dahin vollen Zugang."}
]}
```

### Wie viele Beispiele?

| Aufgabe | Minimum | Empfohlen | Optimum |
|---|---|---|---|
| Stil/Ton anpassen | 20 | 50-100 | 200+ |
| Klassifikation | 50 pro Klasse | 100 pro Klasse | 500+ pro Klasse |
| Domänen-spezifisch | 100 | 500 | 1.000+ |
| Komplexe Aufgaben | 200 | 1.000 | 5.000+ |

### Schritt 2: Datenqualität prüfen

```python
# Checkliste für Trainingsdaten:
# ✅ Konsistente Formatierung
# ✅ Keine Widersprüche zwischen Beispielen
# ✅ Repräsentativ für echte Anfragen
# ✅ Korrekte Antworten (manuell geprüft)
# ✅ Diverse Formulierungen (nicht alle gleich)
# ✅ Edge Cases enthalten
# ✅ Keine sensiblen Daten (PII, Passwörter)
```

### Schritt 3: Fine-Tuning starten (OpenAI Beispiel)

```python
from openai import OpenAI
client = OpenAI()

# Trainingsdatei hochladen
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Fine-Tuning starten
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18",
    hyperparameters={
        "n_epochs": 3,
        "batch_size": "auto",
        "learning_rate_multiplier": "auto"
    }
)

# Status prüfen
status = client.fine_tuning.jobs.retrieve(job.id)
print(f"Status: {status.status}")
# → "running" → "succeeded"

# Fine-tuned Modell nutzen
response = client.chat.completions.create(
    model=status.fine_tuned_model,  # ft:gpt-4o-mini:org:custom-name:id
    messages=[{"role": "user", "content": "Wie setze ich mein Passwort zurück?"}]
)
```

## Die Entscheidungsmatrix

```
                           DATEN VORHANDEN?
                          /               \
                       Ja                  Nein
                      /                      \
              HOHE KONSISTENZ           PROMPTING +
              NÖTIG?                    RAG reicht
              /         \
           Ja            Nein
           |              |
     HOHES VOLUMEN?    PROMPTING +
     /         \       FEW-SHOT
  Ja            Nein
  |              |
FINE-TUNING    PROMPTING +
               EXAMPLES
```

### Praktische Faustregel

**Starte IMMER mit Prompting.** Investiere zuerst 2-3 Tage in Prompt-Optimierung, bevor du über Fine-Tuning nachdenkst. In 90% der Fälle wirst du feststellen: Prompting reicht.

Wenn es nicht reicht, probiere diese Reihenfolge:
1. Besserer System-Prompt
2. Few-Shot-Beispiele im Prompt
3. RAG (eigene Daten)
4. Prompt-Chaining
5. Fine-Tuning (wenn 1-4 nicht reichen)

## Prompt-Distillation: Der goldene Mittelweg

Eine clevere Technik: Nutze ein großes, teures Modell (Opus) um hochqualitative Antworten zu generieren. Nutze diese Antworten als Trainingsdaten für ein kleines, günstiges Modell (Haiku, GPT-4o-mini).

```python
# Phase 1: Großes Modell generiert Trainingsbeispiele
for query in production_queries:
    response = opus_model.generate(query)  # Teuer, langsam, aber gut
    training_data.append({"input": query, "output": response})

# Phase 2: Kleines Modell wird auf diesen Daten fine-tuned
fine_tune(small_model, training_data)

# Phase 3: Kleines Modell in Produktion (günstig, schnell)
result = fine_tuned_small_model.generate(new_query)
```

**Ergebnis:** 90% der Qualität des großen Modells bei 10% der Kosten und 5x der Geschwindigkeit.

---

## Übungen

### Übung 1: Prompt vs. Fine-Tuning
Wähle eine Aufgabe (z.B. E-Mail-Klassifikation) und löse sie mit Few-Shot-Prompting. Wie hoch ist die Accuracy? Würde Fine-Tuning helfen?

### Übung 2: Trainingsdaten erstellen
Erstelle 20 Trainingsdaten-Paare für eine Aufgabe deiner Wahl. Prüfe sie auf Konsistenz und Qualität.

### Übung 3: Kosten-Analyse
Berechne die Kosten für: 100.000 Anfragen/Monat, einmal mit Sonnet (mit langem System-Prompt) und einmal mit fine-tuned GPT-4o-mini (ohne System-Prompt). Was ist günstiger?

### Übung 4: Distillation
Wenn du API-Zugang hast: Generiere 50 Antworten mit einem großen Modell. Nutze sie als Few-Shot-Beispiele für ein kleines Modell. Wie nah kommt das kleine Modell?
