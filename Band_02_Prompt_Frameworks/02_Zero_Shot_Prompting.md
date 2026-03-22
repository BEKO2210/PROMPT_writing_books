# Kapitel 2: Zero-Shot Prompting – Ohne Beispiel zum Ziel

Zero-Shot Prompting ist das, was du bisher die ganze Zeit gemacht hast. Du gibst dem Modell eine Aufgabe – ohne Beispiel, ohne Vorlage, ohne "So soll das Ergebnis aussehen". Einfach: Aufgabe rein, Ergebnis raus.

Klingt unspektakulär? Ist es auch. Aber es lohnt sich, bewusst darüber nachzudenken, weil Zero-Shot die Basis für alles Weitere ist.

## Was Zero-Shot bedeutet

"Shot" kommt aus dem Englischen und bedeutet hier so viel wie "Beispiel". "Zero Shots" heißt: null Beispiele.

Du sagst dem Modell, *was* es tun soll. Aber du zeigst ihm nicht, *wie* das Ergebnis aussehen soll.

**Beispiel für Zero-Shot:**
```
Fasse den folgenden Text in drei Sätzen zusammen:

[Text hier einfügen]
```

Du gibst keine Beispiel-Zusammenfassung. Du vertraust darauf, dass das Modell weiß, was "zusammenfassen" bedeutet und wie eine gute Zusammenfassung aussieht.

Und meistens klappt das. Erstaunlich gut sogar.

## Warum Zero-Shot oft reicht

Moderne LLMs wie GPT-4, Claude 4 oder Gemini sind so gut vortrainiert, dass sie die meisten Standardaufgaben ohne Beispiele bewältigen. Sie haben während ihres Trainings Millionen von Zusammenfassungen, Übersetzungen, Analysen und Texten gesehen. Sie "wissen", wie diese Formate aussehen.

Zero-Shot ist ideal, wenn:

- Die Aufgabe klar und eindeutig ist
- Du ein Standardformat erwartest (Liste, Zusammenfassung, Übersetzung)
- Du schnell ein Ergebnis brauchst und keine Zeit für aufwendige Prompts hast
- Das Thema zum Allgemeinwissen gehört

**Gute Zero-Shot-Aufgaben:**
- "Übersetze diesen Text ins Englische"
- "Schreibe eine Betreffzeile für eine E-Mail über Projektverzögerung"
- "Erkläre Photosynthese für einen 10-Jährigen"
- "Liste 5 Vorteile von Remote-Arbeit auf"

## Wann Zero-Shot nicht reicht

Es gibt Situationen, in denen Zero-Shot an seine Grenzen stößt:

### 1. Ungewöhnliche Formate

Wenn du ein sehr spezifisches Format brauchst, das nicht zum Standard gehört, wird Zero-Shot unpräzise.

```
Schreib eine Produktbeschreibung im Stil einer Weinverkostungs-Notiz
für ein Softwareprodukt.
```

Das Modell wird etwas produzieren, aber ob es deinem Geschmack entspricht? Unwahrscheinlich. Hier wäre ein Beispiel (One-Shot) hilfreicher.

### 2. Konsistente Ausgaben

Wenn du mehrere Texte brauchst, die alle gleich aufgebaut sein sollen, ist Zero-Shot riskant. Jedes Mal entscheidet das Modell neu, wie es die Aufgabe angeht. Mal ist die Zusammenfassung 2 Sätze lang, mal 5. Mal benutzt es Aufzählungszeichen, mal nicht.

### 3. Fachspezifische Aufgaben

Bei sehr spezialisierten Aufgaben – juristisches Schreiben, medizinische Dokumentation, technische Spezifikationen – fehlt dem Modell manchmal der genaue Kontext, wie das Ergebnis in *deinem* Fachgebiet aussehen soll.

### 4. Subjektive Qualität

Wenn "gut" eine Frage des persönlichen Geschmacks ist, kann das Modell nicht erraten, was du meinst. Soll der Blogartikel witzig sein oder seriös? Kurze Sätze oder verschachtelte? Ohne Beispiel ist das Glückssache.

## Zero-Shot mit guter Struktur

Nur weil du keine Beispiele gibst, heißt das nicht, dass dein Prompt kurz sein muss. Du kannst Zero-Shot-Prompts trotzdem strukturiert aufbauen. Tatsächlich sind die besten Zero-Shot-Prompts sehr detailliert – nur eben ohne Beispiel-Output.

**Schwacher Zero-Shot:**
```
Schreib eine E-Mail an einen Kunden.
```

**Starker Zero-Shot:**
```
Schreibe eine professionelle E-Mail an einen Bestandskunden, der sich
über eine verspätete Lieferung beschwert hat.

Inhalt: Entschuldigung, Erklärung (Lieferketten-Problem), konkrete
Lösung (Expresslieferung auf unsere Kosten + 10% Gutschein).

Ton: Verständnisvoll, lösungsorientiert, nicht unterwürfig.
Länge: 150-200 Wörter.
Absender: Kundenservice-Team der Firma TechShop.
```

Das ist immer noch Zero-Shot – kein Beispiel einer fertigen E-Mail. Aber der Prompt gibt dem Modell genug Information, um ein brauchbares Ergebnis zu produzieren.

## Die Zero-Shot-Faustregel

Je klarer deine Aufgabenbeschreibung, desto weniger brauchst du Beispiele. Umgekehrt: Je vager dein Prompt, desto mehr brauchst du Beispiele, um die Lücke zu füllen.

Das lässt sich als Formel ausdrücken:

```
Prompt-Qualität = Klarheit der Anweisung + Qualität der Beispiele
```

Bei Zero-Shot muss die Klarheit der Anweisung die ganze Arbeit machen. Und das geht – wenn du die Grundlagen aus Band 1 anwendest.

## Zero-Shot in der Praxis: 5 Templates

Hier sind fünf Zero-Shot-Templates, die du sofort verwenden kannst:

### Template 1: Zusammenfassung
```
Fasse den folgenden Text zusammen.
Maximal [X] Sätze.
Fokus auf: [Hauptthema/Aspekt].
Zielgruppe: [Wer soll das lesen?].

Text:
[Text einfügen]
```

### Template 2: Analyse
```
Analysiere den folgenden [Text/Datensatz/Sachverhalt].
Fokussiere dich auf: [Aspekte].
Strukturiere deine Analyse in:
1. Zusammenfassung (2-3 Sätze)
2. Haupterkenntnisse (Aufzählung)
3. Empfehlung (1-2 Sätze)

[Inhalt einfügen]
```

### Template 3: Umschreiben
```
Schreibe den folgenden Text um.
Zielgruppe: [Wer?]
Ton: [Welcher Stil?]
Länge: [Ungefähr wie lang?]
Behalte bei: [Was soll gleich bleiben?]

Originaltext:
[Text einfügen]
```

### Template 4: Brainstorming
```
Generiere [X] Ideen für [Thema].
Kontext: [Wofür brauchst du die Ideen?]
Einschränkungen: [Budget, Zeitrahmen, Ressourcen]
Format: Nummerierte Liste mit jeweils 1-2 Sätzen Erklärung.
```

### Template 5: Erklärung
```
Erkläre [Konzept] so, dass [Zielgruppe] es versteht.
Verwende [Analogien/Beispiele/keine Fachbegriffe].
Länge: [X] Wörter.
Beginne mit dem wichtigsten Punkt.
```

## Zusammenfassung

- Zero-Shot = Aufgabe ohne Beispiel
- Funktioniert gut bei Standardaufgaben und klaren Anweisungen
- Schwächen bei ungewöhnlichen Formaten und subjektiver Qualität
- Je klarer dein Prompt, desto besser das Ergebnis ohne Beispiele
- Die meisten deiner Alltagsprompts werden Zero-Shot sein – und das ist völlig okay

---

## Übung

**Zero-Shot Challenge**

Schreibe drei Zero-Shot-Prompts für folgende Aufgaben. Nutze dabei mindestens 3 der 5 Bausteine aus Band 1 (Aufgabe, Kontext, Format, Ton, Einschränkungen):

1. Eine LinkedIn-Post-Idee für dein Fachgebiet
2. Eine Erklärung von Blockchain für deine Großmutter
3. Drei Verbesserungsvorschläge für eine Teammeeting-Kultur

Teste die Prompts in einem LLM deiner Wahl. Bewerte die Ergebnisse auf einer Skala von 1-10. Merke dir die Bewertung – in den nächsten Kapiteln vergleichst du sie mit One-Shot und Few-Shot Varianten derselben Aufgaben.
