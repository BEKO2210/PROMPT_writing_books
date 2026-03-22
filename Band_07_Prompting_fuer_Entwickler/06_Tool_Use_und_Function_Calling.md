# Kapitel 6: Tool Use und Function Calling – KI greift in die echte Welt

Bisher generierte KI Text. Jetzt greift sie in die Welt ein: Datenbanken abfragen, APIs aufrufen, E-Mails senden, Dateien erstellen. Das ist Tool Use – und es verwandelt ein Sprachmodell in einen handlungsfähigen Agenten.

## Was ist Tool Use?

Du definierst Funktionen (Tools) mit Schema. Das Modell entscheidet, wann welches Tool aufgerufen wird, und generiert die Parameter. Du führst die Funktion aus und gibst das Ergebnis zurück. Das Modell verarbeitet das Ergebnis und antwortet dem User.

```
User: "Wie ist das Wetter in Berlin?"
      ↓
LLM entscheidet: Tool "get_weather" mit {"city": "Berlin"}
      ↓
Dein Code führt get_weather("Berlin") aus → {"temp": 12, "condition": "bewölkt"}
      ↓
LLM: "In Berlin sind es 12°C und bewölkt."
```

## Tool-Definition (Anthropic)

```python
import anthropic

client = anthropic.Anthropic()

tools = [
    {
        "name": "get_weather",
        "description": "Ruft die aktuelle Wettervorhersage für eine Stadt ab. "
                       "Nutze dieses Tool wenn der User nach Wetter fragt.",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name der Stadt, z.B. 'Berlin' oder 'München'"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperatur-Einheit. Default: celsius"
                }
            },
            "required": ["city"]
        }
    },
    {
        "name": "search_database",
        "description": "Durchsucht die Produktdatenbank nach Artikeln.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Suchbegriff"
                },
                "category": {
                    "type": "string",
                    "enum": ["electronics", "books", "clothing"],
                    "description": "Kategorie-Filter (optional)"
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximale Anzahl Ergebnisse (default: 5)",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    }
]
```

## Der Tool-Use-Loop

```python
import json

def process_tool_call(tool_name: str, tool_input: dict) -> str:
    """Führe das Tool aus und gib das Ergebnis zurück."""
    if tool_name == "get_weather":
        # Echte API-Call hier
        return json.dumps({
            "city": tool_input["city"],
            "temperature": 12,
            "condition": "bewölkt",
            "humidity": 65
        })
    elif tool_name == "search_database":
        # Echte DB-Query hier
        return json.dumps({
            "results": [
                {"name": "Laptop X", "price": 999},
                {"name": "Tablet Y", "price": 499}
            ],
            "total": 2
        })
    else:
        return json.dumps({"error": f"Unknown tool: {tool_name}"})


def chat_with_tools(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        # Wenn das Modell fertig ist (keine Tool-Calls mehr)
        if response.stop_reason == "end_turn":
            return next(
                block.text for block in response.content
                if block.type == "text"
            )

        # Tool-Calls verarbeiten
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = process_tool_call(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        # Antwort + Tool-Ergebnisse anhängen
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

# Nutzung
answer = chat_with_tools("Wie ist das Wetter in Berlin und München?")
# Das Modell ruft get_weather ZWEIMAL auf (einmal pro Stadt)
# und fasst die Ergebnisse zusammen.
```

## Tool-Design: Best Practices

### 1. Klare, präzise Beschreibungen

```python
# SCHLECHT:
{"name": "search", "description": "Sucht nach Sachen"}

# GUT:
{"name": "search_products",
 "description": "Durchsucht den Produktkatalog nach Artikeln. "
                "Gibt Name, Preis und Verfügbarkeit zurück. "
                "Nutze dieses Tool wenn der User nach Produkten, "
                "Preisen oder Verfügbarkeit fragt."}
```

### 2. Sinnvolle Parameter-Beschreibungen

```python
# SCHLECHT:
"query": {"type": "string"}

# GUT:
"query": {
    "type": "string",
    "description": "Suchbegriff. Kann Produktname, Kategorie oder "
                   "Beschreibung sein. Beispiele: 'rotes Kleid', 'iPhone 16', 'Geschenk unter 50€'"
}
```

### 3. Enums für begrenzte Optionen

```python
"status": {
    "type": "string",
    "enum": ["active", "inactive", "pending"],
    "description": "Filtere nach Status"
}
```

### 4. Wenige, mächtige Tools statt vieler kleiner

```python
# SCHLECHT: 10 einzelne Tools
"get_user_name", "get_user_email", "get_user_address", ...

# GUT: 1 flexibles Tool
"get_user_info": {
    "fields": {
        "type": "array",
        "items": {"enum": ["name", "email", "address", "phone"]},
        "description": "Welche Felder abgerufen werden sollen"
    }
}
```

## Parallele Tool-Calls

Claude und GPT können mehrere Tools gleichzeitig aufrufen:

```
User: "Vergleiche das Wetter in Berlin, München und Hamburg."

LLM generiert 3 parallele Tool-Calls:
  get_weather(city="Berlin")
  get_weather(city="München")
  get_weather(city="Hamburg")

→ Alle 3 werden gleichzeitig ausgeführt
→ LLM bekommt alle 3 Ergebnisse auf einmal
→ Fasst in einer Antwort zusammen
```

## Sicherheit bei Tool Use

### Bestätigungen für kritische Aktionen

```python
# Tool-Definition mit Sicherheitsstufe
critical_tools = {
    "delete_user": "CRITICAL",      # Immer bestätigen
    "send_email": "CONFIRM",        # User fragen
    "search_database": "SAFE",      # Automatisch ausführen
}

def process_tool_call_safe(tool_name, tool_input):
    level = critical_tools.get(tool_name, "CONFIRM")

    if level == "CRITICAL":
        raise PermissionError(f"Tool '{tool_name}' benötigt Admin-Bestätigung")
    elif level == "CONFIRM":
        # User um Bestätigung bitten
        print(f"Tool: {tool_name}, Input: {tool_input}")
        if input("Ausführen? (y/n): ") != "y":
            return '{"status": "cancelled_by_user"}'

    return process_tool_call(tool_name, tool_input)
```

### Input-Validierung

```python
from pydantic import BaseModel, validator

class WeatherInput(BaseModel):
    city: str
    unit: str = "celsius"

    @validator("city")
    def validate_city(cls, v):
        # Keine SQL-Injection, keine Pfadangaben
        if any(c in v for c in [";", "'", "/", "\\"]):
            raise ValueError("Ungültiger Stadtname")
        return v

    @validator("unit")
    def validate_unit(cls, v):
        if v not in ["celsius", "fahrenheit"]:
            raise ValueError("Ungültige Einheit")
        return v
```

## Tool Use in der Praxis

### Beispiel: Kunden-Support-Bot

```python
support_tools = [
    {
        "name": "lookup_order",
        "description": "Suche eine Bestellung nach Bestellnummer oder Kundennummer.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "customer_id": {"type": "string"}
            }
        }
    },
    {
        "name": "check_inventory",
        "description": "Prüfe die Verfügbarkeit eines Produkts.",
        "input_schema": {
            "type": "object",
            "properties": {
                "product_id": {"type": "string"},
                "quantity": {"type": "integer", "default": 1}
            },
            "required": ["product_id"]
        }
    },
    {
        "name": "create_ticket",
        "description": "Erstelle ein Support-Ticket für komplexe Anliegen.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string"},
                "description": {"type": "string"},
                "priority": {"type": "string", "enum": ["low", "medium", "high"]},
                "customer_id": {"type": "string"}
            },
            "required": ["subject", "description", "priority"]
        }
    }
]
```

---

## Übungen

### Übung 1: Eigenes Tool
Definiere ein Tool für einen Anwendungsfall deiner Wahl. Implementiere den Tool-Use-Loop.

### Übung 2: Multi-Tool
Erstelle 3 Tools, die zusammenarbeiten (z.B. Suche → Details → Bestellung). Lass das Modell sie in der richtigen Reihenfolge aufrufen.

### Übung 3: Sicherheit
Implementiere eine Sicherheitsschicht, die kritische Tool-Calls blockiert oder bestätigen lässt.

### Übung 4: Parallele Calls
Teste parallele Tool-Calls: Lass das Modell 5 verschiedene Informationen gleichzeitig abrufen.
