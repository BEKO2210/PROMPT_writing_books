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
| Medikamenteninteraktionen prüfen | ★★☆☆☆ | Zu riskant – Fachdatenbanken nutzen |
| Therapieentscheidungen treffen | ☆☆☆☆☆ | Nein. Nie. Punkt. |

## Medizinische Texte für Patienten

### Befund übersetzen

Der häufigste Anwendungsfall: Einen medizinischen Befund in Patientensprache übersetzen. Die Regeln: Sprachniveau B1, Fachbegriffe beim ersten Auftreten erklären, Sätze max. 15 Wörter, keine Verharmlosung und keine Panikmache. Am Ende immer: *"Was bedeutet das für mich?"* und *"Bitte besprechen Sie offene Fragen mit Ihrem behandelnden Arzt."*

### Aufklärungsbogen vereinfachen

Aufklärungsbögen sind oft unverständlich. Die Struktur für eine vereinfachte Version: Was wird gemacht? → Warum? → Wie läuft es ab? → Welche Risiken? (in einfachen Häufigkeitskategorien) → Was passiert, wenn ich es nicht mache? → Was muss ich vorher/nachher beachten? Bei Bedarf zweisprachig anfordern.

## Differentialdiagnosen strukturieren

Für Ärzte als Gedankenstütze: Symptome, Dauer, Begleitsymptome, Vorerkrankungen, Medikation, Alter/Geschlecht angeben. Dann eine strukturierte DD-Liste anfordern in drei Kategorien:

- **Wahrscheinlich** – häufige Ursachen, mit "Dafür spricht / Dagegen spricht"
- **Weniger wahrscheinlich, aber wichtig** – nicht ausschließen
- **Red Flags** – sofort abklären

Plus empfohlene Diagnostik mit Begründung. Immer mit: *"Dies ist ein Brainstorming-Tool, keine klinische Entscheidungsunterstützung."*

## Patientenkommunikation

### Schwierige Gespräche vorbereiten

Das **SPIKES-Modell** für schwierige Gespräche: Setting (Rahmen vorbereiten), Perception (Was weiß der Patient?), Invitation (Wie viel will er wissen?), Knowledge (Information vermitteln), Emotions (auf Reaktionen reagieren), Strategy (weiteres Vorgehen). Für jede Phase konkrete Formulierungsvorschläge anfordern.

### Arztbrief

Für den Arztbrief-Entwurf: Von/An, Patient (nur Initialen), Diagnosen, Aufnahmegrund, Befunde, Therapie, Empfehlung. Medizinische Fachsprache (Arzt-zu-Arzt), Medikamentenliste mit Dosierung am Ende. Immer: *"Dies ist ein ENTWURF. Der behandelnde Arzt prüft und unterschreibt."*

## Medizinische Fortbildung

**Fallvorstellungen** für klinische Fortbildungen aufbereiten: Vorstellung (anonymisiert) → Anamnese (schrittweise enthüllt) → Untersuchung (mit Nebenbefunden als Ablenkung) → Diagnostik → Diskussionsfragen → Auflösung mit Take-Home-Messages.

**Konzepte erklären:** Niveau an die Zielgruppe anpassen – Studierende (prüfungsrelevante Details markieren), Pflegekräfte (praktisch relevant), Patienten (Analogien und einfache Sprache), Fachärzte anderer Gebiete (fachübergreifend). Schema: Pathophysiologie → Klinik → Diagnostik → Therapie → Prognose.

## Gesundheitskommunikation

Patienteninformationen in fünf Abschnitten: Was ist es? → Wie erkennt man es? → Was kann man tun? → Wann zum Arzt? (Red Flags) → Wo gibt es Hilfe? Max. 2 Seiten, einfaches Deutsch, quellenbasiert. Immer: *"Diese Information ersetzt nicht den Arztbesuch."*

## Ethik und Grenzen

### Was du NIEMALS tun solltest:
1. **KI-Diagnosen als echte Diagnosen behandeln** – Immer ärztlich validieren
2. **Patientendaten in Cloud-LLMs eingeben** – DSGVO-Verstoß, Vertraulichkeitsbruch
3. **KI-generierte Medikamentenempfehlungen befolgen** – Interaktionen und Dosierungen immer in Fachdatenbanken prüfen
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
Erstelle eine Patienteninformation zu einer häufigen Erkrankung (z.B. Diabetes Typ 2, Bluthochdruck). Prüfe sie gegen eine offizielle Quelle (z.B. gesundheitsinformation.de).

### Übung 3: Gesprächsleitfaden
Erstelle einen Gesprächsleitfaden für ein schwieriges Patientengespräch. Sind die Formulierungsvorschläge empathisch und professionell?

### Übung 4: Fallvorstellung
Erstelle eine Fallvorstellung für ein Fachgebiet deiner Wahl. Sind die Diskussionsfragen lehrreich?
