# Kapitel 1: Bildung und E-Learning – KI im Klassenzimmer

Lehrer arbeiten zu viel. Das ist keine Übertreibung, das ist Fakt. Unterrichtsvorbereitung, Materialerstellung, Differenzierung, Korrekturen, Elternbriefe, Verwaltung. Ein 45-Minuten-Unterricht kostet oft 90 Minuten Vorbereitung.

KI kann das nicht alles lösen. Aber sie kann einen erheblichen Teil der Vorbereitungsarbeit übernehmen – wenn du weißt, wie.

## Unterrichtsvorbereitung

### Der Stundenplan-Prompt

```
Erstelle einen Unterrichtsentwurf für eine Einzelstunde (45 Min).

FACH: [Fach]
KLASSE: [Jahrgangsstufe, Schulform]
THEMA: [Thema der Stunde]
LERNZIEL: [Was sollen die SuS am Ende können?]
VORWISSEN: [Was wissen die SuS bereits?]

STRUKTUR:
1. Einstieg (5-8 Min): [Methode zur Aktivierung]
2. Erarbeitung (15-20 Min): [Kernphase]
3. Sicherung (10 Min): [Ergebnissicherung]
4. Transfer/Vertiefung (5-10 Min): [Anwendung]
5. Abschluss (3-5 Min): [Reflexion/Ausblick]

Für jede Phase: Lehreraktivität, Schüleraktivität,
Sozialform (EA/PA/GA/Plenum), Material/Medien.

DIFFERENZIERUNG: Gib für jede Kernphase Hinweise
für leistungsstarke und leistungsschwache SuS.
```

### Beispiel: Geschichtsunterricht

```
Erstelle einen Unterrichtsentwurf für eine Einzelstunde (45 Min).

FACH: Geschichte
KLASSE: 9. Klasse, Gymnasium
THEMA: Der Mauerbau 1961 – Ursachen und unmittelbare Folgen
LERNZIEL: SuS können die politischen Ursachen des Mauerbaus
benennen und die Auswirkungen auf die Berliner Bevölkerung
anhand von Quellen beurteilen.
VORWISSEN: Nachkriegsordnung, Teilung Deutschlands,
Gründung von BRD und DDR.

Einstieg: Bildimpuls (Foto vom 13. August 1961)
Erarbeitung: Quellenarbeit in Gruppen (3 verschiedene Quellen)
Sicherung: Gruppenpräsentation + Tafelanschrieb
Transfer: Diskussion: "Hätte der Mauerbau verhindert werden können?"

DIFFERENZIERUNG:
- Leistungsstark: Zusätzliche Quelle mit Gegenperspektive
- Leistungsschwach: Vorstrukturierter Analysebogen
```

## Arbeitsblätter und Materialien

### Der Arbeitsblatt-Prompt

```
Erstelle ein Arbeitsblatt für [FACH], [KLASSE].

THEMA: [Thema]
DAUER: [Bearbeitungszeit]
AUFBAU:
1. Einstiegsaufgabe (leicht, Aktivierung)
2. Hauptteil (3-4 Aufgaben, aufsteigend in der Schwierigkeit)
3. Zusatzaufgabe (für Schnelle)

AUFGABENTYPEN: [Mischung aus]
- Lückentext / Multiple Choice / Zuordnung
- Offene Fragen (kurz)
- Analyse/Beurteilung (eine komplexere Aufgabe)

FORMATIERUNG:
- Klare Nummerierung
- Platz für Antworten (markiert mit Linien)
- Punkteangabe pro Aufgabe
- Erwartungshorizont separat (für die Lehrkraft)
```

### Differenzierte Materialien

```
Erstelle dasselbe Arbeitsblatt in 3 Niveaustufen:

NIVEAU A (Grundlegend):
- Einfachere Sprache
- Mehr Hilfestellungen und Beispiele
- Geschlossene Aufgabenformate (MC, Lücke)
- Weniger Aufgaben

NIVEAU B (Erweitert):
- Standardformulierung
- Mix aus geschlossenen und offenen Aufgaben
- Transferaufgabe

NIVEAU C (Anspruchsvoll):
- Komplexere Sprache und Quellen
- Offene Aufgabenformate
- Beurteilungs- und Reflexionsaufgabe
- Zusätzliches Material

Kennzeichne die Niveaus NICHT auf dem Blatt
(keine Stigmatisierung). Nutze Farben oder Symbole.
```

## Quiz und Prüfungen

### Der Quiz-Generator

```
Erstelle ein Quiz mit [ANZAHL] Fragen zum Thema [THEMA].

FACH: [Fach]
KLASSE: [Klasse]
FRAGENTYPEN:
- [X] Multiple Choice (4 Optionen, 1 richtig)
- [X] Wahr/Falsch
- [X] Lückentext
- [X] Kurzantwort (1-2 Sätze)
- [X] Zuordnung

SCHWIERIGKEIT: [Mischung angeben, z.B. 30% leicht,
50% mittel, 20% schwer]

ANFORDERUNG:
- Bloom-Taxonomie-Level angeben (Wissen/Verstehen/
  Anwenden/Analysieren/Bewerten/Erschaffen)
- Keine Fangfragen
- Distraktoren bei MC sollen plausibel sein,
  aber klar falsch
- Lösungsschlüssel am Ende
```

### Klausur-Prompt (Oberstufe/Universität)

```
Erstelle eine Klausur (90 Min) für [FACH/KURS].

THEMA: [Themengebiet]
ANFORDERUNGSBEREICHE:
- AFB I (Reproduktion): ~30% → Definieren, Benennen, Beschreiben
- AFB II (Transfer): ~40% → Erklären, Analysieren, Vergleichen
- AFB III (Reflexion): ~30% → Beurteilen, Diskutieren, Stellung nehmen

STRUKTUR:
- Teil A: Kurzfragen (30 Punkte)
- Teil B: Quellenanalyse/Textarbeit (40 Punkte)
- Teil C: Erörterung/Essay (30 Punkte)

Erstelle:
1. Die Klausur (Schülerversion)
2. Den Erwartungshorizont (mit Punkteverteilung)
3. Bewertungskriterien für den Essay-Teil
```

## Feedback und Korrekturen

### Der Feedback-Prompt

```
Hier ist ein Schülertext:
"""[Text einfügen]"""

AUFGABENSTELLUNG war: [Original-Aufgabe]
KLASSE: [Klasse]

Gib Feedback in folgendem Format:

STÄRKEN (2-3 Punkte):
Was hat der/die Schüler/in gut gemacht?

VERBESSERUNGSPOTENZIAL (2-3 Punkte):
Was kann verbessert werden? Konkret und konstruktiv.
Keine vagen Aussagen wie "Mehr Tiefe" – sondern
"In Absatz 2 könnte ein Beispiel die These stützen."

NÄCHSTER SCHRITT (1 Punkt):
Was sollte der/die Schüler/in als Nächstes üben?

TON: Ermutigend aber ehrlich. Altersangemessen.
Wie eine Lehrkraft, die an den Schüler glaubt.
```

### Massenkorrektur-Assistent

```
Ich korrigiere [ANZAHL] Arbeiten zum Thema [THEMA].

Hier ist der Erwartungshorizont:
"""[Erwartungshorizont]"""

Für jeden der folgenden Schülertexte:
1. Punkte vergeben (nach Erwartungshorizont)
2. Zwei Stärken nennen
3. Zwei Verbesserungsvorschläge
4. Gesamtnote vorschlagen

WICHTIG: Ich prüfe und korrigiere dein Feedback.
Du bist der Vorschlag, nicht die finale Bewertung.

Schülertext 1:
"""[Text]"""
```

## Erklärungen und Vereinfachungen

### Komplexe Themen erklären

```
Erkläre [KONZEPT] für Schüler der [KLASSE].

REGELN:
- Fachbegriffe beim ersten Auftreten erklären
- Maximal 1 neuer Fachbegriff pro Absatz
- Alltagsbeispiele und Analogien verwenden
- Absätze max. 4 Sätze lang
- Am Ende: 3 Kontrollfragen zum Selbsttest

ANALOGIE-VORGABE: Vergleiche [KONZEPT] mit etwas
aus der Lebenswelt von [ALTER]-Jährigen.
```

### Texte vereinfachen

```
Vereinfache den folgenden Fachtext für [ZIELGRUPPE]:

"""[Originaltext]"""

REGELN:
- Satzlänge: max. 15 Wörter
- Keine Passivkonstruktionen
- Fremdwörter ersetzen oder in Klammern erklären
- Kernaussagen erhalten, Details weglassen
- Leseniveau: [z.B. B1 Deutsch, 6. Klasse, Einfache Sprache]

Erstelle zwei Versionen:
1. Vereinfacht (leicht verständlich)
2. Stark vereinfacht (Einfache Sprache / Leichte Sprache)
```

## E-Learning und digitale Formate

### Lernpfad erstellen

```
Erstelle einen Lernpfad (Selbstlernmaterial) für [THEMA].

ZIELGRUPPE: [Wer lernt?]
VORWISSEN: [Was wird vorausgesetzt?]
LERNZIEL: [Was können die Lernenden am Ende?]
DAUER: [Gesamtzeit, z.B. 4 Stunden]

STRUKTUR (pro Modul):
1. Einführungstext (max. 300 Wörter)
2. Kerninhalt (Erklärung + Beispiele)
3. Interaktive Elemente (Quiz, Zuordnung, Lückentext)
4. Zusammenfassung (Kernpunkte als Bullet-Liste)
5. Übergang zum nächsten Modul

MODULE:
- Modul 1: [Titel] (Grundlagen)
- Modul 2: [Titel] (Vertiefung)
- Modul 3: [Titel] (Anwendung)
- Modul 4: [Titel] (Zusammenfassung + Abschlusstest)
```

### Karteikarten / Flashcards

```
Erstelle [ANZAHL] Karteikarten zum Thema [THEMA].

FORMAT:
Vorderseite: Frage oder Begriff
Rückseite: Antwort oder Definition (max. 2 Sätze)

VERTEILUNG:
- 40% Definitionen/Fakten
- 30% Verständnisfragen ("Warum...?")
- 20% Anwendungsfragen ("Was passiert, wenn...?")
- 10% Vergleiche ("Unterschied zwischen X und Y?")

EXPORT: Formatiere als CSV (kompatibel mit Anki):
Frage;Antwort;Tag
```

## Elternkommunikation

### Elternbrief

```
Schreibe einen Elternbrief für [ANLASS].

SCHULFORM: [Grundschule/Gymnasium/...]
KLASSE: [Klasse]
INHALT: [Was soll kommuniziert werden?]

TON: Freundlich, professionell, klar.
Keine Fachsprache. Kurze Sätze.

STRUKTUR:
1. Begrüßung
2. Anlass (1-2 Sätze, kein Drumherumreden)
3. Details (Was, Wann, Wo, Was mitbringen?)
4. Rückmeldung (Abschnitt zum Unterschreiben)
5. Kontakt für Fragen

SPRACHE: [Deutsch / Einfaches Deutsch /
Optional: Zweisprachig Deutsch-Türkisch/Arabisch/...]
```

## Inklusion und Förderung

### Individueller Förderplan

```
Erstelle einen Vorschlag für einen Förderplan.

SCHÜLER/IN: [Beschreibung ohne echten Namen]
ALTER/KLASSE: [Klasse]
FÖRDERBEDARF: [z.B. Lese-Rechtschreib-Schwäche,
Dyskalkulie, DaZ, emotional-sozial, Hochbegabung]
STÄRKEN: [Was kann der/die Schüler/in gut?]
SCHWÄCHEN: [Wo liegt der Förderbedarf konkret?]

ERSTELLE:
1. 3 konkrete Förderziele (SMART formuliert)
2. Für jedes Ziel: 2 Maßnahmen (im Unterricht umsetzbar)
3. Materialvorschläge (konkrete Übungen)
4. Beobachtungskriterien (Woran erkenne ich Fortschritt?)
5. Evaluationszeitraum (Wann prüfe ich den Fortschritt?)

WICHTIG: Der Förderplan ist ein Vorschlag. Er ersetzt
keine sonderpädagogische Diagnostik.
```

---

## Übungen

### Übung 1: Unterrichtsentwurf
Erstelle einen Unterrichtsentwurf für dein Fach (oder ein Fach deiner Wahl). Nutze den vollständigen Prompt. Ist das Ergebnis direkt einsetzbar oder braucht es Anpassungen?

### Übung 2: Differenziertes Arbeitsblatt
Erstelle ein Arbeitsblatt in 3 Niveaustufen für ein Thema deiner Wahl. Vergleiche die Stufen – sind sie wirklich unterschiedlich oder nur oberflächlich angepasst?

### Übung 3: Quiz-Generator
Generiere ein 10-Fragen-Quiz mit verschiedenen Fragetypen. Prüfe die Distraktoren bei den MC-Fragen: Sind sie plausibel genug?

### Übung 4: Feedback schreiben
Nimm einen (eigenen oder fiktiven) Schülertext und lass KI-Feedback generieren. Ist der Ton angemessen? Sind die Vorschläge konkret genug?
