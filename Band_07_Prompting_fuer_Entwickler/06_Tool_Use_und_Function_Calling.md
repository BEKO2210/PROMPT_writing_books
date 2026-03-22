# Kapitel 6: Tool Use und Function Calling – KI greift in die echte Welt

Bisher generierte KI Text. Jetzt greift sie in die Welt ein: Datenbanken abfragen, APIs aufrufen, E-Mails senden, Dateien erstellen. Das ist Tool Use – und es verwandelt ein Sprachmodell in einen handlungsfähigen Agenten.

## Was ist Tool Use?

Du definierst Funktionen (Tools) mit Schema. Das Modell entscheidet, wann welches Tool aufgerufen wird, und generiert die Parameter. Du führst die Funktion aus und gibst das Ergebnis zurück. Das Modell verarbeitet das Ergebnis und antwortet dem User.

```
User: "Wie ist das Wetter in Berlin?"
      ↓
LLM entscheidet: Tool "get_weather" mit {"city": "Berlin"}
      ↓
Dein Code führt get_weather("Berlin") aus → {"temp": 12}
      ↓
LLM: "In Berlin sind es 12°C und bewölkt."
```

## Tool-Definition

Ein Tool besteht aus drei Teilen: **Name**, **Beschreibung** und **Input-Schema** (JSON-Schema). Das sieht so aus:

```python
tools = [{
    "name": "get_weather",
    "description": "Ruft das Wetter für eine Stadt ab. "
                   "Nutze dieses Tool wenn der User nach Wetter fragt.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "Stadtname"},
            "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["city"]
    }
}]
```

Bei OpenAI heißt das `functions` statt `tools`, die Struktur ist fast identisch. Bei Google `function_declarations`.

## Der Tool-Use-Loop

Das Herzstück: Eine Schleife, die so lange läuft, bis das Modell keine Tools mehr aufruft:

1. Sende Message an LLM (mit Tools)
2. Wenn `stop_reason == "end_turn"` → fertig, gib Text zurück
3. Wenn Tool-Call → führe Tool aus, hänge Ergebnis an Messages
4. Zurück zu Schritt 1

Das Modell kann dabei **mehrere Tools gleichzeitig** aufrufen (parallele Tool-Calls). Bei "Vergleiche das Wetter in Berlin, München und Hamburg" generiert es drei `get_weather`-Calls auf einmal.

## Tool-Design: Best Practices

### 1. Klare, präzise Beschreibungen

- **Schlecht:** `"Sucht nach Sachen"`
- **Gut:** `"Durchsucht den Produktkatalog. Gibt Name, Preis und Verfügbarkeit zurück. Nutze dieses Tool wenn der User nach Produkten oder Preisen fragt."`

Die Beschreibung ist das Wichtigste. Das Modell entscheidet anhand der Beschreibung, ob es ein Tool nutzt.

### 2. Parameter-Beschreibungen mit Beispielen

Nicht nur den Typ angeben, sondern erklären was erwartet wird: `"Suchbegriff. Kann Produktname, Kategorie oder Beschreibung sein. Beispiele: 'rotes Kleid', 'iPhone 16'"`.

### 3. Enums für begrenzte Optionen

Wenn ein Parameter nur bestimmte Werte annehmen kann, nutze `enum`. Das verhindert ungültige Eingaben und hilft dem Modell.

### 4. Wenige, mächtige Tools statt vieler kleiner

Statt 10 einzelne Tools (`get_user_name`, `get_user_email`, ...) lieber ein flexibles `get_user_info` mit einem `fields`-Array. Weniger Tools = weniger Kontext-Verbrauch = bessere Tool-Auswahl.

## Sicherheit bei Tool Use

### Bestätigungen für kritische Aktionen

Jedes Tool bekommt eine Sicherheitsstufe:

- **SAFE** (z.B. `search_database`) → automatisch ausführen
- **CONFIRM** (z.B. `send_email`) → User fragen
- **CRITICAL** (z.B. `delete_user`) → Admin-Bestätigung nötig

### Input-Validierung

Nie die LLM-generierten Parameter blind an dein System weiterreichen. Validiere mit Pydantic oder eigenen Checks: Keine SQL-Injection-Zeichen in Stadtname, keine Pfadangaben wo keine hingehören, Enum-Werte prüfen.

## Tool Use in der Praxis

Ein typischer **Kunden-Support-Bot** hat drei bis fünf Tools:

- `lookup_order` – Bestellung nachschlagen
- `check_inventory` – Verfügbarkeit prüfen
- `create_ticket` – Support-Ticket erstellen

Jedes Tool mit klarem Schema, sinnvollen Defaults und Required-Feldern. Das Modell wählt selbstständig das richtige Tool basierend auf der User-Frage.

---

## Übungen

### Übung 1: Eigenes Tool
Definiere ein Tool für einen Anwendungsfall deiner Wahl. Implementiere den Tool-Use-Loop.

### Übung 2: Multi-Tool
Erstelle 3 Tools, die zusammenarbeiten (z.B. Suche → Details → Bestellung).

### Übung 3: Sicherheit
Implementiere eine Sicherheitsschicht mit Bestätigungen für kritische Tool-Calls.

### Übung 4: Parallele Calls
Teste parallele Tool-Calls: Lass das Modell 5 verschiedene Informationen gleichzeitig abrufen.
