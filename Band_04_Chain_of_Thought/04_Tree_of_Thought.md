# Kapitel 4: Tree-of-Thought – Wenn ein Denkpfad nicht reicht

Chain-of-Thought denkt linear: A → B → C → Ergebnis. Das funktioniert bei vielen Aufgaben großartig. Aber manche Probleme haben nicht einen einzigen Lösungsweg, sondern mehrere. Und manchmal ist der erste Weg, den das Modell einschlägt, eine Sackgasse.

Tree-of-Thought (ToT) löst genau dieses Problem.

## Die Idee

Stell dir vor, du spielst Schach. Ein guter Schachspieler überlegt nicht nur einen Zug, sondern denkt mehrere Züge parallel durch:

- "Wenn ich den Springer ziehe, dann kann mein Gegner den Läufer nehmen..."
- "Wenn ich stattdessen die Dame ziehe, dann schütze ich den Bauern..."
- "Wenn ich rochiere, dann bringe ich den König in Sicherheit..."

Er bewertet jeden Pfad und wählt den besten. Tree-of-Thought macht genau das mit LLMs.

Das Paper von Yao et al. (2023) – "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" – formalisierte diese Idee. Statt einem linearen Denkpfad erstellt das Modell einen Baum aus möglichen Gedanken, bewertet jeden Zweig und verfolgt die vielversprechendsten weiter.

## CoT vs. ToT – Der Unterschied

| Chain-of-Thought | Tree-of-Thought |
|---|---|
| Ein Denkpfad | Mehrere parallele Denkpfade |
| Linear: A → B → C | Verzweigt: A → B₁ / B₂ / B₃ → C |
| Einmal denken | Denken, bewerten, weiterdenken |
| Schnell | Langsamer, aber gründlicher |
| Gut für Aufgaben mit klarem Lösungsweg | Gut für Aufgaben mit mehreren möglichen Ansätzen |
| Scheitert bei Sackgassen | Kann aus Sackgassen zurückkehren |

Der entscheidende Unterschied: CoT ist ein Zug. ToT ist eine Partie.

## Der ToT-Prozess

Tree-of-Thought besteht aus vier Phasen:

### Phase 1: Generierung
Das Modell erzeugt mehrere mögliche nächste Schritte (Gedanken/Ansätze).

### Phase 2: Bewertung
Jeder Schritt wird bewertet: Wie vielversprechend ist dieser Ansatz?

### Phase 3: Auswahl
Die besten Ansätze werden weiterverfolgt, die schlechten verworfen.

### Phase 4: Expansion
Von den ausgewählten Ansätzen werden wieder neue Schritte generiert – bis eine Lösung gefunden ist.

Das wiederholt sich, bis das Modell eine zufriedenstellende Lösung hat.

## ToT mit einem einzigen Prompt

In der Forschung wird ToT oft als komplexes System mit mehreren API-Calls implementiert. Aber du kannst die Kernidee in einem einzigen Prompt umsetzen. Hier ist das Grundmuster:

```
Aufgabe: [Deine Aufgabe]

Löse das Problem mit der Tree-of-Thought-Methode:

1. ERKUNDEN: Generiere 3 verschiedene Lösungsansätze.
   Beschreibe jeden kurz (2-3 Sätze).

2. BEWERTEN: Analysiere jeden Ansatz.
   Was sind die Stärken? Was sind die Schwächen?
   Wie wahrscheinlich ist Erfolg (1-10)?

3. VERTIEFEN: Wähle den besten Ansatz und arbeite
   ihn detailliert aus.

4. PRÜFEN: Überprüfe dein Ergebnis. Hättest du
   einen anderen Ansatz wählen sollen? Wenn ja, warum?
```

Das ist kein vollständiger ToT-Algorithmus, aber es fängt die Kernidee ein: Mehrere Wege erkunden, bewerten, den besten wählen.

## Praxis-Beispiel 1: Strategische Entscheidung

**Aufgabe:**
```
Unser SaaS-Startup hat 500 zahlende Kunden (Durchschnittspreis
49 Euro/Monat). Das Wachstum stagniert bei 3% pro Monat.
Wir haben 200.000 Euro Runway. Was tun?

Löse das mit der Tree-of-Thought-Methode:

1. ERKUNDEN: Generiere 3 verschiedene Strategien
2. BEWERTEN: Analysiere jede Strategie (Stärken, Schwächen,
   Erfolgschancen, Risiko)
3. VERTIEFEN: Arbeite die beste Strategie aus
   (konkrete Schritte, Timeline, Budget)
4. PRÜFEN: Was könnte schiefgehen? Plan B?
```

**Mögliches Ergebnis:**

```
1. ERKUNDEN:

Strategie A – Growth Hacking:
Aggressives Marketing mit Fokus auf virale Mechanismen.
Referral-Programm, Content Marketing, Social Proof.
Ziel: Wachstumsrate auf 10%/Monat steigern.

Strategie B – Upmarket gehen:
Preiserhöhung und Enterprise-Features. Statt mehr Kunden
mehr Umsatz pro Kunde. Ziel: Durchschnittspreis auf
99 Euro/Monat steigern.

Strategie C – Nische dominieren:
Auf eine spezifische Branche fokussieren, dort der
unangefochtene Marktführer werden. Spezialisierte
Features, gezielte Partnerschaften.

2. BEWERTEN:

Strategie A:
+ Schnell sichtbare Ergebnisse
+ Bewährte Taktiken
- Teuer (bezahltes Marketing verbrennt Runway)
- Unsicher (Viralität ist nicht planbar)
- Churn könnte steigen (schnell gewonnene Kunden churnen oft)
Erfolgschance: 5/10

Strategie B:
+ Erhöht Umsatz ohne neue Kunden
+ Verbessert Unit Economics
- Risiko: bestehende Kunden könnten kündigen
- Enterprise-Sales sind lang und teuer
- Braucht Feature-Entwicklung
Erfolgschance: 6/10

Strategie C:
+ Klarer Differenzierungsvorteil
+ Höhere Conversion durch Spezialisierung
+ Word-of-mouth in Nischen ist stark
- Limitiert den adressierbaren Markt
- Braucht tiefes Branchenwissen
Erfolgschance: 7/10

3. VERTIEFEN: Strategie C

Monat 1-2: Analyse
- Bestehende Kunden analysieren: Welche Branche ist überrepräsentiert?
- 20 Kundeninterviews: Was fehlt euch?
- Wettbewerbsanalyse in dieser Nische
Budget: 10.000 Euro (Analyse-Tools, Interview-Incentives)

Monat 3-4: Spezialisierung
- 3-5 branchenspezifische Features entwickeln
- Landing Page für die Nische
- Case Studies mit bestehenden Kunden
Budget: 40.000 Euro (Entwicklung)

Monat 5-8: Go-to-Market
- Content Marketing für die Nische (Blog, Whitepaper)
- Branchenevents und Messen
- Partnerschaften mit Branchenverbänden
- Gezielte LinkedIn-Ads
Budget: 60.000 Euro (Marketing)

Monat 9-12: Skalieren
- Feedback einarbeiten
- Preisanpassung für den Nischenplan
- Zweite Nische evaluieren
Budget: 40.000 Euro

Reserve: 50.000 Euro

4. PRÜFEN:

Risiken:
- Die Nische ist zu klein → Plan B: Zweite Nische parallel testen
- Bestehende Kunden fühlen sich vernachlässigt → Lösung:
  Core-Produkt weiter pflegen, Nischen-Features sind Add-ons
- Wettbewerber kopiert die Strategie → Lösung: Schnell tief
  in die Nische eindringen, Switching Costs aufbauen

Sollte ich einen anderen Ansatz gewählt haben?
Strategie B (Upmarket) wäre der sicherere Weg. Aber bei
200.000 Euro Runway und 3% Wachstum brauchen wir einen
Hebel, nicht einen linearen Verbesserung. Nische dominieren
bietet diesen Hebel.
```

Siehst du den Unterschied zu einem normalen Prompt? Du bekommst nicht "eine" Empfehlung, sondern einen Überblick über die Optionen, eine begründete Wahl und einen konkreten Plan.

## Praxis-Beispiel 2: Kreative Problemlösung

```
Ich möchte meiner Schwester zum 30. Geburtstag etwas
Besonderes schenken. Budget: 200 Euro. Sie mag Literatur,
Kochen und Wandern.

Löse das mit Tree-of-Thought:
1. Generiere 3 kreative Geschenkideen
2. Bewerte jede Idee (Originalität, Persönlichkeit,
   Budget-Passung, Machbarkeit)
3. Arbeite die beste Idee aus
4. Gibt es einen Haken, den ich übersehe?
```

Das Modell generiert drei sehr unterschiedliche Ideen, bewertet sie nach deinen Kriterien und arbeitet die beste im Detail aus. Das Ergebnis ist durchdachter als "Kauf einen Gutschein."

## Praxis-Beispiel 3: Technische Architektur

```
Wir müssen eine Benachrichtigungsfunktion für unsere App
bauen. Anforderungen:
- Push-Notifications (iOS + Android)
- E-Mail-Notifications
- In-App-Notifications
- User kann Benachrichtigungen individuell ein/ausschalten
- Max. 10.000 Notifications pro Minute

Architekturentscheidung mit Tree-of-Thought:
1. Generiere 3 Architektur-Ansätze
2. Bewerte jeden nach: Skalierbarkeit, Entwicklungsaufwand,
   Kosten, Wartbarkeit
3. Empfehle den besten Ansatz mit Begründung
4. Was sind die größten technischen Risiken?
```

## Praxis-Beispiel 4: Verhandlungsstrategie

```
Ich verhandle nächste Woche mein Gehalt. Aktuelle Situation:
- 52.000 Euro brutto, seit 2 Jahren keine Erhöhung
- Ich habe ein wichtiges Projekt erfolgreich geleitet
- Marktüblich für meine Position: 58.000-65.000 Euro
- Mein Chef ist zahlenorientiert und eher sparsam

Entwickle eine Verhandlungsstrategie mit Tree-of-Thought:
1. Generiere 3 verschiedene Verhandlungsansätze
2. Bewerte jeden Ansatz (Erfolgschance, Risiko, Vorbereitung nötig)
3. Arbeite den besten aus (Eröffnung, Argumente, Antworten
   auf Einwände, Plan B)
4. Was ist der schlimmste realistische Ausgang und wie gehe
   ich damit um?
```

## Der erweiterte ToT-Prompt

Für komplexere Aufgaben nutze ich eine erweiterte Version:

```
Aufgabe: [Deine Aufgabe]

Löse das mit einem strukturierten Tree-of-Thought-Prozess:

RUNDE 1 – BREITE EXPLORATION:
Generiere 4 grundlegend verschiedene Ansätze. Für jeden:
- Name des Ansatzes (2-3 Wörter)
- Kernidee (1 Satz)
- Größter Vorteil
- Größtes Risiko
- Bewertung: 1-10

RUNDE 2 – TOP 2 VERTIEFEN:
Nimm die zwei besten Ansätze und arbeite sie aus:
- Detaillierter Plan (5-7 Schritte)
- Benötigte Ressourcen
- Timeline
- Erfolgskriterien

RUNDE 3 – FINALE ENTSCHEIDUNG:
Vergleiche die beiden vertieften Ansätze direkt:
- Welcher ist robuster?
- Welcher hat das bessere Risiko-Rendite-Verhältnis?
- Entscheidung mit Begründung

RUNDE 4 – STRESSTEST:
- Was passiert, wenn die wichtigste Annahme falsch ist?
- Was ist der Worst Case?
- Wie passe ich den Plan an, wenn die ersten Ergebnisse
  enttäuschend sind?
```

Dieser Prompt erzwingt einen mehrstufigen Denkprozess, der dem echten ToT-Algorithmus nahekommt.

## ToT für Alltagsentscheidungen

Du musst ToT nicht nur für große strategische Fragen nutzen. Hier sind Alltags-Beispiele:

**Urlaubsplanung:**
```
Ich habe 10 Tage Urlaub im September und 2.000 Euro Budget.
Ich mag Natur, gutes Essen und möchte nicht mehr als 4 Stunden
fliegen. Alleinreisend.

Tree-of-Thought:
1. Generiere 3 Reiseziele mit Kurzprofil
2. Bewerte nach: Kosten, Erreichbarkeit, Natur, Essen,
   Solo-Freundlichkeit
3. Arbeite das beste Ziel aus (Route, Unterkünfte, Highlights)
```

**Produktkauf:**
```
Ich brauche einen neuen Laptop. Budget: 1.200 Euro.
Nutzung: 50% Büroarbeit, 30% Programmieren, 20% Streaming.

Tree-of-Thought:
1. Schlage 3 Laptops vor (verschiedene Marken/Ansätze)
2. Vergleiche systematisch (Leistung, Display, Akku, Gewicht,
   Preis-Leistung)
3. Empfehlung mit Begründung
```

## Wann ToT statt CoT?

Die Entscheidung ist einfacher, als du denkst:

**Nutze CoT, wenn:**
- Es einen klaren Lösungsweg gibt
- Du die Schritte kennst
- Geschwindigkeit wichtig ist
- Die Aufgabe analytisch ist

**Nutze ToT, wenn:**
- Es mehrere mögliche Lösungswege gibt
- Du unsicher bist, welcher Ansatz der beste ist
- Du eine kreative oder strategische Entscheidung triffst
- Du den Suchraum erkunden willst
- Du Gründlichkeit über Geschwindigkeit stellst

Die Faustregel: Wenn du bei einer Aufgabe selbst sagen würdest "Hmm, da gibt es verschiedene Möglichkeiten..." – dann ist ToT die richtige Wahl.

## Häufige Fehler bei ToT

### Fehler 1: Zu ähnliche Ansätze
```
Ansatz 1: Social Media Marketing
Ansatz 2: Content Marketing
Ansatz 3: Influencer Marketing
```
Das sind keine "grundlegend verschiedenen" Ansätze – das sind drei Varianten derselben Idee. Sag dem Modell explizit: "Die Ansätze sollen sich grundlegend unterscheiden."

### Fehler 2: Bewertung ohne Kriterien
Wenn du sagst "bewerte die Ansätze", bewertet das Modell nach eigenen Kriterien, die vielleicht nicht deine sind. Gib immer Bewertungskriterien vor.

### Fehler 3: Zu viele Äste
Vier Ansätze sind meistens optimal. Bei drei fehlt manchmal die Breite. Bei fünf oder mehr wird es unübersichtlich und die Qualität der Bewertung sinkt.

### Fehler 4: Keine Entscheidung erzwingen
Ohne explizite Aufforderung zur Entscheidung liefert das Modell oft "es kommt darauf an" – was nutzlos ist. Erzwinge eine Empfehlung: "Wähle EINEN Ansatz und begründe deine Wahl."

## ToT vs. "Gib mir 3 Optionen"

Du könntest fragen: "Was ist der Unterschied zwischen ToT und einfach 'Gib mir 3 Optionen'?"

Der Unterschied liegt in der Bewertung und Vertiefung:

**"Gib mir 3 Optionen":**
- Erzeugt drei Ideen
- Keine Analyse
- Keine Empfehlung
- Du musst selbst bewerten

**ToT:**
- Erzeugt drei Ideen
- Bewertet sie systematisch nach deinen Kriterien
- Vertieft den besten Ansatz
- Stresstestet die Lösung
- Gibt eine begründete Empfehlung

Das ist der Unterschied zwischen "hier sind drei Optionen" und "hier sind drei Optionen, hier ist warum Option 2 am besten ist, hier ist der Plan, und hier ist, was schiefgehen kann."

---

## Übungen

### Übung 1: ToT für eine persönliche Entscheidung
Wähle eine echte Entscheidung, die du gerade triffst (Karriere, Kauf, Hobby, etc.). Nutze den ToT-Grundprompt mit 3 Ansätzen. Hat der Prozess dir geholfen? War die Empfehlung des Modells überzeugend?

### Übung 2: Erweiterter ToT
Nutze den erweiterten ToT-Prompt (4 Runden) für eine komplexe Aufgabe:
"Wie sollte eine Stadt mit 100.000 Einwohnern den öffentlichen Nahverkehr in den nächsten 10 Jahren umgestalten?"
Analysiere die Qualität: Waren die Ansätze wirklich verschieden? War die Bewertung fundiert?

### Übung 3: CoT vs. ToT
Nimm folgende Aufgabe und löse sie einmal mit CoT und einmal mit ToT:
"Ein Restaurant hat abends 80% Auslastung, mittags nur 30%. Was tun?"
Vergleiche die Ergebnisse: Welcher Ansatz war nützlicher? Warum?

### Übung 4: ToT-Prompt optimieren
Erstelle einen eigenen ToT-Prompt-Template für deinen Arbeitsbereich. Teste ihn mit 3 verschiedenen Aufgaben. Passe ihn an, bis er zuverlässig gute Ergebnisse liefert. Dokumentiere dein finales Template.
