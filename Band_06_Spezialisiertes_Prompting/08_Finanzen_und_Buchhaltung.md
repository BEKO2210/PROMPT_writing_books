# Kapitel 8: Finanzen und Buchhaltung – KI rechnet mit

**Disclaimer:** KI ist kein Steuerberater und kein Wirtschaftsprüfer. Finanzdaten sind sensibel – lade keine echten Kontodaten oder Steuerbescheide in Cloud-LLMs. Und: KI macht Rechenfehler. Jede Zahl nachprüfen.

Trotzdem: Für Finanzanalyse, Berichtserstellung, Budgetplanung und das Verstehen komplexer Finanzdokumente ist KI ein starkes Werkzeug.

## Finanzberichte analysieren

### Jahresabschluss verstehen

```
Analysiere folgenden Jahresabschluss:

"""[GuV und/oder Bilanz einfügen]"""

ERSTELLE:
1. ZUSAMMENFASSUNG (3-5 Sätze für Nicht-Finanzler)
2. KENNZAHLEN:
   - Umsatzwachstum (YoY)
   - Gewinnmarge (Brutto + Netto)
   - EBITDA / EBIT
   - Eigenkapitalquote
   - Liquiditätsgrad
   - Return on Equity
3. STÄRKEN: Was läuft finanziell gut?
4. RISIKEN: Was ist besorgniserregend?
5. VERGLEICH: Wie stehen die Zahlen im Branchenvergleich?
6. EMPFEHLUNG: Was sollte das Management beachten?

Erkläre alle Kennzahlen so, dass ein Nicht-BWLer
sie versteht.
```

### Kennzahlen erklären

```
Erkläre folgende Finanzkennzahl für [ZIELGRUPPE]:

KENNZAHL: [z.B. EBITDA, Quick Ratio, P/E Ratio,
Debt-to-Equity, Working Capital]

ERKLÄRE:
1. Was misst diese Kennzahl? (1 Satz)
2. Wie berechnet man sie? (Formel + Beispiel)
3. Was ist ein "guter" Wert? (Branchenabhängig)
4. Was passiert, wenn der Wert zu hoch/niedrig ist?
5. Alltagsanalogie (z.B. "EBITDA ist wie dein
   Gehalt vor Steuern und Miete – was du verdienst,
   bevor die Fixkosten kommen")

ZIELGRUPPE: [Laie/Gründer/Investor/Student]
```

## Budgetplanung

### Budget erstellen

```
Erstelle ein Budgetplan-Template für [ZEITRAUM].

UNTERNEHMEN/ABTEILUNG: [Kontext]
ZEITRAUM: [Monat/Quartal/Jahr]
VORJAHRESBUDGET: [Wenn vorhanden]

STRUKTUR:
| Kategorie | Budget | Ist | Abweichung | % |
|---|---|---|---|---|
| Personalkosten | | | | |
| Marketing | | | | |
| IT/Software | | | | |
| Büro/Miete | | | | |
| Reisekosten | | | | |
| [Weitere Kategorien] | | | | |
| **Gesamt** | | | | |

ZUSÄTZLICH:
1. Annahmen hinter dem Budget (Was wurde vorausgesetzt?)
2. Risikopuffer (Empfohlener Prozentsatz)
3. Szenario-Analyse: Best Case / Base Case / Worst Case
4. Trigger-Punkte: Ab welcher Abweichung muss gehandelt werden?
```

### Cashflow-Prognose

```
Erstelle eine Cashflow-Prognose für [ZEITRAUM].

AUSGANGSDATEN:
- Aktueller Kontostand: [Betrag]
- Erwartete Einnahmen: [Aufschlüsselung]
- Fixkosten monatlich: [Aufschlüsselung]
- Variable Kosten: [Aufschlüsselung]
- Geplante Investitionen: [Aufschlüsselung]

PROGNOSE (pro Monat):
| Monat | Einnahmen | Ausgaben | Saldo | Kumuliert |
|---|---|---|---|---|

WARNSCHWELLEN:
- Ab welchem Kontostand wird es kritisch?
- Wann droht ein Liquiditätsengpass?
- Welche Maßnahmen sind dann möglich?
```

## Steuern und Buchhaltung

### Steuerfrage strukturieren

```
Ich habe eine Steuerfrage:
[Frage in eigenen Worten]

KONTEXT:
- Rechtsform: [GmbH/Einzelunternehmen/Freiberufler/...]
- Land: [Deutschland/Österreich/Schweiz]
- Relevanter Zeitraum: [Jahr]

HILF MIR, die Frage zu strukturieren:
1. Welches Steuergesetz ist relevant?
2. Was sind die Grundregeln?
3. Welche Ausnahmen gibt es?
4. Was muss ich dokumentieren?
5. Welche Fristen gelten?
6. Was sollte ich meinen Steuerberater fragen?
   (Konkrete Fragen formulieren)

WICHTIG: Dies ist keine Steuerberatung. Die
Informationen dienen der Vorbereitung eines
Gesprächs mit einem Steuerberater.
```

### Belege kategorisieren

```
Kategorisiere folgende Ausgaben für die Buchhaltung:

"""[Liste von Ausgaben einfügen]"""

FÜR JEDE AUSGABE:
1. Kategorie (SKR03/SKR04-Konto oder Oberkategorie)
2. Vorsteuerabzug möglich? (Ja/Nein/Teilweise)
3. Betriebsausgabe? (Voll/Anteilig/Nein)
4. Besonderheiten (z.B. Bewirtung: 70% absetzbar)

SORTIERE nach Kategorie und erstelle eine Übersicht.

HINWEIS: Endgültige Zuordnung durch Steuerberater
bestätigen lassen.
```

## Investitionsanalyse

### Investitionsbewertung

```
Bewerte folgende Investitionsmöglichkeit:

INVESTITION: [Was? z.B. neue Maschine, Software, Standort]
KOSTEN: [Anschaffungskosten + laufende Kosten]
ERWARTETER NUTZEN: [Einsparungen, Umsatzsteigerung]
ZEITRAUM: [Über welchen Zeitraum?]
ALTERNATIVE: [Was passiert, wenn wir NICHT investieren?]

BERECHNE:
1. ROI (Return on Investment)
2. Amortisationszeit
3. Kapitalwert (NPV) bei [X]% Diskontierungssatz
4. Break-Even-Punkt

SZENARIO-ANALYSE:
- Best Case: [Annahmen]
- Base Case: [Annahmen]
- Worst Case: [Annahmen]

EMPFEHLUNG: Investieren oder nicht? Begründung.

WICHTIG: Alle Berechnungen nachprüfen. KI kann
bei Finanzmathematik Fehler machen.
```

## Finanzberichterstattung

### Management-Bericht

```
Erstelle einen monatlichen Management-Bericht
basierend auf folgenden Zahlen:

"""[Finanzdaten einfügen]"""

VERGLEICH MIT: [Vormonat / Vorjahr / Budget]

STRUKTUR:
1. EXECUTIVE SUMMARY (5 Sätze, das Wichtigste)
2. KPI-DASHBOARD (Tabelle: Ist vs. Plan vs. Vorjahr)
3. UMSATZANALYSE (nach Produkt/Region/Kunde)
4. KOSTENANALYSE (Wo sind die größten Abweichungen?)
5. CASHFLOW-STATUS
6. TOP-3-THEMEN (Was muss besprochen werden?)
7. AUSBLICK (Was erwarten wir für den nächsten Monat?)

TON: Sachlich, auf den Punkt. Geschäftsführer haben
5 Minuten für diesen Bericht. Kein Wort zu viel.
```

### Investor-Pitch vorbereiten

```
Erstelle die Finanzslides für einen Investor-Pitch.

UNTERNEHMEN: [Name, Phase, Branche]
BISHERIGE KENNZAHLEN: [Umsatz, Kosten, Wachstum]
FUNDING-ZIEL: [Wie viel wird gesucht?]
VERWENDUNG: [Wofür?]

SLIDES:
1. MARKTGRÖSSE (TAM/SAM/SOM mit Quellen)
2. GESCHÄFTSMODELL (Wie verdient ihr Geld?)
3. UNIT ECONOMICS (CAC, LTV, Marge pro Kunde)
4. FINANZ-ÜBERSICHT (Ist-Zahlen + Projektion 3 Jahre)
5. USE OF FUNDS (Wofür wird das Geld eingesetzt?)
6. MILESTONES (Was wird mit dem Geld erreicht?)

Für jede Slide: Die Kernaussage (1 Satz) und
die unterstützenden Daten/Grafiken.
```

## Persönliche Finanzen

### Budget-Check

```
Hilf mir, mein persönliches Budget zu analysieren.

MONATLICHES NETTOEINKOMMEN: [Betrag]
AUSGABEN:
[Liste aller Ausgaben]

ANALYSIERE:
1. Wo liegt mein Geld? (Kategorien und Prozente)
2. 50/30/20-Regel: Stimmt die Verteilung?
   (50% Bedürfnisse / 30% Wünsche / 20% Sparen)
3. Wo sind Einsparpotenziale?
4. Welche Ausgaben sind überproportional?
5. Sparrate: Ist sie ausreichend?
6. 3 konkrete Tipps, die sofort umsetzbar sind

WICHTIG: Keine Anlageberatung.
```

---

## Übungen

### Übung 1: Kennzahlen verstehen
Nimm einen öffentlichen Jahresbericht eines Unternehmens (z.B. von der DAX-Website) und lass die wichtigsten Kennzahlen erklären. Verstehst du jetzt, wie es dem Unternehmen geht?

### Übung 2: Budget erstellen
Erstelle ein Budget für ein (reales oder fiktives) Projekt. Sind die Szenario-Analysen realistisch?

### Übung 3: Steuerfrage
Formuliere eine Steuerfrage und lass sie strukturieren. Sind die generierten Fragen für den Steuerberater sinnvoll?

### Übung 4: Persönliches Budget
Analysiere dein eigenes monatliches Budget (oder ein fiktives). Sind die Einsparpotenziale realistisch?
