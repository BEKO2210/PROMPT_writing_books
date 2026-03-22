# Kapitel 8: Frameworks im Vergleich – Welches wann?

Du kennst jetzt drei Frameworks: RTF, CRAFT und RISEN. Die Frage, die sich jeder stellt: Welches soll ich benutzen?

Die Antwort ist einfacher, als du denkst.

## Die Entscheidungsmatrix

Frag dich bei jeder Aufgabe drei Fragen:

**Frage 1: Wie komplex ist die Aufgabe?**
- Einfach → RTF
- Mittel → CRAFT
- Komplex → RISEN

**Frage 2: Wie wichtig ist die Qualität beim ersten Versuch?**
- Egal, ich überarbeite sowieso → RTF
- Sollte gut sein → CRAFT
- Muss direkt verwendbar sein → RISEN

**Frage 3: Gibt es einen klaren Prozess mit mehreren Schritten?**
- Nein → RTF oder CRAFT
- Ja → RISEN

Wenn du dir unsicher bist, nimm CRAFT. Es ist der beste Kompromiss.

## Alle drei Frameworks an einem Beispiel

Aufgabe: Du willst einen Newsletter-Text über ein neues Produkt schreiben lassen.

### RTF-Version

```
Role: Marketing-Texter
Task: Schreibe einen Newsletter-Text, der unser neues
Projektmanagement-Tool "FlowBoard" vorstellt. Hauptfeatures:
KI-gestützte Aufgabenverteilung, Echtzeit-Kollaboration,
Integration mit Slack und Teams.
Format: 200-250 Wörter, mit einem Call-to-Action am Ende
```

Dauer: 30 Sekunden. Ergebnis: Brauchbar, aber generisch.

### CRAFT-Version

```
Context: Wir sind ein B2B-SaaS-Startup mit 500 Newsletter-Abonnenten,
hauptsächlich Teamleiter und Projektmanager in Unternehmen mit
20-100 Mitarbeitern. Unser letzter Newsletter hatte eine Öffnungsrate
von 35%.

Role: Erfahrener SaaS-Marketing-Texter, der sich auf Launch-
Kommunikation spezialisiert hat.

Action: Schreibe einen Newsletter-Text, der unser neues
Projektmanagement-Tool "FlowBoard" vorstellt. Hauptfeatures:
KI-gestützte Aufgabenverteilung, Echtzeit-Kollaboration,
Integration mit Slack und Teams.

Format: 200-250 Wörter. Struktur: Aufmerksamkeitsstarker Einstieg
(Problem, das FlowBoard löst), 3 Features als kurze Absätze,
Call-to-Action (kostenlose 14-Tage-Testversion).

Tone: Enthusiastisch aber nicht übertrieben. Nutzen-orientiert
statt Feature-orientiert. "Das kann FlowBoard für dich tun" statt
"FlowBoard hat diese Features".
```

Dauer: 2 Minuten. Ergebnis: Deutlich besser. Passt zur Zielgruppe.

### RISEN-Version

```
Role: Senior Content-Strategin mit 8 Jahren Erfahrung in B2B-SaaS-
Launches. Du hast Newsletter für Unternehmen wie Asana und Monday
geschrieben.

Instructions: Erstelle einen Newsletter-Text für den Launch unseres
neuen Projektmanagement-Tools "FlowBoard". Der Newsletter soll
informieren und zur Anmeldung für die kostenlose Testversion
motivieren.

Steps:
1. Beginne mit einem konkreten Schmerzpunkt, den Projektmanager
   täglich erleben (z.B. manuelle Aufgabenverteilung, Tool-Chaos)
2. Stelle FlowBoard als Lösung vor (1-2 Sätze, keine Feature-Liste)
3. Hebe die 3 Hauptvorteile hervor (KI-Aufgabenverteilung,
   Echtzeit-Kollaboration, Slack/Teams-Integration) – jeweils mit
   einem konkreten Nutzen-Satz
4. Füge einen Social Proof ein (z.B. "Bereits 200 Teams in der
   Beta-Phase")
5. Schließe mit einem klaren Call-to-Action

End Goal: Der Newsletter soll eine Klickrate von mindestens 5%
auf den CTA-Button erzielen. Jeder Leser soll nach dem Lesen
genau wissen, was FlowBoard ist und warum er es ausprobieren sollte.

Narrowing:
- Maximal 250 Wörter
- Keine technischen Details (API, Infrastruktur)
- Nicht "revolutionär", "bahnbrechend" oder ähnliche Hyperbeln
- Zielgruppe: Teamleiter, nicht C-Level
- Kein Vergleich mit Wettbewerbern
```

Dauer: 5 Minuten. Ergebnis: Exzellent. Direkt verwendbar.

## Der Zeitaufwand-Qualität-Tradeoff

Ich habe das gerade angedeutet, und es ist der wichtigste Punkt dieses Kapitels:

| Framework | Schreibzeit | Ergebnis-Qualität | Nachbearbeitungszeit |
|---|---|---|---|
| RTF | 30 Sekunden | 60-70% | 10-15 Minuten |
| CRAFT | 2-3 Minuten | 80-90% | 3-5 Minuten |
| RISEN | 5-10 Minuten | 90-95% | 0-2 Minuten |

Wenn du rechnest: RTF braucht insgesamt ~15 Minuten (30 Sek. schreiben + 15 Min. überarbeiten). RISEN braucht insgesamt ~10 Minuten (7 Min. schreiben + 2 Min. überarbeiten). RISEN ist also oft *schneller*, obwohl der Prompt länger dauert.

Aber das gilt nur für komplexe Aufgaben. Für eine einfache Übersetzung wäre ein RISEN-Prompt absurder Overkill.

## Frameworks mischen

Noch ein Geheimnis: Du musst dich nicht für ein Framework entscheiden. In der Praxis mische ich ständig.

Mein typischer Workflow:

1. **Anfang:** RTF für die erste Idee
2. **Verfeinerung:** CRAFT für den finalen Prompt
3. **Komplexe Projekte:** RISEN für die Strategie, CRAFT für die Einzeltexte

Das ist kein Betrug. Das ist Pragmatismus.

## Andere Frameworks, die du kennen solltest

RTF, CRAFT und RISEN sind nicht die einzigen Frameworks. Hier sind drei weitere, die du vielleicht mal antreffen wirst:

### RACE
- **R**ole, **A**ction, **C**ontext, **E**xpectation
- Ähnlich wie CRAFT, mit "Expectation" statt "Tone" und "Format"
- Gut, wenn du klare Erwartungen an das Ergebnis formulieren willst

### CRISPE
- **C**apacity, **R**ole, **I**nsight, **S**tatement, **P**ersonality, **E**xperiment
- Sechs Elemente – das detaillierteste Framework
- Gut für kreative Aufgaben, wo Persönlichkeit wichtig ist
- Für meinen Geschmack zu umständlich für den Alltag

### CO-STAR
- **C**ontext, **O**bjective, **S**tyle, **T**one, **A**udience, **R**esponse
- Sechs Elemente mit starkem Fokus auf Zielgruppe
- Gut für Marketing und Kommunikation

Mein Rat: Lerne RTF, CRAFT und RISEN. Die decken 95% aller Fälle ab. Die anderen Frameworks sind Varianten, die du kennen solltest, aber nicht brauchen wirst.

## Die Framework-Entscheidung auf einen Blick

```
Aufgabe kommt rein
    │
    ├── Einfach? → RTF
    │
    ├── Mittel? → CRAFT
    │
    └── Komplex?
         │
         ├── Klarer Prozess? → RISEN
         │
         └── Kein klarer Prozess? → CRAFT + mehr Kontext
```

## Zusammenfassung

- Es gibt kein "bestes" Framework – nur das richtige für die Aufgabe
- RTF für Speed, CRAFT für Qualität, RISEN für Komplexität
- Mehr Aufwand beim Prompt = weniger Aufwand bei der Nachbearbeitung
- Frameworks können gemischt werden
- Drei Frameworks reichen für den Alltag

---

## Übung

**Framework-Battle**

Nimm eine Aufgabe deiner Wahl (am besten eine echte aus deinem Arbeitsalltag) und schreibe sie in allen drei Frameworks:

1. RTF-Version
2. CRAFT-Version
3. RISEN-Version

Teste alle drei im selben LLM. Bewerte:
- Welches Ergebnis ist am besten?
- Welcher Prompt hat am längsten gedauert?
- Bei welchem Framework war der Zeitaufwand insgesamt (Prompt + Nachbearbeitung) am niedrigsten?
- Gibt es einen klaren Gewinner?

Dokumentiere deine Ergebnisse. Das ist wertvolles Wissen für deinen persönlichen Prompt-Workflow.
