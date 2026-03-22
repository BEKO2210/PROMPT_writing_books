# Kapitel 9: Context Engineering – Die Evolution des Prompt Engineering

Prompt Engineering war Band 1. Context Engineering ist Band 7.

Der Unterschied: Prompt Engineering optimiert den Text, den du an ein LLM schickst. Context Engineering optimiert *alles*, was das Modell sieht – System-Prompt, Tools, Retrieval-Ergebnisse, Konversationshistorie, Caching, und wie all diese Teile zusammenspielen.

## Was ist Context Engineering?

Jeder API-Call an ein LLM hat mehrere Kontextschichten:

```
┌─────────────────────────────────────────┐
│           MODEL CONTEXT WINDOW          │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     1. SYSTEM-PROMPT             │   │
│  │     - Rolle und Verhalten        │   │
│  │     - Regeln und Einschränkungen │   │
│  │     - Output-Format              │   │
│  └──────────────────────────────────┘   │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     2. TOOL-DEFINITIONEN         │   │
│  │     - Verfügbare Tools + Schema  │   │
│  │     - Beschreibungen             │   │
│  └──────────────────────────────────┘   │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     3. RETRIEVAL-KONTEXT (RAG)   │   │
│  │     - Relevante Dokumente        │   │
│  │     - Suchergebnisse             │   │
│  └──────────────────────────────────┘   │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     4. KONVERSATIONSHISTORIE     │   │
│  │     - Bisherige Messages         │   │
│  │     - Tool-Ergebnisse            │   │
│  └──────────────────────────────────┘   │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │     5. AKTUELLE NACHRICHT        │   │
│  │     - User-Prompt                │   │
│  └──────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

Context Engineering optimiert jede dieser Schichten – und ihr Zusammenspiel.

## Schicht 1: System-Prompt Engineering

### Die Anatomie eines Produktions-System-Prompts

```python
SYSTEM_PROMPT = """
# Rolle
Du bist der Kundenservice-Assistent von TechCorp.
Du hilfst Kunden mit Fragen zu unseren Produkten und Services.

# Verhalten
- Antworte auf Deutsch
- Duze die Kunden
- Sei freundlich, aber effizient – keine unnötigen Floskeln
- Wenn du die Antwort nicht weißt: Sage es ehrlich und leite an den menschlichen Support weiter

# Fähigkeiten
- Du kannst Bestellungen nachschlagen (Tool: lookup_order)
- Du kannst den Bestellstatus prüfen (Tool: check_status)
- Du kannst Rückgaben einleiten (Tool: initiate_return)
- Du kannst KEINE Zahlungen verarbeiten oder Preise ändern

# Einschränkungen
- Gib NIEMALS interne Systeminfos preis
- Diskutiere NICHT über Wettbewerber
- Versprich KEINE Rabatte oder Sonderkonditionen
- Bei technischen Problemen: Erstelle ein Ticket, versuche nicht selbst zu debuggen

# Kontext
- Heute ist {date}
- Aktuelle Promotions: {current_promotions}
- Bekannte Probleme: {known_issues}

# Output-Format
- Kurze, klare Antworten (max. 3 Absätze)
- Bei Schritt-für-Schritt-Anleitungen: Nummerierte Liste
- Bei mehreren Optionen: Bullet Points
"""
```

### System-Prompt-Patterns

**Pattern 1: Identity + Constraints**
```
Wer bist du? → Rolle, Name, Expertise
Was kannst du? → Fähigkeiten, Tools
Was kannst du NICHT? → Grenzen, Verbote
```

**Pattern 2: Dynamic Context**
```python
# Kontext, der sich bei jedem Call ändert
system = f"""
Aktuelles Datum: {datetime.now().strftime('%d.%m.%Y')}
Benutzer: {user.name} (Kunde seit {user.since}, Plan: {user.plan})
Letzte Interaktion: {user.last_interaction}
Offene Tickets: {user.open_tickets}
"""
```

**Pattern 3: Graduated Response**
```
Für einfache Fragen: Antworte direkt (1-2 Sätze)
Für mittlere Fragen: Antworte mit Erklärung (1 Absatz)
Für komplexe Fragen: Antworte strukturiert (Überschriften, Listen)
Für Fragen außerhalb deines Wissens: Leite weiter
```

## Schicht 2: Tool-Kontext-Optimierung

Die Beschreibungen deiner Tools sind Teil des Kontexts – und sie beeinflussen stark, wie gut das Modell die Tools nutzt.

### Schlechte Tool-Beschreibung
```
"name": "search"
"description": "Sucht Dinge"
```
→ Modell weiß nicht, wann es das Tool nutzen soll.

### Gute Tool-Beschreibung
```
"name": "search_knowledge_base"
"description": "Durchsucht die interne Wissensdatenbank von TechCorp.
Enthält: Produktdokumentation, FAQ, Troubleshooting-Guides, Prozessbeschreibungen.
Enthält NICHT: Bestelldaten, Kundendaten, Finanzdaten.
Nutze dieses Tool BEVOR du eine Frage beantwortest, die spezifisches Produktwissen erfordert.
Beispiel-Queries: 'Rückgabe einleiten', 'Garantiebedingungen Laptop Pro', 'Passwort zurücksetzen'"
```

## Schicht 3: RAG-Kontext-Optimierung

### Kontext-Reihenfolge

Die Reihenfolge der Chunks im Kontext beeinflusst die Qualität:

```python
# Am relevantesten zuerst (Primacy Bias)
# ODER am relevantesten zuletzt (Recency Bias)
# Empfehlung: Am relevantesten zuerst UND zuletzt

def arrange_context(chunks, query):
    # Sortiere nach Relevanz
    ranked = sorted(chunks, key=lambda c: c.similarity, reverse=True)

    if len(ranked) <= 3:
        return ranked

    # Bestes am Anfang, zweitbestes am Ende
    return [ranked[0]] + ranked[2:] + [ranked[1]]
```

### Kontext-Kompression

Zu viel Kontext ist schlechter als zu wenig:

```python
# Vor dem Einfügen in den Prompt: Zusammenfassen
summary = client.messages.create(
    model="claude-haiku-3-5-20241022",
    max_tokens=200,
    messages=[{
        "role": "user",
        "content": f"Fasse die für diese Frage relevanten Informationen zusammen:\n\nFrage: {question}\n\nDokument:\n{chunk}"
    }]
).content[0].text
```

## Schicht 4: Konversationshistorie managen

### Problem: Kontext-Fenster voll

Lange Konversationen sprengen das Kontext-Fenster. Strategien:

```python
class ConversationManager:
    def __init__(self, max_messages=20, max_tokens=50000):
        self.messages = []
        self.max_messages = max_messages
        self.max_tokens = max_tokens

    def add_and_trim(self, message):
        self.messages.append(message)

        # Strategie 1: Älteste entfernen
        while len(self.messages) > self.max_messages:
            self.messages.pop(1)  # Index 0 = System, behalten

        # Strategie 2: Zusammenfassen statt entfernen
        if self.estimate_tokens() > self.max_tokens:
            self._summarize_old_messages()

    def _summarize_old_messages(self):
        old = self.messages[1:-4]  # Mittlere Messages
        summary = summarize_conversation(old)
        self.messages = (
            [self.messages[0]]  # System
            + [{"role": "user", "content": f"[Zusammenfassung bisheriger Konversation: {summary}]"}]
            + self.messages[-4:]  # Letzte 4 Messages
        )
```

## Schicht 5: Prompt Caching

Anthropics Prompt Caching ist eine der mächtigsten Optimierungen:

```python
# Ohne Caching: 200K Token System-Prompt = teuer bei JEDEM Call
# Mit Caching: Erster Call zahlt voll, alle weiteren 90% günstiger

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": LONG_SYSTEM_PROMPT,  # z.B. 50.000 Token
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": user_question}]
)

# Cache-Statistiken prüfen
print(f"Cache Write: {message.usage.cache_creation_input_tokens}")
print(f"Cache Read:  {message.usage.cache_read_input_tokens}")
# Erster Call: Cache Write = 50.000, Cache Read = 0
# Zweiter Call: Cache Write = 0, Cache Read = 50.000 (90% günstiger!)
```

### Was cachen?

| Kontext-Teil | Cachen? | Warum |
|---|---|---|
| System-Prompt | ✅ Immer | Ändert sich selten |
| Tool-Definitionen | ✅ Immer | Ändert sich nie |
| RAG-Dokumente | ⚠️ Manchmal | Nur wenn wiederholt dieselben Docs |
| Konversationshistorie | ✅ Ja | Prefix bleibt gleich, nur neue Messages kommen dazu |
| User-Prompt | ❌ Nein | Ändert sich bei jedem Call |

## Context Engineering Checkliste

Für jeden produktionsreifen LLM-Call prüfe:

### System-Prompt
- [ ] Rolle klar definiert?
- [ ] Fähigkeiten und Grenzen explizit?
- [ ] Dynamischer Kontext (Datum, User-Info) eingefügt?
- [ ] Output-Format spezifiziert?
- [ ] Gecacht?

### Tools
- [ ] Beschreibungen detailliert genug?
- [ ] Beispiele in den Beschreibungen?
- [ ] Negative Beispiele ("Nutze dieses Tool NICHT für...")?
- [ ] Gecacht?

### RAG
- [ ] Relevante Chunks ausgewählt (nicht zu viele)?
- [ ] Reranking angewandt?
- [ ] Quellen referenzierbar?
- [ ] Kontext-Reihenfolge optimiert?

### History
- [ ] Alte Messages zusammengefasst oder getrimmt?
- [ ] Token-Budget eingehalten?
- [ ] Prefix gecacht?

### Prompt
- [ ] Klar und eindeutig?
- [ ] Alle nötigen Informationen enthalten?
- [ ] Nicht zu lang?

## Von Prompt Engineering zu Context Engineering

| Prompt Engineering | Context Engineering |
|---|---|
| "Wie schreibe ich den Prompt?" | "Wie designe ich den gesamten Kontext?" |
| Einzelner Text-Input | System + Tools + RAG + History + Prompt |
| Statisch | Dynamisch (ändert sich pro User, pro Anfrage) |
| Trial and Error | Systematisch, messbar, versioniert |
| Ein Skill | Eine Disziplin |

Context Engineering ist die Zukunft. Wer nur Prompts schreibt, schöpft 20% des Potenzials aus. Wer den gesamten Kontext designt, schöpft 100% aus.

---

## Übungen

### Übung 1: System-Prompt Audit
Nimm einen bestehenden System-Prompt und prüfe ihn gegen die Checkliste. Was fehlt?

### Übung 2: Caching implementieren
Implementiere Prompt Caching für einen Anwendungsfall mit langem System-Prompt. Miss den Kostenunterschied.

### Übung 3: Konversationsmanager
Baue einen ConversationManager mit Zusammenfassungs-Strategie. Teste: Behält das Modell den Kontext?

### Übung 4: Full Context Design
Designe den kompletten Kontext für einen produktionsreifen Chatbot: System-Prompt, Tools, RAG-Integration, History-Management, Caching. Dokumentiere jede Entscheidung.
