# Kapitel 7: Ethische KI-Nutzung – Mehr als nur Compliance

Gesetze sagen dir, was du nicht darfst. Ethik sagt dir, was du nicht solltest – auch wenn du es dürftest. Der EU AI Act und die DSGVO setzen einen Mindeststandard. Aber Mindeststandards reichen nicht, wenn du KI verantwortungsvoll einsetzen willst.

Dieses Kapitel geht über die Regulierung hinaus. Es geht um die Fragen, die kein Gesetz beantwortet: Wann sollte ich KI einsetzen – und wann bewusst nicht? Wem gehört der Output? Wie transparent muss ich sein? Und was schulde ich den Menschen, die von meinen KI-Entscheidungen betroffen sind?

## Die großen ethischen Fragen

### 1. Transparenz: Muss ich sagen, dass KI beteiligt war?

Rechtlich: In manchen Fällen ja (EU AI Act, siehe Kapitel 6). Aber ethisch? Hier wird es komplizierter.

**Szenario 1:** Du schreibst eine E-Mail mit KI-Unterstützung. Musst du das sagen? Nein – genauso wenig wie du sagst, dass du Rechtschreibprüfung benutzt hast. Die E-Mail ist deine, du hast sie geprüft und abgeschickt.

**Szenario 2:** Du schreibst einen Fachartikel komplett mit KI und veröffentlichst ihn unter deinem Namen. Musst du das sagen? Ethisch: Ja. Dein Name impliziert, dass du der Autor bist. Wenn die intellektuelle Leistung größtenteils von einer KI stammt, ist das irreführend.

**Szenario 3:** Dein Unternehmen nutzt KI für Kreditentscheidungen. Müssen die Kunden das wissen? Absolut. Menschen haben ein Recht zu wissen, wenn eine Maschine über sie entscheidet.

**Meine Faustregel:** Je höher der Einsatz für andere Menschen, desto höher die Transparenzpflicht. Eine KI-gestützte E-Mail ist unproblematisch. Eine KI-gestützte Kündigung ist es nicht.

### 2. Verantwortung: Wer haftet für KI-Fehler?

Wenn dein KI-Chatbot einem Kunden falsche Informationen gibt – wer ist verantwortlich? Nicht die KI. Nicht der Hersteller (in den meisten Fällen). **Du** bist verantwortlich. Der Betreiber des Systems. Der Mensch, der entschieden hat, KI für diese Aufgabe einzusetzen.

Das Air-Canada-Urteil (2024) hat das klar gemacht: Ein Airline-Chatbot gab falsche Informationen über Erstattungsrichtlinien. Die Airline versuchte zu argumentieren, der Chatbot sei eine separate Entität. Das Gericht sagte: Nein. Der Chatbot ist euer Werkzeug. Ihr seid verantwortlich.

**Die Konsequenz:** Setze KI nur für Aufgaben ein, deren Ergebnisse du überprüfen und verantworten kannst. Wenn du die Antwort nicht beurteilen kannst, solltest du sie nicht automatisiert geben.

### 3. Autonomie: Darf KI Entscheidungen treffen?

Art. 22 DSGVO gibt EU-Bürgern das Recht, nicht einer ausschließlich auf automatisierter Verarbeitung beruhenden Entscheidung unterworfen zu werden, die ihnen gegenüber rechtliche Wirkung entfaltet.

Übersetzt: Wenn eine KI über Menschen entscheidet (Kredit, Job, Versicherung), muss ein Mensch die finale Entscheidung treffen. Die KI darf empfehlen, aber nicht entscheiden.

Das klingt einfach. In der Praxis ist es schwieriger: Wenn ein Mensch die KI-Empfehlung in 99% der Fälle einfach durchwinkt – ist das wirklich menschliche Aufsicht? Oder ist es Alibi-Kontrolle? Echte menschliche Aufsicht bedeutet, dass der Mensch die Empfehlung versteht, hinterfragen kann und regelmäßig überschreibt.

### 4. Fairness: Gleiche Behandlung für alle?

Kapitel 4 hat gezeigt, dass KI diskriminieren kann. Die ethische Forderung geht über Bias-Detection hinaus: Selbst wenn dein System technisch unbiased ist – ist die Anwendung fair?

Ein Beispiel: Du nutzt KI, um Bewerbungen vorzufiltern. Das System hat keinen messbaren Bias. Aber: Es filtert alle Bewerbungen ohne Hochschulabschluss aus – in einer Position, in der ein Hochschulabschluss gar nicht nötig ist. Technisch kein Bias. Aber fair?

### 5. Originalität und geistiges Eigentum

Wem gehört der Output eines LLMs? Wenn du Claude einen Artikel schreiben lässt – bist du der Autor? Kann der Text urheberrechtlich geschützt werden?

Die rechtliche Lage (Stand 2026): In den meisten Jurisdiktionen ist rein KI-generierter Content **nicht urheberrechtlich schützbar**, weil kein menschlicher Schöpfer beteiligt war. Wenn du den Text substanziell bearbeitest, kann dein Beitrag geschützt sein. Die Grenzen sind noch nicht klar ausjudiziert.

Die ethische Frage: Wenn du einen KI-generierten Text verkaufst – sollte der Käufer das wissen? Wenn du KI-generierte Kunst als Auftragsarbeit ablieferst – ist das Betrug?

Meine Meinung: Transparenz ist der Schlüssel. Wer KI als Werkzeug nutzt (wie einen Taschenrechner oder eine Suchmaschine), muss das nicht bei jeder Nutzung offenlegen. Wer KI als Ghostwriter nutzt und die kreative Leistung als eigene verkauft, sollte das kommunizieren.

## Ethische Frameworks

### Die UNESCO-Empfehlung (2021)

Die UNESCO hat als erste internationale Organisation Ethik-Richtlinien für KI verabschiedet, unterzeichnet von 193 Mitgliedstaaten. Die Kernprinzipien:

1. **Menschenrechte und Menschenwürde achten**
2. **Friedlich, gerecht und vernetzt leben**
3. **Diversität und Inklusion sicherstellen**
4. **Umwelt und Ökosystem schützen**
5. **Proportionalität und Schadensvermeidung**
6. **Sicherheit**
7. **Fairness und Nichtdiskriminierung**
8. **Nachhaltigkeit**
9. **Privatsphäre**
10. **Transparenz und Erklärbarkeit**
11. **Menschliche Aufsicht und Kontrolle**

### Anthropics Constitutional AI

Anthropic (die Macher von Claude) verfolgen einen Ansatz namens "Constitutional AI": Statt das Modell nur durch menschliches Feedback zu trainieren, geben sie ihm eine "Verfassung" – eine Sammlung von Prinzipien, an die es sich halten soll. Das Modell wird dann trainiert, seine eigenen Antworten gegen diese Prinzipien zu prüfen.

**Im Januar 2026 wurde die Verfassung grundlegend überarbeitet:** Der Wechsel ging von regelbasierter zu **begründungsbasierter Ausrichtung** – das Modell lernt nicht mehr nur "Tu X nicht", sondern *warum* ethische Prinzipien existieren. Die neue Verfassung etabliert eine 4-stufige Prioritätshierarchie: (1) Sicherheit, (2) Ethik, (3) Compliance, (4) Hilfreichkeit.

Bemerkenswert: Anthropic ist das erste große KI-Unternehmen, das in einem offiziellen Dokument die Möglichkeit von KI-Bewusstsein und moralischem Status anerkennt.

Die ursprünglichen Prinzipien basieren auf der UN-Menschenrechtserklärung, Apples Terms of Service und nicht-westlichen kulturellen Werten.

### Dein eigenes ethisches Framework

Für dein Unternehmen oder Team empfehle ich ein einfaches Framework mit fünf Fragen, die du vor jedem KI-Einsatz stellen solltest:

1. **Würde ich es jedem erzählen?** (Transparenztest)
2. **Was ist das Schlimmste, das passieren kann?** (Schadenstest)
3. **Behandle ich alle gleich?** (Fairnesstest)
4. **Würde ich das auch ohne KI so entscheiden?** (Autonomietest)
5. **Kann ich es verantworten?** (Verantwortungstest)

Wenn du bei einer dieser Fragen zögerst – überdenke den Einsatz.

## Die Umweltfrage

Ein Thema, das oft vergessen wird: KI hat einen CO₂-Fußabdruck. Das Training großer Modelle verbraucht enorme Mengen Energie. Auch die Inferenz (jeder API-Call) verbraucht Strom.

Schätzungen: Ein einzelner ChatGPT-Request verbraucht etwa 10x so viel Energie wie eine Google-Suche. Bei Milliarden Anfragen pro Tag summiert sich das.

Was du tun kannst:
- **Das kleinste ausreichende Modell nutzen.** Haiku statt Opus, wenn Haiku reicht.
- **Ergebnisse cachen.** Dieselbe Frage nicht wiederholt stellen.
- **Batches statt Einzelanfragen.** Effizienter für das Rechenzentrum.
- **Nicht für triviale Aufgaben nutzen.** "Hey KI, was ist 2+2?" ist Energieverschwendung.

---

## Übungen

### Übung 1: Transparenz-Check
Nimm 5 KI-Anwendungsfälle in deinem Alltag. Bei welchen solltest du transparent sein? Bei welchen nicht? Begründe.

### Übung 2: Der 5-Fragen-Test
Nimm deinen wichtigsten KI-Einsatz und beantworte die 5 ethischen Fragen ehrlich. Wo zögerst du?

### Übung 3: Ethik-Richtlinie
Erstelle eine einfache Ethik-Richtlinie (1 Seite) für KI-Nutzung in deinem Team. Was ist erlaubt, was nicht, warum?

### Übung 4: Grenzfälle diskutieren
Diskutiere mit Kollegen: Ist es ethisch vertretbar, einen KI-generierten Blogartikel ohne Kennzeichnung zu veröffentlichen? Gibt es eine Grenze?
