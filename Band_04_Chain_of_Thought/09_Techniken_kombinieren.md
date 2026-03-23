# Kapitel 9: Reasoning-Techniken kombinieren – Das Orchester

Du hast jetzt sieben Instrumente gelernt: Chain-of-Thought, Zero-Shot CoT, Tree-of-Thought, Self-Consistency, ReAct, Meta-Prompting und Reflexion. Jedes für sich ist mächtig. Aber die wahre Kraft entsteht, wenn du sie kombinierst.

Ein Orchester klingt nicht großartig, weil jedes Instrument einzeln gut ist. Es klingt großartig, weil die Instrumente zusammenspielen.

## Die Kombinations-Matrix

Nicht jede Kombination macht Sinn. Hier ist meine Matrix:

| Kombination | Sinn? | Wann? |
|---|---|---|
| CoT + Reflexion | ★★★★★ | Immer bei wichtigen Aufgaben |
| CoT + Self-Consistency | ★★★★★ | Wenn Korrektheit kritisch ist |
| ToT + Reflexion | ★★★★☆ | Komplexe Entscheidungen |
| ReAct + CoT | ★★★★☆ | Recherche-Aufgaben |
| Meta + Reflexion | ★★★★☆ | Prompt-Entwicklung |
| CoT + ToT | ★★★☆☆ | Selten – ähnliche Funktion |
| SC + Reflexion | ★★★☆☆ | Doppelte Qualitätssicherung |
| ToT + SC | ★★☆☆☆ | Overkill für die meisten Aufgaben |

## Kombination 1: CoT + Reflexion (Der Standard)

Die häufigste und nützlichste Kombination. Das Modell denkt Schritt für Schritt und überprüft dann seine Arbeit.

```
Aufgabe: [Deine Aufgabe]

PHASE 1 – DENKEN (Chain-of-Thought):
Löse die Aufgabe Schritt für Schritt.
Zeige jeden Denkschritt.

PHASE 2 – PRÜFEN (Reflexion):
Gehe jeden Denkschritt nochmal durch.
Gibt es Fehler? Logische Lücken? Falsche Annahmen?

PHASE 3 – KORRIGIEREN:
Falls Fehler gefunden: Korrigiere und gib die
bereinigte Antwort.
Falls keine Fehler: Bestätige und gib die finale Antwort.
```

### Beispiel: Finanzberechnung

```
Ein Unternehmen hat folgende Quartalszahlen:
- Umsatz Q1: 120.000 Euro
- Umsatz Q2: 145.000 Euro
- Umsatz Q3: 130.000 Euro
- Umsatz Q4: 180.000 Euro
- Fixkosten: 40.000 Euro/Quartal
- Variable Kosten: 35% des Umsatzes

Berechne den Jahresgewinn und die Gewinnmarge.

PHASE 1 – Schritt für Schritt:
[Berechnung]

PHASE 2 – Prüfung:
[Jeden Schritt verifizieren]

PHASE 3 – Finale Antwort:
[Korrigierte Berechnung, falls nötig]
```

## Kombination 2: ToT + Reflexion (Der Stratege)

Für komplexe Entscheidungen: Erst mehrere Optionen erkunden, dann die gewählte Option kritisch prüfen.

```
Aufgabe: [Strategische Entscheidung]

PHASE 1 – EXPLORATION (Tree-of-Thought):
Generiere 3 verschiedene Strategien.
Bewerte jede (Stärken, Schwächen, Risiken).
Wähle die beste.

PHASE 2 – STRESSTEST (Reflexion):
Nimm die gewählte Strategie und hinterfrage sie:
- Was sind die schwächsten Annahmen?
- Was passiert im Worst Case?
- Welchen Einwand würde ein Skeptiker haben?

PHASE 3 – OPTIMIERUNG:
Passe die Strategie an, um die gefundenen
Schwächen zu adressieren.

PHASE 4 – FINALE EMPFEHLUNG:
Zusammenfassung mit konkretem Aktionsplan.
```

### Beispiel: Markteintrittsstrategie

```
Wir sind ein deutsches Softwareunternehmen (B2B, ERP)
und möchten in den US-Markt expandieren.

Team: 45 Mitarbeiter, 8 Mio Euro Jahresumsatz.
Budget für Expansion: 500.000 Euro.

PHASE 1 – EXPLORATION:
3 Eintrittsstrategien entwickeln und bewerten.

PHASE 2 – STRESSTEST:
Die beste Strategie auf Herz und Nieren prüfen.

PHASE 3 – OPTIMIERUNG:
Schwächen adressieren.

PHASE 4 – AKTIONSPLAN:
Erste 90 Tage, konkrete Schritte.
```

## Kombination 3: ReAct + CoT + Reflexion (Der Forscher)

Für Recherche-Aufgaben, bei denen Fakten gesammelt, analysiert und verifiziert werden müssen.

```
Frage: [Recherche-Frage]

PHASE 1 – RECHERCHE (ReAct):
Sammle relevante Informationen.
Für jeden Fakt: Quelle/Grundlage angeben.
Gedanke → Aktion → Beobachtung (3-5 Zyklen)

PHASE 2 – ANALYSE (Chain-of-Thought):
Analysiere die gesammelten Informationen
Schritt für Schritt.
Welche Schlüsse lassen sich ziehen?

PHASE 3 – VERIFIKATION (Reflexion):
Prüfe die Analyse:
- Basiert sie auf soliden Fakten?
- Gibt es alternative Interpretationen?
- Was habe ich möglicherweise übersehen?

PHASE 4 – ERGEBNIS:
Zusammenfassung mit Confidence-Bewertung.
```

## Kombination 4: Meta + CoT + SC (Der Perfektionist)

Für Aufgaben, bei denen die Antwort wirklich stimmen muss.

```
Aufgabe: [Kritische Aufgabe]

PHASE 1 – META-ANALYSE:
Bevor du anfängst: Was ist die beste Herangehensweise
an diese Aufgabe? Welche Schritte brauchst du?

PHASE 2 – AUSFÜHRUNG (Chain-of-Thought):
Führe die Aufgabe Schritt für Schritt aus.

PHASE 3 – GEGENPROBE (Self-Consistency):
Löse die Aufgabe nochmal mit einem anderen Ansatz.
Kommen beide Ansätze zum selben Ergebnis?

PHASE 4 – FINALISIERUNG:
Wenn ja: Finale Antwort.
Wenn nein: Analysiere den Unterschied und bestimme
die korrekte Antwort.
```

## Die Reasoning-Pipeline

Für regelmäßig wiederkehrende komplexe Aufgaben lohnt es sich, eine feste Pipeline zu definieren. Hier ist mein Template:

```
=== REASONING-PIPELINE ===

INPUT:
[Aufgabe/Frage]

STUFE 1 – VERSTEHEN:
Was genau wird gefragt?
Welche Informationen habe ich?
Welche fehlen?
Welche Annahmen muss ich treffen?

STUFE 2 – PLANEN:
Welche Reasoning-Technik(en) passen?
In welcher Reihenfolge?
Was sind meine Erfolgskriterien?

STUFE 3 – AUSFÜHREN:
[Hier kommt die gewählte Technik-Kombination]

STUFE 4 – PRÜFEN:
Erfüllt das Ergebnis die Erfolgskriterien?
Gibt es offene Fragen?
Wie sicher bin ich (0-100%)?

STUFE 5 – LIEFERN:
Finale Antwort.
Confidence Score.
Offene Punkte (falls vorhanden).

=== PIPELINE ENDE ===
```

## Praxis-Beispiel: Vollständige Pipeline

```
=== REASONING-PIPELINE ===

INPUT:
Soll ich als Freelancer eine GmbH gründen?
Aktuell: 75.000 Euro Jahresumsatz, allein, keine
Mitarbeiter geplant, Software-Entwicklung.

STUFE 1 – VERSTEHEN:
- Gefragt: GmbH ja/nein für einen Solo-Freelancer
- Vorhandene Infos: Umsatz, Branche, Teamgröße
- Fehlend: Gewinnmarge, private Situation, Wachstumspläne,
  aktuelle Steuerbelastung
- Annahmen: Gewinnmarge ~60% (typisch für Software-Freelancer),
  keine besonderen privaten Umstände

STUFE 2 – PLANEN:
- Technik: ToT (mehrere Optionen) + Reflexion (Prüfung)
- Reihenfolge: 1) Optionen erkunden 2) Beste vertiefen
  3) Prüfen
- Erfolgskriterien: Klare Empfehlung mit Zahlen

STUFE 3 – AUSFÜHREN:

[Tree-of-Thought]
Option A: Weiter als Freiberufler
+ Kein Gründungsaufwand
+ Keine Buchführungspflicht (EÜR reicht)
+ Kein Mindestkapital
- Volle persönliche Haftung
- Hoher persönlicher Steuersatz bei 75k Umsatz
Bewertung: 6/10

Option B: GmbH gründen
+ Haftungsbeschränkung
+ Steuervorteile ab ~60.000 Euro Gewinn
+ Professionelleres Auftreten
- 25.000 Euro Stammkapital (12.500 einzuzahlen)
- Buchführungspflicht, Jahresabschluss
- Geschäftsführergehalt nötig
- Kosten: Steuerberater ~3.000-5.000 Euro/Jahr
Bewertung: 7/10

Option C: UG (haftungsbeschränkt)
+ Haftungsbeschränkung
+ Nur 1 Euro Stammkapital
+ Steuervorteile ähnlich GmbH
- Muss 25% des Gewinns zurücklegen bis 25.000 Euro
- Weniger seriös als GmbH
- Gleicher Verwaltungsaufwand wie GmbH
Bewertung: 5/10

Gewählt: Option B (GmbH)

[Reflexion – Stresstest]
- Schwache Annahme: 60% Gewinnmarge. Bei niedrigerer
  Marge lohnt sich die GmbH weniger.
- Steuervergleich nötig:
  Freiberufler: ~45.000 Gewinn × ~42% (inkl. Soli) ≈ 18.900 Euro
  GmbH: ~45.000 Gewinn × 15% KSt + ~15% GewSt ≈ 13.500 Euro
  + Geschäftsführergehalt separat besteuert
  → Tatsächliche Ersparnis geringer als gedacht
- Bei 75.000 Umsatz ist der Break-Even knapp.
  Eher ab 100.000+ Umsatz sinnvoll.

STUFE 4 – PRÜFEN:
Die Reflexion hat die erste Einschätzung korrigiert.
GmbH lohnt sich bei 75.000 Euro Umsatz wahrscheinlich
NOCH NICHT. Erst ab ~100.000 Euro.
Confidence: 70% (Steuerrecht ist komplex, individuelle
Beratung nötig).

STUFE 5 – LIEFERN:

EMPFEHLUNG: Bei 75.000 Euro Jahresumsatz als Solo-
Freelancer: NOCH KEINE GmbH gründen.

Begründung: Der Steuervorteil bei deinem Umsatzniveau
ist marginal und wird durch die Gründungskosten und
laufenden Verwaltungsaufwand aufgefressen. Die GmbH
lohnt sich typischerweise ab ~100.000 Euro Umsatz.

Nächste Schritte:
1. Wachstum anstreben auf 100k+ Umsatz
2. Dann: Steuerberater-Gespräch mit konkretem Vergleich
3. UG als Einstieg erwägen, wenn Haftung das Hauptthema ist

Confidence: 70%
Offener Punkt: Individuelle Steuerberatung einholen,
da persönliche Faktoren den Break-Even verschieben können.

=== PIPELINE ENDE ===
```

## Wann welche Kombination?

Hier ist mein Entscheidungsbaum:

```
Ist die Aufgabe einfach?
├── JA → Kein Reasoning nötig. Normaler Prompt.
└── NEIN → Braucht Reasoning.
    │
    Gibt es einen klaren Lösungsweg?
    ├── JA → CoT (+ Reflexion bei wichtigen Aufgaben)
    └── NEIN → Gibt es mehrere mögliche Ansätze?
        ├── JA → ToT (+ Reflexion)
        └── NEIN → Braucht das Modell externe Infos?
            ├── JA → ReAct (+ CoT)
            └── NEIN → Ist Korrektheit kritisch?
                ├── JA → CoT + SC + Reflexion
                └── NEIN → CoT reicht.
```

## Die Kosten-Nutzen-Rechnung

Jede zusätzliche Technik kostet Tokens. Hier sind ungefähre Faktoren:

| Technik | Token-Faktor | Qualitätsgewinn |
|---|---|---|
| Nur Prompt (Baseline) | 1x | Baseline |
| + CoT | 2-3x | +30-50% |
| + Reflexion | 3-5x | +15-25% |
| + SC (3 Durchläufe) | 6-9x | +10-20% |
| + ToT | 4-6x | +20-30% |
| Volle Pipeline | 10-15x | +50-80% |

Die volle Pipeline lohnt sich nicht für eine Alltagsfrage. Aber für eine Geschäftsentscheidung, die zehntausende Euro beeinflusst? Absolut.

## Eigene Pipelines bauen

Du musst nicht meine Pipelines nutzen. Bau deine eigenen. Hier ist das Framework:

### Schritt 1: Definiere deine häufigsten Aufgabentypen
z.B. "Kundenpräsentationen erstellen", "Code Reviews", "Strategische Analysen"

### Schritt 2: Wähle die passenden Techniken pro Typ
- Kundenpräsentation: Meta (Prompt optimieren) → CoT (Inhalt strukturieren) → Reflexion (Qualität prüfen)
- Code Review: CoT (Code durchgehen) → Reflexion (Checkliste) → Self-Consistency (zweite Meinung)
- Strategische Analyse: ToT (Optionen erkunden) → CoT (beste vertiefen) → Reflexion (Stresstest)

### Schritt 3: Erstelle Templates
Schreibe fertige Prompt-Templates für jede Pipeline. Speichere sie in deiner Template-Bibliothek (Band 2).

### Schritt 4: Iteriere
Teste jedes Template mit mindestens 5 Aufgaben. Passe an, was nicht funktioniert. Entferne Schritte, die keinen Mehrwert bringen.

## Häufige Fehler bei Kombinationen

### Fehler 1: Alles auf einmal
Du brauchst nicht für jede Frage die volle Pipeline. Das ist wie mit Kanonen auf Spatzen schießen. Starte simpel (CoT) und eskaliere nur, wenn nötig.

### Fehler 2: Falsche Reihenfolge
ToT vor CoT macht Sinn (erst erkunden, dann vertiefen). CoT vor ToT nicht (warum erst vertieft denken, um dann breit zu suchen?).

### Fehler 3: Redundante Techniken
CoT + Zero-Shot CoT ist redundant. SC + 3-Runden-Reflexion ist Overkill. Jede Technik in der Pipeline sollte einen einzigartigen Mehrwert bringen.

### Fehler 4: Kein Abbruchkriterium
Ohne klares Ziel kann die Pipeline endlos laufen. Definiere immer: "Wann bin ich fertig?" und "Was ist gut genug?"

---

## Übungen

### Übung 1: Pipeline für deinen Beruf
Identifiziere die 3 häufigsten komplexen Aufgaben in deinem Job. Entwerfe für jede eine Reasoning-Pipeline. Teste jede mit einer echten Aufgabe.

### Übung 2: Kombinations-Experiment
Nimm diese Aufgabe und löse sie mit 3 verschiedenen Kombinations-Ansätzen:

"Ein Restaurant-Besitzer möchte seinen Umsatz in 6 Monaten um 30% steigern. Budget: 15.000 Euro. Standort: Mittelgroße Stadt, 80.000 Einwohner."

- Ansatz 1: CoT allein
- Ansatz 2: ToT + Reflexion
- Ansatz 3: Volle Pipeline

Vergleiche Qualität, Tiefe und Nützlichkeit der Ergebnisse.

### Übung 3: Pipeline-Optimierung
Nimm die volle Pipeline aus diesem Kapitel und kürze sie. Entferne Schritte, die du für überflüssig hältst. Teste die gekürzte Version. Ist das Ergebnis gleich gut? Besser? Schlechter?

### Übung 4: Template-Bibliothek
Erstelle 3 fertige Pipeline-Templates für verschiedene Aufgabentypen. Speichere sie so, dass du sie schnell kopieren und anpassen kannst. Teste jedes Template mit 3 verschiedenen Aufgaben.
