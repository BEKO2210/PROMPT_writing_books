# Kapitel 2: Agentic Coding Tools – Die neue Generation der Entwicklerwerkzeuge

2024 war das Jahr der Coding-Assistenten. 2025 war das Jahr der Coding-Agenten. 2026 ist das Jahr, in dem sie zum Standard geworden sind.

Der Unterschied: Ein Assistent schlägt Code vor, den du einfügst. Ein Agent schreibt Code, führt ihn aus, liest Fehlermeldungen, fixt Bugs und commitet – alles autonom. Du gibst die Richtung vor. Der Agent erledigt die Schrittarbeit.

## Die Landschaft (Stand März 2026)

### Tier 1: Agentic-First

| Tool | Modell | Stärke | Preis |
|---|---|---|---|
| **Claude Code** (Anthropic) | Claude Opus 4 / Sonnet 4 | Terminal-Agent, plant & handelt autonom, Git-integriert | API-basiert (pay per token) |
| **Cursor** | Multi-Model (Claude, GPT, Gemini) | IDE mit Agent-Mode, Composer, multi-file Edits | $20/Monat (Pro) |
| **Windsurf** (Codeium) | Multi-Model | Cascade-Flow, kontextuelles Verständnis | $15/Monat (Pro) |
| **Devin** (Cognition) | Proprietär | Vollautonomer Agent, eigene Sandbox | Enterprise |

### Tier 2: Assistenten mit Agent-Fähigkeiten

| Tool | Modell | Stärke | Preis |
|---|---|---|---|
| **GitHub Copilot** | GPT-4o + Claude | IDE-integriert, Agent-Mode (Preview), Workspace-Kontext | $10-$39/Monat |
| **Cline** | Multi-Model (via API) | Open Source, VS-Code-Extension, volle Kontrolle | Kostenlos (+ API-Kosten) |
| **Aider** | Multi-Model (via API) | Terminal-basiert, Git-integriert, diff-basiert | Kostenlos (+ API-Kosten) |
| **Continue** | Multi-Model | Open Source, IDE-Extension, anpassbar | Kostenlos (+ API-Kosten) |

### Tier 3: Spezialisiert

| Tool | Fokus | Stärke |
|---|---|---|
| **Bolt.new** | Full-Stack Web-Apps | Generiert komplette Apps im Browser |
| **v0** (Vercel) | Frontend/UI | React-Komponenten aus Beschreibungen |
| **Lovable** | Full-Stack | Produkt-Building für Nicht-Entwickler |
| **Replit Agent** | Full-Stack | Deployment inklusive |

## Wie du in Coding-Agenten optimal promptest

### Claude Code

Claude Code ist ein Terminal-basierter Agent, der direkt in deinem Repo arbeitet:

```bash
# Starten
claude

# In Claude Code prompten:
"Lies die README und erkläre mir die Architektur dieses Projekts."

"Implementiere eine REST-API für User-Management:
- CRUD-Endpoints (GET, POST, PUT, DELETE)
- Zod-Validierung
- Prisma ORM
- Schreibe Tests mit Vitest
- Committe am Ende mit aussagekräftiger Commit-Message."
```

**Best Practices für Claude Code:**
1. **CLAUDE.md nutzen** – Erstelle eine `CLAUDE.md`-Datei im Root deines Projekts mit Architektur, Konventionen und Befehlen. Claude Code liest sie automatisch.
2. **Kleine, klare Aufgaben** – "Implementiere Feature X" ist besser als "Baue die ganze App".
3. **Lass ihn planen** – "Erstelle zuerst einen Plan, bevor du implementierst."
4. **Tests zuerst** – "Schreibe zuerst die Tests, dann die Implementierung."
5. **Git nutzen** – Claude Code commitet automatisch. Prüfe die Commits.

### CLAUDE.md – Das Projektgedächtnis

Die wichtigste Datei für agentic Coding:

```markdown
# Projektname

## Architektur
- Monorepo mit Turborepo
- Backend: Node.js + Express + TypeScript
- Frontend: Next.js 15 + React 19
- DB: PostgreSQL + Prisma

## Befehle
- `npm run build` – Alles bauen
- `npm run test` – Tests ausführen
- `npm run lint` – Linting
- `npm run dev` – Entwicklungsserver

## Konventionen
- Alle Dateien: kebab-case
- Alle Funktionen: camelCase
- Alle Typen: PascalCase
- Error Handling: Result-Pattern, kein throw
- Commits: Conventional Commits (feat:, fix:, chore:)
- Branch-Naming: feature/kurze-beschreibung

## Vermeide
- any-Types
- console.log in Production-Code
- Star-Imports
- Class Components (nur Functional Components)
```

### Cursor

Cursor hat drei Modi: Tab-Completion, Chat und Composer (Agent).

**Tab-Completion:**
Cursor vervollständigt Code inline. Optimiere durch:
- Gute Variablennamen (die Completion wird besser)
- Kommentare als Hints: `// TODO: Validate email format`
- Typ-Annotationen (TypeScript/Python Type Hints)

**Chat (Cmd+L):**
```
Kontext: Markiere relevanten Code, dann frage:
"Erkläre, warum dieser Code bei mehr als 1000 Items
langsam wird und schlage eine Optimierung vor."
```

**Composer / Agent Mode (Cmd+I):**
```
"Erstelle eine neue API-Route /api/v2/users mit:
- Pagination (cursor-based)
- Filtering (nach Name, Email, Status)
- Sorting (nach jedem Feld, ASC/DESC)
- Rate Limiting (100 req/min)
Nutze die bestehende Middleware aus src/middleware/.
Schreibe Tests."
```

**Cursor Rules (.cursorrules):**
```
# .cursorrules
You are a senior TypeScript developer.
Always use strict TypeScript - no 'any'.
Use Zod for runtime validation.
Follow the repository's existing patterns.
Write tests for every new function.
Use descriptive variable names.
Prefer composition over inheritance.
```

### GitHub Copilot

Copilot hat sich von einem Autocomplete-Tool zu einem Agent entwickelt:

**Copilot Chat (in VS Code):**
```
@workspace Wie ist die Authentifizierung in diesem
Projekt implementiert?

@workspace Schreibe eine Migration, die eine
"notifications"-Tabelle hinzufügt.
```

**Copilot Agent Mode:**
```
Implementiere folgendes GitHub Issue: #123
Lies das Issue, verstehe die Anforderungen,
implementiere, teste und erstelle einen PR.
```

### Cline (Open Source)

Cline ist der Open-Source-Champion: Volle Kontrolle, jedes Modell, kein Vendor-Lock-in.

```
# In Cline (VS Code Extension):
"Analysiere die Performance dieses Projekts:
1. Lies alle API-Routes
2. Identifiziere N+1 Query-Probleme
3. Schlage Optimierungen vor
4. Implementiere die wichtigste Optimierung
5. Schreibe einen Benchmark-Test"
```

**Cline Best Practices:**
- `.clinerules` für Projekt-Konventionen
- Auto-approve für sichere Operationen (read, list)
- Manual-approve für Schreiboperationen
- API-Budget setzen (Token-Limit pro Task)

### Aider

Terminal-basiert, Git-integriert, minimal:

```bash
# Starten mit einem Modell
aider --model claude-sonnet-4-20250514

# In Aider:
/add src/api/users.ts src/models/user.ts
> Füge Pagination zur Users-API hinzu.
> Nutze cursor-based Pagination mit Prisma.
```

**Aider-Stärken:**
- Versteht Git nativ (zeigt Diffs, commitet)
- Funktioniert mit jedem Modell via API
- Lightweight, keine IDE nötig
- Architect-Modus: Erst planen (mit starkem Modell), dann implementieren (mit schnellem Modell)

## Welches Tool für welchen Zweck?

| Situation | Empfehlung |
|---|---|
| Kleine Änderungen, quick Fixes | Cursor Tab-Completion, Copilot |
| Neue Features (multi-file) | Cursor Composer, Claude Code |
| Große Refactorings | Claude Code, Aider |
| Code verstehen (onboarding) | Claude Code, Cursor Chat |
| Prototyping (0 → 1) | Bolt.new, v0, Cursor Composer |
| Open Source / Budget | Cline, Aider, Continue |
| Enterprise / Compliance | GitHub Copilot Enterprise, Cursor Business |

## Effektive Strategien für alle Tools

### 1. Kontext ist King
Alle Tools profitieren von Kontext. Je mehr relevante Dateien du referenzierst oder in den Kontext gibst, desto besser das Ergebnis.

### 2. Inkrementell arbeiten
Nicht "baue mir die ganze App" – sondern Schritt für Schritt. Ein Feature nach dem anderen. Ein Modul nach dem anderen.

### 3. Tests als Qualitätsgate
Lass den Agent Tests schreiben. Dann: Tests ausführen. Wenn sie rot sind: Agent fixen lassen. Die Feedback-Loop ist der Schlüssel.

### 4. Reviewe alles
Auch agentic-generierter Code muss reviewed werden. Git Diff lesen. Verstehen, was geändert wurde. Nicht blind mergen.

### 5. Versionskontrolle als Safety Net
Git ist dein Undo-Button. Commite oft. Branch für experimentelle Änderungen. Wenn der Agent Mist baut: `git checkout .`

---

## Übungen

### Übung 1: CLAUDE.md erstellen
Erstelle eine CLAUDE.md für ein eigenes Projekt (oder ein Open-Source-Projekt, das du kennst). Welche Informationen braucht ein KI-Agent, um guten Code zu schreiben?

### Übung 2: Tool-Vergleich
Nimm dieselbe Aufgabe und löse sie mit zwei verschiedenen Tools (z.B. Cursor + Aider oder Copilot + Claude Code). Vergleiche die Ergebnisse und den Workflow.

### Übung 3: Agent-Modus testen
Nutze den Agent-Modus eines Tools (Cursor Composer, Claude Code, Copilot Agent) für ein echtes Feature. Wie viel musstest du manuell nacharbeiten?

### Übung 4: Fehlerbehebung
Gib einem Coding-Agent einen Bug-Report und lass ihn autonom debuggen. Wie weit kommt er ohne dein Eingreifen?
