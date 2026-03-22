# Vorwort

Willkommen in der Fortgeschrittenen-Liga.

Drei Bände liegen hinter dir. Du weißt, was KI ist, wie LLMs funktionieren, was die 5 Bausteine eines guten Prompts sind. Du kennst Frameworks wie CRAFT, RTF und RISEN. Du kannst Prompt-Ketten bauen, Delimiter setzen, Temperatur einstellen und System-Prompts schreiben. Du debuggst Prompts systematisch statt alles wegzuwerfen und neu anzufangen.

Kurz: Du bist gut.

Aber "gut" reicht nicht für das, was jetzt kommt.

## Warum dieses Buch anders ist

In den ersten drei Bänden hast du gelernt, WAS du dem Modell sagen sollst. Welche Bausteine, welche Frameworks, welche Techniken. Du hast dem Modell Anweisungen gegeben und es hat geliefert.

Band 4 dreht das um. Hier lernst du nicht, was du sagst – sondern wie das Modell *denken* soll.

Das ist ein fundamentaler Unterschied. Stell dir vor, du arbeitest mit einem sehr klugen Praktikanten. In den ersten drei Bänden hast du gelernt, ihm klare Aufgaben zu geben. "Schreib mir das. Analysiere jenes. Formatiere es so." Der Praktikant hat geliefert, weil deine Anweisungen gut waren.

Aber jetzt stehst du vor Problemen, die eine einfache Anweisung nicht löst. Logikrätsel. Mehrstufige Analysen. Entscheidungen mit unvollständigen Informationen. Komplexe Schlussfolgerungen.

Für diese Probleme reicht "Mach das" nicht. Du musst dem Praktikanten sagen: "Denk so darüber nach."

Und genau das tun Reasoning-Techniken.

## Was dich erwartet

**Chain-of-Thought** – Die Mutter aller Reasoning-Techniken. Du bringst das Modell dazu, Schritt für Schritt zu denken statt direkt zur Antwort zu springen. Bei komplexen Aufgaben verbessert das die Ergebnisse um 20-60%.

**Zero-Shot Chain-of-Thought** – CoT ohne Beispiele. Manchmal reichen fünf magische Wörter: "Denke Schritt für Schritt nach." Wann das funktioniert und wann nicht.

**Tree-of-Thought** – Statt einem Denkpfad erkundest du mehrere gleichzeitig. Das Modell bewertet verschiedene Ansätze und wählt den besten. Wie ein Schachspieler, der mehrere Züge vorausdenkt.

**Self-Consistency** – Du lässt das Modell dasselbe Problem mehrfach lösen und nimmst die häufigste Antwort. Wie eine Jury-Abstimmung – die Mehrheit hat meistens recht.

**ReAct** – Reasoning + Acting. Das Modell denkt, handelt, beobachtet und plant den nächsten Schritt. Die Grundlage für alles, was heute als "KI-Agent" gehypt wird.

**Meta-Prompting** – Prompts, die Prompts verbessern. Du lässt das Modell seinen eigenen Prompt analysieren und optimieren. Klingt nach Inception – ist es auch.

**Reflexion und Selbstkorrektur** – Das Modell überprüft seine eigene Arbeit und korrigiert Fehler. Wie ein Autor, der seinen Text Korrektur liest – nur automatisiert.

**Techniken kombinieren** – Das mächtigste Kapitel. Du lernst, wie du CoT, ToT, Self-Consistency und ReAct zu komplexen Reasoning-Pipelines verbindest.

## Für wen ist dieser Band?

Für dich, wenn du Band 1-3 gelesen hast. Oder wenn du schon Erfahrung mit Prompts hast und merkst: Bei einfachen Aufgaben sind meine Ergebnisse super, aber bei komplexen Problemen liefert die KI Unsinn.

Du brauchst die Grundlagen aus den vorherigen Bänden. Besonders Prompt-Chaining (Band 3, Kapitel 1), System-Prompts (Band 3, Kapitel 5) und Prompt-Debugging (Band 3, Kapitel 7) werden hier vorausgesetzt.

## Mein eigener Weg zu Reasoning

Ich erinnere mich noch genau an den Moment, als mir klar wurde, dass Reasoning-Techniken existieren. Ich hatte einen langen Prompt geschrieben, in dem ich Claude gebeten habe, eine Geschäftsstrategie zu analysieren. Der Output war – naja, oberflächlich. Bullet Points, die wie aus einem Lehrbuch kopiert klangen. Keine echte Analyse, keine Abwägung, kein "Einerseits ... andererseits."

Dann habe ich fünf Wörter hinzugefügt: "Denke Schritt für Schritt nach."

Das Ergebnis war ein komplett anderer Text. Plötzlich hat das Modell Annahmen hinterfragt. Risiken abgewogen. Gegenargumente gefunden, die mir selbst nicht eingefallen wären. Es war, als hätte ich einen Schalter umgelegt – vom Textgenerator zum Denkpartner.

Seitdem habe ich Hunderte von Stunden damit verbracht, verschiedene Reasoning-Techniken zu testen, zu vergleichen und zu kombinieren. Dieses Buch ist das Ergebnis.

## Wie du dieses Buch am besten nutzt

Lies die Kapitel der Reihe nach. Jedes baut auf dem vorherigen auf. Chain-of-Thought (Kapitel 2) ist die Grundlage für alles Weitere. Tree-of-Thought (Kapitel 4) setzt voraus, dass du CoT verstanden hast. Und das Kombinationskapitel (Kapitel 9) braucht alles.

Die Übungen sind diesmal anspruchsvoller als in den vorherigen Bänden. Das ist Absicht. Du bist kein Anfänger mehr, und die Übungen spiegeln das wider. Nimm dir Zeit dafür. Manche wirst du mehrfach versuchen müssen.

Und: Führe dein Prompt-Protokoll weiter. Notiere, welche Reasoning-Technik du bei welcher Aufgabe eingesetzt hast und was das Ergebnis war. Nach diesem Band wirst du Muster erkennen, die dir sagen, welche Technik wann am besten funktioniert.

Los geht's. Wir bringen die KI zum Denken.

*Belkis Aslani, März 2026*
