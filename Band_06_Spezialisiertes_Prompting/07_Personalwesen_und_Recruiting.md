# Kapitel 7: Personalwesen und Recruiting – KI als HR-Partner

HR-Abteilungen ertrinken in Text. Stellenausschreibungen, Bewerbungen, Feedback-Gespräche, Onboarding-Materialien, Policies, E-Mails an Kandidaten. KI kann einen großen Teil dieser Textarbeit übernehmen – aber hier gelten besondere Regeln.

Denn HR arbeitet mit Menschen. Und Fehler in HR betreffen Karrieren, Einkommen und Lebensumstände. Bias in einem KI-generierten Jobinserat kann ganze Bewerbergruppen ausschließen. Ein schlecht formuliertes Absageschreiben kann den Ruf deines Unternehmens ruinieren.

## Stellenausschreibungen

### Jobinserat erstellen

```
Erstelle eine Stellenausschreibung für [POSITION].

UNTERNEHMEN: [Name, Branche, Größe, Kultur]
POSITION: [Titel, Abteilung, Berichtet an]
STANDORT: [Ort / Remote / Hybrid]
GEHALT: [Bereich, falls angegeben]

STRUKTUR:
1. HOOK (2-3 Sätze): Warum ist dieser Job spannend?
   (Nicht: "Wir suchen..." sondern was den Job besonders macht)
2. AUFGABEN (5-7 Punkte): Was macht man konkret?
   (Verben am Anfang: "Du entwickelst...", "Du führst...")
3. PROFIL – MUSS (4-5 Punkte): Ohne geht es nicht
4. PROFIL – NICE TO HAVE (2-3 Punkte): Wäre toll
5. WIR BIETEN (5-7 Punkte): Echte Benefits, keine Floskeln
6. BEWERBUNGSPROZESS: Wie bewirbt man sich? Was passiert dann?

REGELN:
- Genderneutrale Sprache (oder m/w/d)
- Keine übertriebenen Anforderungen ("10 Jahre Erfahrung
  in einer 3 Jahre alten Technologie")
- Keine Buzzwords ohne Inhalt ("dynamisches Team",
  "flache Hierarchien" – nur wenn es stimmt)
- Konkret statt vage ("Budget von 500k€ verantworten"
  statt "Budgetverantwortung")
```

### Bias-Check für Stellenausschreibungen

```
Prüfe folgende Stellenausschreibung auf Bias:

"""[Stellenausschreibung einfügen]"""

PRÜFE AUF:
1. GENDER-BIAS: Werden Formulierungen verwendet, die
   ein Geschlecht bevorzugen? (z.B. "durchsetzungsstark"
   → eher männlich konnotiert)
2. ALTERS-BIAS: Schließen Formulierungen ältere oder
   jüngere Bewerber aus? (z.B. "Digital Native",
   "junges Team")
3. ERFAHRUNGS-BIAS: Sind die Anforderungen realistisch
   oder schließen sie Quereinsteiger unnötig aus?
4. KULTUR-BIAS: Setzen Formulierungen bestimmte
   kulturelle Hintergründe voraus?
5. DISABILITY-BIAS: Ist die Ausschreibung inklusiv
   formuliert?

Für jeden gefundenen Bias: Originaltext → Verbesserungsvorschlag.
```

## Bewerbermanagement

### Absageschreiben

```
Schreibe ein Absageschreiben für [SITUATION].

SITUATION: [Nach Bewerbungseingang / Nach Erstgespräch /
Nach finaler Runde / Position wurde gestrichen]
BEWERBER/IN: [Kontext, z.B. "sehr gute Bewerbung,
knapp gescheitert"]

TON: Wertschätzend, ehrlich, professionell.
Nicht: "Leider müssen wir Ihnen mitteilen..."
Sondern: Direkt, respektvoll, mit konkretem Grund
(wenn möglich).

ENTHALTEN:
1. Dank für die Bewerbung/das Gespräch
2. Klare Absage (nicht drumherum reden)
3. Wenn möglich: Konkreter Grund (nicht "andere
   Kandidaten passten besser")
4. Positives Feedback (wenn ehrlich möglich)
5. Ermutigung / Tür offen lassen (wenn aufrichtig)
6. Zeitrahmen bis zur endgültigen Entscheidung
   (falls noch nicht final)

LÄNGE: Max. 150 Wörter. Kürzer = respektvoller.
```

### Interview-Fragen generieren

```
Erstelle Interviewfragen für [POSITION].

INTERVIEW-RUNDE: [Erstgespräch / Fachgespräch / Kulturfit]
DAUER: [30/45/60 Min]

FRAGENKATEGORIEN:
1. EINSTIEG (2 Fragen): Warm-up, Motivation
2. FACHLICH (3-5 Fragen): Kompetenz prüfen
3. SITUATIV (3 Fragen): "Erzählen Sie von einer
   Situation, in der Sie..." (STAR-Methode)
4. KULTUR (2 Fragen): Passt die Person zum Team?
5. ABSCHLUSS (1-2 Fragen): Erwartungen, Fragen

FÜR JEDE FRAGE:
- Die Frage
- Was sie prüft
- Worauf in der Antwort achten (Grün-Flags / Red-Flags)
- Follow-up-Frage (wenn die Antwort oberflächlich ist)

VERMEIDE:
- Illegale Fragen (Familienplanung, Religion, etc.)
- Rätsel/Brainteaser (korrelieren nicht mit Leistung)
- "Wo sehen Sie sich in 5 Jahren?" (sagt nichts aus)
```

## Onboarding

### Onboarding-Plan

```
Erstelle einen Onboarding-Plan für [POSITION].

DAUER: [Erste Woche / Erster Monat / Erste 90 Tage]
UNTERNEHMEN: [Kontext]
TEAM: [Teamgröße, Arbeitsweise]

WOCHE 1: "Ankommen"
- Tag 1: [Begrüßung, Setup, Rundgang, Lunch mit Team]
- Tag 2-3: [Einführungen, Systeme, erste Aufgabe]
- Tag 4-5: [Erstes Mini-Projekt, Buddy-Gespräch]

MONAT 1: "Verstehen"
- Woche 2: [Prozesse kennenlernen]
- Woche 3: [Erste eigenständige Aufgaben]
- Woche 4: [Feedback-Gespräch, Zielvereinbarung]

TAG 30-90: "Beitragen"
- Monat 2: [Eigene Projekte übernehmen]
- Monat 3: [Volle Produktivität, 90-Tage-Review]

FÜR JEDEN MEILENSTEIN:
- Was wird erwartet?
- Wer ist Ansprechpartner?
- Woran erkennt man, dass es gut läuft?
- Was tun, wenn es nicht gut läuft?
```

## Mitarbeiterfeedback

### Feedback-Gespräch vorbereiten

```
Hilf mir, ein Feedback-Gespräch vorzubereiten.

MITARBEITER/IN: [Rolle, Seniorität, wie lange im Unternehmen]
ANLASS: [Regelmäßig / Anlassbezogen / Jahresgespräch]
POSITIVE ASPEKTE: [Was läuft gut? Konkrete Beispiele]
VERBESSERUNGSBEDARF: [Was muss besser werden? Konkrete Beispiele]
ZIEL: [Was soll nach dem Gespräch anders sein?]

ERSTELLE:
1. GESPRÄCHSLEITFADEN (Struktur, Zeitplan)
2. FORMULIERUNGSHILFEN für schwierige Punkte
   - Nicht: "Sie sind zu langsam"
   - Sondern: "Bei Projekt X lag die Deadline um 2 Wochen
     zurück. Was hat dazu geführt?"
3. FRAGEN für den/die Mitarbeiter/in
   (Selbsteinschätzung, Wünsche, Hindernisse)
4. ZIELVEREINBARUNG (SMART formuliert)
5. FOLLOW-UP-PLAN (Wann wird nachgehakt?)

TON: Wertschätzend, konkret, zukunftsorientiert.
Feedback nach der SBI-Methode:
Situation → Behavior → Impact.
```

### Zeugnis erstellen

```
Erstelle ein qualifiziertes Arbeitszeugnis.

MITARBEITER/IN: [Name, Position, Zeitraum]
AUFGABEN: [Haupttätigkeiten]
LEISTUNG: [Bewertung: sehr gut/gut/befriedigend/ausreichend]
SOZIALVERHALTEN: [Bewertung]
BEENDIGUNGSGRUND: [Auf eigenen Wunsch / Betriebsbedingt / ...]

ERSTELLE ein Zeugnis nach deutschen Standards:
1. Einleitung (Daten, Position)
2. Unternehmensbeschreibung (1-2 Sätze)
3. Aufgabenbeschreibung
4. Leistungsbeurteilung
5. Sozialverhalten (intern + extern)
6. Beendigungsformel
7. Schlussformel mit Zukunftswünschen

WICHTIG: Deutsche Arbeitszeugnisse verwenden eine
Codierte Sprache. Nutze die korrekte Zeugnis-Codierung
für die gewünschte Note.
Beispiel: "stets zur vollsten Zufriedenheit" = Note 1
"zur vollen Zufriedenheit" = Note 2
```

## HR-Policies

```
Erstelle eine Policy für [THEMA].

THEMEN:
[z.B. Remote Work / Social Media / Weiterbildung /
Reisekosten / Anti-Diskriminierung / Whistleblowing]

UNTERNEHMEN: [Branche, Größe, Kultur]
GELTUNGSBEREICH: [Für wen gilt die Policy?]

STRUKTUR:
1. Zweck und Geltungsbereich
2. Definitionen
3. Regeln/Richtlinien (klar, nummeriert)
4. Verantwortlichkeiten (Wer macht was?)
5. Konsequenzen bei Verstoß
6. Ansprechpartner
7. Inkrafttreten und Revision

SPRACHE: Klar, unmissverständlich, nicht juristisch
überladen. Mitarbeiter müssen es verstehen.

WICHTIG: Policy-Entwurf. Vor Einführung rechtlich und
durch den Betriebsrat (falls vorhanden) prüfen lassen.
```

---

## Übungen

### Übung 1: Stellenausschreibung
Erstelle eine Stellenausschreibung für eine Position, die du kennst. Prüfe sie danach mit dem Bias-Check-Prompt. Findest du versteckte Biases?

### Übung 2: Interview-Fragen
Generiere Interviewfragen für eine Position deiner Wahl. Sind die STAR-Fragen konkret genug? Würden die Follow-ups helfen?

### Übung 3: Feedback formulieren
Bereite ein (fiktives) Feedback-Gespräch vor. Achte darauf, dass die SBI-Methode eingehalten wird. Klingt es wie ein echtes Gespräch?

### Übung 4: Arbeitszeugnis
Lass ein Arbeitszeugnis für Note 2 erstellen. Prüfe die Zeugnis-Codierung – stimmen die Formulierungen mit der gewünschten Note überein?
