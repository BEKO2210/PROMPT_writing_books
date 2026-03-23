# Kapitel 9: Branchenübergreifende Prinzipien – Was überall gilt

Acht Branchen. Acht Kapitel. Hunderte spezifische Prompts. Aber unter der Oberfläche gelten überall dieselben Prinzipien.

Dieses Kapitel destilliert die universellen Regeln für spezialisiertes Prompting – egal in welcher Branche du arbeitest.

## Prinzip 1: Fachsprache rein, Fachsprache raus

KI versteht Fachsprache. Und sie produziert bessere Ergebnisse, wenn du sie verwendest.

```
SCHLECHT:
"Erklär mir, was mit meinen Blutwerten los ist."

GUT:
"Interpretiere folgende Laborwerte: Hb 11,2 g/dl,
MCV 72 fl, Ferritin 8 ng/ml. Welche Differentialdiagnosen
ergeben sich bei einer 35-jährigen Patientin?"
```

Die Fachsprache signalisiert dem Modell: "Ich bin vom Fach. Antworte auf meinem Niveau." Das reduziert generische Antworten und erhöht die Fachtiefe.

### Die Zwei-Stufen-Methode

Wenn du selbst kein Experte bist:

```
Stufe 1: "Erkläre mir [Thema] in Fachsprache,
als wäre ich ein [Berufsbezeichnung]."

Stufe 2: "Jetzt übersetze das in einfache Sprache,
die meine Kunden/Schüler/Patienten verstehen."
```

So bekommst du die fachliche Tiefe UND die verständliche Version.

## Prinzip 2: Rollen mit Fachexpertise

Du kennst Rollen aus Band 1. Im spezialisierten Prompting werden Rollen noch wichtiger:

```
Du bist ein erfahrener [BERUF] mit [X] Jahren
Berufserfahrung in [SPEZIALGEBIET]. Du arbeitest
für [ART VON UNTERNEHMEN/INSTITUTION].

DEIN ANSATZ:
- [Methodisch/Konservativ/Pragmatisch]
- [Welche Standards befolgst du?]
- [Welche Fehler vermeidest du besonders?]
```

### Beispiele für spezialisierte Rollen

| Branche | Rolle |
|---|---|
| Bildung | "Gymnasiallehrerin, 15 Jahre, Mathe/Physik, NRW" |
| Marketing | "Performance Marketing Manager, B2B SaaS, 50k€ Monatsbudget" |
| Datenanalyse | "Senior Data Analyst, E-Commerce, Python/SQL, arbeitet mit nicht-technischem Management" |
| Wissenschaft | "Postdoc, Sozialpsychologie, quantitative Methoden, publiziert in Tier-1-Journals" |
| Recht | "Fachanwalt für Arbeitsrecht, mittelständische Unternehmen, 10 Jahre Erfahrung" |
| Medizin | "Hausarzt, Landarztpraxis, breites Patientenspektrum, pragmatischer Ansatz" |
| HR | "Head of People, Tech-Scale-up, 200 Mitarbeiter, remote-first" |
| Finanzen | "CFO eines Mittelständlers, produzierendes Gewerbe, Fokus auf Cashflow" |

Je spezifischer die Rolle, desto spezifischer die Antworten.

## Prinzip 3: Kontext ist König (besonders in Fachbereichen)

In Band 1 hast du gelernt, dass Kontext wichtig ist. In Fachbereichen ist er unverzichtbar.

### Der Kontext-Stack

```
BRANCHE: [In welchem Feld arbeiten wir?]
REGULIERUNG: [Welche Gesetze/Standards gelten?]
UNTERNEHMEN: [Größe, Kultur, Branche]
ZIELGRUPPE: [Wer soll das Ergebnis lesen/nutzen?]
VORWISSEN: [Was weiß die Zielgruppe bereits?]
FORMAT: [Welches Dokument wird erwartet?]
EINSCHRÄNKUNGEN: [Was darf NICHT im Ergebnis stehen?]
```

### Beispiel: Derselbe Prompt, anderer Kontext

```
"Erstelle einen Bericht über unsere Quartalszahlen."

Kontext A (Vorstand):
→ Executive Summary, KPIs, Abweichungsanalyse, Empfehlungen. 2 Seiten.

Kontext B (Investor):
→ Wachstumsstory, Unit Economics, Marktposition, Projektion. 5 Slides.

Kontext C (Team):
→ Transparente Zahlen, Kontext zu Erfolgen und Herausforderungen, nächste Schritte. Lockerer Ton.

Kontext D (Finanzamt):
→ Formale Berichterstattung nach HGB/IFRS. Keine Interpretation.
```

Derselbe Datensatz, vier komplett verschiedene Dokumente. Der Kontext bestimmt alles.

## Prinzip 4: Halluzinationen sind hier gefährlich

In einem Blogpost ist eine falsche Zahl peinlich. In einem Rechtsgutachten ist sie ein Haftungsfall. In einer medizinischen Empfehlung potenziell lebensbedrohlich.

### Die Verifikations-Checkliste

Für jeden fachlichen KI-Output:

- [ ] **Zahlen prüfen.** Jede Zahl, jede Berechnung, jede Statistik.
- [ ] **Quellen prüfen.** Existiert die zitierte Quelle? Sagt sie das, was behauptet wird?
- [ ] **Gesetze prüfen.** Ist die genannte Rechtsnorm aktuell? Korrekt zitiert?
- [ ] **Fachbegriffe prüfen.** Werden sie korrekt verwendet?
- [ ] **Empfehlungen hinterfragen.** Basiert die Empfehlung auf den Daten oder auf allgemeinem "Gesundem Menschenverstand"?

### Der Verifikations-Prompt

```
Prüfe deine eigene Antwort:
1. Welche Fakten hast du genannt, bei denen du dir
   nicht 100% sicher bist? Markiere sie.
2. Welche Quellen hast du implizit vorausgesetzt?
   Nenne sie explizit.
3. Gibt es alternative Interpretationen, die du
   nicht erwähnt hast?
4. Was könnte an deiner Antwort falsch sein?
```

## Prinzip 5: Disclaimer sind nicht optional

In regulierten Bereichen gehört ein Disclaimer zum Output:

```
Füge am Ende jedes [rechtlichen/medizinischen/
finanziellen] Outputs folgenden Hinweis hinzu:

"Hinweis: Diese Information wurde mit Unterstützung
von KI erstellt und dient ausschließlich der Orientierung.
Sie ersetzt keine [rechtliche Beratung / ärztliche
Konsultation / professionelle Finanzberatung].
Bitte konsultieren Sie einen [Fachanwalt / Arzt /
Steuerberater] für Ihre individuelle Situation."
```

Das ist keine Formalität. Das ist Verantwortung.

## Prinzip 6: Datenschutz bei fachlichen Daten

### Was du NIEMALS in ein Cloud-LLM laden solltest:
- Echte Patientendaten
- Echte Mandantendaten
- Steuerunterlagen mit Klarnamen
- Personaldaten mit Klarnamen
- Unveröffentlichte Finanzzahlen
- Geschäftsgeheimnisse

### Alternativen:
1. **Anonymisieren** – Namen, Adressen, Kontonummern durch Platzhalter ersetzen
2. **Aggregieren** – Statt Einzeldaten Zusammenfassungen verwenden
3. **Lokale LLMs** – Ollama, LM Studio oder andere lokale Modelle für sensible Daten
4. **Enterprise-Versionen** – ChatGPT Enterprise, Claude Team/Enterprise mit Datenschutzgarantie

## Prinzip 7: Vom Fachexperten zum Prompt-Experten

Du bist Experte in DEINEM Fach. KI ist das Werkzeug. Die besten Ergebnisse kommen von Menschen, die beides können – fachlich urteilen UND gut prompten.

### Der Experten-Workflow

```
1. DU definierst die Frage (Fachexpertise)
2. KI liefert einen Entwurf (Geschwindigkeit)
3. DU prüfst auf Korrektheit (Fachexpertise)
4. KI überarbeitet nach deinem Feedback (Iteration)
5. DU gibst frei (Verantwortung)
```

Die Schritte 1, 3 und 5 sind DEINE. Die kann keine KI übernehmen. Nicht weil sie es nicht könnte, sondern weil die Verantwortung bei dir liegt.

## Prinzip 8: Prompt-Bibliothek aufbauen

Nach diesem Kapitel hast du dutzende Prompt-Templates gesehen. Die nützlichsten solltest du speichern.

### Aufbau einer Fach-Prompt-Bibliothek

```
KATEGORIE: [z.B. Vertragsrecht, Patientenkommunikation]
PROMPT-NAME: [z.B. "Vertragsprüfung Standard"]
TEMPLATE: [Der Prompt mit [PLATZHALTERN]]
VARIABLEN: [Was muss eingesetzt werden?]
BEISPIEL: [Ein ausgefülltes Beispiel]
QUALITÄTSCHECK: [Worauf achte ich beim Ergebnis?]
LETZTE AKTUALISIERUNG: [Datum]
```

Speichere sie dort, wo du schnell darauf zugreifen kannst – Notion, Obsidian, ein Git-Repository, oder einfach eine Textdatei.

---

## Übungen

### Übung 1: Fachsprache testen
Schreibe denselben Prompt einmal mit und einmal ohne Fachsprache. Vergleiche die Ergebnisse. Wie stark ist der Unterschied?

### Übung 2: Kontext-Variation
Nimm einen Prompt und variiere nur den Kontext (Zielgruppe, Format, Unternehmensgröße). Wie verändert sich das Ergebnis?

### Übung 3: Halluzinations-Jagd
Generiere einen fachlichen Text und prüfe ihn systematisch auf Fehler. Findest du welche? Wie schwerwiegend sind sie?

### Übung 4: Prompt-Bibliothek starten
Erstelle die ersten 5 Einträge deiner persönlichen Fach-Prompt-Bibliothek. Für Prompts, die du regelmäßig nutzen würdest.
