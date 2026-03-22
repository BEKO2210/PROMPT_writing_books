# Kapitel 3: Datenanalyse – KI als Data Analyst

Du hast Daten. Vielleicht eine Excel-Tabelle mit Verkaufszahlen. Vielleicht einen CSV-Export aus deinem CRM. Vielleicht eine Umfrage mit 500 Antworten. Und du brauchst Erkenntnisse daraus.

Früher hättest du dafür SQL gelernt, Python-Pandas-Tutorials geschaut oder einen Analysten beauftragt. Heute lädst du die Daten in ein LLM und fragst.

Aber *wie* du fragst, entscheidet über die Qualität der Antworten.

## Daten vorbereiten

### Der Daten-Check-Prompt

Bevor du analysierst, lass die KI deine Daten verstehen. Füge die ersten 20 Zeilen deiner Tabelle ein und frage nach Datenstruktur, Datentypen, fehlenden Werten, Ausreißern, Korrelationen und möglichen Analysen.

```
Hier sind meine Daten:
"""[Erste 20 Zeilen deiner CSV/Tabelle]"""

Analysiere die Datenstruktur:
1. Spalten und ihre Bedeutung
2. Datentypen (Text/Zahl/Datum/Kategorie)
3. Fehlende Werte und Ausreißer
4. Welche Analysen bieten sich an?
```

**Daten bereinigen:** Beschreibe die Probleme (fehlende Werte, Duplikate, inkonsistente Formate) und frage für jedes Problem nach Identifikation, Behebung und Risiken. Wichtig: Zielsprache angeben – Python, SQL oder Excel-Formeln.

## Explorative Analyse

Der Überblick-Prompt folgt einem festen Schema: Zusammenfassung (Kennzahlen wie Min, Max, Durchschnitt, Median), Verteilungen, Trends, Zusammenhänge und die **Top 3 Insights** – plus was davon überraschend ist und was man als Nächstes untersuchen sollte.

**Segmentierung** funktioniert am besten, wenn du nicht nur das Kriterium nennst, sondern auch das Ziel (Kundenwert? Churn-Risiko? Kaufverhalten?). Für jedes Segment: Name, Größe, Charakteristik, Verhalten, Potenzial und empfohlene Maßnahme.

## Visualisierungen

KI kann dir den perfekten Charttyp empfehlen – wenn du sagst, was du zeigen willst. Die fünf Visualisierungsziele: **Vergleich, Trend, Verteilung, Zusammenhang, Proportion**. Jedes Ziel hat einen idealen Charttyp.

Gib immer an: Daten, Ziel, Zielgruppe (Experten vs. Management). Fordere den besten Charttyp plus zwei Alternativen an, mit Achsenbeschriftung und farbenblind-freundlicher Farbempfehlung.

**Dashboard-Design:** Oben die 3-4 wichtigsten KPIs als Zahlen, Mitte die Trend-Charts, unten Detail-Tabellen mit Filtern. Definiere Warnschwellen (rot/gelb/grün) für jeden KPI.

## Berichterstellung

Die Berichtsstruktur, die für Management funktioniert:

1. **Executive Summary** – 3-5 Sätze, das Wichtigste
2. **KPI-Übersicht** – Tabelle: Ist vs. Soll vs. Vorperiode
3. **Highlights** – Was lief gut? (2-3 Punkte)
4. **Herausforderungen** – Was lief nicht gut? (2-3 Punkte)
5. **Ursachenanalyse** – Warum? Für die Top-Abweichung
6. **Empfehlungen** – Was tun wir? (2-3 konkrete Maßnahmen)
7. **Ausblick** – Was erwarten wir nächste Periode?

Der Schlüsselsatz: *"Sachlich, datengetrieben. Keine Floskeln wie 'positiver Trend' ohne Zahlen dahinter."*

## SQL und Datenbankabfragen

Für SQL-Generierung: Tabellenstruktur beschreiben, gewünschtes Ergebnis formulieren, Datenbank-Dialekt angeben (MySQL/PostgreSQL/BigQuery), und **Zeile-für-Zeile-Erklärung** anfordern plus Performance-Hinweise.

Für bestehende Schemata: Lass dir Entitäten, Beziehungen, typische Abfragen, Performance-Engpässe und Index-Empfehlungen erklären.

## Statistik und Umfragen

**Statistische Analyse:** Formuliere deine Hypothese in natürlicher Sprache, beschreibe deine Daten und Stichprobengröße. Frage nach dem geeigneten Test, den Voraussetzungen, der Interpretation und dem Code. Der Zusatz *"Erkläre alles so, dass jemand ohne Statistik-Studium es versteht"* macht den Unterschied.

**Umfragen analysieren:** Trenne quantitative Fragen (Verteilungen, Mittelwerte, Gruppenvergleiche) von offenen Fragen (Kategorisierung, Sentiment, auffällige Zitate). Am Ende: Top 5 Erkenntnisse, Überraschungen, Handlungsempfehlungen und methodische Einschränkungen.

## Best Practices für Datenanalyse mit KI

**1. Daten nie komplett hochladen.** Bei sensiblen Daten: Nur Struktur und anonymisierte Beispiele zeigen. Niemals echte Kundendaten, Personaldaten oder Finanzdaten in ein Cloud-LLM laden.

**2. Ergebnisse verifizieren.** KI kann rechnen – aber sie macht Fehler. Besonders bei Prozentrechnungen und Aggregationen. Stichprobenartig nachprüfen.

**3. Kontext geben.** "Analysiere diese Daten" ist zu wenig. Sag der KI, was du suchst, was du erwartest und was dich überraschen würde.

**4. Iterativ arbeiten.** Erster Prompt → Überblick. Zweiter Prompt → Deep Dive in auffällige Bereiche. Dritter Prompt → Handlungsempfehlungen.

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
