# Kapitel 6: Kontext-Fenster meistern – Wenn das Modell vergisst

Stell dir vor, du führst ein Gespräch mit jemandem, der sich nur an die letzten 20 Minuten erinnern kann. Alles davor? Weg. Nicht verdrängt, nicht gespeichert – einfach weg.

So funktionieren LLMs. Sie haben ein Kontext-Fenster. Alles, was hineinpasst, können sie "sehen". Alles darüber hinaus existiert für sie nicht mehr.

Und wenn du dieses Fenster nicht managst, wirst du irgendwann merken: Das Modell vergisst deine Anweisungen vom Anfang der Konversation. Es wiederholt sich. Es widerspricht sich selbst. Nicht weil es schlecht ist – sondern weil der Anfang des Gesprächs buchstäblich nicht mehr in seinem Kontext liegt.

## Was ist das Kontext-Fenster?

Das Kontext-Fenster ist die maximale Menge an Text (gemessen in Tokens), die ein Modell gleichzeitig verarbeiten kann. Es umfasst alles: den System-Prompt, deine Nachrichten, die Antworten des Modells und alles, was sonst noch Teil der Konversation ist.

### Aktuelle Kontextgrößen (Stand: 2026)

| Modell | Kontext-Fenster | Ungefähr in Wörtern |
|--------|----------------|---------------------|
| GPT-4o | 128.000 Tokens | ~96.000 Wörter |
| Claude 3.5 Sonnet | 200.000 Tokens | ~150.000 Wörter |
| Gemini 2.0 | 1.000.000 Tokens | ~750.000 Wörter |
| Llama 3.3 | 128.000 Tokens | ~96.000 Wörter |

Das klingt nach viel. 96.000 Wörter – das ist ein ganzes Buch. Warum sollte das ein Problem sein?

### Warum es trotzdem ein Problem ist

1. **Die Konversation wächst schnell.** Jede Nachricht von dir UND jede Antwort des Modells zählt. Ein längeres Gespräch mit ausführlichen Antworten kann schnell 50.000+ Tokens erreichen.

2. **Nicht alles im Fenster bekommt gleich viel Aufmerksamkeit.** Studien zeigen: LLMs sind am besten darin, Informationen am Anfang und am Ende des Kontexts zu verarbeiten. Alles in der Mitte kann untergehen. Das nennt man den "Lost in the Middle"-Effekt.

3. **System-Prompts fressen Platz.** Ein ausführlicher System-Prompt mit 500 Tokens reduziert dein verfügbares Fenster.

## Strategien für effizientes Kontext-Management

### Strategie 1: Neue Konversation für neue Aufgaben

Die einfachste und effektivste Strategie. Wenn du eine neue Aufgabe anfängst, starte eine neue Konversation. Nimm nicht den Chat von gestern Morgen, in dem du eine E-Mail geschrieben hast, um jetzt Code zu debuggen.

Warum? Weil der alte Kontext (E-Mail, deine Angaben, die Antwort) immer noch im Fenster liegt und Platz wegnimmt. Und weil das Modell sich möglicherweise vom alten Kontext beeinflussen lässt.

### Strategie 2: Zusammenfassen statt Weiterscrollen

Wenn eine Konversation lang wird und du den Kontext behalten willst:

```
Fasse unsere bisherige Konversation in 5 Bullet Points zusammen.
Nenne: die Aufgabe, die wichtigsten Entscheidungen, offene Punkte.
```

Kopiere die Zusammenfassung, starte eine neue Konversation, füge sie ein:

```
Hier ist der Kontext unserer bisherigen Arbeit:
"""
[Zusammenfassung einfügen]
"""

Wir machen jetzt weiter mit: [nächster Schritt]
```

Du verlierst Details, behältst aber das Wesentliche. Und du hast ein frisches Kontext-Fenster.

### Strategie 3: Relevante Informationen wiederholen

Wenn du merkst, dass das Modell eine Anweisung vom Anfang vergessen hat, wiederhole sie:

```
Zur Erinnerung: Wir schreiben in der Du-Form und vermeiden
Fachbegriffe. Bitte überarbeite den letzten Absatz entsprechend.
```

Das ist kein Zeichen, dass du etwas falsch machst. Es ist die Realität von endlichen Kontext-Fenstern.

### Strategie 4: Kontext komprimieren

Statt riesige Texte komplett einzufügen, fasse sie vorher zusammen:

```
# Statt 5.000 Wörter Jahresbericht einzufügen:
Hier sind die Kerndaten aus unserem Jahresbericht 2025:
- Umsatz: 12,3 Mio EUR (+15% ggü. Vorjahr)
- Mitarbeiter: 89 (Vorjahr: 72)
- Hauptwachstum: SaaS-Segment (+28%)
- Herausforderungen: Fachkräftemangel, steigende Cloudkosten
- Ausblick: Expansion nach Österreich und Schweiz geplant

Basierend auf diesen Daten: [deine Aufgabe]
```

500 Tokens statt 7.000. Das Modell hat trotzdem alle relevanten Informationen.

### Strategie 5: Chaining statt Mega-Konversationen

Das kennst du schon aus Kapitel 1. Statt alles in einer langen Konversation zu machen, zerlege die Aufgabe in Ketten. Jeder Schritt in einer eigenen Konversation (oder zumindest mit klarer Trennung).

## Der "Lost in the Middle"-Effekt

Dieses Phänomen ist so wichtig, dass es einen eigenen Abschnitt verdient.

Forscher haben 2023 nachgewiesen: Wenn du einem LLM einen langen Text gibst, kann es Informationen am Anfang und am Ende zuverlässig finden. Informationen in der Mitte werden oft übersehen.

Was bedeutet das für dich?

### Wichtigstes nach vorne oder hinten

Wenn du einen langen Prompt schreibst, packe die wichtigsten Anweisungen an den Anfang oder ans Ende. Nicht in die Mitte.

```
# Gute Struktur
[Wichtigste Anweisung]
[Kontext und Details]
[Zusammenfassung der wichtigsten Anweisung]
```

### Bei langen Texten: Fragen vorher stellen

```
# Schlecht
[5.000 Wörter Text]
Beantworte folgende Fragen zu diesem Text: ...

# Besser
Beantworte folgende Fragen zum nachfolgenden Text:
1. Was ist die Hauptaussage?
2. Welche Gegenargumente werden genannt?
3. Welche Daten werden zitiert?

---
[5.000 Wörter Text]
```

Wenn das Modell die Fragen VOR dem Text sieht, weiß es, worauf es achten muss, während es den Text verarbeitet.

## Wie erkenne ich, dass das Kontext-Fenster voll wird?

Die meisten Plattformen zeigen dir das nicht direkt an. Aber diese Anzeichen sprechen dafür:

1. **Das Modell wiederholt sich** – Es gibt Antworten, die es schon vorher gegeben hat
2. **Es ignoriert Anweisungen** – Besonders solche vom Anfang der Konversation
3. **Es widerspricht sich** – Position A am Anfang, Position B am Ende
4. **Die Qualität sinkt** – Antworten werden generischer und weniger spezifisch
5. **Fehlermeldung** – Manche Plattformen zeigen eine explizite Warnung

Wenn eines dieser Anzeichen auftritt: Neue Konversation. Mit Zusammenfassung.

## Praxisbeispiel: Ein langes Recherche-Projekt

Du recherchierst für eine Präsentation über erneuerbare Energien.

**Schlechter Ansatz:** Eine einzige Konversation mit 30 Nachrichten.

```
Nachricht 1: "Erkläre Solarenergie"
Nachricht 5: "Wie funktioniert Windkraft?"
Nachricht 10: "Vergleiche die Kosten"
Nachricht 15: "Was sagt die Politik?"
Nachricht 20: "Erstelle mir eine Zusammenfassung"
Nachricht 25: "Mach daraus Präsentationsfolien"
```

Bis Nachricht 25 hat das Modell die Details aus Nachricht 1-5 möglicherweise vergessen.

**Besserer Ansatz:** Mehrere kurze Konversationen mit Übergaben.

```
Konversation 1: Solarenergie → Zusammenfassung speichern
Konversation 2: Windkraft → Zusammenfassung speichern
Konversation 3: Kostenvergleich → Zusammenfassung speichern
Konversation 4: Alle 3 Zusammenfassungen + "Erstelle Präsentationsfolien"
```

Jede Konversation hat ein frisches Fenster und vollen Fokus.

## Token-Budgetierung

Wenn du über die API arbeitest und Token kosten, hilft es, bewusst zu budgetieren:

```
Gesamtbudget: 128.000 Tokens
- System-Prompt: 500 Tokens
- Verfügbar für Konversation: 127.500 Tokens
- Davon Input (du): ~40%  → 51.000 Tokens
- Davon Output (Modell): ~60% → 76.500 Tokens
```

In der Praxis wirst du selten an diese Grenzen kommen. Aber für Anwendungen, die automatisiert laufen (z.B. ein Chatbot auf deiner Website), ist Token-Budgetierung wichtig, weil sie direkt die Kosten beeinflusst.

---

## Übung

**Kontext-Fenster-Experiment**

1. Starte eine neue Konversation mit deinem LLM
2. Gib am Anfang eine klare Anweisung: "Antworte in jeder Nachricht mit genau 3 Sätzen. Nicht mehr, nicht weniger."
3. Stelle 15-20 verschiedene Fragen zu verschiedenen Themen
4. Beobachte: Ab welcher Nachricht fängt das Modell an, die 3-Sätze-Regel zu brechen?
5. Wiederhole die Anweisung und beobachte, ob es sofort wieder funktioniert

Das zeigt dir in der Praxis, wie Kontext-Erosion funktioniert – und wie du dagegen steuerst.
