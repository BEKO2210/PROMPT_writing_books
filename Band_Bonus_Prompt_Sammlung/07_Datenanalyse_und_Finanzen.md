# Datenanalyse & Finanzen

## Daten-Check

```
Hier sind meine Daten:
"""[ERSTE 20 ZEILEN DER CSV/TABELLE]"""

Analysiere:
1. Spalten und ihre Bedeutung
2. Datentypen (Text/Zahl/Datum/Kategorie)
3. Fehlende Werte und Ausreißer
4. Mögliche Korrelationen
5. Welche Analysen bieten sich an?
```

## Explorative Analyse

```
Hier sind meine Daten:
"""[DATEN EINFÜGEN]"""

Erstelle eine explorative Analyse:
1. Zusammenfassung (Anzahl, Zeitraum, Min/Max/Durchschnitt)
2. Verteilungen (Auffälligkeiten, Schiefe, Ausreißer)
3. Trends (zeitlich, saisonal)
4. Zusammenhänge (Korrelationen)
5. Top 3 Insights + was als Nächstes untersuchen
```

## Chart-Empfehlung

```
Ich habe folgende Daten: [BESCHREIBUNG]
Ziel: [Vergleich/Trend/Verteilung/Zusammenhang/Proportion]
Zielgruppe: [Experten/Management/Kunden]

Empfiehl den besten Charttyp + 2 Alternativen.
Achsenbeschriftung, Farbempfehlung (farbenblind-freundlich),
Titel und Beschriftungen.
Code in [Python matplotlib/Excel/Google Sheets].
```

## SQL generieren

```
Tabellenstruktur:
[TABELLEN UND SPALTEN BESCHREIBEN]

Schreibe eine SQL-Abfrage für: [WAS WILLST DU WISSEN]
Datenbank: [MySQL/PostgreSQL/BigQuery]
Sortierung: [KRITERIUM]
Limit: Top [X] Ergebnisse
Zeitraum: [VON BIS]

Erkläre die Abfrage Zeile für Zeile.
Performance-Hinweise bei großen Datenmengen.
```

## Dashboard-Konzept

```
Erstelle ein Dashboard-Konzept für [ABTEILUNG/ZWECK].
Datenquellen: [WELCHE DATEN]
Nutzer: [WER SCHAUT DRAUF]
Aktualisierung: [Echtzeit/Täglich/Wöchentlich]

Layout:
OBEN: 3-4 KPI-Karten (Zahl + Trend)
MITTE: Trend-Charts und Vergleiche
UNTEN: Detail-Tabellen mit Filtern
Warnschwellen: Rot/Gelb/Grün für jeden KPI.
```

## Umfrage analysieren

```
Ich habe [ANZAHL] Umfrage-Antworten:
"""[DATEN]"""

Analysiere:
1. Quantitativ: Häufigkeiten, Mittelwerte, Gruppenvergleiche
2. Offene Fragen: Themen-Kategorisierung, Sentiment, Zitate
3. Top 5 Erkenntnisse
4. Überraschungen
5. Handlungsempfehlungen
6. Methodische Einschränkungen
```

## Jahresabschluss verstehen

```
Analysiere folgenden Jahresabschluss:
"""[GUV UND/ODER BILANZ]"""

1. Zusammenfassung für Nicht-Finanzler (3-5 Sätze)
2. Kennzahlen: Umsatzwachstum, Gewinnmarge, EBITDA,
   Eigenkapitalquote, Liquiditätsgrad, ROE
3. Stärken und Risiken
4. Branchenvergleich
5. Empfehlung fürs Management

Erkläre alle Kennzahlen verständlich.
```

## Cashflow-Prognose

```
Erstelle eine Cashflow-Prognose für [ZEITRAUM].
Kontostand: [BETRAG]
Erwartete Einnahmen: [AUFSCHLÜSSELUNG]
Fixkosten monatlich: [AUFSCHLÜSSELUNG]
Variable Kosten: [AUFSCHLÜSSELUNG]
Investitionen: [GEPLANT]

Monats-Tabelle: Einnahmen | Ausgaben | Saldo | Kumuliert.
Warnschwellen: Wann wird es kritisch?
Maßnahmen bei Liquiditätsengpass.
```

## Steuerfrage strukturieren

```
Steuerfrage: [IN EIGENEN WORTEN]
Rechtsform: [GMBH/EINZELUNTERNEHMEN/FREIBERUFLER]
Land: [DE/AT/CH]
Zeitraum: [JAHR]

Strukturiere für meinen Steuerberater:
1. Relevantes Steuergesetz
2. Grundregeln
3. Ausnahmen
4. Dokumentationspflichten
5. Fristen
6. Konkrete Fragen an den Steuerberater

NICHT: Steuerberatung. Vorbereitung für das Gespräch.
```

## Kennzahl erklären

```
Erkläre [FINANZKENNZAHL] für [ZIELGRUPPE].
z.B. EBITDA, Quick Ratio, P/E Ratio, CAC, LTV

1. Was misst sie? (1 Satz)
2. Formel + Rechenbeispiel
3. Was ist ein "guter" Wert? (branchenabhängig)
4. Was wenn zu hoch/zu niedrig?
5. Alltagsanalogie
```

## Persönliches Budget analysieren

```
Nettoeinkommen: [BETRAG]
Ausgaben: [LISTE ALLER AUSGABEN]

Analysiere:
1. Kategorien und Prozente
2. 50/30/20-Regel: Stimmt die Verteilung?
   (50% Bedürfnisse / 30% Wünsche / 20% Sparen)
3. Einsparpotenziale
4. Überproportionale Ausgaben
5. Sparrate: Ausreichend?
6. 3 sofort umsetzbare Tipps
Keine Anlageberatung.
```

## Belege kategorisieren

```
Kategorisiere folgende Ausgaben für die Buchhaltung:
"""[AUSGABENLISTE]"""

Pro Ausgabe:
1. Kategorie (SKR03/SKR04 oder Oberkategorie)
2. Vorsteuerabzug möglich? (Ja/Nein/Teilweise)
3. Betriebsausgabe? (Voll/Anteilig/Nein)
4. Besonderheiten (z.B. Bewirtung: 70% absetzbar)

Sortiere nach Kategorie. Erstelle Übersicht.
Hinweis: Endgültige Zuordnung durch Steuerberater bestätigen.
```

## Investor-Pitch Finanzslides

```
Erstelle Finanzslides für einen Investor-Pitch.
Unternehmen: [NAME, PHASE, BRANCHE]
Kennzahlen: [UMSATZ, KOSTEN, WACHSTUM]
Funding-Ziel: [BETRAG]
Verwendung: [WOFÜR]

Slides:
1. Marktgröße (TAM/SAM/SOM)
2. Geschäftsmodell
3. Unit Economics (CAC, LTV, Marge)
4. Finanz-Übersicht (Ist + 3-Jahres-Projektion)
5. Use of Funds
6. Milestones
Pro Slide: Kernaussage (1 Satz) + unterstützende Daten.
```

## Statistischen Test wählen

```
Hypothese: [IN NATÜRLICHER SPRACHE]
Daten: [BESCHREIBUNG]
Stichprobe: N = [ZAHL]
Variablen: [ABHÄNGIG/UNABHÄNGIG]

1. Welcher Test ist geeignet? Warum?
2. Voraussetzungen des Tests
3. Interpretation des Ergebnisses
4. Nullhypothese
5. Relevante Effektstärke
6. Code in [Python/R]

Alles so erklären, dass jemand ohne Statistik-Studium es versteht.
```

## Segmentierungsanalyse

```
Segmentiere meine Kundendaten nach [KRITERIUM].
Daten: [BESCHREIBUNG]
Ziel: [Kundenwert/Kaufverhalten/Churn-Risiko]

Pro Segment:
1. Name (beschreibend, z.B. "Power-User")
2. Größe (Anzahl und Prozent)
3. Charakteristik
4. Verhalten
5. Potenzial (Wachstum? Risiko?)
6. Empfohlene Maßnahme
```

## Preisgestaltung analysieren

```
Produkt: [BESCHREIBUNG]
Aktuelle Kunden: [ANZAHL]
Aktueller Preis: [BETRAG]
Geplante Änderung: [NEUER PREIS]

Analysiere:
1. Break-Even: Wie viele Kunden darf ich verlieren?
2. Preiswahrnehmung: Wie wirkt die Änderung?
3. Wettbewerbsreaktion: Was könnten andere tun?
4. Empfehlung: Sofort, gestaffelt oder gar nicht?
```

## Daten bereinigen

```
Meine Daten haben folgende Probleme:
[z.B. fehlende Werte, Duplikate, inkonsistente Formate]

Für jedes Problem:
1. Wie identifiziere ich es? (Query/Code)
2. Strategie zur Behebung
3. Risiken der Behebung
Code in [Python/SQL/Excel-Formeln].
```

## A/B-Test auswerten

```
A/B-Test Ergebnis:
Variante A: [METRIK] bei [N] Nutzern
Variante B: [METRIK] bei [N] Nutzern
Testzeitraum: [DAUER]

Analysiere:
1. Ist das Ergebnis statistisch signifikant?
2. Konfidenzintervall
3. Effektstärke (praktisch relevant?)
4. Empfehlung: B implementieren, weiter testen, oder verwerfen?
5. Was könnte das Ergebnis verfälschen?
```

## Automatischen Bericht erstellen

```
Erstelle einen [wöchentlichen/monatlichen] Bericht aus:
"""[DATEN]"""

Vergleich mit: [Vorwoche/Vormonat/Vorjahr]
Zielgruppe: [GESCHÄFTSFÜHRUNG/TEAM/KUNDEN]

1. Executive Summary (3-5 Sätze)
2. KPI-Übersicht (Ist vs. Soll vs. Vorperiode)
3. Highlights (2-3) und Herausforderungen (2-3)
4. Ursachenanalyse für Top-Abweichung
5. 2-3 konkrete Empfehlungen
6. Ausblick nächste Periode
Ton: Sachlich. Keine Floskeln ohne Zahlen.
```
