# Kapitel 2: LLMs verstehen – Wie Sprachmodelle funktionieren

OK, jetzt wird's ein bisschen technischer. Aber keine Sorge – ich erkläre das so, dass du es auch ohne Informatik-Studium verstehst. Versprochen.

## Was sind Large Language Models?

LLM steht für "Large Language Model" – großes Sprachmodell. Der Name sagt eigentlich schon alles:

- **Large:** Diese Modelle sind riesig. Sie haben Milliarden von Parametern. GPT-4 hat geschätzte 1,8 Billionen Parameter. Claude und Gemini spielen in ähnlichen Größenordnungen. Das sind Zahlen, die sich kein Mensch mehr vorstellen kann.
- **Language:** Sie arbeiten mit Sprache. Text rein, Text raus. Manche können inzwischen auch Bilder und Audio verarbeiten, aber im Kern sind es Sprachmodelle.
- **Model:** Es sind mathematische Modelle. Keine Programme im klassischen Sinn, die Regeln abarbeiten. Sondern statistische Modelle, die Muster gelernt haben.

## Wie "denkt" ein LLM?

Kurzantwort: Gar nicht. Jedenfalls nicht so, wie du und ich denken.

Wenn du ChatGPT fragst "Was ist die Hauptstadt von Frankreich?", dann passiert Folgendes: Das Modell schaut sich deine Frage an und berechnet, welches Wort am wahrscheinlichsten als nächstes kommt. Und dann das nächste. Und das nächste. Wort für Wort.

Es denkt nicht: "Hmm, Frankreich... Paris ist die Hauptstadt." Es "denkt": "Nach 'Die Hauptstadt von Frankreich ist' kommt mit 98,7% Wahrscheinlichkeit das Wort 'Paris'."

Ich weiß, das klingt ernüchternd. Wie kann etwas, das nur Wörter aneinanderreiht, so kluge Antworten geben? Der Trick liegt im Training. Diese Modelle haben so unglaublich viel Text gesehen, dass ihre Vorhersagen erstaunlich gut sind. Manchmal täuschend gut. Manchmal so gut, dass man vergisst, dass da keine Intelligenz dahintersteckt.

Aber genau deshalb passieren auch Fehler. Sogenannte **Halluzinationen** – wenn das Modell dir mit fester Überzeugung etwas Falsches erzählt. Dazu kommen wir in Kapitel 5 noch genauer.

## Training: Woher kommt das Wissen?

LLMs werden mit gigantischen Textmengen trainiert. Bücher, Webseiten, Wikipedia, Code-Repositories, wissenschaftliche Paper, Foren, Nachrichtenartikel – alles, was in Textform existiert und zugänglich ist.

Das Training läuft grob in zwei Phasen:

**Phase 1: Pre-Training**
Das Modell liest (vereinfacht gesagt) das halbe Internet und lernt, wie Sprache funktioniert. Welche Wörter zusammengehören. Wie Sätze aufgebaut sind. Welche Antwort auf welche Frage typischerweise folgt. Das ist der teure Teil – Pre-Training kostet Hunderte Millionen Euro an Rechenleistung.

**Phase 2: Fine-Tuning und RLHF**
Das rohe Modell nach dem Pre-Training ist wie ein Lexikon mit Persönlichkeitsstörung. Es weiß viel, aber es antwortet wirr und manchmal gefährlich. Deshalb wird es nachtrainiert:
- **Fine-Tuning:** Menschliche Trainer zeigen dem Modell, wie gute Antworten aussehen
- **RLHF (Reinforcement Learning from Human Feedback):** Menschen bewerten Antworten als gut oder schlecht, und das Modell lernt, bessere Antworten zu geben

Das Ergebnis ist das, was du als ChatGPT, Claude oder Gemini kennst – ein Modell, das höflich, hilfreich und halbwegs sicher antwortet.

## Die wichtigsten Begriffe – einfach erklärt

Wenn du über LLMs liest, stolperst du ständig über ein paar Fachbegriffe. Hier sind die wichtigsten:

### Token

LLMs denken nicht in Wörtern, sondern in Token. Ein Token ist ein Stückchen Text – manchmal ein ganzes Wort, manchmal nur ein Teil davon.

Beispiel: Das Wort "Prompt" ist meistens ein Token. Das Wort "Prompt Engineering" sind zwei Token. Das Wort "Unwahrscheinlichkeit" wird in mehrere Token zerlegt.

Warum ist das wichtig? Weil LLMs ein Limit haben, wie viele Token sie auf einmal verarbeiten können. Das bringt uns zum nächsten Begriff.

### Context Window

Das Context Window (Kontextfenster) ist die maximale Menge an Text, die ein LLM gleichzeitig "sehen" kann. Das umfasst sowohl deinen Prompt als auch die Antwort des Modells.

- GPT-4: bis zu 128.000 Token (~100 Buchseiten)
- Claude 3.5/4: bis zu 200.000 Token (~150 Buchseiten)
- Gemini 1.5/2: bis zu 1.000.000 Token (~750 Buchseiten)

Das klingt nach viel, und meistens reicht es auch. Aber bei sehr langen Dokumenten oder komplexen Gesprächen kann es eng werden. Dann "vergisst" das Modell ältere Teile des Gesprächs.

### Parameter

Parameter sind die "Stellschrauben" des Modells. Je mehr Parameter, desto mehr Muster kann das Modell lernen. Mehr Parameter bedeutet tendenziell bessere Ergebnisse – aber auch höhere Kosten und langsamere Antworten.

Du musst die genaue Zahl nicht kennen. Merk dir einfach: Größere Modelle sind meistens besser, kosten aber mehr.

### Temperatur

Die Temperatur steuert, wie "kreativ" das Modell antwortet.

- **Temperatur 0:** Sehr vorhersagbar. Das Modell wählt immer das wahrscheinlichste Wort. Gut für Fakten, Zusammenfassungen, Code.
- **Temperatur 1:** Kreativer, aber auch unvorhersagbarer. Gut für Brainstorming, Geschichten, kreatives Schreiben.
- **Temperatur > 1:** Zunehmend chaotisch. Kann lustig sein, produziert aber oft Unsinn.

In den meisten Chat-Interfaces (ChatGPT, Claude) kannst du die Temperatur nicht direkt einstellen – das machen nur Entwickler über die API. Aber es hilft zu verstehen, warum du manchmal verschiedene Antworten auf die gleiche Frage bekommst.

## Die wichtigsten LLMs – eine Übersicht

Stand März 2026 gibt es eine Handvoll Modelle, die du kennen solltest:

### ChatGPT / GPT-4o / GPT-5 (OpenAI)
Der Platzhirsch. Das bekannteste LLM. Gut für allgemeine Aufgaben, Konversation, Code. Kostenlose Version verfügbar, Pro-Version mit erweiterten Funktionen.

### Claude (Anthropic)
Mein persönlicher Favorit für längere Texte und komplexe Aufgaben. Claude hat ein besonders großes Kontextfenster und ist gut darin, Nuancen zu verstehen. Aktuell in Version 4.

### Gemini (Google)
Googles Antwort auf ChatGPT. Stark bei Recherche und Fakten, weil es Zugriff auf Google-Suche hat. Riesiges Kontextfenster von bis zu einer Million Token.

### LLaMA / Meta AI (Meta)
Open-Source-Modell von Meta. Kann kostenlos heruntergeladen und auf eigenem Rechner betrieben werden. Besonders interessant für Entwickler und Datenschutz-Bewusste.

### DeepSeek (DeepSeek)
Ein chinesisches Open-Source-Modell, das 2025 für Aufsehen gesorgt hat, weil es trotz geringerer Trainingskosten mit den Top-Modellen mithalten konnte. Zeigt, dass mehr Geld nicht automatisch bessere Modelle bedeutet.

### Mistral (Mistral AI)
Europäisches Open-Source-Modell aus Frankreich. Kompakt, schnell und überraschend leistungsfähig. Zeigt, dass auch kleinere Modelle ihren Platz haben.

## Welches Modell ist das beste?

Keins. Oder alle. Es kommt drauf an.

Ich weiß, das ist eine unbefriedigende Antwort. Aber es ist die ehrliche. Jedes Modell hat Stärken und Schwächen. ChatGPT ist gut für schnelle Konversation. Claude ist stark bei langen, komplexen Texten. Gemini kann live im Internet suchen.

Mein Tipp: Leg dir kostenlose Accounts bei mindestens zwei verschiedenen Anbietern an. Teste denselben Prompt in verschiedenen Modellen. Du wirst schnell merken, was dir liegt.

## Das Wichtigste aus diesem Kapitel

- LLMs sind statistische Modelle, die Wort für Wort vorhersagen
- Sie "denken" nicht – sie berechnen Wahrscheinlichkeiten
- Training besteht aus Pre-Training (viel Text lesen) und Fine-Tuning (gute Antworten lernen)
- Token sind die Grundeinheit – Modelle haben ein begrenztes Kontextfenster
- Es gibt viele gute LLMs – kein einzelnes ist "das Beste" für alles

---

## Übung

**Teste denselben Prompt in zwei verschiedenen LLMs.**

1. Geh auf chat.openai.com und erstelle einen kostenlosen Account (falls du noch keinen hast)
2. Geh auf claude.ai und erstelle einen kostenlosen Account
3. Gib beiden genau denselben Prompt: "Erkläre mir in 3 Sätzen, warum der Himmel blau ist."
4. Vergleiche die Antworten:
   - Welche ist verständlicher?
   - Welche ist genauer?
   - Welche gefällt dir besser – und warum?

Schreib deine Beobachtungen auf. Das ist der Anfang deines Prompt-Tagebuchs, das dir in den nächsten Kapiteln noch sehr nützlich sein wird.
