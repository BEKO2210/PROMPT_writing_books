# Kapitel 8: Reflexion und Selbstkorrektur – Das Modell als eigener Lektor

Im letzten Kapitel hast du Meta-Prompting kennengelernt: Prompts, die Prompts verbessern. Dieses Kapitel geht einen Schritt weiter. Hier bringst du das Modell dazu, seine eigene Arbeit systematisch zu überprüfen und Fehler zu korrigieren.

Der Unterschied zu Meta-Prompting: Meta-Prompting verbessert die *Qualität*. Reflexion korrigiert *Fehler*.

## Die Idee

Reflexion in LLMs basiert auf einer einfachen Beobachtung: Modelle sind besser darin, Fehler in einem Text zu finden, als einen fehlerfreien Text beim ersten Versuch zu schreiben.

Das kennst du von dir selbst. Wenn du einen Text schreibst, übersiehst du Tippfehler und logische Lücken. Wenn du denselben Text eine Stunde später nochmal liest, springt dich jeder Fehler an. Die "Betriebsblindheit" der Erstellung weicht dem frischen Blick der Prüfung.

Bei LLMs funktioniert das ähnlich. In der Generierungsphase fokussiert sich das Modell auf den nächsten Token. In der Reflexionsphase kann es den gesamten Text überblicken und Inkonsistenzen erkennen.

## Das Reflexion-Framework

Das Paper "Reflexion: Language Agents with Verbal Reinforcement Learning" (Shinn et al., 2023) formalisierte den Ansatz:

1. **Generieren:** Das Modell produziert eine Antwort
2. **Bewerten:** Die Antwort wird gegen Kriterien geprüft
3. **Reflektieren:** Das Modell analysiert, was falsch war
4. **Verbessern:** Das Modell erstellt eine korrigierte Version

Dieser Zyklus kann mehrfach durchlaufen werden, bis die Antwort die Qualitätskriterien erfüllt.

## Reflexion in einem einzigen Prompt

### Das Grundmuster

```
Aufgabe: [Deine Aufgabe]

Schritt 1 – ENTWURF:
Beantworte die Aufgabe.

Schritt 2 – PRÜFUNG:
Prüfe deinen Entwurf auf:
- Sachliche Fehler
- Logische Lücken
- Fehlende wichtige Punkte
- Widersprüche
- Unklare Formulierungen

Schritt 3 – KORREKTUR:
Erstelle eine korrigierte Version, die alle gefundenen
Probleme behebt. Markiere, was du geändert hast.
```

### Beispiel: Sachtext

```
Aufgabe: Erkläre, wie Photosynthese funktioniert.
Zielgruppe: 15-Jährige.

Schritt 1 – ENTWURF:
[Modell schreibt Erklärung]

Schritt 2 – PRÜFUNG:
Prüfe auf: Sachliche Korrektheit, Verständlichkeit
für 15-Jährige, Vollständigkeit.

Schritt 3 – KORREKTUR:
[Modell korrigiert und verbessert]
```

**Was typischerweise passiert:**
- Entwurf: Verwendet Fachbegriffe wie "Thylakoid-Membran" ohne Erklärung
- Prüfung: "Für 15-Jährige zu komplex. Thylakoid-Membran nicht erklärt."
- Korrektur: Ersetzt Fachbegriffe durch Alltagssprache, fügt Analogien hinzu

## Gezielte Reflexions-Checklisten

Die allgemeine Prüfung ("Ist das gut?") liefert vage Ergebnisse. Besser: Spezifische Checklisten.

### Für Texte

```
Prüfe den Text auf folgende Punkte:

□ FAKTEN: Sind alle Behauptungen korrekt? Welche kann
  ich nicht verifizieren?
□ LOGIK: Folgt die Argumentation? Gibt es Sprünge?
□ VOLLSTÄNDIGKEIT: Fehlt ein wichtiger Aspekt?
□ WIDERSPRÜCHE: Widerspricht sich der Text irgendwo?
□ TON: Passt der Ton zur Zielgruppe?
□ LÄNGE: Ist die Länge angemessen? Zu lang? Zu kurz?
□ STRUKTUR: Ist die Reihenfolge sinnvoll?

Für jedes Problem: Beschreibe es und schlage einen Fix vor.
```

### Für Code

```
Prüfe den Code auf:

□ KORREKTHEIT: Tut er, was er soll?
□ EDGE CASES: Was passiert bei leeren Eingaben, Null-Werten,
  sehr großen Zahlen?
□ FEHLERBEHANDLUNG: Werden Fehler sinnvoll abgefangen?
□ PERFORMANCE: Gibt es offensichtliche Performance-Probleme?
□ SICHERHEIT: Gibt es Injection-Risiken oder andere
  Sicherheitslücken?
□ LESBARKEIT: Versteht ein anderer Entwickler den Code?

Für jedes Problem: Erkläre es und zeige den Fix.
```

### Für Analysen

```
Prüfe die Analyse auf:

□ ANNAHMEN: Welche Annahmen wurden gemacht?
  Sind sie gerechtfertigt?
□ DATEN: Basiert die Analyse auf korrekten Daten?
□ KAUSALITÄT VS. KORRELATION: Werden Zusammenhänge
  als Ursache-Wirkung dargestellt, die keine sind?
□ GEGENARGUMENTE: Wurden Gegenargumente berücksichtigt?
□ BIAS: Ist die Analyse einseitig?
□ SCHLUSSFOLGERUNG: Folgt die Schlussfolgerung logisch
  aus der Analyse?
```

## Selbstkorrektur in der Praxis

### Praxis-Beispiel 1: Vertragsprüfung

```
Prüfe folgenden Vertragsentwurf für einen Freelancer-Auftrag:

"""
[Vertragstext]
"""

Phase 1 – ERSTE EINSCHÄTZUNG:
Ist der Vertrag grundsätzlich fair und vollständig?

Phase 2 – DETAILPRÜFUNG:
Prüfe Klausel für Klausel:
- Ist sie klar formuliert?
- Fehlen wichtige Regelungen?
- Gibt es Fallstricke für den Freelancer?
- Gibt es Fallstricke für den Auftraggeber?

Phase 3 – VERBESSERUNGSVORSCHLÄGE:
Für jedes gefundene Problem: Schlage eine
verbesserte Formulierung vor.

Phase 4 – ZUSAMMENFASSUNG:
Top 3 der wichtigsten Änderungen.
```

### Praxis-Beispiel 2: Business-Idee validieren

```
Bewerte folgende Geschäftsidee:

"[Deine Geschäftsidee]"

Runde 1 – ENTHUSIAST:
Beschreibe die Idee so positiv wie möglich.
Was sind die größten Chancen?

Runde 2 – SKEPTIKER:
Hinterfrage alles. Was sind die größten Risiken?
Warum könnte die Idee scheitern?

Runde 3 – REALITÄTSCHECK:
Prüfe, ob der Enthusiast die Risiken unterschätzt hat.
Prüfe, ob der Skeptiker die Chancen ignoriert hat.

Runde 4 – FINALE BEWERTUNG:
Basierend auf allen drei Perspektiven:
Bewertung auf einer Skala von 1-10 mit Begründung.
Nenne die 3 wichtigsten Dinge, die du zuerst klären
würdest, bevor du investierst.
```

### Praxis-Beispiel 3: Bewerbungsanschreiben

```
Schreibe ein Bewerbungsanschreiben für folgende Stelle:

Stelle: [Stellenbeschreibung]
Mein Profil: [Kurzprofil]

ENTWURF:
[Modell schreibt Anschreiben]

SELBSTKORREKTUR:
Lies das Anschreiben nochmal und prüfe:
1. Geht es konkret auf die Stellenanforderungen ein?
   (Nicht nur allgemeine Phrasen)
2. Zeigt es echten Mehrwert für das Unternehmen?
3. Klingt es nach einer echten Person oder nach
   einem KI-Template?
4. Ist der erste Satz so interessant, dass man weiterliest?
5. Ist der letzte Satz ein konkreter Call-to-Action?

FINALE VERSION:
[Korrigiertes Anschreiben]
```

## Die Chain-of-Verification (CoVe)

Eine spezielle Reflexionstechnik, die sich auf Faktentreue konzentriert:

```
Aufgabe: [Deine Frage/Aufgabe]

Schritt 1: Beantworte die Frage.

Schritt 2: Extrahiere aus deiner Antwort alle
faktischen Behauptungen (einzeln auflisten).

Schritt 3: Überprüfe jede Behauptung einzeln:
- Behauptung: [X]
  Korrekt? JA / NEIN / UNSICHER
  Falls NEIN/UNSICHER: Korrektur

Schritt 4: Erstelle eine korrigierte Antwort,
die nur verifizierte Fakten enthält. Kennzeichne
unsichere Angaben als solche.
```

### Beispiel

```
Erzähle mir über die Geschichte von Spotify.

Schritt 1: ANTWORT:
Spotify wurde 2006 von Daniel Ek und Martin Lorentzon
in Stockholm gegründet. Der Dienst ging 2008 in Europa
an den Start. 2011 expandierte Spotify in die USA.
2018 ging das Unternehmen an die Börse (NYSE). Heute
hat Spotify über 600 Millionen Nutzer.

Schritt 2: BEHAUPTUNGEN:
1. Gründung 2006
2. Gründer: Daniel Ek und Martin Lorentzon
3. Ort: Stockholm
4. Europastart: 2008
5. USA-Expansion: 2011
6. Börsengang: 2018 (NYSE)
7. Über 600 Millionen Nutzer

Schritt 3: VERIFIKATION:
1. Gründung 2006 → KORREKT
2. Daniel Ek und Martin Lorentzon → KORREKT
3. Stockholm → KORREKT
4. Europastart 2008 → KORREKT
5. USA-Expansion 2011 → KORREKT
6. Börsengang 2018 → KORREKT, aber NYSE stimmt nicht.
   Korrektur: Spotify ging an die NYSE als Direct Listing.
   Tatsächlich war es die NYSE – also doch korrekt.
7. 600+ Millionen Nutzer → UNSICHER. Stand meines Wissens
   hatte Spotify Anfang 2024 rund 615 Millionen Nutzer.
   Aktuellere Zahlen habe ich nicht.

Schritt 4: KORRIGIERTE ANTWORT:
[Antwort mit Unsicherheitsmarkierung bei Nutzerzahl]
```

CoVe ist besonders wertvoll bei:
- Historischen Darstellungen
- Biographien
- Statistiken und Zahlen
- Wissenschaftlichen Erklärungen

Es eliminiert Halluzinationen nicht vollständig, macht sie aber sichtbar.

## Reflexion bei kreativen Aufgaben

Reflexion ist nicht nur für Fakten nützlich. Auch bei kreativen Aufgaben hilft eine Überprüfungsrunde:

```
Schreibe eine Kurzgeschichte (300 Wörter):
Thema: Ein Programmierer findet einen Bug,
der die Realität verändert.

ENTWURF:
[Geschichte]

REFLEXION:
1. Hat die Geschichte einen klaren Spannungsbogen?
   (Setup, Konflikt, Auflösung)
2. Ist der Protagonist greifbar?
3. Ist das Ende befriedigend oder fühlt es sich
   abgebrochen an?
4. Gibt es einen Satz, der besonders schwach ist?
   → Umschreiben.
5. Gibt es einen Satz, der besonders stark ist?
   → Behalten und verstärken.

FINALE VERSION:
[Verbesserte Geschichte]
```

## Automatisierte Selbstkorrektur

Für fortgeschrittene Nutzer: Du kannst Reflexion als festen Bestandteil jedes Prompts einbauen:

### System-Prompt für Selbstkorrektur

```
Du bist ein Assistent mit eingebauter Qualitätskontrolle.

Für JEDE Antwort, die du gibst:
1. Schreibe zuerst deine Antwort
2. Prüfe sie intern auf: Sachfehler, Lücken, Klarheit
3. Wenn du Probleme findest, korrigiere sie BEVOR du
   die Antwort abschickst
4. Markiere korrigierte Stellen mit [korrigiert]
5. Gib am Ende einen Confidence Score (0-100%)

Wenn dein Confidence Score unter 70% liegt, sag das
explizit und erkläre, warum du unsicher bist.
```

Das als System-Prompt oder Custom Instruction einzurichten bedeutet: Jede Antwort durchläuft automatisch einen Reflexionsprozess.

## Grenzen der Selbstkorrektur

### Grenze 1: Das Modell weiß nicht, was es nicht weiß
Wenn eine Halluzination plausibel klingt, wird sie im Reflexionsschritt nicht unbedingt entdeckt. Das Modell prüft gegen sein Wissen – und wenn das Wissen falsch ist, bleibt die Halluzination bestehen.

### Grenze 2: Über-Korrektur
Manchmal korrigiert das Modell etwas Richtiges zu etwas Falschem. Besonders bei Grenzfällen, wo es unsicher ist, kann es die richtige Antwort durch eine falsche ersetzen.

### Grenze 3: Bestätigungs-Bias
Das Modell neigt dazu, seine eigene Arbeit zu bestätigen. "Ja, das sieht gut aus" kommt häufiger als ehrliche Kritik. Gegenmaßnahme: Explizit harte Kritik fordern.

### Grenze 4: Token-Kosten
Reflexion verdoppelt (oder verdreifacht) die Antwortlänge. Bei API-Nutzung heißt das: doppelte Kosten. Nutze Reflexion gezielt, nicht bei jeder Antwort.

## Reflexion vs. Self-Consistency

Beides sind Methoden, um die Qualität zu erhöhen. Aber sie arbeiten unterschiedlich:

| Reflexion | Self-Consistency |
|---|---|
| Ein Durchlauf mit Prüfung | Mehrere unabhängige Durchläufe |
| Findet qualitative Fehler | Findet quantitative Fehler |
| Verbessert Texte, Analysen, Code | Verbessert Berechnungen, Fakten |
| "Ist das gut?" | "Ist das richtig?" |
| Kostet ~2x Tokens | Kostet 3-5x Tokens |

Ideal: Kombiniere beide. Self-Consistency für die Antwort, Reflexion für die Qualität.

---

## Übungen

### Übung 1: Faktencheck mit CoVe
Lass das Modell einen kurzen Text über ein Thema schreiben, das du gut kennst. Dann lass es CoVe durchführen. Hat es seine eigenen Fehler gefunden? Welche hat es übersehen?

### Übung 2: Code-Reflexion
Lass das Modell eine Programmieraufgabe lösen (z.B. eine Funktion, die prüft, ob eine Klammer-Sequenz gültig ist). Dann lass es den Code mit der Code-Checkliste prüfen. Hat es Bugs gefunden?

### Übung 3: Drei-Runden-Reflexion
Wähle eine Aufgabe und führe 3 Reflexionsrunden durch. Vergleiche Version 1, 2 und 3. Ab welcher Runde sinkt der Verbesserungseffekt?

### Übung 4: Selbstkorrektur-System-Prompt
Richte den automatischen Selbstkorrektur-System-Prompt ein und nutze ihn einen Tag lang für alle Aufgaben. Beobachte: Bei welchen Aufgaben hilft die automatische Reflexion? Bei welchen ist sie überflüssig?
