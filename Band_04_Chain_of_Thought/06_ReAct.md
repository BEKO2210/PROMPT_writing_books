# Kapitel 6: ReAct – Denken UND Handeln

Bis hierhin haben wir Techniken gelernt, bei denen das Modell denkt. Chain-of-Thought, Tree-of-Thought, Self-Consistency – alles passiert im Kopf des Modells. Es analysiert, bewertet, schlussfolgert.

Aber was, wenn Denken allein nicht reicht?

Was, wenn das Modell Informationen braucht, die es nicht hat? Wenn es nachschlagen muss? Wenn es ein Werkzeug benutzen muss? Wenn es handeln muss?

Hier kommt ReAct ins Spiel.

## Die Idee

ReAct steht für **Re**asoning + **Act**ing. Das Paper von Yao et al. (2023) – ja, derselbe Yao, der auch Tree-of-Thought erfunden hat – kombinierte zwei Fähigkeiten, die vorher getrennt betrachtet wurden:

1. **Reasoning:** Das Modell denkt nach (wie bei CoT)
2. **Acting:** Das Modell führt Aktionen aus (suchen, berechnen, nachschlagen)

Der Ablauf ist ein Loop:

```
Gedanke → Aktion → Beobachtung → Gedanke → Aktion → Beobachtung → ... → Antwort
```

Das Modell denkt, handelt, schaut sich das Ergebnis an, denkt weiter, handelt wieder – bis es genug Informationen hat, um eine finale Antwort zu geben.

## ReAct im Alltag

Du machst das selbst ständig. Wenn dich jemand fragt "Wie ist das Wetter morgen in München?", durchläufst du einen ReAct-Prozess:

1. **Gedanke:** "Ich weiß nicht, wie das Wetter morgen ist. Ich muss nachschauen."
2. **Aktion:** Du öffnest eine Wetter-App.
3. **Beobachtung:** "Morgen: 18°C, bewölkt, 40% Regenwahrscheinlichkeit."
4. **Gedanke:** "OK, eher wechselhaft. Ich sollte einen Regenschirm empfehlen."
5. **Antwort:** "Morgen in München: 18 Grad, bewölkt. Nimm einen Schirm mit."

Ohne die Aktion (Wetter-App checken) hättest du nur raten können. Das Handeln war nötig, um eine gute Antwort zu geben.

## Das ReAct-Muster

Im Prompt sieht ReAct so aus:

```
Aufgabe: [Deine Aufgabe]

Nutze folgendes Format:

Gedanke 1: [Was du über das Problem denkst]
Aktion 1: [Was du tust, um mehr zu erfahren]
Beobachtung 1: [Was du durch die Aktion erfährst]

Gedanke 2: [Was du jetzt denkst, basierend auf der Beobachtung]
Aktion 2: [Nächster Schritt]
Beobachtung 2: [Was du erfährst]

...

Gedanke N: [Finale Schlussfolgerung]
Antwort: [Deine Antwort]
```

## ReAct ohne Werkzeuge: Die Simulation

"Aber ich nutze die API nicht und mein Chatbot kann nicht im Internet suchen!" – kein Problem. Du kannst ReAct als Denkstruktur nutzen, auch wenn das Modell keine echten Aktionen ausführen kann.

Der Trick: Das Modell **simuliert** die Aktionen und Beobachtungen basierend auf seinem Wissen.

### Beispiel: Reiseplanung

```
Ich möchte im Oktober 5 Tage nach Lissabon reisen.
Budget: 1.500 Euro. Direkt ab Frankfurt.

Plane die Reise im ReAct-Format:

Gedanke: Was muss ich zuerst klären?
Aktion: [Recherche/Überlegung]
Beobachtung: [Ergebnis]
... und so weiter, bis der Plan steht.
```

**Mögliches Ergebnis:**

```
Gedanke 1: Zuerst muss ich die Flugkosten klären,
da sie den größten Budgetposten ausmachen.
Aktion 1: Flugpreise Frankfurt-Lissabon im Oktober recherchieren.
Beobachtung 1: Direktflüge kosten typischerweise 120-200 Euro
(Hin+Rück) mit TAP oder Ryanair. Im Oktober ist Nebensaison,
also eher am unteren Ende: ~150 Euro.

Gedanke 2: Mit 150 Euro für Flüge bleiben 1.350 Euro für
Unterkunft, Essen, Aktivitäten und Transport. Jetzt Unterkunft klären.
Aktion 2: Unterkunftsoptionen in Lissabon für 5 Nächte recherchieren.
Beobachtung 2: Hotels im Zentrum (Baixa/Alfama): 80-120 Euro/Nacht.
Hostels: 30-50 Euro/Nacht. Airbnb: 60-90 Euro/Nacht.
Für Budget und Komfort: Airbnb in Alfama, ~70 Euro/Nacht = 350 Euro.

Gedanke 3: Flug 150 + Unterkunft 350 = 500 Euro.
Bleiben 1.000 Euro für Essen (5 Tage), Aktivitäten und Transport.
Das ist komfortabel. Jetzt den Tagesplan strukturieren.
Aktion 3: Top-Sehenswürdigkeiten und Aktivitäten auflisten.
Beobachtung 3: Belém (Turm + Pastéis de Belém), Alfama
(Castelo São Jorge), Sintra (Tagesausflug), LX Factory,
Tram 28, Oceanário. Sintra-Tagesausflug ~40 Euro (Zug + Eintritt).

Gedanke 4: Ich habe genug Information für einen konkreten
5-Tage-Plan.
Aktion 4: Tagesplan erstellen.
Beobachtung 4: [Detaillierter Plan für Tag 1-5]

Antwort: [Zusammengefasster Reiseplan mit Budget-Aufstellung]
```

Das Modell hat seine Recherche-Erfahrung aus den Trainingsdaten genutzt, um realistische Preise und Empfehlungen zu geben. Keine echte Internet-Suche, aber ein strukturierter Denkprozess, der deutlich besser ist als "Hier sind 10 Tipps für Lissabon."

## ReAct mit echten Werkzeugen

Wenn du Tools wie ChatGPT mit Browsing, Claude mit Artifacts oder Gemini mit Google Search nutzt, wird ReAct noch mächtiger. Das Modell kann dann echte Aktionen ausführen:

### Werkzeuge, die LLMs nutzen können:
- **Web-Suche:** Aktuelle Informationen nachschlagen
- **Code-Ausführung:** Python, JavaScript etc. direkt ausführen
- **Rechner:** Komplexe Berechnungen durchführen
- **Dateien lesen:** PDFs, CSVs, Bilder analysieren
- **APIs aufrufen:** Daten von externen Diensten abrufen

### Beispiel mit Web-Suche:

```
Recherchiere: Welches Land hat 2025 die höchste
Lebensqualität und warum?

Nutze Web-Suche und das ReAct-Format.
```

Das Modell würde:
1. **Gedanke:** "Ich brauche aktuelle Rankings."
2. **Aktion:** Suche nach "Quality of Life Index 2025"
3. **Beobachtung:** Ergebnisse auswerten
4. **Gedanke:** "Mehrere Rankings vergleichen für Robustheit"
5. **Aktion:** Zweite Suche mit anderem Ranking
6. **Beobachtung:** Vergleich der Ergebnisse
7. **Antwort:** Fundierte Antwort mit Quellen

## ReAct-Prompts für verschiedene Aufgaben

### Recherche-Aufgabe

```
Frage: [Deine Frage]

Beantworte die Frage mit dem ReAct-Ansatz:

Für jeden Schritt:
- DENKEN: Was weißt du? Was fehlt dir?
- HANDELN: Welche Information musst du suchen/berechnen?
- BEOBACHTEN: Was hast du herausgefunden?

Wiederhole, bis du genug Information hast.
Dann: Finale Antwort mit Begründung.
```

### Problemlösung

```
Problem: [Beschreibung]

Löse das Problem im ReAct-Format:

DENKEN: Was ist das Problem genau? Was sind mögliche Ursachen?
HANDELN: Welchen Test/Check würdest du als Erstes machen?
BEOBACHTEN: Was wäre das wahrscheinliche Ergebnis?

Wiederhole, bis du die Ursache gefunden und eine Lösung hast.
```

### Faktencheck

```
Behauptung: "[Zu prüfende Aussage]"

Überprüfe diese Behauptung im ReAct-Format:

DENKEN: Was genau wird behauptet? Welche Fakten müsste
ich prüfen?
HANDELN: Welche Quelle würde ich konsultieren?
BEOBACHTEN: Was sagt die Quelle?

Finale Bewertung: WAHR / FALSCH / TEILWEISE WAHR / NICHT PRÜFBAR
Begründung: [Warum?]
```

## ReAct und KI-Agenten

ReAct ist die theoretische Grundlage für das, was heute als "KI-Agenten" gehypt wird. Ein KI-Agent ist im Kern ein LLM, das:

1. Eine Aufgabe bekommt
2. Darüber nachdenkt (Reasoning)
3. Werkzeuge nutzt (Acting)
4. Die Ergebnisse beobachtet (Observation)
5. Weiterdenkt und weiterhandelt
6. Bis die Aufgabe erledigt ist

Tools wie AutoGPT, LangChain Agents, Claude Computer Use und OpenAI Assistants implementieren genau dieses Muster.

### Was KI-Agenten heute können:
- E-Mails lesen und beantworten
- Code schreiben und testen
- Dokumente erstellen und formatieren
- Daten aus verschiedenen Quellen zusammentragen
- Web-Recherche durchführen
- Termine planen

### Warum das für dich relevant ist

Auch wenn du keine KI-Agenten programmierst: Das Verständnis von ReAct hilft dir, besser mit ihnen zu arbeiten. Wenn du einem Agenten eine Aufgabe gibst, formuliere sie so, dass der Agent klar weiß:

- **Was er denken soll** (Ziel, Kontext, Einschränkungen)
- **Was er tun darf** (Welche Werkzeuge, welche Aktionen)
- **Wann er stoppen soll** (Erfolgskriterien)

Das ist Prompting für Agenten – und es funktioniert nach denselben Prinzipien wie alles, was du bisher gelernt hast.

## Praxis-Beispiel: Komplexe Analyse

```
Aufgabe: Analysiere, ob es sich lohnt, eine Eigentumswohnung
in München zu kaufen oder weiter zu mieten.

Meine Situation:
- Miete aktuell: 1.200 Euro kalt
- Kaufpreis Wohnung: 450.000 Euro
- Eigenkapital: 100.000 Euro
- Einkommen: 5.500 Euro netto/Monat
- Zinssatz aktuell: 3,5%
- Geplante Nutzung: 15+ Jahre

Nutze ReAct:

DENKEN: Was muss ich zuerst berechnen/klären?
HANDELN: [Berechne/Recherchiere]
BEOBACHTEN: [Ergebnis]
... wiederhole bis zur Empfehlung.

Am Ende: Klare Empfehlung mit Begründung und
den wichtigsten Zahlen.
```

Das Modell würde schrittweise durchrechnen: Kreditrate, Nebenkosten, Opportunity Cost des Eigenkapitals, Wertsteigerung, Break-Even-Punkt. Jeder Schritt wird durch den vorherigen informiert.

## Praxis-Beispiel: Fehlersuche

```
Problem: Meine React-App zeigt nach dem Login eine
leere Seite. Keine Fehlermeldung in der Konsole.

Debug das mit ReAct:

DENKEN: Was könnte eine leere Seite ohne Fehler verursachen?
HANDELN: Welchen Check mache ich zuerst?
BEOBACHTEN: [Erwartetes Ergebnis]

Arbeite dich systematisch zur Ursache vor.
```

```
DENKEN: Leere Seite ohne Fehler nach Login. Das deutet auf
ein Routing-Problem oder einen State-Management-Fehler hin.
Der Login funktioniert offenbar (kein Fehler), aber die
Weiterleitung oder das Rendering danach nicht.

HANDELN: Prüfe die Router-Konfiguration.
Gibt es eine Route für die Post-Login-Seite?
BEOBACHTEN: Ja, Route "/dashboard" existiert.

DENKEN: Route existiert. Wird nach dem Login auch
dorthin navigiert?
HANDELN: Prüfe den Login-Handler.
Wird navigate("/dashboard") aufgerufen?
BEOBACHTEN: Ja, navigate wird aufgerufen.

DENKEN: Navigation scheint korrekt. Wird die Dashboard-
Komponente gerendert?
HANDELN: Füge ein console.log in die Dashboard-Komponente ein.
BEOBACHTEN: console.log erscheint NICHT.

DENKEN: Die Komponente wird nicht gerendert, obwohl die
Route existiert. Ist die Route möglicherweise durch eine
Auth-Guard geschützt, die den State noch nicht hat?
HANDELN: Prüfe die ProtectedRoute-Komponente.
BEOBACHTEN: ProtectedRoute prüft "isAuthenticated" aus dem
Redux Store. Der Login setzt den Token im localStorage,
aber updated den Redux Store erst nach einem Re-Render.

DENKEN: Race Condition! Der Login speichert den Token,
navigiert sofort, aber der Auth-State im Redux ist noch false.
Die ProtectedRoute blockt und rendert nichts (statt zu redirecten).

ANTWORT: Race Condition zwischen Token-Speicherung und
Auth-State-Update. Fix: Im Login-Handler erst den Redux
Store updaten, DANN navigieren. Oder: ProtectedRoute soll
auch localStorage prüfen als Fallback.
```

Das ist systematisches Debugging, wie es ein erfahrener Entwickler machen würde. ReAct zwingt das Modell zu diesem strukturierten Ansatz.

## ReAct Best Practices

### 1. Klare Aktion-Typen definieren
Sag dem Modell, welche Arten von Aktionen es zur Verfügung hat:
```
Verfügbare Aktionen:
- SUCHE: Information nachschlagen
- BERECHNE: Mathematische Berechnung durchführen
- PRÜFE: Eine Annahme überprüfen
- VERGLEICHE: Zwei Optionen gegenüberstellen
```

### 2. Beobachtungen realistisch halten
In der Simulation kann das Modell dazu neigen, die "perfekte" Beobachtung zu erfinden. Fordere Realismus:
```
Deine Beobachtungen sollen realistisch sein. Nicht jede
Suche liefert sofort die perfekte Antwort.
```

### 3. Loop-Limit setzen
Ohne Limit kann das Modell endlos im Kreis denken:
```
Maximal 5 Denken-Handeln-Beobachten-Zyklen.
Dann: Beste verfügbare Antwort.
```

### 4. Abbruchbedingung definieren
```
Stoppe, wenn:
- Du genug Information für eine fundierte Antwort hast
- Du dieselbe Information zum zweiten Mal suchst
- Der nächste Schritt keinen Mehrwert bringen würde
```

## ReAct vs. Chain-of-Thought

| CoT | ReAct |
|---|---|
| Nur Denken | Denken + Handeln |
| Nutzt vorhandenes Wissen | Kann neues Wissen beschaffen |
| Ein Durchlauf | Iterativer Loop |
| Schneller | Gründlicher |
| Gut für geschlossene Fragen | Gut für offene Recherche |
| Alle Infos im Prompt | Infos werden unterwegs gesammelt |

Die Faustregel: Wenn das Modell alle Informationen hat, die es braucht → CoT. Wenn es zusätzliche Informationen braucht → ReAct.

## Häufige Fehler bei ReAct

### Fehler 1: Aktionen ohne Mehrwert
Das Modell "handelt", aber die Aktion bringt keine neue Information:
```
HANDELN: Nochmal über das Problem nachdenken.
```
Das ist keine Aktion, das ist Denken. Eine Aktion muss neue Information produzieren.

### Fehler 2: Zu lange Loops
Das Modell dreht sich im Kreis und sucht immer weiter, obwohl es schon genug weiß. Setze ein Loop-Limit.

### Fehler 3: ReAct für einfache Aufgaben
"Was ist 5 + 3?" braucht keinen ReAct-Loop. Das ist mit direkter Antwort besser bedient.

### Fehler 4: Simulation mit Fakten verwechseln
In der simulierten Variante "erfindet" das Modell die Beobachtungen aus seinem Trainingswissen. Das ist nützlich für Planung und Strukturierung, aber nicht für Faktenfragen. Für echte Fakten brauchst du echte Werkzeuge.

---

## Übungen

### Übung 1: ReAct-Recherche
Nutze den ReAct-Ansatz für eine Recherche-Frage:
"Welches Programmiersprache sollte ein Anfänger 2026 als Erstes lernen?"
Führe mindestens 3 Denken-Handeln-Beobachten-Zyklen durch.

### Übung 2: ReAct-Debugging
Beschreibe ein technisches Problem, das du kürzlich hattest (oder erfinde eins). Lass das Modell es mit ReAct debuggen. War der Prozess systematischer als eine direkte Frage?

### Übung 3: ReAct mit Werkzeugen
Wenn du Zugang zu einem LLM mit Web-Suche hast (ChatGPT Plus, Gemini, Perplexity): Stelle eine aktuelle Frage im ReAct-Format. Vergleiche: Nutzt das Modell die Web-Suche systematischer, wenn du den ReAct-Prompt nutzt?

### Übung 4: Agent-Prompt schreiben
Schreib einen Prompt, der ein LLM als "Recherche-Agent" für ein Thema deiner Wahl einsetzt. Der Agent soll:
- 3 verschiedene Aspekte recherchieren
- Seine Quellen bewerten
- Eine Zusammenfassung mit Quellenbewertung liefern
