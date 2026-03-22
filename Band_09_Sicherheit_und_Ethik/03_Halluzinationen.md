# Kapitel 3: Halluzinationen – Wenn KI überzeugend lügt

Du hast es schon in Band 1 gehört: KI kann Dinge erfinden, die nicht stimmen. In Band 4 hast du gelernt, wie Chain-of-Thought das reduziert. In Band 6 habe ich bei Medizin und Recht gewarnt. Jetzt gehen wir in die Tiefe.

Halluzinationen sind nicht nur ein kleines Ärgernis. Sie sind das fundamentale Vertrauensproblem von LLMs. Und sie sind gefährlicher, als die meisten Menschen denken – weil sie so überzeugend klingen.

## Was genau sind Halluzinationen?

Eine Halluzination ist, wenn ein LLM Informationen generiert, die falsch sind, aber als Fakt präsentiert werden. Das Modell "glaubt" nicht, dass sie wahr sind – es hat kein Konzept von Wahrheit. Es generiert die wahrscheinlichste nächste Token-Sequenz, und manchmal ist die wahrscheinlichste Sequenz faktisch falsch.

### Typen von Halluzinationen

**Fakten-Halluzinationen:** Das Modell erfindet Fakten. *"Albert Einstein gewann den Nobelpreis für die Relativitätstheorie."* (Er gewann ihn für den photoelektrischen Effekt.)

**Quellen-Halluzinationen:** Das Modell erfindet Quellen – Autorennamen, Zeitschriften, DOIs, die nicht existieren. Besonders gefährlich in der Wissenschaft und im Recht.

**Logik-Halluzinationen:** Das Modell zieht falsche Schlüsse aus richtigen Prämissen. Die Argumentation klingt überzeugend, aber der logische Sprung ist falsch.

**Zahlen-Halluzinationen:** Das Modell erfindet Statistiken, Prozentzahlen und Berechnungen. *"Studien zeigen, dass 73% der Deutschen..."* – eine Studie, die nicht existiert, mit einer Zahl, die erfunden ist.

**Kompetenz-Halluzinationen:** Das Modell behauptet, etwas zu können, was es nicht kann. *"Ich habe die URL überprüft und sie ist sicher"* – obwohl es keine URLs prüfen kann.

## Warum halluzinieren LLMs?

### Das Grundproblem

LLMs sind Muster-Vervollständiger, keine Wissensdatenbanken. Sie generieren die wahrscheinlichste nächste Wortsequenz basierend auf ihren Trainingsdaten. Wenn die wahrscheinlichste Sequenz faktisch falsch ist – zum Beispiel, weil die korrekte Information selten in den Trainingsdaten vorkommt – generiert das Modell trotzdem diese Sequenz.

### Wann halluzinieren Modelle besonders häufig?

1. **Bei spezifischen Fakten:** Namen, Daten, Zahlen, URLs, Zitate. Je spezifischer, desto wahrscheinlicher falsch.
2. **Bei seltenem Wissen:** Nischen-Themen, die selten in den Trainingsdaten vorkommen.
3. **Bei veralteten Informationen:** Alles nach dem Trainings-Cutoff ist dem Modell unbekannt.
4. **Bei hoher Temperatur:** Mehr "Kreativität" bedeutet mehr Abweichung von den wahrscheinlichsten Tokens.
5. **Bei langen Antworten:** Je länger die Antwort, desto mehr Gelegenheiten für Fehler.
6. **Wenn das Modell keine gute Antwort hat:** Statt "Ich weiß es nicht" zu sagen, generiert es eine plausibel klingende Antwort. Das liegt am Training – Modelle werden belohnt für hilfreiche Antworten, nicht für Ehrlichkeit.

### Halluzinationsraten (Vectara-Benchmark, Stand 2026)

Vectara, ein auf Retrieval spezialisiertes Unternehmen, misst Halluzinationsraten bei Zusammenfassungsaufgaben. Die Raten sind über die Jahre dramatisch gesunken – von 21,8% (2021) auf unter 1% bei den besten Modellen (2025):

| Modell | Halluzinationsrate |
|--------|-------------------|
| Gemini 2.0 Flash | 0,7% |
| o3-mini-high | 0,8% |
| GPT-5 | 1,4% |
| GPT-4o | 1,5% |
| Claude Sonnet | 4,4% |

Vier Modelle liegen inzwischen unter 1% – ein Meilenstein.

**Aber:** Auf einem schwierigeren Benchmark (7.700 Artikel, bis zu 32.000 Tokens) sieht das Bild anders aus: Jedes getestete Reasoning-Modell überschritt 10% Halluzinationsrate. Überraschend: Reasoning-Modelle ("Denk-Modelle") schneiden bei faktenbasierten Zusammenfassungen **schlechter** ab als einfache Modelle.

**Quellen-Halluzinationen in der Rechtswelt:** Stanford CodeX fand, dass allgemeine LLMs in 30-45% der Rechtsrecherche-Antworten Fallzitate erfinden.

**Der Kosten-Faktor:** Deloitte fand, dass 47% der Enterprise-KI-Nutzer 2024 mindestens eine wichtige Entscheidung auf Basis halluzinierter Inhalte trafen. Geschätzter globaler finanzieller Schaden: **67,4 Milliarden Dollar** im Jahr 2024.

**Der Vertrauens-Paradox (MIT, Januar 2025):** Modelle verwenden Wörter wie "definitiv" und "sicherlich" **34% häufiger bei falschen Antworten** als bei richtigen. Je überzeugter die KI klingt, desto vorsichtiger solltest du sein.

## Echte Konsequenzen

**Die Gerichtsfälle häufen sich:** Über **700 Gerichtsverfahren** betreffen inzwischen KI-halluzinierte Inhalte (Stand 2026, laut LexisNexis/Bloomberg Law Tracking). Die Rate beschleunigte sich von 2 pro Woche auf 2-3 pro Tag bis Frühjahr 2025.

**Mata v. Avianca (2023, New York):** Der Wendepunkt. Zwei Anwälte reichten einen Schriftsatz mit sechs fiktiven Gerichtsentscheidungen ein – alle von ChatGPT generiert. 5.000 Dollar Strafe, öffentliche Bloßstellung.

**MyPillow/Lindell (Juli 2025):** Zwei Anwälte mussten je 3.000 Dollar zahlen, weil sie 24+ halluzinierte Fallzitate einreichten.

**Noland v. Land of the Free (Kalifornien, September 2025):** 21 von 23 Zitaten waren erfunden. 10.000 Dollar Strafe. Und ein Novum: Das Gericht sprach auch die Pflicht an, **die Zitate des Gegners** auf KI-Fälschungen zu prüfen.

**Colorado (2025):** Ein Anwalt wurde suspendiert, weil er in mehreren Fällen erfundene Zitate eingereicht hatte.

**Pennsylvania (2025-2026):** Mindestens 13 Fälle mit bestätigten KI-Halluzinationen.

**Medizinische Fehlinformationen:** Studien zeigen, dass LLMs bei medizinischen Fragen in 5-15% der Fälle potenziell schädliche Informationen generieren. In einem Fall empfahl ein Chatbot einem Elternteil, dem Kind eine gefährliche Menge eines Medikaments zu geben.

## Gegenmaßnahmen

### Strategie 1: Verifiziere alles

Die wichtigste Regel, die ich in diesem Buch geschrieben habe, und ich wiederhole sie hier zum letzten Mal: **Vertraue, aber verifiziere.** Jede Zahl. Jede Quelle. Jedes Zitat. Jede Aussage, die als Fakt präsentiert wird.

Das ist unbequem. Es kostet Zeit. Aber es ist der einzige Weg, der zuverlässig funktioniert.

### Strategie 2: RAG (Retrieval Augmented Generation)

Aus Band 7 kennst du RAG. In der Sicherheit ist RAG die wichtigste technische Gegenmaßnahme gegen Halluzinationen. Statt das Modell aus dem Gedächtnis antworten zu lassen, gibst du ihm die relevanten Dokumente als Kontext. Das reduziert Halluzinationen um 60-80% in den meisten Szenarien.

**Aber Vorsicht:** RAG eliminiert Halluzinationen nicht. Das Modell kann die Dokumente falsch interpretieren oder Informationen erfinden, die nicht in den Dokumenten stehen. RAG + Quellenangabe + menschliche Prüfung ist die sicherste Kombination.

### Strategie 3: Citationen anfordern

Fordere das Modell auf, seine Quellen zu nennen. Bei Claude: Citationen aktivieren, die auf spezifische Stellen in den mitgegebenen Dokumenten verweisen. Bei RAG: "Zitiere die relevanten Stellen aus dem Kontext."

**Einschränkung:** Ohne RAG kann das Modell Quellen erfinden. Citationen sind nur verlässlich, wenn das Modell auf echte Dokumente im Kontext verweist.

### Strategie 4: Temperatur senken

Niedrigere Temperatur = weniger "Kreativität" = weniger Halluzinationen. Für faktische Aufgaben: Temperatur 0.0 oder nahe daran. Für kreative Aufgaben: Höhere Temperatur, aber dann mit menschlicher Prüfung.

### Strategie 5: "Ich weiß es nicht" erlauben

Viele System-Prompts fordern: "Beantworte die Frage." Besser: "Beantworte die Frage. Wenn du die Antwort nicht sicher weißt, sage ehrlich: 'Ich bin mir nicht sicher.' Das ist besser als eine möglicherweise falsche Antwort."

Modelle, die explizit die Erlaubnis bekommen, unsicher zu sein, halluzinieren weniger. Sie müssen nicht jede Frage mit einer überzeugenden Antwort beantworten.

### Strategie 6: Chain-of-Thought und Extended Thinking

Aus Band 4: Wenn das Modell Schritt für Schritt denkt, macht es weniger Fehler. Extended Thinking (Claude) und Reasoning-Modi (o3) reduzieren Halluzinationen messbar, weil das Modell seine eigene Logik überprüfen kann.

### Strategie 7: Self-Consistency

Stelle dieselbe Frage mehrfach und vergleiche die Antworten. Wenn drei von fünf Antworten übereinstimmen, ist die Wahrscheinlichkeit höher, dass sie korrekt sind. Wenn alle fünf unterschiedlich sind, ist das ein Warnsignal.

## Halluzinationen als Feature?

Ein Gedanke zum Schluss: In manchen Kontexten sind Halluzinationen kein Bug, sondern ein Feature. Kreatives Schreiben, Brainstorming, Ideengenerierung – hier willst du, dass das Modell über das Bekannte hinausgeht. Die Fähigkeit, plausible aber neue Verbindungen zu ziehen, ist genau das, was Kreativität auszeichnet.

Das Problem entsteht, wenn du kreative Fähigkeiten in einem faktischen Kontext einsetzt. Ein Modell, das großartige Geschichten erfindet, erfindet auch großartige Quellen. Die Lösung ist nicht, Halluzinationen abzuschaffen – sondern zu wissen, wann sie ein Risiko sind und wann nicht.

---

## Übungen

### Übung 1: Halluzinationen provozieren
Frage ein LLM nach sehr spezifischen Fakten (z.B. "Wann wurde das Rathaus von Buxtehude gebaut?"). Verifiziere die Antwort. Wie oft liegt das Modell falsch?

### Übung 2: Quellen-Check
Lass ein LLM 5 Quellen zu einem Thema nennen (ohne RAG). Überprüfe jede einzelne. Wie viele existieren wirklich?

### Übung 3: "Ich weiß es nicht"-Prompt
Schreibe zwei System-Prompts: Einen der fordert "Beantworte immer" und einen mit "Sage ehrlich, wenn du unsicher bist." Vergleiche die Halluzinationsrate bei 10 Faktenfragen.

### Übung 4: Self-Consistency testen
Stelle dieselbe Faktenfrage 5 Mal (mit Temperatur 0.5). Wie konsistent sind die Antworten? Korreliert Konsistenz mit Korrektheit?
