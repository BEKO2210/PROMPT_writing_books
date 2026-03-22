# Kapitel 6: Medizin und Gesundheit – KI im Kittel

**Disclaimer:** KI ist kein Arzt. Dieses Kapitel zeigt, wie medizinische Fachkräfte KI als Assistenten nutzen können – nicht als Ersatz für klinisches Urteil. KI darf keine Diagnosen stellen und keine Therapieentscheidungen treffen. Wenn du Patient bist: Besprich alles mit deinem Arzt.

Klarer kann ich es nicht sagen. Jetzt zum Inhalt.

## Wo KI in der Medizin hilft

| Aufgabe | KI-Eignung | Warum |
|---|---|---|
| Medizinische Texte vereinfachen | ★★★★★ | Kernkompetenz von LLMs |
| Differentialdiagnosen brainstormen | ★★★★☆ | Gut als Gedankenstütze, nicht als Entscheidung |
| Patientenkommunikation formulieren | ★★★★★ | Sprache und Ton anpassen |
| Fachliteratur zusammenfassen | ★★★★☆ | Mit Vorsicht (Halluzinationen prüfen) |
| Leitlinien-Zusammenfassungen | ★★★☆☆ | Nur als Einstieg, immer Original prüfen |
| Medikamenteninteraktionen prüfen | ★★☆☆☆ | Zu riskant für KI allein – Datenbanken nutzen |
| Therapieentscheidungen treffen | ☆☆☆☆☆ | Nein. Nie. Punkt. |

## Medizinische Texte für Patienten

### Befund übersetzen

```
Übersetze folgenden medizinischen Befund in
patientenverständliche Sprache:

"""[Befund einfügen]"""

REGELN:
- Sprachniveau: B1 Deutsch (kein Fachjargon)
- Jeder Fachbegriff wird beim ersten Auftreten in
  Klammern einfach erklärt
- Sätze max. 15 Wörter
- Keine Verharmlosung, aber auch keine Panikmache
- Sachlich, ruhig, klar
- Am Ende: "Was bedeutet das für mich?" (2-3 Sätze)
- Hinweis: "Bitte besprechen Sie offene Fragen mit
  Ihrem behandelnden Arzt."
```

### Aufklärungsbogen vereinfachen

```
Vereinfache folgenden Aufklärungsbogen für einen
medizinischen Eingriff:

"""[Aufklärungsbogen einfügen]"""

ZIEL: Patienten sollen VERSTEHEN, was passiert.
Nicht nur unterschreiben.

FORMAT:
1. WAS WIRD GEMACHT? (3-5 Sätze, einfache Sprache)
2. WARUM? (Indikation, einfach erklärt)
3. WIE LÄUFT ES AB? (Schritt für Schritt)
4. WELCHE RISIKEN GIBT ES? (Häufigkeit in einfachen
   Kategorien: häufig/selten/sehr selten)
5. WAS PASSIERT, WENN ICH ES NICHT MACHE? (Alternativen)
6. WAS MUSS ICH VORHER/NACHHER BEACHTEN?

SPRACHE: Einfaches Deutsch. Leichte Sprache wenn möglich.
Optional: Zweisprachig [Deutsch + andere Sprache].
```

## Differentialdiagnosen strukturieren

### DD-Brainstorming (für Ärzte)

```
KONTEXT: Ich bin Arzt und nutze KI als Gedankenstütze.
Dies ist keine klinische Entscheidung.

Patient stellt sich vor mit:
- Hauptbeschwerde: [Symptom]
- Seit: [Dauer]
- Begleitende Symptome: [Aufzählung]
- Vorerkrankungen: [Aufzählung]
- Medikation: [Aufzählung]
- Alter/Geschlecht: [Angabe]

Erstelle eine strukturierte Differentialdiagnose-Liste:

WAHRSCHEINLICH (häufige Ursachen):
1. [Diagnose] – Dafür spricht: / Dagegen spricht:
2. ...

WENIGER WAHRSCHEINLICH, ABER WICHTIG:
1. [Diagnose] – Warum nicht ausschließen:
2. ...

RED FLAGS (sofort abklären):
1. [Diagnose] – Warnsignale:

EMPFOHLENE DIAGNOSTIK:
1. [Untersuchung] – Was wird damit geprüft?
2. ...

WICHTIG: Dies ist ein Brainstorming-Tool, keine
klinische Entscheidungsunterstützung. Die finale
Beurteilung obliegt dem behandelnden Arzt.
```

## Patientenkommunikation

### Schwierige Gespräche vorbereiten

```
Hilf mir, ein schwieriges Patientengespräch vorzubereiten.

SITUATION: [z.B. Diagnosemitteilung, Therapieänderung,
schlechte Prognose, Non-Compliance ansprechen]

PATIENT: [Alter, Kontext, bisherige Kommunikation]

Erstelle einen Gesprächsleitfaden nach dem
SPIKES-Modell:
1. SETTING: Wie bereite ich den Rahmen vor?
2. PERCEPTION: Wie erfrage ich, was der Patient
   bereits weiß?
3. INVITATION: Wie frage ich, wie viel er wissen möchte?
4. KNOWLEDGE: Wie vermittle ich die Information?
   (Formulierungsvorschläge)
5. EMOTIONS: Wie reagiere ich auf emotionale Reaktionen?
   (Konkrete Sätze)
6. STRATEGY: Wie bespreche ich das weitere Vorgehen?

TON: Empathisch, ehrlich, nicht bevormundend.
Formulierungsvorschläge für schwierige Sätze.
```

### Arztbrief

```
Erstelle einen Arztbrief-Entwurf.

VON: [Facharzt/Klinik]
AN: [Hausarzt/Weiterbehandler]

PATIENT: [Initialen, Alter, Geschlecht]
DIAGNOSEN: [Aufzählung]
AUFNAHMEGRUND: [Warum?]
BEFUNDE: [Relevante Befunde]
THERAPIE: [Was wurde gemacht?]
EMPFEHLUNG: [Wie weiter?]

FORMAT:
- Standardisierter Arztbrief-Aufbau
- Medizinische Fachsprache (Arzt-zu-Arzt)
- Klar strukturiert
- Medikamentenliste mit Dosierung am Ende

WICHTIG: Dies ist ein ENTWURF. Der behandelnde
Arzt prüft und unterschreibt.
```

## Medizinische Fortbildung

### Fallvorstellung aufbereiten

```
Erstelle eine Fallvorstellung für eine klinische Fortbildung.

FACHGEBIET: [z.B. Innere Medizin, Chirurgie, Pädiatrie]
THEMA/DIAGNOSE: [Was soll gelernt werden?]
SCHWIERIGKEITSGRAD: [PJ-Studierende/Assistenzärzte/Fachärzte]

AUFBAU:
1. VORSTELLUNG (Anonymisiert):
   Alter, Geschlecht, Aufnahmegrund

2. ANAMNESE (schrittweise enthüllt):
   - Was fragt man zuerst?
   - Was erfährt man?

3. UNTERSUCHUNG:
   - Relevante Befunde
   - Nebenbefunde (Ablenkung)

4. DIAGNOSTIK:
   - Welche Untersuchungen anordnen?
   - Ergebnisse

5. DISKUSSIONSFRAGEN:
   - "Welche Differentialdiagnosen kommen in Frage?"
   - "Welche Untersuchung hat die höchste Priorität?"
   - "Wie würden Sie therapieren?"

6. AUFLÖSUNG:
   - Diagnose + Begründung
   - Therapie + Verlauf
   - Take-Home-Messages (3 Lernpunkte)
```

### Medizinische Konzepte erklären

```
Erkläre [MEDIZINISCHES KONZEPT] für [ZIELGRUPPE].

ZIELGRUPPE:
- Medizinstudierende im [X]. Semester
- ODER: Pflegekräfte
- ODER: Patienten (Laiensprache)
- ODER: Fachärzte eines anderen Fachgebiets

ERKLÄRE:
1. Pathophysiologie (Was passiert im Körper?)
2. Klinisches Bild (Wie äußert sich das?)
3. Diagnostik (Wie findet man es?)
4. Therapie (Was tut man dagegen?)
5. Prognose (Wie geht es aus?)

NIVEAU: Anpassen an Zielgruppe.
Für Studenten: Prüfungsrelevante Details markieren.
Für Patienten: Analogien und einfache Sprache.
```

## Gesundheitskommunikation

### Gesundheitsinformation erstellen

```
Erstelle eine Patienteninformation zu [ERKRANKUNG/THEMA].

ZIELGRUPPE: Patienten und Angehörige
SPRACHE: Einfaches Deutsch (B1)
LÄNGE: Max. 2 Seiten

STRUKTUR:
1. Was ist [Erkrankung]? (3-4 Sätze)
2. Wie erkennt man es? (Symptome, einfach)
3. Was kann man tun? (Behandlung, Selbsthilfe)
4. Wann zum Arzt? (Red Flags)
5. Wo gibt es Hilfe? (Anlaufstellen, Hotlines)

REGELN:
- Keine Panikmache
- Keine Verharmlosung
- Quellenbasiert (auf Leitlinien verweisen)
- Hinweis: "Diese Information ersetzt nicht den
  Arztbesuch"
```

## Ethik und Grenzen

Medizin-KI hat besondere ethische Anforderungen:

### Was du NIEMALS tun solltest:
1. **KI-Diagnosen als echte Diagnosen behandeln** – Immer ärztlich validieren
2. **Patientendaten in Cloud-LLMs eingeben** – DSGVO-Verstoß, Vertraulichkeitsbruch
3. **KI-generierte Medikamentenempfehlungen befolgen** – Interaktionen, Kontraindikationen, Dosierungen immer in Fachdatenbanken prüfen
4. **Patienten KI-generierte Texte ungeprüft geben** – Jeder Text muss von einem Mediziner freigegeben werden

### Datenschutz in der Medizin
- Gesundheitsdaten sind besonders geschützt (Art. 9 DSGVO)
- Keine echten Patientendaten in KI-Tools eingeben
- Anonymisierung ist Pflicht – und "Name entfernen" reicht nicht (Kombination aus Alter, Diagnose, Ort kann identifizieren)
- Lokale LLMs (z.B. Ollama) oder zertifizierte medizinische KI-Plattformen nutzen

---

## Übungen

### Übung 1: Befund übersetzen
Nimm einen medizinischen Befund (aus dem Internet oder einen eigenen) und lass ihn in Patientensprache übersetzen. Ist das Ergebnis verständlich UND korrekt?

### Übung 2: Patienteninformation
Erstelle eine Patienteninformation zu einer häufigen Erkrankung (z.B. Diabetes Typ 2, Bluthochdruck, Depression). Prüfe sie gegen eine offizielle Quelle (z.B. gesundheitsinformation.de).

### Übung 3: Gesprächsleitfaden
Erstelle einen Gesprächsleitfaden für ein schwieriges Patientengespräch. Sind die Formulierungsvorschläge empathisch und professionell?

### Übung 4: Fallvorstellung
Erstelle eine Fallvorstellung für ein Fachgebiet deiner Wahl. Sind die Diskussionsfragen lehrreich?
