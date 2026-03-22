# Kapitel 3: Datenanalyse – KI als Data Analyst

Du hast Daten. Vielleicht eine Excel-Tabelle mit Verkaufszahlen. Vielleicht einen CSV-Export aus deinem CRM. Vielleicht eine Umfrage mit 500 Antworten. Und du brauchst Erkenntnisse daraus.

Früher hättest du dafür SQL gelernt, Python-Pandas-Tutorials geschaut oder einen Analysten beauftragt. Heute lädst du die Daten in ein LLM und fragst.

Aber *wie* du fragst, entscheidet über die Qualität der Antworten.

## Daten vorbereiten

### Der Daten-Check-Prompt

Bevor du analysierst, lass die KI deine Daten verstehen:

```
Hier sind meine Daten:
"""[Erste 20 Zeilen deiner CSV/Tabelle einfügen]"""

Analysiere die Datenstruktur:
1. Wie viele Spalten gibt es und was bedeuten sie?
2. Welche Datentypen hat jede Spalte (Text/Zahl/Datum/Kategorie)?
3. Gibt es fehlende Werte? In welchen Spalten?
4. Gibt es offensichtliche Ausreißer oder Fehler?
5. Welche Spalten korrelieren vermutlich miteinander?
6. Welche Analysen bieten sich bei diesen Daten an?
```

### Daten bereinigen

```
Meine Daten haben folgende Probleme:
[z.B. fehlende Werte, inkonsistente Formate,
Duplikate, Ausreißer]

Schlage für jedes Problem vor:
1. Wie identifiziere ich es? (Query/Code)
2. Wie behebe ich es? (Strategie)
3. Was könnte schiefgehen? (Risiken)

Gib den Code in [Python/SQL/Excel-Formeln].
```

## Explorative Analyse

### Der Überblick-Prompt

```
Hier sind meine Daten:
"""[Daten einfügen oder beschreiben]"""

Erstelle eine explorative Analyse:

1. ZUSAMMENFASSUNG
   - Wie viele Datensätze?
   - Zeitraum (wenn zeitliche Daten vorhanden)
   - Wichtigste Kennzahlen (Min, Max, Durchschnitt, Median)

2. VERTEILUNGEN
   - Wie sind die wichtigsten Variablen verteilt?
   - Gibt es Auffälligkeiten (Schiefe, Ausreißer)?

3. TRENDS
   - Gibt es zeitliche Trends?
   - Saisonale Muster?

4. ZUSAMMENHÄNGE
   - Welche Variablen hängen zusammen?
   - Gibt es überraschende Korrelationen?

5. TOP-INSIGHTS
   - Die 3 wichtigsten Erkenntnisse
   - Was davon ist überraschend?
   - Was sollte man als Nächstes untersuchen?
```

### Segmentierung

```
Segmentiere meine Kundendaten nach [KRITERIUM].

DATEN: [Beschreibung der Daten]
SEGMENTIERUNGSZIEL: [z.B. Kundenwert, Kaufverhalten,
Engagement, Churn-Risiko]

FÜR JEDES SEGMENT:
1. Name (beschreibend, z.B. "Power-User", "Gelegenheitskäufer")
2. Größe (Anzahl und Prozent)
3. Charakteristik (Was definiert dieses Segment?)
4. Verhalten (Was tun sie? Was kaufen sie?)
5. Potenzial (Wachstum? Risiko? Upselling?)
6. Empfohlene Maßnahme (Was sollten wir tun?)
```

## Visualisierungen beschreiben

KI kann (noch) nicht direkt Charts erstellen, aber sie kann dir den Code oder die Beschreibung liefern:

### Chart-Empfehlung

```
Ich habe folgende Daten und möchte sie visualisieren:
[Beschreibung der Daten]

ZIEL der Visualisierung: [Vergleich/Trend/Verteilung/
Zusammenhang/Proportion]
ZIELGRUPPE: [Wer sieht die Grafik? Experten? Management?]

Empfiehl:
1. Den besten Charttyp (und warum)
2. 2 Alternativen
3. Was auf welche Achse gehört
4. Farbempfehlung (farbenblind-freundlich)
5. Titel und Beschriftungen

Generiere den Code in [Python matplotlib/seaborn/plotly
/ Excel-Anleitung / Google Sheets].
```

### Dashboard-Design

```
Erstelle ein Dashboard-Konzept für [ABTEILUNG/ZWECK].

DATENQUELLEN: [Welche Daten fließen ein?]
NUTZER: [Wer nutzt das Dashboard?]
AKTUALISIERUNG: [Echtzeit/Täglich/Wöchentlich/Monatlich]

DASHBOARD-LAYOUT (4-6 Karten):
Für jede Karte:
- KPI/Metrik
- Charttyp
- Benchmark/Vergleichswert
- Drill-Down-Möglichkeit

OBEN: Die 3-4 wichtigsten KPIs als Kennzahlen
MITTE: Trend-Charts und Vergleiche
UNTEN: Detail-Tabellen und Filter

Warnschwellen: Ab welchen Werten wird ein KPI rot/gelb/grün?
```

## Berichterstellung

### Automatischer Bericht

```
Erstelle einen [wöchentlichen/monatlichen] Bericht
basierend auf folgenden Daten:

"""[Daten einfügen]"""

VERGLEICHSZEITRAUM: [Vorwoche/Vormonat/Vorjahr]
ZIELGRUPPE: [Geschäftsführung/Team/Kunden]

STRUKTUR:
1. Executive Summary (3-5 Sätze, das Wichtigste)
2. KPI-Übersicht (Tabelle: Ist vs. Soll vs. Vorperiode)
3. Highlights (Was lief gut? 2-3 Punkte)
4. Herausforderungen (Was lief nicht gut? 2-3 Punkte)
5. Ursachenanalyse (Warum? Für die Top-Abweichung)
6. Empfehlungen (Was tun wir? 2-3 konkrete Maßnahmen)
7. Ausblick (Was erwarten wir für die nächste Periode?)

TON: Sachlich, datengetrieben. Keine Floskeln wie
"positiver Trend" ohne Zahlen dahinter.
```

## SQL und Datenbankabfragen

### SQL generieren

```
Ich habe folgende Datenbanktabellen:
[Tabellenstruktur beschreiben oder Schema einfügen]

Schreibe eine SQL-Abfrage für:
[Was willst du wissen?]

ANFORDERUNGEN:
- [MySQL/PostgreSQL/SQLite/BigQuery]
- Ergebnis sortiert nach [Kriterium]
- Nur die Top [X] Ergebnisse
- Zeitraum: [Von-Bis]

Erkläre die Abfrage Zeile für Zeile.
Gibt es Performance-Bedenken bei großen Datenmengen?
```

### Datenmodell erklären

```
Hier ist mein Datenbankschema:
"""[Schema einfügen]"""

Erkläre:
1. Welche Entitäten gibt es?
2. Wie hängen sie zusammen (Beziehungen)?
3. Welche Abfragen sind typisch für dieses Schema?
4. Wo sind potenzielle Performance-Engpässe?
5. Welche Indizes würdest du empfehlen?
```

## Statistik

### Statistische Analyse

```
Ich möchte folgende Hypothese testen:
[Hypothese in natürlicher Sprache]

DATEN: [Beschreibung]
STICHPROBENGRÖSSE: [N]
VARIABLEN: [Abhängig/Unabhängig]

Beantworte:
1. Welcher statistische Test ist geeignet? Warum?
2. Welche Voraussetzungen müssen erfüllt sein?
3. Wie interpretiere ich das Ergebnis?
4. Was wäre die Nullhypothese?
5. Welche Effektstärke wäre relevant?
6. Generiere den Code in [Python/R] für den Test.

WICHTIG: Erkläre alles so, dass jemand ohne
Statistik-Studium es versteht.
```

## Umfragen analysieren

```
Ich habe [ANZAHL] Antworten einer Umfrage.
Hier sind die Ergebnisse:
"""[Daten einfügen]"""

ANALYSIERE:
1. Quantitative Fragen:
   - Verteilungen (Häufigkeiten, Prozente)
   - Mittelwerte und Standardabweichungen
   - Gruppenvergleiche (wenn demografische Daten vorhanden)

2. Offene Fragen:
   - Häufigste Themen (Kategorisierung)
   - Sentiment (positiv/neutral/negativ)
   - Auffällige Zitate (anonymisiert)

3. Zusammenfassung:
   - Top 5 Erkenntnisse
   - Überraschungen
   - Handlungsempfehlungen
   - Methodische Einschränkungen
```

## Best Practices für Datenanalyse mit KI

### 1. Daten nie komplett hochladen
Bei sensiblen Daten: Nur Struktur und anonymisierte Beispiele zeigen. Niemals echte Kundendaten, Personaldaten oder Finanzdaten in ein Cloud-LLM laden.

### 2. Ergebnisse verifizieren
KI kann rechnen – aber sie macht Fehler. Besonders bei Prozentrechnungen und Aggregationen. Stichprobenartig nachprüfen.

### 3. Kontext geben
"Analysiere diese Daten" ist zu wenig. Sag der KI, was du suchst, was du erwartest und was dich überraschen würde.

### 4. Iterativ arbeiten
Erster Prompt → Überblick. Zweiter Prompt → Deep Dive in auffällige Bereiche. Dritter Prompt → Handlungsempfehlungen.

---

## Übungen

### Übung 1: Explorative Analyse
Nimm einen öffentlichen Datensatz (z.B. von Kaggle oder data.gov) und führe eine explorative Analyse mit KI durch. Stimmen die "Top-Insights" mit dem überein, was du selbst siehst?

### Übung 2: Visualisierung
Beschreibe ein Datenset und lass dir Chart-Empfehlungen geben. Erstelle den Chart mit dem generierten Code. Stimmt die Empfehlung?

### Übung 3: Bericht
Generiere einen Monatsbericht aus fiktiven Daten. Ist der Bericht präsentationsfähig oder muss er überarbeitet werden?

### Übung 4: SQL
Beschreibe ein Datenbankschema und lass SQL-Abfragen generieren. Teste sie (z.B. in einem Online-SQL-Editor). Sind sie korrekt?
