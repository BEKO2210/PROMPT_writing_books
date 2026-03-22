# Kapitel 3: One-Shot Prompting – Ein Beispiel sagt mehr als tausend Worte

Du kennst das Sprichwort. Und bei Prompting stimmt es ganz besonders.

One-Shot Prompting bedeutet: Du gibst dem Modell genau ein Beispiel, bevor du die eigentliche Aufgabe stellst. Ein einziges Beispiel, das zeigt: "So soll das Ergebnis aussehen."

## Warum ein einziges Beispiel so viel bewirkt

Stell dir vor, jemand bittet dich: "Schreib eine Produktbewertung." Du würdest wahrscheinlich fragen: "Wie soll die aussehen? Lang? Kurz? Mit Sternen? Formal?"

Aber wenn jemand sagt: "Schreib eine Produktbewertung. Hier ist ein Beispiel: *'Der Akku hält ewig, die Kamera ist solide, aber die App stürzt regelmäßig ab. 3,5/5 Sterne.'* Jetzt schreib eine für Kopfhörer." – dann weißt du sofort, was gemeint ist. Länge, Stil, Struktur – alles klar.

Genau so funktioniert One-Shot bei LLMs. Das Modell erkennt das Muster im Beispiel und repliziert es.

## Die Anatomie eines One-Shot-Prompts

Ein One-Shot-Prompt hat drei Teile:

1. **Aufgabenbeschreibung** – Was soll das Modell tun?
2. **Beispiel** – Ein konkretes Input-Output-Paar
3. **Eigentliche Aufgabe** – Die Aufgabe, die das Modell lösen soll

**Struktur:**
```
[Aufgabenbeschreibung]

Beispiel:
Input: [Beispiel-Eingabe]
Output: [Beispiel-Ausgabe]

Aufgabe:
Input: [Deine tatsächliche Eingabe]
Output:
```

## One-Shot in Aktion

### Beispiel 1: Produktbeschreibungen

```
Schreibe kurze, ansprechende Produktbeschreibungen für einen
Online-Shop.

Beispiel:
Produkt: Thermobecher 500ml, Edelstahl, doppelwandig
Beschreibung: Dein Kaffee bleibt heiß, deine Hand bleibt kühl.
Der doppelwandige Edelstahl-Thermobecher hält Getränke bis zu
6 Stunden warm – perfekt für lange Meetings und Pendler-Morgen.
BPA-frei und spülmaschinengeeignet.

Aufgabe:
Produkt: Bluetooth-Kopfhörer, Over-Ear, Active Noise Cancelling, 30h Akku
Beschreibung:
```

Das Modell versteht sofort: Es soll eine ähnlich lange, ähnlich aufgebaute Beschreibung schreiben. Mit Benefit-Sprache. Mit konkreten Details.

### Beispiel 2: Daten extrahieren

```
Extrahiere strukturierte Daten aus Kundenbewertungen.

Beispiel:
Bewertung: "Super schnelle Lieferung, aber die Verpackung war
beschädigt. Das Produkt selbst funktioniert einwandfrei. Würde
wieder bestellen."
Extraktion:
- Lieferung: positiv (schnell)
- Verpackung: negativ (beschädigt)
- Produkt: positiv (funktioniert)
- Wiederkauf: ja

Aufgabe:
Bewertung: "Habe den Artikel nach 2 Wochen zurückgeschickt. Die
Farbe war komplett anders als auf dem Foto. Der Kundenservice war
allerdings sehr hilfsbereit und hat sofort erstattet."
Extraktion:
```

Ohne das Beispiel hätte das Modell die Daten vielleicht als Fließtext ausgegeben, oder mit anderen Kategorien, oder in einem völlig anderen Format. Das Beispiel definiert das Schema.

### Beispiel 3: Tonalität treffen

```
Schreibe Social-Media-Posts im Stil unserer Marke.

Beispiel:
Thema: Neues Feature – Dark Mode
Post: Dark Mode ist da. Endlich. Eure Augen können uns danken.
Ab sofort in der App. Update und ausprobieren. 🌙

Aufgabe:
Thema: Neues Feature – Offline-Modus
Post:
```

Hier zeigt das Beispiel nicht nur das Format, sondern den Ton. Kurze Sätze. Frech. Direkt. Das Modell übernimmt diesen Stil.

## Wann One-Shot besser ist als Zero-Shot

One-Shot lohnt sich besonders in diesen Situationen:

### Ungewöhnliche Formate
Wenn du ein Format brauchst, das nicht zum Standard gehört. Statt es umständlich zu beschreiben, zeigst du es einfach.

### Konsistenz
Wenn du mehrere ähnliche Texte brauchst, die alle gleich aufgebaut sein sollen. Das Beispiel definiert den Standard.

### Subjektive Qualität
Wenn "gut" eine Geschmacksfrage ist. Statt zu beschreiben, wie der Text klingen soll, zeigst du es.

### Komplexe Transformationen
Wenn du Daten von einem Format in ein anderes umwandeln willst. Ein Beispiel ist klarer als jede Beschreibung.

## Die Qualität des Beispiels entscheidet

Das ist der wichtigste Punkt in diesem Kapitel: Dein Beispiel muss gut sein. Wenn du ein mittelmäßiges Beispiel gibst, bekommst du mittelmäßige Ergebnisse. Das Modell repliziert, was es sieht – inklusive der Schwächen.

**Kriterien für ein gutes Beispiel:**

1. **Repräsentativ** – Es sollte typisch für die Aufgabe sein, nicht ein Sonderfall
2. **Hochwertig** – Es sollte das Qualitätsniveau zeigen, das du erwartest
3. **Vollständig** – Es sollte alle Elemente enthalten, die du im Output willst
4. **Eindeutig** – Es sollte kein Rauschen oder irrelevante Elemente enthalten

**Schlechtes Beispiel:**
```
Beispiel:
Eingabe: Hund
Ausgabe: Ein Hund ist ein Tier das bellt und als haustier gehalten wird es gibt viele Rassen zum beispiel Pudel oder Schäferhund
```

**Gutes Beispiel:**
```
Beispiel:
Eingabe: Hund
Ausgabe: Ein Hund (Canis lupus familiaris) ist ein domestiziertes
Säugetier aus der Familie der Canidae. Als eines der ältesten
Haustiere des Menschen gibt es heute über 350 anerkannte Rassen,
von kleinen Chihuahuas bis zu großen Deutschen Doggen.
```

Du siehst den Unterschied. Das erste Beispiel hat keine Satzzeichen, keine Struktur und keine Tiefe. Wenn du das als Vorlage gibst, wundere dich nicht über schlampige Ergebnisse.

## One-Shot vs. Längere Anweisungen

Manchmal fragen sich Leute: "Soll ich lieber ein Beispiel geben oder lieber genauer beschreiben, was ich will?"

Die Antwort: Es kommt drauf an.

| Situation | Besserer Ansatz |
|---|---|
| Format ist schwer zu beschreiben | One-Shot (zeigen statt erklären) |
| Stil/Ton soll getroffen werden | One-Shot (Beispiel definiert den Ton) |
| Logik/Regeln sollen befolgt werden | Anweisung (klare Regeln formulieren) |
| Beides nötig | Kombination (Regeln + Beispiel) |

Und ja, du kannst beides kombinieren. Ein Prompt mit klaren Anweisungen UND einem Beispiel ist oft die beste Lösung.

## Zusammenfassung

- One-Shot = Eine Aufgabe mit genau einem Beispiel
- Das Beispiel definiert Format, Stil, Struktur und Qualitätsniveau
- Funktioniert besser als Zero-Shot bei ungewöhnlichen Formaten und subjektiver Qualität
- Die Qualität des Beispiels bestimmt die Qualität des Ergebnisses
- Kann mit Anweisungen kombiniert werden

---

## Übung

**One-Shot Upgrade**

Nimm die drei Zero-Shot-Prompts aus der Übung des letzten Kapitels und mache daraus One-Shot-Prompts:

1. Schreibe zuerst selbst ein Beispiel für das gewünschte Ergebnis
2. Füge es in den Prompt ein
3. Teste den neuen Prompt im selben LLM
4. Bewerte das Ergebnis auf der gleichen 1-10 Skala
5. Vergleiche: Hat sich die Qualität verbessert?

Besonders spannend: Teste den gleichen One-Shot-Prompt mit verschiedenen LLMs (ChatGPT, Claude, Gemini). Wo macht das Beispiel den größten Unterschied?
