# Code & Entwicklung

## Feature implementieren

```
Implementiere folgendes Feature:
"""[FEATURE-BESCHREIBUNG]"""

Technologie: [SPRACHE/FRAMEWORK]
Bestehender Code-Kontext: [RELEVANTE DATEIEN/ARCHITEKTUR]

Anforderungen:
- Typisiert (TypeScript/Python Type Hints)
- Fehlerbehandlung
- Edge Cases berücksichtigen
- Tests (Unit + ggf. Integration)
- Dokumentation (JSDoc/Docstring)
```

## Bug fixen

```
Bug: [BESCHREIBUNG DES FEHLVERHALTENS]
Erwartet: [WAS SOLLTE PASSIEREN]
Tatsächlich: [WAS PASSIERT STATTDESSEN]
Reproduzieren: [SCHRITTE]

Relevanter Code:
"""[CODE EINFÜGEN]"""

Finde die Ursache, erkläre sie, und liefere den Fix.
Bonus: Wie hätte der Bug verhindert werden können?
```

## Code Review

```
Reviewe folgenden Code:
"""[CODE EINFÜGEN]"""

Prüfe auf:
1. Korrektheit (Logik, Edge Cases)
2. Lesbarkeit (Benennung, Struktur)
3. Performance (Bottlenecks, unnötige Operationen)
4. Sicherheit (Injection, XSS, Secrets)
5. Best Practices der Sprache

Format: Problem → Warum problematisch → Verbesserung.
```

## Refactoring

```
Refactore folgenden Code:
"""[CODE]"""

Ziel: [Lesbarkeit/Performance/Testbarkeit/Modularität]

Regeln:
- Funktionalität NICHT ändern
- Schritt für Schritt, nicht alles auf einmal
- Jeden Schritt erklären
- Vorher/Nachher zeigen
```

## Tests schreiben

```
Schreibe Tests für:
"""[CODE/FUNKTION]"""

Framework: [Jest/Pytest/Go Test/JUnit]
Abdeckung:
- Happy Path (Normalfall)
- Edge Cases (Grenzwerte, leere Inputs)
- Error Cases (ungültige Inputs, Exceptions)
- Grenzwerte (0, -1, MAX_INT, leerer String, null)

Mindestens [X] Testfälle. Beschreibende Testnamen.
```

## API-Endpunkt designen

```
Designe einen REST-API-Endpunkt.
Ressource: [WAS WIRD VERWALTET]
Operationen: [CRUD oder spezifische Aktionen]

Für jeden Endpunkt:
- HTTP-Methode + URL
- Request-Body (JSON-Schema)
- Response (Erfolg + Fehler)
- Authentifizierung
- Rate Limiting
- Beispiel-Requests (curl)

Folge REST-Konventionen. Versionierung beachten.
```

## Datenbank-Schema

```
Designe ein Datenbankschema für [ANWENDUNG].
Anforderungen: [FEATURE-LISTE]
Datenbank: [PostgreSQL/MySQL/MongoDB]

Erstelle:
1. Entitäten und ihre Attribute
2. Beziehungen (1:1, 1:N, N:M)
3. SQL CREATE TABLE Statements
4. Indizes (für häufige Queries)
5. Beispiel-Queries für die 3 häufigsten Use Cases
```

## Git Commit Message

```
Hier sind meine Änderungen:
"""[GIT DIFF ODER BESCHREIBUNG]"""

Schreibe eine Commit Message nach Conventional Commits:
type(scope): kurze Beschreibung

Body: Was und WARUM (nicht WIE – das sieht man im Diff).
Types: feat, fix, refactor, docs, test, chore, perf.
Max. 72 Zeichen Betreff. Body bei Bedarf.
```

## README schreiben

```
Schreibe eine README.md für [PROJEKT].
Sprache/Framework: [TECH STACK]
Zweck: [WAS TUT DAS PROJEKT]

Struktur:
1. Projekt-Name + 1-Satz-Beschreibung
2. Features (Bullet Points)
3. Installation (Schritt für Schritt)
4. Nutzung (Beispiele)
5. Konfiguration (Env Vars, Optionen)
6. Beitragen (Contribution Guide)
7. Lizenz
```

## Architektur-Entscheidung

```
Ich muss eine Architektur-Entscheidung treffen.
Problem: [WAS MUSS GELÖST WERDEN]
Optionen:
A: [OPTION A]
B: [OPTION B]
C: [OPTION C]

Kontext: [TEAM-GRÖSSE, BUDGET, TIMELINE, BESTEHENDE SYSTEME]

Vergleiche nach: Komplexität, Skalierbarkeit, Kosten,
Wartbarkeit, Time-to-Market, Team-Expertise.
ADR-Format (Architecture Decision Record).
```

## Code erklären

```
Erkläre folgenden Code Zeile für Zeile:
"""[CODE]"""

Zielgruppe: [Junior-Entwickler/Nicht-Techniker/Selbst]
Erkläre: Was tut jede Zeile? Warum so und nicht anders?
Welche Konzepte werden verwendet?
Wo sind potenzielle Probleme?
```

## Performance optimieren

```
Dieser Code ist zu langsam:
"""[CODE]"""

Aktuelle Performance: [METRIK, z.B. 5s für 10k Records]
Ziel: [METRIK, z.B. unter 500ms]

Analysiere:
1. Wo sind die Bottlenecks?
2. Quick Wins (wenig Aufwand, großer Effekt)
3. Größere Optimierungen (mehr Aufwand)
4. Optimierter Code mit Erklärung
5. Tradeoffs (Lesbarkeit vs. Performance)
```

## Regex erstellen

```
Erstelle einen Regex für: [WAS SOLL GEFUNDEN WERDEN]
Sprache/Engine: [JavaScript/Python/PCRE]

Beispiele, die matchen sollen: [BEISPIELE]
Beispiele, die NICHT matchen sollen: [GEGENBEISPIELE]

Liefere:
1. Den Regex
2. Erklärung jedes Teils
3. Test mit allen Beispielen
4. Edge Cases, die du bedacht hast
```

## Docker-Setup

```
Erstelle ein Docker-Setup für [ANWENDUNG].
Tech Stack: [SPRACHE, FRAMEWORK, DATENBANK]
Umgebung: [Entwicklung/Produktion/Beides]

Erstelle:
1. Dockerfile (Multi-Stage für Produktion)
2. docker-compose.yml (mit allen Services)
3. .dockerignore
4. Wichtige Hinweise (Volumes, Ports, Env Vars)
```

## CI/CD Pipeline

```
Erstelle eine CI/CD Pipeline für [PROJEKT].
Platform: [GitHub Actions/GitLab CI/Jenkins]
Sprache: [TECH STACK]
Deployment: [WOHIN]

Stages:
1. Lint + Type Check
2. Unit Tests
3. Build
4. Integration Tests (optional)
5. Deploy to [Staging/Production]

Branch-Strategie: [main/develop/feature]
```

## Error Handling Design

```
Designe eine Error-Handling-Strategie für [ANWENDUNG].
Typ: [API/CLI/Web-App/Library]
Sprache: [SPRACHE]

Definiere:
1. Error-Hierarchie (Basis-Klassen)
2. Error-Codes und Messages
3. Logging-Strategie (was loggen, welches Level)
4. User-facing vs. Internal Errors
5. Retry-Strategie (was retrien, was nicht)
6. Graceful Degradation
```

## MCP-Server konzipieren

```
Konzipiere einen MCP-Server für [ANWENDUNGSFALL].
Datenquelle: [WAS SOLL ANGEBUNDEN WERDEN]
Nutzer: [WER NUTZT DEN SERVER]

Definiere:
1. Tools (Funktionen, die der Agent aufrufen kann)
2. Resources (Daten, die gelesen werden können)
3. Prompts (vordefinierte Templates)
Pro Tool: Name, Beschreibung, Parameter, Rückgabe.
Sicherheit: Welche Zugriffe sind kritisch?
```

## Migration planen

```
Plane eine Migration von [ALT] nach [NEU].
Betroffene Daten: [UMFANG]
Betroffene Systeme: [LISTE]
Nutzer: [ANZAHL]
Downtime-Toleranz: [KEINE/KURZ/FLEXIBLE]

Erstelle:
1. Migrationsstrategie (Big Bang/Phasenweise/Parallel)
2. Schritt-für-Schritt-Plan
3. Rollback-Plan
4. Testplan
5. Kommunikationsplan
6. Risiken und Mitigationen
```

## System-Prompt für Chatbot

```
Schreibe einen produktionsreifen System-Prompt für
einen Chatbot.
Unternehmen: [NAME, BRANCHE]
Aufgabe: [WAS SOLL DER BOT TUN]
Tools: [WELCHE TOOLS HAT ER]
Zielgruppe: [WER SPRICHT MIT IHM]

Struktur:
- Rolle und Identität
- Verhalten und Ton
- Fähigkeiten (was kann er)
- Grenzen (was kann/darf er NICHT)
- Dynamischer Kontext (Datum, User-Info)
- Output-Format
- Sicherheitsregeln (kein System-Prompt preisgeben)
```
