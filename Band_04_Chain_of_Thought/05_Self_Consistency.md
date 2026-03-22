# Kapitel 5: Self-Consistency – Die Macht der Mehrheit

Du kennst das: Du fragst das Modell etwas, bekommst eine Antwort. Dann stellst du dieselbe Frage nochmal – und bekommst eine andere Antwort. Welche stimmt?

Self-Consistency gibt dir die Antwort: Beide könnten stimmen. Aber wenn du zehnmal fragst und achtmal dieselbe Antwort bekommst, ist die wahrscheinlich richtig.

## Die Idee

Self-Consistency (SC) wurde 2023 von Wang et al. in dem Paper "Self-Consistency Improves Chain of Thought Reasoning in Language Models" vorgestellt. Die Kernidee ist bestechend einfach:

1. Stelle dieselbe Frage mehrfach (mit leicht unterschiedlicher Temperatur oder Formulierung)
2. Lass das Modell jedes Mal mit Chain-of-Thought antworten
3. Sammle alle Endantworten
4. Nimm die häufigste Antwort (Majority Vote)

Das ist wie eine Jury-Abstimmung. Nicht jeder Geschworene hat recht, aber die Mehrheit meistens.

## Warum funktioniert das?

LLMs sind probabilistisch. Bei jeder Antwort wählen sie aus einer Verteilung möglicher nächster Tokens. Das bedeutet: Dieselbe Frage kann unterschiedliche Denkwege und unterschiedliche Antworten produzieren.

Manche dieser Denkwege führen zum richtigen Ergebnis, manche nicht. Aber – und das ist der Schlüssel – der richtige Denkweg wird statistisch häufiger produziert als falsche. Wenn du also genug Samples nimmst, setzt sich die richtige Antwort durch.

Stell dir vor, du würfelst mit einem leicht gezinkten Würfel. Bei einem Wurf weißt du nicht, ob die 6 häufiger kommt. Bei hundert Würfen siehst du das Muster.

## Self-Consistency manuell umsetzen

Du brauchst keine Programmierung für Self-Consistency. Du kannst es manuell machen:

### Methode 1: Mehrfach fragen

Stell deine Frage 3-5 Mal in neuen Chat-Konversationen (nicht im selben Chat, denn dort beeinflusst die vorherige Antwort die nächste).

**Frage (jedes Mal identisch):**
```
Ein Zug fährt um 9:15 los. Die Fahrt dauert 2 Stunden
und 48 Minuten. Unterwegs hält er 3 Mal je 5 Minuten.
Wann kommt er an?

Denke Schritt für Schritt.
```

**Durchlauf 1:** "12:18"
**Durchlauf 2:** "12:18"
**Durchlauf 3:** "12:03" (hat die Halte vergessen)
**Durchlauf 4:** "12:18"
**Durchlauf 5:** "12:18"

Majority Vote: **12:18** (4 von 5). Richtig.

### Methode 2: Variierte Formulierung

Statt dieselbe Frage wortwörtlich zu wiederholen, formulierst du sie leicht anders. Das erzeugt natürliche Variation.

**Variante A:** "Ein Zug startet um 9:15. Fahrzeit: 2h 48min. 3 Halte à 5 min. Ankunft?"
**Variante B:** "Abfahrt 9:15 Uhr, 2 Stunden 48 Minuten Fahrt, plus 3 Zwischenhalte von jeweils 5 Minuten. Wann Ankunft?"
**Variante C:** "Berechne die Ankunftszeit: Start 09:15, Reisedauer 168 Minuten, 3 Stopps zu je 5 Minuten."

Wenn alle drei Varianten dieselbe Antwort geben, kannst du ziemlich sicher sein.

### Methode 3: Temperatur variieren

Wenn du die API nutzt (oder ein Tool wie Playground), kannst du die Temperatur ändern:
- Durchlauf 1: Temperatur 0.3
- Durchlauf 2: Temperatur 0.5
- Durchlauf 3: Temperatur 0.7

Niedrige Temperatur = deterministischer. Hohe Temperatur = kreativer/variabler. Verschiedene Temperaturen erzeugen verschiedene Denkwege.

## Self-Consistency in einem einzigen Prompt

Du kannst Self-Consistency auch in einem einzigen Prompt simulieren:

```
Aufgabe: [Deine Aufgabe]

Löse diese Aufgabe 3 Mal mit unterschiedlichen Denkwegen.
Zeige jeden Denkweg separat.

Denkweg 1:
[Lass das Modell arbeiten]

Denkweg 2:
[Lass das Modell arbeiten]

Denkweg 3:
[Lass das Modell arbeiten]

Vergleich:
- Denkweg 1 ergibt: ___
- Denkweg 2 ergibt: ___
- Denkweg 3 ergibt: ___

Finale Antwort (Mehrheitsentscheidung): ___
```

**Wichtig:** Das ist eine Simulation, kein echtes Self-Consistency. Echtes SC braucht unabhängige Durchläufe. Im selben Prompt beeinflusst der erste Denkweg den zweiten. Trotzdem liefert auch die Simulation bessere Ergebnisse als ein einzelner Durchlauf.

## Praxis-Beispiel 1: Komplexe Berechnung

```
Ein Freelancer verdient in Q1 2026:
- Januar: 4.200 Euro (3 Projekte)
- Februar: 3.800 Euro (2 Projekte + 1 Retainer von 800 Euro)
- März: 5.100 Euro (4 Projekte)

Seine monatlichen Fixkosten sind 1.900 Euro.
Er legt 25% des Gewinns (nach Fixkosten) für Steuern zurück.
Er möchte 500 Euro/Monat sparen.

Frage: Wie viel Geld hat er am Ende von Q1 frei verfügbar
(nach Fixkosten, Steuerrücklage und Sparen)?

Löse das auf 3 verschiedene Arten:

Methode 1 – Monatsweise:
[Berechne jeden Monat einzeln]

Methode 2 – Quartalsweise:
[Berechne alles für das gesamte Quartal]

Methode 3 – Von hinten (Gegenprobe):
[Starte mit dem Gesamtumsatz und ziehe alles ab]

Vergleiche die Ergebnisse. Stimmen sie überein?
```

Wenn alle drei Methoden dasselbe Ergebnis liefern, ist es mit hoher Wahrscheinlichkeit richtig. Wenn nicht, zeigen die Abweichungen, wo der Fehler liegt.

## Praxis-Beispiel 2: Textinterpretation

```
Lies diesen Vertragsabschnitt:

"Der Auftragnehmer gewährt dem Auftraggeber ein nicht-exklusives,
zeitlich unbegrenztes Nutzungsrecht an den erstellten Werken.
Die Übertragung an Dritte bedarf der schriftlichen Zustimmung
des Auftragnehmers."

Frage: Darf der Auftraggeber die Werke auf seiner Website
veröffentlichen, ohne zu fragen?

Analysiere das aus 3 Perspektiven:

Perspektive 1 – Wörtliche Auslegung:
Was sagt der Text wortwörtlich?

Perspektive 2 – Juristische Auslegung:
Was bedeuten die Fachbegriffe genau?

Perspektive 3 – Praxisbezogene Auslegung:
Was würde ein Anwalt raten?

Vergleiche die drei Perspektiven.
Kommen sie zum selben Ergebnis?
```

Hier ist Self-Consistency besonders wertvoll, weil Textinterpretation subjektiv sein kann. Wenn alle drei Perspektiven übereinstimmen, hast du eine robuste Interpretation.

## Praxis-Beispiel 3: Diagnose

```
Meine Website lädt langsam (8 Sekunden).
Stack: WordPress, Shared Hosting, 50 Plugins,
unkomprimierte Bilder, kein CDN.

Analysiere die Ursache aus 3 Blickwinkeln:

Blickwinkel 1 – Server-Seite:
Was auf dem Server könnte das Problem sein?

Blickwinkel 2 – Client-Seite:
Was im Browser könnte das Problem sein?

Blickwinkel 3 – Netzwerk:
Was auf dem Weg dazwischen könnte das Problem sein?

Erstelle eine priorisierte Liste der wahrscheinlichsten
Ursachen (kombiniert aus allen 3 Blickwinkeln).
```

## Wann Self-Consistency nutzen?

### SC ist ideal bei:
- **Berechnungen** – Dreimal rechnen, dreimal dasselbe? Dann stimmt's.
- **Textinterpretation** – Verschiedene Lesarten, konsistentes Ergebnis.
- **Diagnosen** – Verschiedene Ansätze führen zur selben Ursache.
- **Fakten-Fragen** – "Wann war das?" – 3x dieselbe Antwort = wahrscheinlich richtig.
- **Entscheidungen unter Unsicherheit** – Wenn du nicht sicher bist, ob die erste Antwort stimmt.

### SC ist überflüssig bei:
- **Kreative Aufgaben** – "Schreib mir ein Gedicht" dreimal → drei verschiedene Gedichte. Kein "richtiges".
- **Meinungsbasierte Fragen** – Keine objektive Mehrheit möglich.
- **Einfache Faktenfragen** – "Hauptstadt von Frankreich?" braucht kein SC.
- **Formatierung** – "Mach daraus eine Tabelle" hat nur ein korrektes Ergebnis.

### Die Kostenfrage

Self-Consistency ist teuer. Drei Durchläufe kosten dreimal so viele Tokens. Bei API-Nutzung kann das ins Geld gehen.

Meine Faustregel: Nutze SC, wenn die Kosten eines Fehlers höher sind als die Kosten von 3x mehr Tokens.

- Falsche Berechnung in einem Businessplan? → SC lohnt sich.
- Falsche Formulierung in einer E-Mail? → SC ist Overkill.

## Self-Consistency kombiniert mit anderen Techniken

### SC + CoT (Standard)
```
[Frage] – Denke Schritt für Schritt.
```
3x ausführen → Majority Vote.

### SC + ToT
```
[Frage] – Generiere 3 Ansätze, bewerte jeden.
```
3x ausführen → Prüfe, ob alle drei Durchläufe denselben Ansatz als besten wählen.

### SC + Rollen
```
Durchlauf 1: "Du bist ein Finanzberater. [Frage]"
Durchlauf 2: "Du bist ein Wirtschaftsprüfer. [Frage]"
Durchlauf 3: "Du bist ein Steuerberater. [Frage]"
```
Verschiedene Rollen, selbe Frage → Wenn alle drei übereinstimmen, ist die Antwort robust.

## Der Confidence Score

Eine Erweiterung, die ich oft nutze:

```
[Frage]

Denke Schritt für Schritt.
Am Ende: Gib deinen Confidence Score an (0-100%).
0% = rate nur. 100% = absolut sicher.
```

Wenn du das über mehrere Durchläufe machst:
- Durchlauf 1: Antwort A, Confidence 85%
- Durchlauf 2: Antwort A, Confidence 90%
- Durchlauf 3: Antwort B, Confidence 45%

Dann weißt du: Antwort A ist wahrscheinlich richtig (2x gewählt, hohe Confidence). Antwort B war ein Ausreißer mit niedriger Confidence.

## Häufige Fehler bei Self-Consistency

### Fehler 1: Nicht genug Durchläufe
Zwei Durchläufe reichen nicht – bei 50/50 hast du keinen Tie-Breaker. Minimum: 3 Durchläufe. Ideal: 5 Durchläufe für höhere Sicherheit.

### Fehler 2: Durchläufe im selben Chat
Im selben Chat-Verlauf beeinflusst die erste Antwort die zweite. Für echtes SC brauchst du unabhängige Konversationen.

### Fehler 3: Nuance ignorieren
Majority Vote funktioniert nur bei Aufgaben mit klarer Antwort. Bei nuancierten Fragen kann es sein, dass alle drei Antworten leicht unterschiedlich, aber alle akzeptabel sind. Dann ist SC nicht das richtige Werkzeug.

### Fehler 4: SC als Wahrheitsgarantie
Wenn alle drei Durchläufe falsch sind, hilft SC nicht. Das Modell kann konsistent halluzinieren. SC erhöht die Wahrscheinlichkeit einer richtigen Antwort, garantiert sie aber nicht.

---

## Übungen

### Übung 1: Manuelles Self-Consistency
Öffne 3 neue Chat-Konversationen mit deinem LLM. Stelle in jeder exakt dieselbe Frage:

"In einem Raum sind 5 Maschinen. Jede produziert 8 Teile pro Stunde. Maschine 3 hat 30% weniger Output wegen Wartung. Maschine 5 produziert doppelt so schnell. Wie viele Teile werden in 3 Stunden produziert? Denke Schritt für Schritt."

Vergleiche die 3 Antworten. Stimmen sie überein?

### Übung 2: Einzel-Prompt SC
Nutze den Einzel-Prompt-SC-Ansatz (3 Denkwege in einem Prompt) für eine Aufgabe deiner Wahl. Kommen die 3 Wege zum selben Ergebnis?

### Übung 3: SC + Rollen
Teste die Rollen-Variante: Stelle eine fachliche Frage an 3 verschiedene "Experten-Rollen". Vergleiche die Antworten. Wo stimmen sie überein, wo nicht?

### Übung 4: Confidence Score kalibrieren
Stelle dem Modell 10 Faktenfragen, die du selbst beantworten kannst. Lass es jedes Mal einen Confidence Score geben. Dann prüfe: Korreliert der Score mit der Richtigkeit? Ab welchem Score ist das Modell zuverlässig?
