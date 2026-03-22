# Kapitel 2: Chain-of-Thought – Die Mutter aller Reasoning-Techniken

Chain-of-Thought (CoT) ist die wichtigste Reasoning-Technik. Wenn du aus diesem ganzen Buch nur eine Sache mitnimmst, dann diese.

## Die Idee

Chain-of-Thought bedeutet: Du bringst das Modell dazu, seinen Denkprozess zu zeigen, bevor es eine Antwort gibt. Statt direkt zum Ergebnis zu springen, soll es die Zwischenschritte aufschreiben.

Das Konzept stammt aus einem Paper von Jason Wei et al. (Google Brain, 2022). Die Forscher zeigten, dass LLMs bei Aufgaben wie Mathematik, Logik und Alltagsreasoning dramatisch besser werden, wenn man ihnen Beispiele mit Denkschritten gibt.

Dramatisch besser heißt: Bei manchen Benchmarks verbesserte sich die Genauigkeit um über 50 Prozentpunkte. Fünfzig. Das ist kein marginaler Gewinn – das ist ein Paradigmenwechsel.

## Wie CoT funktioniert

Die klassische CoT-Methode nutzt Few-Shot Learning (das kennst du aus Band 2). Du gibst dem Modell ein Beispiel mit Denkschritten und stellst dann deine eigentliche Frage.

### Das Grundmuster

```
Frage: Lisa hat 5 Äpfel. Sie gibt 2 an Tom und kauft dann
3 neue. Wie viele hat sie?

Denkschritte:
- Lisa startet mit 5 Äpfeln
- Sie gibt 2 an Tom: 5 - 2 = 3
- Sie kauft 3 neue: 3 + 3 = 6
- Lisa hat 6 Äpfel

Antwort: 6

---

Frage: Ein Laden hat 50 T-Shirts. Am Montag werden 12 verkauft.
Am Dienstag kommen 20 neue und 8 werden verkauft.
Wie viele sind am Dienstagabend da?

Denkschritte:
```

Das Modell sieht das Muster (Frage → Denkschritte → Antwort) und reproduziert es:

```
Denkschritte:
- Der Laden startet mit 50 T-Shirts
- Montag: 12 verkauft → 50 - 12 = 38
- Dienstag: 20 neue → 38 + 20 = 58
- Dienstag: 8 verkauft → 58 - 8 = 50
- Am Dienstagabend sind 50 T-Shirts da

Antwort: 50
```

Ohne CoT würde das Modell vielleicht direkt "50" antworten – oder "42" oder "70", je nachdem, wie die Wahrscheinlichkeitsverteilung gerade ausfällt. Mit CoT wird es fast immer richtig antworten, weil jeder Zwischenschritt den nächsten informiert.

## Warum funktioniert das?

Die Erklärung ist eleganter, als man denkt.

Wenn ein LLM direkt antworten muss, hat es nur die ursprüngliche Frage als Kontext. Es muss in einem einzigen "Denkschritt" (eigentlich: einem Token-Vorhersage-Durchlauf) die Antwort produzieren.

Wenn es dagegen Zwischenschritte aufschreibt, wird jeder Zwischenschritt Teil des Kontexts für den nächsten Schritt. Das Modell hat buchstäblich mehr Information zur Verfügung, wenn es die finale Antwort generiert.

Stell dir vor, du löst ein Kreuzworträtsel. Du könntest versuchen, direkt das letzte Wort einzutragen – aber die Chancen stehen schlecht. Wenn du aber die einfachen Wörter zuerst ausfüllst, geben dir die Buchstaben Hinweise für die schwierigen. Genau so funktioniert CoT für LLMs.

## CoT in der Praxis: Fünf Domänen

Genug Theorie. Lass uns CoT in verschiedenen Kontexten sehen.

### 1. Mathematische Textaufgaben

**Ohne CoT:**
```
Ein Unternehmen hat 120 Mitarbeiter. 30% arbeiten in der IT,
die Hälfte davon sind Entwickler. Von den Entwicklern arbeiten
40% remote. Wie viele IT-Entwickler arbeiten remote?
```

Typisches Ergebnis: "7" oder "8" – oft falsch, weil das Modell Schritte überspringt.

**Mit CoT:**
```
Ein Unternehmen hat 120 Mitarbeiter. 30% arbeiten in der IT,
die Hälfte davon sind Entwickler. Von den Entwicklern arbeiten
40% remote. Wie viele IT-Entwickler arbeiten remote?

Löse das Schritt für Schritt:
1. Berechne die Anzahl der IT-Mitarbeiter
2. Berechne die Anzahl der Entwickler
3. Berechne die Anzahl der Remote-Entwickler
```

Ergebnis:
```
1. IT-Mitarbeiter: 120 × 0,30 = 36
2. Davon Entwickler: 36 × 0,5 = 18
3. Davon remote: 18 × 0,40 = 7,2 → aufgerundet 8
   (oder 7, je nach Rundungskonvention)

Antwort: 7 IT-Entwickler arbeiten remote
(bei ganzen Personen abgerundet).
```

Siehst du den Unterschied? Mit CoT kann das Modell nicht nur die richtige Antwort geben, sondern auch transparent machen, wie es dahin kam. Du kannst jeden Schritt prüfen.

### 2. Logisches Schlussfolgern

**Ohne CoT:**
```
Folgende Aussagen sind wahr:
- Alle Manager haben Zugang zum Serverraum
- Einige Entwickler haben Zugang zum Serverraum
- Niemand mit Zugang zum Serverraum darf von zu Hause arbeiten
- Sarah arbeitet von zu Hause

Kann Sarah ein Manager sein?
```

Ohne CoT antwortet das Modell oft unsicher oder falsch: "Es ist möglich, dass Sarah ein Manager ist, aber..."

**Mit CoT:**
```
Folgende Aussagen sind wahr:
- Alle Manager haben Zugang zum Serverraum
- Einige Entwickler haben Zugang zum Serverraum
- Niemand mit Zugang zum Serverraum darf von zu Hause arbeiten
- Sarah arbeitet von zu Hause

Kann Sarah ein Manager sein?

Analysiere das logisch, Schritt für Schritt:
1. Was wissen wir über Manager?
2. Was wissen wir über Personen mit Serverraum-Zugang?
3. Was wissen wir über Sarah?
4. Welche Schlussfolgerung ergibt sich?
```

Ergebnis:
```
1. Alle Manager haben Zugang zum Serverraum (Aussage 1)
2. Niemand mit Serverraum-Zugang darf von zu Hause arbeiten (Aussage 3)
3. Daraus folgt: Kein Manager darf von zu Hause arbeiten
4. Sarah arbeitet von zu Hause (Aussage 4)
5. Da kein Manager von zu Hause arbeiten darf, Sarah aber von zu Hause
   arbeitet, kann Sarah KEIN Manager sein.

Antwort: Nein, Sarah kann kein Manager sein.
```

Sauber. Logisch. Überprüfbar.

### 3. Entscheidungsfindung

**Ohne CoT:**
```
Unser Startup hat 50.000 Euro Budget für Marketing.
Sollen wir in Google Ads oder Instagram investieren?
Wir verkaufen B2B-Software für kleine Unternehmen.
```

Ohne CoT bekommst du eine oberflächliche Empfehlung: "Google Ads ist besser für B2B." Punkt. Keine Analyse, keine Abwägung.

**Mit CoT:**
```
Unser Startup hat 50.000 Euro Budget für Marketing.
Sollen wir in Google Ads oder Instagram investieren?
Wir verkaufen B2B-Software für kleine Unternehmen.

Analysiere diese Entscheidung systematisch:
1. Definiere die Zielgruppe und ihr Verhalten
2. Bewerte Google Ads für diesen Kontext (Stärken, Schwächen, erwarteter ROI)
3. Bewerte Instagram für diesen Kontext (Stärken, Schwächen, erwarteter ROI)
4. Berücksichtige das Budget von 50.000 Euro
5. Gib eine begründete Empfehlung
```

Das Ergebnis ist eine strukturierte Analyse, die du tatsächlich als Entscheidungsgrundlage nutzen kannst. Das Modell berücksichtigt B2B-Suchintention, CPCs, Conversion-Raten und Budget-Effizienz.

### 4. Textanalyse

**Ohne CoT:**
```
Analysiere diesen Kundenbewertungstext: "Das Produkt an sich ist
nicht schlecht, aber der Kundenservice ist eine Katastrophe.
Drei Mal angerufen, drei Mal in der Warteschleife gestorben.
Wenn man dann mal jemanden erreicht, wird man abgewimmelt."

Ist diese Bewertung positiv, negativ oder neutral?
```

Ohne CoT: "Negativ." Das stimmt zwar, aber es fehlt die Nuance.

**Mit CoT:**
```
Analysiere diesen Kundenbewertungstext: "Das Produkt an sich ist
nicht schlecht, aber der Kundenservice ist eine Katastrophe.
Drei Mal angerufen, drei Mal in der Warteschleife gestorben.
Wenn man dann mal jemanden erreicht, wird man abgewimmelt."

Analysiere Schritt für Schritt:
1. Identifiziere alle Aspekte, die bewertet werden
2. Bewerte die Stimmung für jeden Aspekt einzeln
3. Identifiziere die verwendete Sprache und ihren Tonfall
4. Gib ein Gesamturteil mit Begründung
```

Ergebnis:
```
1. Aspekte:
   - Produkt: "nicht schlecht" → leicht positiv/neutral
   - Kundenservice: "Katastrophe" → stark negativ
   - Erreichbarkeit: "Warteschleife gestorben" → stark negativ
   - Gesprächsqualität: "abgewimmelt" → stark negativ

2. Stimmung pro Aspekt:
   - Produkt: ★★★☆☆ (neutral-positiv)
   - Kundenservice: ★☆☆☆☆ (stark negativ)

3. Sprache/Tonfall:
   - Umgangssprachlich ("Warteschleife gestorben")
   - Sarkastisch/frustriert
   - "Nicht schlecht" = zurückhaltend positiv (deutsche Untertreibung)

4. Gesamturteil: NEGATIV
   Das Produkt wird akzeptiert, aber der Kundenservice – der
   offensichtlich gebraucht wurde – ist der Hauptkritikpunkt.
   Der Kunde ist frustriert, nicht vom Produkt, sondern vom
   Service-Erlebnis.
```

Das ist eine echte Analyse. Die könntest du in einem Teammeeting präsentieren.

### 5. Code-Debugging

**Ohne CoT:**
```
Warum gibt dieser Python-Code eine falsche Summe?

numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(len(numbers)):
    total += numbers[i-1]
print(total)
```

Ohne CoT: "Der Code hat einen Off-by-One-Error." Stimmt, aber hilft nicht wirklich.

**Mit CoT:**
```
Warum gibt dieser Python-Code eine falsche Summe?

numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(len(numbers)):
    total += numbers[i-1]
print(total)

Debugge Schritt für Schritt:
1. Was macht jede Zeile?
2. Gehe die Schleife Iteration für Iteration durch
3. Was wird tatsächlich addiert?
4. Was sollte addiert werden?
5. Wo liegt der Fehler?
```

Ergebnis:
```
1. numbers = [1, 2, 3, 4, 5], total startet bei 0

2. Schleife durchgehen:
   - i=0: numbers[0-1] = numbers[-1] = 5 → total = 5
   - i=1: numbers[1-1] = numbers[0] = 1 → total = 6
   - i=2: numbers[2-1] = numbers[1] = 2 → total = 8
   - i=3: numbers[3-1] = numbers[2] = 3 → total = 11
   - i=4: numbers[4-1] = numbers[3] = 4 → total = 15

3. Addiert wird: 5, 1, 2, 3, 4 = 15 (statt 1, 2, 3, 4, 5 = 15)

4. Moment – das Ergebnis ist zufällig gleich! Aber die Reihenfolge
   ist verschoben. Der Bug zeigt sich bei unterschiedlichen Werten.

   Beispiel: numbers = [1, 2, 3, 4, 10]
   - Erwartet: 1+2+3+4+10 = 20
   - Tatsächlich: numbers[-1]=10, [0]=1, [1]=2, [2]=3, [3]=4 → 20

   Auch hier zufällig gleich! Das liegt daran, dass alle Elemente
   addiert werden, nur in anderer Reihenfolge. Die Summe bleibt gleich.

5. PLOT TWIST: Der Code gibt tatsächlich die richtige Summe!
   Der "Bug" existiert nicht – die Summe ist kommutativ. Allerdings
   greift der Code auf das falsche Element zu (numbers[i-1] statt
   numbers[i]), was bei anderen Operationen als Addition zu echten
   Fehlern führen würde. Der Fix für korrektes Indexing:
   numbers[i] statt numbers[i-1].
```

Siehst du, was da passiert ist? Durch das schrittweise Durchgehen hat das Modell erkannt, dass die Frage eine Falle enthält. Ohne CoT hätte es blind behauptet, es gäbe einen Summierungsfehler.

## Die vier CoT-Varianten

Nicht jedes CoT sieht gleich aus. Es gibt vier Hauptvarianten, die du kennen solltest:

### Variante 1: Explizite Schritte vorgeben

Du sagst dem Modell genau, welche Schritte es durchlaufen soll.

```
Analysiere diesen Geschäftsplan:
Schritt 1: Identifiziere das Geschäftsmodell
Schritt 2: Bewerte den Zielmarkt
Schritt 3: Analysiere die Wettbewerbssituation
Schritt 4: Prüfe die finanzielle Machbarkeit
Schritt 5: Gib eine Gesamtbewertung mit Note (1-10)
```

**Wann nutzen:** Wenn du genau weißt, welche Analyse-Schritte sinnvoll sind. Gibt dir maximale Kontrolle.

### Variante 2: Offene Schritte

Du sagst dem Modell, dass es Schritt für Schritt denken soll, ohne die Schritte vorzugeben.

```
Analysiere diesen Geschäftsplan. Denke Schritt für Schritt
und zeige deinen Denkprozess.
```

**Wann nutzen:** Wenn du nicht sicher bist, welche Schritte die richtigen sind. Das Modell wählt selbst – manchmal überraschend gut.

### Variante 3: Few-Shot CoT

Du gibst ein komplettes Beispiel mit Denkschritten, bevor du deine Frage stellst.

```
Beispiel:
Frage: Soll ein Restaurant um 11 Uhr oder um 18 Uhr öffnen,
wenn die Zielgruppe Büroangestellte sind?
Denkprozess: Büroangestellte arbeiten typischerweise 9-17 Uhr.
Um 11 Uhr sind sie bei der Arbeit → Mittagspause ab 12 Uhr
ist realistisch. Um 18 Uhr sind sie gerade fertig → Abendessen
ab 18:30 ist realistisch. Für Mittagsgeschäft: 11 Uhr.
Für Abendgeschäft: 18 Uhr. Für maximalen Umsatz: 11 Uhr,
da die Konkurrenz abends höher ist.
Antwort: 11 Uhr für Mittagsgeschäft (empfohlen), 18 Uhr für
Abendgeschäft.

Meine Frage: Soll ein Co-Working-Space Monats- oder
Tagestickets anbieten, wenn die Zielgruppe Freelancer sind?
Denkprozess:
```

**Wann nutzen:** Wenn du einen bestimmten Denkstil demonstrieren willst. Das Modell imitiert die Struktur deines Beispiels.

### Variante 4: CoT mit Zusammenfassung

Das Modell denkt ausführlich, fasst aber am Ende zusammen.

```
Bewerte diese drei Investitionsoptionen für einen
konservativen Anleger mit 100.000 Euro:
A) ETF-Portfolio
B) Immobilie
C) Staatsanleihen

Denke ausführlich über jede Option nach.
Am Ende: Gib eine klare Empfehlung in 2-3 Sätzen.
```

**Wann nutzen:** Wenn du den Denkprozess sehen willst, aber auch eine klare Zusammenfassung brauchst. Ideal für Berichte und Präsentationen.

## CoT-Qualität optimieren

Nicht jedes CoT liefert automatisch gute Ergebnisse. Hier sind die wichtigsten Optimierungen:

### Optimierung 1: Granularität anpassen

**Zu grob:**
```
Denke nach und antworte.
```
→ Das Modell macht vielleicht 2-3 oberflächliche Schritte.

**Zu fein:**
```
Schritt 1: Lies die Frage.
Schritt 2: Identifiziere die relevanten Zahlen.
Schritt 3: Prüfe, ob du alle Informationen hast.
Schritt 4: Wähle die passende Rechenoperation.
Schritt 5: Führe die Berechnung aus.
Schritt 6: Prüfe das Ergebnis.
Schritt 7: Formuliere die Antwort.
Schritt 8: Überprüfe, ob die Antwort die Frage beantwortet.
```
→ Aufgebläht, das Modell produziert Fülltext.

**Genau richtig:**
```
Analysiere Schritt für Schritt:
1. Was sind die gegebenen Informationen?
2. Was wird gesucht?
3. Löse das Problem
4. Prüfe dein Ergebnis
```
→ Genug Struktur, um den Denkprozess zu leiten, aber nicht so viel, dass es einengend wird.

### Optimierung 2: Domänen-spezifische Schritte

Passe die Schritte an die Domäne an:

**Für juristische Analyse:**
```
1. Identifiziere den Sachverhalt
2. Bestimme die einschlägigen Rechtsnormen
3. Prüfe den Tatbestand (Subsumtion)
4. Beurteile die Rechtsfolge
```

**Für medizinische Fragen:**
```
1. Symptome zusammenfassen
2. Mögliche Differenzialdiagnosen auflisten
3. Wahrscheinlichkeiten bewerten
4. Empfohlene nächste Schritte
```

**Für technische Problemlösung:**
```
1. Problem reproduzieren und verstehen
2. Mögliche Ursachen identifizieren
3. Wahrscheinlichste Ursache bestimmen
4. Lösung vorschlagen und begründen
```

### Optimierung 3: Denkprozess vom Ergebnis trennen

```
Aufgabe: [Deine Aufgabe]

Zeige deinen Denkprozess in einem Block "ANALYSE:"
und gib dann dein Ergebnis in einem Block "ERGEBNIS:".
```

Das macht die Antwort lesbarer und du kannst den Denkprozess überspringen, wenn du nur das Ergebnis brauchst.

## Wann CoT NICHT funktioniert

CoT ist kein Allheilmittel. Es gibt Situationen, in denen es nicht hilft oder sogar schadet:

### Problem 1: Zu einfache Aufgaben
Bei trivialen Fragen produziert CoT unnötigen Overhead:
```
Frage: Was ist die Hauptstadt von Deutschland?

Denkprozess: Deutschland ist ein Land in Europa.
Die Hauptstadt eines Landes ist die Stadt, in der die
Regierung sitzt. Die deutsche Regierung sitzt in Berlin.
Also ist Berlin die Hauptstadt von Deutschland.

Antwort: Berlin.
```
Vier Sätze für etwas, das ein Wort braucht. Verschwendung.

### Problem 2: Kreative Aufgaben
Bei Brainstorming oder kreativem Schreiben kann CoT den Kreativitätsfluss bremsen:
```
Schreib mir ein Gedicht über Liebe.
Denke Schritt für Schritt:
1. Welche Metaphern passen?
2. Welches Reimschema?
3. Welche Emotionen?
```
→ Das Ergebnis wird analytisch statt emotional. Für kreative Aufgaben lass das Modell frei laufen.

### Problem 3: Falsches Reasoning
Manchmal denkt das Modell sorgfältig und kommt trotzdem zum falschen Ergebnis. CoT zeigt dir dann wenigstens, *wo* es falsch abgebogen ist – aber es verhindert Fehler nicht komplett.

### Problem 4: Halluzinierte Schritte
Das Modell kann "Denkschritte" erfinden, die plausibel klingen, aber falsch sind. Besonders bei Wissensaufgaben:
```
Denkprozess: Der Vertrag von Lissabon wurde 2007
unterzeichnet und trat 2009 in Kraft. Er legte fest,
dass die EU maximal 30 Mitgliedsstaaten haben darf...
```
Der letzte Satz ist erfunden. CoT kann Halluzinationen in Denkschritten verstecken.

## CoT Best Practices – Zusammenfassung

| Tipp | Details |
|---|---|
| Nutze CoT bei komplexen Aufgaben | Mathe, Logik, Analyse, Planung |
| Überspring CoT bei einfachen Aufgaben | Übersetzung, Formatierung, Faktenabruf |
| Passe Granularität an | 3-5 Schritte sind meistens ideal |
| Nutze domänenspezifische Schritte | Juristisch, medizinisch, technisch |
| Trenne Denkprozess und Ergebnis | ANALYSE: und ERGEBNIS: Blöcke |
| Prüfe die Zwischenschritte | CoT macht Fehler sichtbar – nutze das |
| Kombiniere CoT mit Rollen | "Du bist ein Experte für X. Denke Schritt für Schritt..." |

---

## Übungen

### Übung 1: CoT-Varianten vergleichen
Nimm diese Aufgabe und löse sie mit allen vier CoT-Varianten (explizite Schritte, offene Schritte, Few-Shot CoT, CoT mit Zusammenfassung):

"Ein Startup hat 200.000 Euro Jahresbudget. Die Fixkosten betragen 8.000 Euro/Monat. Sie möchten 3 Entwickler einstellen (je 5.000 Euro/Monat). Reicht das Budget? Wenn nein, welche Optionen gibt es?"

Vergleiche die Ergebnisse. Welche Variante liefert die nützlichste Antwort?

### Übung 2: Domain-CoT entwickeln
Wähle ein Thema, das dich interessiert (z.B. Kochen, Sport, Finanzen). Entwickle eine domänenspezifische CoT-Schrittfolge (3-5 Schritte), die für typische Fragen in diesem Bereich funktioniert. Teste sie mit 3 verschiedenen Fragen.

### Übung 3: CoT-Grenzen testen
Teste CoT bewusst in Situationen, wo es nicht helfen sollte:
- Eine kreative Schreibaufgabe
- Eine einfache Wissensfrage
- Eine Aufgabe, bei der das Modell die Fakten nicht kennen kann

Dokumentiere: Hat CoT geholfen, geschadet oder keinen Unterschied gemacht?

### Übung 4: Fehler im Denkprozess finden
Gib dem Modell diese Aufgabe mit CoT und prüfe jeden Zwischenschritt:

"In einem Raum sind 3 Lichtschalter. Jeder gehört zu einer von 3 Lampen im Nebenraum. Du darfst den Raum mit den Lampen nur einmal betreten. Wie findest du heraus, welcher Schalter zu welcher Lampe gehört?"

Hat das Modell die richtige Lösung gefunden? Wo war der Denkprozess gut, wo fehlerhaft?
