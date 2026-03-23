# Kapitel 1: Was ist Reasoning eigentlich?

Bevor wir in die Techniken einsteigen, müssen wir klären, was "Reasoning" bei KI überhaupt bedeutet. Denn der Begriff wird inflationär benutzt und meistens falsch verstanden.

## Denkt eine KI wirklich?

Kurze Antwort: Nein. Nicht so wie du und ich.

Lange Antwort: Es kommt darauf an, was du mit "Denken" meinst.

Ein LLM wie GPT-4, Claude oder Gemini ist – das weißt du aus Band 1 – ein statistisches Sprachmodell. Es berechnet für jedes Token die Wahrscheinlichkeit, dass es als Nächstes kommt. Das ist kein Denken im menschlichen Sinne. Es gibt kein Bewusstsein, keine Intention, kein Verstehen.

Aber – und das ist der spannende Teil – wenn du das Modell dazu bringst, seine Antwort Schritt für Schritt aufzubauen, passiert etwas Interessantes. Die Zwischenschritte erzeugen Kontext, der die nachfolgenden Schritte beeinflusst. Das Modell "denkt" nicht wirklich, aber es simuliert einen Denkprozess, der zu besseren Ergebnissen führt.

Stell dir das so vor: Wenn du jemanden fragst "Was ist 347 × 28?", gibt es zwei Wege:

**Weg 1 – Direkte Antwort:**
"9716." (Vielleicht richtig, vielleicht nicht. Die meisten Menschen würden raten.)

**Weg 2 – Schritt für Schritt:**
"347 × 28 ... das ist 347 × 30 minus 347 × 2 ... 347 × 30 = 10.410 ... 347 × 2 = 694 ... 10.410 - 694 = 9.716."

Dieselbe Person, dieselbe Frage – aber Weg 2 ist zuverlässiger, weil die Zwischenschritte als Kontrolle dienen. Genau so funktioniert Reasoning bei LLMs.

## Reasoning vs. Prompting – der Unterschied

In den ersten drei Bänden hast du Prompting gelernt. Du gibst dem Modell eine Aufgabe und optimierst, wie du sie formulierst.

Reasoning geht einen Schritt weiter. Du optimierst nicht nur die Aufgabe, sondern den **Denkprozess**, den das Modell durchläuft, um zur Antwort zu kommen.

| Prompting (Band 1-3) | Reasoning (Band 4) |
|---|---|
| WAS soll das Modell tun? | WIE soll es denken? |
| Fokus auf Input | Fokus auf Prozess |
| Ergebnis direkt | Ergebnis über Zwischenschritte |
| Gut für einfache Aufgaben | Nötig für komplexe Aufgaben |
| "Schreib mir eine E-Mail" | "Analysiere das Problem Schritt für Schritt, wäge Optionen ab und empfiehl die beste Lösung" |

Das heißt nicht, dass Prompting überflüssig wird. Reasoning-Techniken *bauen* auf gutem Prompting auf. Du brauchst weiterhin klare Aufgaben, guten Kontext, passende Rollen und saubere Struktur. Reasoning kommt obendrauf.

## Warum LLMs ohne Reasoning scheitern

Lass mich dir zeigen, wo Standard-Prompting an seine Grenzen stößt.

### Beispiel 1: Logisches Schlussfolgern

```
Prompt:
Alle Katzen haben Fell. Max hat Fell. Ist Max eine Katze?

Typische Antwort ohne Reasoning:
Ja, Max ist wahrscheinlich eine Katze.
```

Falsch. Dass alle Katzen Fell haben, heißt nicht, dass alles mit Fell eine Katze ist. Hunde haben auch Fell. Das ist ein klassischer logischer Fehlschluss – und LLMs fallen ohne Reasoning-Anleitung regelmäßig darauf rein.

### Beispiel 2: Mehrstufige Probleme

```
Prompt:
Ein Bauer hat 17 Schafe. Alle bis auf 9 sterben.
Wie viele hat er noch?

Typische Antwort ohne Reasoning:
Der Bauer hat noch 8 Schafe. (17 - 9 = 8)
```

Auch falsch. "Alle bis auf 9 sterben" bedeutet: 9 überleben. Die Antwort ist 9. Das Modell hat gerechnet statt zu lesen – ein klassischer Fehler bei Textaufgaben.

### Beispiel 3: Planung und Strategie

```
Prompt:
Ich habe 5.000 Euro und möchte ein Online-Business starten.
Was soll ich tun?

Typische Antwort ohne Reasoning:
1. Finde eine Nische
2. Erstelle eine Website
3. Nutze Social Media Marketing
4. Biete einen Mehrwert
5. Sei konsistent
```

Nicht falsch, aber nutzlos. Das sind generische Ratschläge, die du auf jeder dritten Webseite findest. Keine echte Analyse, keine Abwägung, keine Berücksichtigung der Budgetbeschränkung, keine konkreten Handlungsschritte.

In all diesen Fällen fehlt dem Modell eines: ein strukturierter Denkprozess. Es springt direkt zur Antwort, ohne den Weg dorthin zu durchdenken.

## Die Reasoning-Revolution: Ein kurzer historischer Abriss

Reasoning in LLMs ist kein neues Konzept, aber es hat sich rasant entwickelt:

**2022 – Chain-of-Thought wird entdeckt**
Google-Forscher Jason Wei und sein Team veröffentlichten das Paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models". Die Kernidee: Wenn man dem Modell Beispiele mit Zwischenschritten zeigt, produziert es selbst Zwischenschritte – und liefert bessere Ergebnisse. Das Paper hat das Feld verändert.

**2022 – Zero-Shot CoT**
Kojima et al. zeigten, dass manchmal ein einziger Satz reicht: "Let's think step by step." Keine Beispiele nötig. Das Modell aktiviert seinen "Reasoning-Modus" allein durch diese Anweisung. Einfach, aber wirkungsvoll.

**2023 – Tree-of-Thought**
Yao et al. erweiterten CoT zu einem Baum. Statt einem linearen Denkpfad erkundet das Modell mehrere Pfade, bewertet sie und wählt den besten. Besonders nützlich bei Problemen mit mehreren möglichen Lösungen.

**2023 – ReAct und Agenten**
Yao et al. (ja, derselbe Yao) kombinierten Reasoning mit Actions. Das Modell denkt nicht nur, es handelt auch – es kann Werkzeuge nutzen, Informationen suchen und auf Basis der Ergebnisse weiterdenken. Die Geburt der KI-Agenten.

**2024 – Reasoning-Modelle**
OpenAI brachte o1 heraus, ein Modell, das Reasoning als festen Bestandteil seiner Architektur hat. Es "denkt" intern, bevor es antwortet. Google folgte mit Gemini 2.0 Flash Thinking. Anthropic integrierte erweiterte Reasoning-Fähigkeiten in Claude. Reasoning wurde vom Prompt-Trick zur Modelleigenschaft.

**2025 – Deep Research und autonomes Reasoning**
Modelle wie GPT-4o mit Deep Research, Claude mit erweitertem Denken und Gemini Deep Research können minutenlang eigenständig recherchieren und denken, bevor sie antworten. Die Grenze zwischen Prompting und Reasoning verschwimmt.

## Die fünf Ebenen des Reasoning

Nicht jede Reasoning-Technik ist gleich komplex. Ich unterteile sie in fünf Ebenen:

### Ebene 1: Lineares Reasoning (Chain-of-Thought)
Das Modell denkt Schritt für Schritt in einer geraden Linie. A → B → C → Ergebnis.
- Einfachste Form
- Funktioniert bei den meisten Aufgaben
- Kapitel 2 und 3 dieses Buches

### Ebene 2: Verzweigtes Reasoning (Tree-of-Thought)
Das Modell erkundet mehrere Denkpfade gleichzeitig und bewertet sie.
- Komplexer, aber mächtiger
- Besonders gut bei Problemen mit mehreren Lösungen
- Kapitel 4

### Ebene 3: Validiertes Reasoning (Self-Consistency)
Das Modell löst dasselbe Problem mehrfach und wählt die konsistenteste Antwort.
- Erhöht die Zuverlässigkeit
- Kostet mehr Tokens, aber liefert bessere Ergebnisse
- Kapitel 5

### Ebene 4: Interaktives Reasoning (ReAct)
Das Modell denkt, handelt, beobachtet und plant den nächsten Schritt.
- Die Grundlage für KI-Agenten
- Reasoning + externe Werkzeuge
- Kapitel 6

### Ebene 5: Rekursives Reasoning (Meta-Prompting, Reflexion)
Das Modell reflektiert über seinen eigenen Denkprozess und verbessert ihn.
- Die fortgeschrittenste Form
- Prompts, die Prompts verbessern
- Kapitel 7 und 8

## Wann brauchst du Reasoning?

Nicht immer. Und das ist wichtig zu verstehen.

### Reasoning LOHNT sich bei:
- **Logischen Aufgaben** – Schlussfolgerungen, Beweise, Argumentationsanalysen
- **Mathematik** – Textaufgaben, Berechnungen, Statistik
- **Planung** – Strategie, Projektplanung, Entscheidungsfindung
- **Analyse** – Pro/Contra, SWOT, Risikobewertung
- **Fehlersuche** – Debugging, Diagnose, Ursachenanalyse
- **Mehrstufige Aufgaben** – Alles, was mehr als einen Schritt erfordert
- **Aufgaben mit Constraints** – Budget, Zeitrahmen, Ressourcenlimits

### Reasoning ist ÜBERFLÜSSIG bei:
- **Einfachen Textaufgaben** – "Schreib mir eine kurze E-Mail"
- **Übersetzungen** – "Übersetze diesen Absatz ins Englische"
- **Formatierung** – "Mach daraus eine Tabelle"
- **Kreativem Brainstorming** – "Gib mir 10 Ideen für ..."
- **Zusammenfassungen** – "Fasse diesen Text zusammen"
- **Faktenabruf** – "Was ist die Hauptstadt von Frankreich?"

Die Faustregel: Wenn du die Aufgabe selbst in 10 Sekunden lösen könntest, braucht das Modell kein Reasoning. Wenn du selbst nachdenken müsstest, braucht das Modell es auch.

## Reasoning und Token-Kosten

Ein wichtiger Praxis-Aspekt: Reasoning kostet mehr Tokens. Das Modell produziert nicht nur die Antwort, sondern auch die Zwischenschritte. Bei Chain-of-Thought kann die Antwort 3-5x so lang sein wie ohne. Bei Tree-of-Thought noch mehr.

Das bedeutet:
- **Mehr Kosten** bei API-Nutzung (du zahlst pro Token)
- **Längere Antwortzeiten** (mehr Tokens = mehr Rechenzeit)
- **Mehr Kontext-Fenster-Verbrauch** (die Zwischenschritte belegen Platz)

Deshalb: Nutze Reasoning gezielt, nicht pauschal. Nicht jeder Prompt braucht "Denke Schritt für Schritt". Aber bei den richtigen Aufgaben ist der ROI enorm.

## Ein Experiment zum Einstieg

Bevor wir in die einzelnen Techniken einsteigen, möchte ich, dass du ein Gefühl dafür bekommst, was Reasoning bewirkt. Mach folgendes Experiment:

### Aufgabe
Gib deinem LLM diese Aufgabe – einmal ohne und einmal mit Reasoning-Anweisung:

**Version A (ohne Reasoning):**
```
Drei Freunde – Anna, Ben und Clara – gehen in ein Restaurant.
Anna sitzt links von Ben.
Clara sitzt nicht neben Anna.
In welcher Reihenfolge sitzen sie von links nach rechts?
```

**Version B (mit Reasoning):**
```
Drei Freunde – Anna, Ben und Clara – gehen in ein Restaurant.
Anna sitzt links von Ben.
Clara sitzt nicht neben Anna.
In welcher Reihenfolge sitzen sie von links nach rechts?

Denke Schritt für Schritt:
1. Liste alle möglichen Sitzordnungen auf
2. Prüfe jede Bedingung einzeln
3. Eliminiere alle Optionen, die eine Bedingung verletzen
4. Nenne die verbleibende Lösung
```

Vergleiche die Antworten. Version A wird wahrscheinlich direkt eine Antwort geben – manchmal richtig, manchmal falsch. Version B wird den Denkprozess zeigen und mit höherer Wahrscheinlichkeit richtig liegen.

### Auflösung

Die möglichen Reihenfolgen (von links nach rechts):
1. Anna, Ben, Clara ✓ (Anna links von Ben ✓, Clara nicht neben Anna ✓)
2. Anna, Clara, Ben ✗ (Anna links von Ben? Nein, Ben sitzt nicht rechts von Anna)
3. Ben, Anna, Clara ✗ (Anna links von Ben? Nein, Anna sitzt rechts)
4. Ben, Clara, Anna ✗ (Anna links von Ben? Nein)
5. Clara, Anna, Ben ✗ (Clara neben Anna? Ja – Bedingung verletzt)
6. Clara, Ben, Anna ✗ (Anna links von Ben? Nein)

Warte – schauen wir nochmal. "Anna sitzt links von Ben" heißt Anna kommt in der Reihe vor Ben, aber nicht unbedingt direkt daneben:
1. Anna, Ben, Clara – Anna links von Ben ✓, Clara neben Ben (nicht neben Anna) ✓
2. Anna, Clara, Ben – Anna links von Ben ✓, Clara neben Anna ✗

Antwort: Anna, Ben, Clara.

Hast du gesehen, was gerade passiert ist? Selbst ich musste die Schritte durchgehen, um sicher zu sein. Und genau deshalb funktioniert Reasoning.

## Die Grundregel dieses Buches

Jedes Kapitel in diesem Buch folgt demselben Muster:

1. **Was ist die Technik?** – Konzept und Hintergrund
2. **Wie funktioniert sie?** – Mechanismus und Aufbau
3. **Wann nutze ich sie?** – Einsatzgebiete und Grenzen
4. **Praktische Beispiele** – Mindestens 5 pro Kapitel, verschiedene Domänen
5. **Vorher/Nachher** – Direkter Vergleich: ohne vs. mit Technik
6. **Häufige Fehler** – Was schiefgehen kann und wie du es vermeidest
7. **Übungen** – Zum Selbst-Ausprobieren

Mein Anspruch: Nach jedem Kapitel kannst du die Technik sofort anwenden. Keine Theorie ohne Praxis.

---

## Übungen

### Übung 1: Reasoning-Bedarf erkennen
Bewerte die folgenden Aufgaben: Braucht das Modell Reasoning? Ja oder Nein? Begründe kurz.

1. "Übersetze 'Guten Morgen' auf Spanisch"
2. "Ein Zug fährt um 8:00 ab und braucht 3,5 Stunden. Er hat 20 Minuten Verspätung. Wann kommt er an?"
3. "Schreib mir ein Gedicht über den Herbst"
4. "Ich habe 3 Bewerbungen. Kandidat A hat 10 Jahre Erfahrung aber keine Führungserfahrung. Kandidat B hat 5 Jahre und führt ein 3er-Team. Kandidat C hat 7 Jahre und einen MBA. Wer passt am besten für die Teamleiter-Stelle?"
5. "Fasse diesen Artikel in 3 Sätzen zusammen"

### Übung 2: Erstes Reasoning-Experiment
Nimm eine Aufgabe aus deinem Alltag, bei der du normalerweise mit dem KI-Ergebnis unzufrieden bist. Teste sie zweimal:
- Einmal wie gewohnt
- Einmal mit dem Zusatz "Denke Schritt für Schritt nach. Zeige deinen Denkprozess."
Dokumentiere den Unterschied in deinem Prompt-Protokoll.

### Übung 3: Reasoning-Ebenen zuordnen
Ordne diese Techniken den fünf Ebenen zu (du kennst sie noch nicht alle im Detail – nutze dein Verständnis aus der Übersicht):
- Das Modell prüft seine eigene Antwort und korrigiert Fehler → Ebene ?
- Das Modell löst ein Problem auf drei verschiedene Arten und wählt die konsistenteste → Ebene ?
- Das Modell erklärt seine Lösung Schritt für Schritt → Ebene ?
- Das Modell sucht im Internet, liest Ergebnisse und denkt weiter → Ebene ?
- Das Modell prüft drei verschiedene Lösungswege und wählt den besten → Ebene ?
