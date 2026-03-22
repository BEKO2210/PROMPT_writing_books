# Kapitel 10: Zusammenfassung und Ausblick

Drei Bände. Du bist offiziell kein Anfänger mehr.

Lass mich zusammenfassen, was du in Band 3 gelernt hast – und was als Nächstes kommt.

## Was du jetzt kannst

1. **Prompt-Chaining** – Du zerlegst komplexe Aufgaben in Ketten. Jeder Schritt baut auf dem vorherigen auf. Du kennst vier Ketten-Muster und weißt, wann sich Chaining lohnt und wann ein einzelner Prompt reicht.

2. **Delimiter einsetzen** – Du strukturierst deine Prompts mit `"""`, Backticks, XML-Tags und Markdown-Überschriften. Das Modell kann verschiedene Teile deines Prompts sauber trennen. Und du weißt, warum Delimiter auch ein Sicherheitsthema sind.

3. **Negative Prompts** – Du sagst dem Modell, was es NICHT tun soll. Du verhinderst Standardfloskeln, KI-typische Muster und unerwünschte Formate. Und du kombinierst positive und negative Anweisungen für maximale Präzision.

4. **Temperatur und Parameter** – Du weißt, was Temperatur, Top-P, Max Tokens und Penalties bewirken. Du kannst Parameter bewusst einstellen statt den Standard zu akzeptieren. Und du hast Parameter-Profile für typische Aufgaben.

5. **System-Prompts** – Du verstehst, wie System-Prompts funktionieren und warum sie mächtiger sind als normale Prompts. Du hast fünf fertige System-Prompts und weißt, wie du Custom Instructions sinnvoll nutzt.

6. **Kontext-Fenster** – Du kennst die Grenzen der Modelle und hast Strategien, um damit umzugehen. Zusammenfassen, neue Konversationen, Kontext komprimieren – du weißt, was zu tun ist, wenn das Modell anfängt zu vergessen.

7. **Prompt-Debugging** – Du hast ein 5-Schritte-System, um nicht funktionierende Prompts systematisch zu verbessern. Statt alles wegzuwerfen, findest du den Fehler und behebst ihn.

8. **Batch-Prompting** – Du verarbeitest mehrere Items effizient in einem Prompt. Du kennst die optimalen Batch-Größen und weißt, wie du das Output-Format sicherstellst.

9. **Modelle vergleichen** – Du kennst die Stärken und Schwächen der wichtigsten Modelle und wählst das richtige Werkzeug für die richtige Aufgabe.

## Checkliste: Bin ich bereit für Band 4?

- [ ] Ich habe mindestens 3 Prompt-Ketten gebaut und getestet
- [ ] Ich benutze Delimiter in jedem Prompt, der länger als 3 Sätze ist
- [ ] Ich kombiniere positive und negative Anweisungen routinemäßig
- [ ] Ich habe mit Temperatur experimentiert und weiß, welche Werte für meine Aufgaben passen
- [ ] Ich habe einen System-Prompt / Custom Instructions eingerichtet und nutze sie täglich
- [ ] Ich weiß, wann ich eine neue Konversation starten muss (Kontext-Fenster)
- [ ] Ich debugge Prompts systematisch statt alles neu zu schreiben
- [ ] Ich habe Batch-Prompting für mindestens 5 Items getestet
- [ ] Ich habe mindestens 2 verschiedene Modelle ausprobiert
- [ ] Mein Prompt-Protokoll hat mindestens 30 Einträge

Bei 7 von 10? Weiter zu Band 4.

## Was dich in Band 4 erwartet

Band 4 heißt "Reasoning-Techniken" – und hier wird es richtig spannend. Denn bis jetzt hast du dem Modell gesagt, WAS es tun soll. In Band 4 lernst du, WIE es denken soll.

### Chain-of-Thought (CoT)

Die wichtigste Reasoning-Technik. Statt eine Antwort direkt zu verlangen, bittest du das Modell, Schritt für Schritt zu denken. Das klingt simpel, verbessert aber die Ergebnisse bei logischen Aufgaben dramatisch.

```
# Ohne CoT
Was ist 17 × 24?

# Mit CoT
Was ist 17 × 24? Denke Schritt für Schritt.
```

Bei einfacher Mathematik ist der Unterschied klein. Bei komplexen Problemen – Logik, Analyse, Planung – ist er enorm.

### Tree-of-Thought (ToT)

Chain-of-Thought, aber verzweigt. Das Modell denkt nicht nur einen Weg, sondern mehrere gleichzeitig. Es bewertet verschiedene Lösungsansätze und wählt den besten.

### Self-Consistency

Statt einer Antwort generierst du mehrere und nimmst die, die am häufigsten vorkommt. Wie eine Abstimmung unter Experten – die Mehrheit hat meistens recht.

### ReAct

Reasoning + Acting. Das Modell denkt UND handelt. Es plant einen Schritt, führt ihn aus, beobachtet das Ergebnis und plant den nächsten Schritt. Die Grundlage für KI-Agenten.

### Meta-Prompting

Prompts über Prompts. Du lässt das Modell seinen eigenen Prompt verbessern. Klingt nach Inception – ist es auch irgendwie.

## Wie die Reihe weitergeht

**Anfänger (Band 1–3) ✓**
- Band 1: Grundlagen ✓
- Band 2: Prompt-Frameworks ✓
- Band 3: Fortgeschrittene Basics ✓ *(du bist hier)*

**Fortgeschritten (Band 4–6)**
- Band 4: Reasoning-Techniken ← *als Nächstes*
- Band 5: Kreatives Prompting
- Band 6: Spezialisiertes Prompting

**Profi (Band 7–9)**
- Band 7: Prompting für Entwickler
- Band 8: Business & Produktivität
- Band 9: Sicherheit & Ethik

**Experte (Band 10)**
- Band 10: Die Zukunft

## Ein Gedanke zum Schluss

In den letzten drei Bänden hast du eine Menge Werkzeuge gesammelt. Grundlagen, Frameworks, Techniken. Du weißt, wie Prompts aufgebaut sind, wie du sie strukturierst, wie du Parameter einstellst und wie du Fehler behebst.

Jetzt kommt der Teil, wo es richtig interessant wird. Die Anfänger-Phase ist vorbei. Ab Band 4 geht es darum, das Modell nicht nur als Textgenerator zu nutzen, sondern als Denkpartner.

Chain-of-Thought, Tree-of-Thought, Self-Consistency – das sind die Techniken, die den Unterschied machen zwischen "KI als bessere Suchmaschine" und "KI als intellektuelles Werkzeug".

Und dafür brauchst du alles, was du in den letzten drei Bänden gelernt hast. Jeder Baustein, den du gemeistert hast, wird relevant.

Also: Prompt-Protokoll nachführen. Die Übungen, die du übersprungen hast, nachholen (ja, du weißt genau welche). Und dann: Band 4.

Wir sehen uns dort.

*Belkis Aslani*

---

## Ressourcen und weiterführende Links

**Prompt-Chaining:**
- LangChain Dokumentation – Framework für Prompt-Ketten (für Entwickler)
- "Chain-of-Verification" (Dhuliawala et al., 2023) – Akademisches Paper zu verketteter Verifikation

**Delimiter und Strukturierung:**
- OpenAI Prompt Engineering Guide – Best Practices für Delimiter
- Anthropic Claude Documentation – Empfehlungen zu XML-Tags in Prompts

**Temperatur und Parameter:**
- Google AI Studio (aistudio.google.com) – Kostenlos Parameter testen
- OpenAI Playground (platform.openai.com/playground) – GPT-Parameter einstellen

**System-Prompts:**
- Anthropic System Prompts – Veröffentlichte System-Prompts als Referenz
- "System Prompts" (GitHub Repository) – Sammlung von System-Prompts

**Modellvergleiche:**
- Chatbot Arena (lmarena.ai) – Community-basierter Modellvergleich
- Artificial Analysis (artificialanalysis.ai) – Objektive Benchmarks und Preisvergleiche
- LMSYS Leaderboard – Akademische Benchmarks

**Wissenschaftlich:**
- "Lost in the Middle" (Liu et al., 2023) – Studie zum Kontext-Fenster-Effekt
- "Batch Prompting" (Cheng et al., 2023) – Forschung zu Batch-Effizienz
