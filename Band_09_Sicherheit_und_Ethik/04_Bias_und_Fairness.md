# Kapitel 4: Bias und Fairness – Wenn KI diskriminiert

KI ist nicht neutral. Sie wurde mit menschlichen Daten trainiert, und menschliche Daten enthalten menschliche Vorurteile. Das Ergebnis: KI-Systeme können diskriminieren – systematisch, skaliert und oft unsichtbar.

Das ist kein theoretisches Problem. Es passiert in Bewerbungsprozessen, Kreditentscheidungen, Polizeiarbeit, Gesundheitsversorgung und Justiz. Und es betrifft dich, wenn du KI für Entscheidungen nutzt, die Menschen betreffen.

## Was ist KI-Bias?

Bias bedeutet systematische Verzerrung. Ein KI-Modell ist "biased", wenn es bestimmte Gruppen von Menschen systematisch anders behandelt als andere – ohne dass es dafür einen sachlichen Grund gibt.

### Woher kommt der Bias?

**1. Trainingsdaten-Bias**

LLMs werden mit Texten aus dem Internet trainiert. Das Internet spiegelt die Gesellschaft wider – mit allen Vorurteilen, Stereotypen und Ungleichheiten. Wenn in den Trainingsdaten Ärzte häufiger als männlich und Krankenschwestern häufiger als weiblich beschrieben werden, lernt das Modell dieses Muster.

Das ist kein Fehler im Training. Es ist eine korrekte Abbildung der Daten. Aber korrekte Abbildung ungerechter Realität führt zu ungerechten Ergebnissen.

**2. Reprsentations-Bias**

Manche Gruppen sind in den Trainingsdaten überrepräsentiert, andere unterrepräsentiert. Englischsprachige, westliche, gut vernetzte Communities produzieren mehr Text im Internet. Folge: Das Modell "versteht" diese Perspektiven besser als andere.

Für deutschsprachige Nutzer ist das relevant: Die Trainingsdaten sind überwiegend englisch. Deutschsprachige Kontexte, Rechtslagen und kulturelle Normen sind unterrepräsentiert.

**3. Label-Bias**

Wenn Menschen Trainingsdaten annotieren (z.B. "Ist dieser Text toxisch?"), bringen sie ihre eigenen Biases ein. Was als "toxisch" gilt, unterscheidet sich je nach Kultur, Generation und persönlicher Erfahrung.

**4. Algorithmus-Bias**

Bestimmte Trainingsmethoden können Bias verstärken. RLHF (Reinforcement Learning from Human Feedback) optimiert auf menschliche Bewertungen – die selbst biased sein können.

## Wo Bias im Alltag auftritt

### Bewerbungen und HR

Amazons berüchtigtes KI-Recruiting-Tool (2018) benachteiligte systematisch Frauen, weil es auf historischen Einstellungsdaten trainiert wurde – und in der Vergangenheit wurden mehr Männer eingestellt. Amazon schaltete das System ab.

Das Problem existiert 2026 noch immer. Wenn du in Band 6 die HR-Prompts nutzt, beachte:

*"Erstelle eine Stellenausschreibung"* kann gender-biased Formulierungen produzieren. "Durchsetzungsstark", "analytisch", "teamfähig" – Studien zeigen, dass diese Wörter unterschiedliche Geschlechter unterschiedlich ansprechen.

*"Bewerte diesen Lebenslauf"* kann Bewerber mit nicht-westlichen Namen, Lücken im Lebenslauf oder nicht-traditionellen Karrierewegen systematisch schlechter bewerten.

### Kredit und Finanzen

KI-Systeme für Kreditentscheidungen können Wohnort, Postleitzahl oder Einkaufsmuster als Proxy für ethnische Zugehörigkeit nutzen – selbst wenn Ethnizität nicht direkt im Datensatz steht. Das nennt man "Proxy-Diskriminierung".

### Sprache und Übersetzung

*"The doctor told the nurse that she..."* – welches Pronomen wählt das Modell für "doctor" und welches für "nurse"? In vielen Sprachen mit grammatischem Geschlecht (Deutsch eingeschlossen) muss das Modell eine Wahl treffen. Und diese Wahl spiegelt Stereotypen wider.

### Bild-Generierung

Frag ein Bildgenerations-Modell nach "CEO" und du bekommst überwiegend weiße Männer in Anzügen. Frag nach "Krankenschwester" und du bekommst überwiegend weiße Frauen. Die Modelle reproduzieren visuelle Stereotypen.

### Medizin

Medizinische KI-Systeme, die auf Daten trainiert werden, in denen bestimmte ethnische Gruppen unterrepräsentiert sind, können bei diesen Gruppen schlechtere Diagnosen liefern. Hautkrebs-Erkennung funktioniert besser auf heller Haut als auf dunkler – weil die Trainingsdaten mehrheitlich helle Haut zeigen.

## Bias erkennen

### In deinen eigenen Prompts

Teste systematisch: Lass dasselbe Prompt mit verschiedenen Namen, Geschlechtern, Altersangaben und kulturellen Hintergründen laufen. Unterscheiden sich die Ergebnisse?

*"Schreibe eine Empfehlung für einen Mitarbeiter namens Thomas Müller, 35, der eine Beförderung anstrebt."*

vs.

*"Schreibe eine Empfehlung für eine Mitarbeiterin namens Ayşe Yılmaz, 35, die eine Beförderung anstrebt."*

Sind die Empfehlungen gleich stark? Werden die gleichen Adjektive verwendet? Wird die gleiche Kompetenz zugeschrieben?

### In KI-Systemen

**Disparate Impact Test:** Vergleiche die Ergebnisse für verschiedene demografische Gruppen. Wenn eine Gruppe systematisch schlechter abschneidet, liegt möglicherweise Bias vor.

**Counterfactual Testing:** Ändere einen einzelnen Faktor (Name, Geschlecht, Herkunft) und schau, ob sich das Ergebnis ändert. Wenn ja: Bias.

**Red Teaming:** Teste gezielt mit edge cases und sensiblen Szenarien (mehr in Kapitel 9).

## Bias reduzieren

### Strategie 1: Bewusstsein

Der erste Schritt: Wissen, dass Bias existiert. Du liest dieses Kapitel – das ist bereits der wichtigste Schritt. Die meisten Bias-Probleme entstehen nicht aus böser Absicht, sondern aus Unwissenheit.

### Strategie 2: Diverse Perspektiven einfordern

*"Beantworte diese Frage aus mindestens 3 verschiedenen kulturellen/sozialen Perspektiven."*

*"Prüfe deine Antwort auf mögliche Gender-, Alters- oder Kultur-Biases."*

Das Modell kann sich selbst (teilweise) korrigieren, wenn es explizit darauf hingewiesen wird.

### Strategie 3: Bias-Checks als Workflow-Schritt

In Band 6 habe ich bei Stellenausschreibungen einen Bias-Check-Prompt gezeigt. Mach das zur Routine: Jeder Text, der Menschen betrifft (Stellenausschreibungen, Bewertungen, Empfehlungen), wird vor dem Versand auf Bias geprüft.

### Strategie 4: Diverse Testdaten

Teste deine Prompts und Systeme mit diversen Eingabedaten. Nicht nur "Max Mustermann", sondern auch "Fatima Al-Hussein", "Nguyen Van Minh" und "Olga Petrowna".

### Strategie 5: Menschliche Kontrolle

Bei allen Entscheidungen, die Menschen betreffen: Ein Mensch prüft das KI-Ergebnis. Besonders in HR, Kredit, Justiz, Gesundheit und Bildung.

### Strategie 6: Transparenz

Wenn KI bei Entscheidungen mitwirkt, die Menschen betreffen: Kommuniziere das. Menschen haben ein Recht zu wissen, ob eine KI an der Entscheidung beteiligt war. (Das fordert auch der EU AI Act – mehr in Kapitel 6.)

## Die ethische Dimension

Bias ist nicht nur ein technisches Problem. Es ist ein gesellschaftliches. KI-Systeme, die Bias reproduzieren, zementieren bestehende Ungleichheiten – und skalieren sie. Ein biased Mensch trifft hundert Entscheidungen am Tag. Ein biased KI-System trifft Millionen.

Die Verantwortung liegt bei dir. Nicht beim Modell, nicht beim Hersteller – bei dir, dem Nutzer. Du entscheidest, wofür du KI einsetzt, wie du die Ergebnisse prüfst und ob du Bias tolerierst oder aktiv bekämpfst.

---

## Übungen

### Übung 1: Bias-Test
Lass ein LLM Empfehlungsschreiben für 6 fiktive Personen schreiben (verschiedene Namen, Geschlechter, Hintergründe). Vergleiche Wortwahl, Stärke und Ton.

### Übung 2: Stellenausschreibungs-Check
Nimm eine echte Stellenausschreibung und prüfe sie auf die 5 Bias-Typen aus Band 6 (Gender, Alter, Erfahrung, Kultur, Disability).

### Übung 3: Counterfactual Test
Erstelle einen Prompt, der eine Entscheidung trifft (z.B. Kreditwürdigkeit). Ändere nur den Namen. Ändert sich das Ergebnis?

### Übung 4: Bias-Bewusstsein
Fordere ein LLM auf, einen kontroversen Sachverhalt aus 3 verschiedenen kulturellen Perspektiven zu beleuchten. Sind die Perspektiven wirklich unterschiedlich?
