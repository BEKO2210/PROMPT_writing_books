# Kapitel 1: Code-Generierung mit KI – Von der Funktion zum System

"Schreib mir eine Python-Funktion, die prüft, ob eine Zahl eine Primzahl ist." Das kann jeder. Und es ist ungefähr so nützlich wie "Schreib mir ein Gedicht über Liebe" – du bekommst ein generisches Ergebnis, das meistens funktioniert, aber selten genau das ist, was du brauchst.

In diesem Kapitel lernst du, wie du KI für professionelle Software-Entwicklung nutzt – von der Einzelfunktion bis zur Systemarchitektur.

## Warum die meisten Code-Prompts schlecht sind

### Problem 1: Zu wenig Kontext

```
SCHLECHT:
"Schreib eine Login-Funktion."

GUT:
"Schreib eine Login-Funktion für eine Express.js-API.
Tech-Stack: Node.js 22, TypeScript 5.4, PostgreSQL mit Prisma ORM.
Auth: JWT mit Access + Refresh Token (RS256).
Passwort-Hashing: bcrypt, 12 Rounds.
Rate Limiting: Max. 5 Versuche pro 15 Min pro IP.
Input-Validierung: Zod-Schema.
Error Handling: Custom AppError-Klasse mit HTTP-Statuscodes.
Logging: Pino-Logger, keine sensiblen Daten loggen."
```

### Problem 2: Kein existierender Codebase-Kontext

KI weiß nicht, wie dein Projekt aufgebaut ist. Ohne Kontext schreibt sie Code, der nicht in dein Projekt passt.

```
Hier ist mein Projekt-Kontext:

ARCHITEKTUR: Hexagonal Architecture (Ports & Adapters)
ORDNERSTRUKTUR:
  src/
    domain/       # Business-Logik, Entities, Value Objects
    application/  # Use Cases, Ports (Interfaces)
    infrastructure/ # Adapter (DB, API, etc.)
    api/          # REST Controller, DTOs

KONVENTIONEN:
- Error Handling über Result-Type (kein throw)
- Dependency Injection via Constructor
- Alle DB-Zugriffe über Repository-Interfaces
- Tests: Vitest, AAA-Pattern, keine Mocks für Domain-Logik

Schreibe [AUFGABE] so, dass sie in diese Architektur passt.
```

### Problem 3: Keine Qualitätsanforderungen

```
SCHLECHT:
"Schreib eine Funktion zum Sortieren."

GUT:
"Schreib eine Sortierfunktion mit folgenden Anforderungen:
- TypeScript, generisch (funktioniert mit jedem Typ)
- Stabile Sortierung
- O(n log n) im Average Case
- Immutable: Gibt neues Array zurück, verändert das Original nicht
- Vergleichsfunktion als Parameter (wie Array.sort)
- JSDoc-Dokumentation
- Edge Cases: Leeres Array, ein Element, bereits sortiert
- Unit Tests mit Vitest (min. 5 Testfälle)"
```

## Der professionelle Code-Prompt

Mein Framework für Code-Generierung:

```
AUFGABE: [Was soll gebaut werden?]
KONTEXT: [Wo wird es eingebaut? Existierender Code?]
TECH-STACK: [Sprache, Framework, Versionen]
ARCHITEKTUR: [Patterns, Strukturen, Konventionen]

ANFORDERUNGEN:
- Funktional: [Was muss es tun?]
- Nicht-funktional: [Performance, Sicherheit, Skalierbarkeit]
- Edge Cases: [Was kann schiefgehen?]

QUALITÄT:
- Error Handling: [Strategie]
- Logging: [Was loggen, was nicht?]
- Tests: [Test-Framework, Testfälle]
- Dokumentation: [JSDoc/Docstring/README]

EINSCHRÄNKUNGEN:
- [Was NICHT verwenden: bestimmte Libraries, Patterns]
- [Max. Dateigröße, Komplexität]
- [Kompatibilität: Browser, Node-Versionen]
```

## Code-Generierung nach Aufgabentyp

### Neue Features implementieren

```
Implementiere folgendes Feature:

FEATURE: [Beschreibung]
USER STORY: "Als [Rolle] möchte ich [Aktion],
damit [Nutzen]."
AKZEPTANZKRITERIEN:
1. [Kriterium 1]
2. [Kriterium 2]
3. [Kriterium 3]

EXISTIERENDER CODE:
"""[Relevante Code-Abschnitte einfügen]"""

DATENMODELL: [Welche Daten sind beteiligt?]

IMPLEMENTIERE:
1. Datenbank-Migration (wenn nötig)
2. Backend-Logik (Service + Repository)
3. API-Endpoint (Controller + Validierung)
4. Tests (Unit + Integration)

Keine Frontend-Änderungen in diesem PR.
```

### Bugs fixen

```
BUG: [Beschreibung des Problems]
ERWARTETES VERHALTEN: [Was sollte passieren?]
TATSÄCHLICHES VERHALTEN: [Was passiert stattdessen?]
REPRODUKTION: [Schritte zum Reproduzieren]

FEHLERMELDUNG:
"""[Error-Log einfügen]"""

RELEVANTER CODE:
"""[Code-Abschnitt einfügen]"""

AUFGABE:
1. Identifiziere die Ursache (Root Cause Analysis)
2. Schlage einen Fix vor (erkläre warum)
3. Implementiere den Fix
4. Schreibe einen Regressions-Test, der den Bug abdeckt
5. Prüfe: Kann der Fix andere Stellen beeinflussen?
```

### Refactoring

```
Refactore folgenden Code:

"""[Code einfügen]"""

ZIEL: [z.B. Lesbarkeit, Performance, Testbarkeit,
Separation of Concerns, DRY]

REGELN:
- Verhalten darf sich NICHT ändern (pure Refactoring)
- Existierende Tests müssen weiterhin grün sein
- Keine neuen Dependencies einführen
- Commits in logische Schritte aufteilen

ERKLÄRE für jede Änderung:
- Was wurde geändert?
- Warum?
- Welches Design-Pattern wurde angewandt?
```

### Code Reviews

```
Reviewe folgenden Code:

"""[Code einfügen / PR-Diff]"""

PRÜFE AUF:
1. KORREKTHEIT: Tut der Code, was er soll?
2. SICHERHEIT: SQL Injection, XSS, Auth-Lücken?
3. PERFORMANCE: N+1 Queries? Unnötige Berechnungen?
4. LESBARKEIT: Verständliche Variablennamen? Kommentare nötig?
5. FEHLERBEHANDLUNG: Werden Fehler abgefangen und sinnvoll behandelt?
6. TESTS: Ausreichend abgedeckt? Edge Cases?
7. KONVENTIONEN: Passt es zum Rest des Projekts?

FORMAT:
Für jedes Finding:
- Datei + Zeile
- Schwere: 🔴 Blocker / 🟡 Verbesserung / 🟢 Nitpick
- Problem
- Vorgeschlagener Fix
```

### Test-Generierung

```
Schreibe Tests für folgenden Code:

"""[Code einfügen]"""

TEST-FRAMEWORK: [Jest/Vitest/pytest/Go testing/...]
TEST-ARTEN:
- Unit Tests (isoliert, gemockte Dependencies)
- Integration Tests (mit DB/API)
- Edge Case Tests

NAMING: describe/it-Pattern (BDD-Style)
PATTERN: Arrange-Act-Assert (AAA)

ABDECKUNG:
- Happy Path (normaler Ablauf)
- Error Cases (was kann schiefgehen?)
- Boundary Values (Grenzwerte)
- Null/Undefined/Empty
- Concurrent Access (wenn relevant)

Mindestens [X] Testfälle. Ziel: >90% Branch Coverage.
```

## Architektur-Prompts

### System Design

```
Designe die Architektur für folgendes System:

SYSTEM: [Beschreibung]
ANFORDERUNGEN:
- Funktional: [Was muss es können?]
- Nicht-funktional:
  - Erwartete Last: [Requests/Sekunde]
  - Verfügbarkeit: [99.9%? 99.99%?]
  - Latenz: [P95 < Xms]
  - Datenmenge: [Wie viel Daten?]
  - Compliance: [DSGVO? PCI-DSS?]

ERSTELLE:
1. High-Level-Architektur (Komponenten + Interaktion)
2. Datenfluss (Wie fließen Daten durch das System?)
3. Datenmodell (Entitäten, Beziehungen)
4. API-Design (Endpoints, Verben, Payloads)
5. Technologie-Empfehlung (mit Begründung)
6. Trade-offs (Was gewinnen wir? Was verlieren wir?)
7. Skalierungsstrategie (Wie wächst das System?)
```

### Datenbank-Design

```
Designe ein Datenbankschema für [ANWENDUNG].

DATENBANK: [PostgreSQL/MySQL/MongoDB/...]
ENTITIES: [Liste der Entitäten]

FÜR JEDE ENTITY:
- Felder (Name, Typ, Constraints)
- Beziehungen (1:1, 1:N, N:M)
- Indizes (für erwartete Queries)

BERÜCKSICHTIGE:
- Normalisierung (3. Normalform oder bewusste Denormalisierung?)
- Soft Deletes (deleted_at statt physischem Löschen?)
- Audit-Trail (created_at, updated_at, created_by)
- Multi-Tenancy (wenn relevant)

ERSTELLE:
1. ER-Diagramm (als Text/Mermaid)
2. SQL CREATE TABLE Statements
3. Migrations-Dateien (für [Prisma/TypeORM/Alembic/...])
4. Seed-Daten (Testdaten)
```

## Sprach-spezifische Tipps

### Python
```
STIL: PEP 8, Type Hints (Python 3.12+), f-Strings
IMPORTS: Absolute Imports, keine Star-Imports
ASYNC: asyncio mit async/await wenn I/O-bound
DATENKLASSEN: Pydantic v2 für Validierung, dataclass für interne Strukturen
TESTING: pytest, parametrize für Varianten, fixtures für Setup
```

### TypeScript
```
STIL: strict Mode, kein any, keine type assertions (as)
IMPORTS: Named Imports, Barrel-Files sparsam
ASYNC: Promises, async/await, keine Callbacks
VALIDIERUNG: Zod für Runtime-Validierung, TypeScript für Compile-Time
TESTING: Vitest, describe/it, expect-Syntax
LINTING: ESLint + Prettier (konfiguriert)
```

### Go
```
STIL: gofmt, Effective Go, keine generischen Interface{}-Typen
ERROR HANDLING: Explicit error returns (if err != nil), keine panic()
CONCURRENCY: Goroutines + Channels, context.Context für Cancellation
TESTING: table-driven tests, testify für Assertions
STRUCTURE: cmd/ pkg/ internal/ nach Standard Go Layout
```

### Rust
```
STIL: clippy, rustfmt, idiomatic Rust
ERROR HANDLING: Result<T, E>, thiserror für Custom Errors, anyhow für Applications
OWNERSHIP: Borrowing statt Cloning wo möglich
ASYNC: tokio Runtime, async/await
TESTING: #[cfg(test)], unit tests im gleichen File, integration tests in tests/
```

## Anti-Patterns in der Code-Generierung

### Anti-Pattern 1: Blind Copy-Paste

KI-generierter Code kann Bugs enthalten. Immer reviewen, nie blind einfügen.

### Anti-Pattern 2: Zu große Prompts

"Schreib mir die komplette Anwendung" → funktioniert nicht. Bau sie Modul für Modul.

### Anti-Pattern 3: Keine Iteration

Der erste Output ist selten perfekt. Iteriere:
```
"Der Code funktioniert, aber:
1. Die Error-Messages sind zu generisch
2. Das Logging fehlt
3. Die Funktion ist zu lang (>50 Zeilen)
Verbessere diese 3 Punkte."
```

### Anti-Pattern 4: KI-Code nicht testen

KI-generierter Code muss genauso (oder strenger) getestet werden wie handgeschriebener Code. Vertraue nicht – verifiziere.

### Anti-Pattern 5: Veraltete Patterns akzeptieren

KI-Modelle haben Wissens-Cutoffs. Code-Patterns können veraltet sein. Prüfe:
- Werden aktuelle API-Versionen verwendet?
- Sind deprecated Methoden im Code?
- Entspricht der Code aktuellen Best Practices?

---

## Übungen

### Übung 1: Der volle Code-Prompt
Wähle eine Aufgabe aus deinem Arbeitsalltag und schreibe einen vollständigen Code-Prompt (Aufgabe, Kontext, Tech-Stack, Architektur, Anforderungen, Qualität). Vergleiche das Ergebnis mit einem einfachen "Schreib mir X"-Prompt.

### Übung 2: Code Review
Nimm ein eigenes Code-Stück (oder Open-Source-Code) und lass es reviewen. Stimmen die Findings? Gibt es False Positives?

### Übung 3: Test-Generierung
Lass für eine bestehende Funktion Tests generieren. Laufen sie? Decken sie die wichtigen Edge Cases ab?

### Übung 4: Bug-Analyse
Nimm einen echten Bug (z.B. aus einem GitHub Issue) und lass die KI eine Root Cause Analysis durchführen. Liegt sie richtig?
