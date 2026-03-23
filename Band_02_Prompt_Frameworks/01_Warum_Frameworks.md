# Kapitel 1: Warum Frameworks?

Bevor wir uns die einzelnen Frameworks anschauen, müssen wir eine grundlegende Frage klären: Warum braucht man überhaupt Frameworks für Prompts?

Die ehrliche Antwort: Brauchst du nicht. Du kannst auch ohne Frameworks gute Prompts schreiben. Du hast die 5 Bausteine aus Band 1, du hast Erfahrung gesammelt, und manchmal reicht ein einfacher Satz, um genau das Ergebnis zu bekommen, das du willst.

Aber.

## Das Problem mit der Intuition

Kennst du das? Du schreibst einen Prompt, bekommst ein brauchbares Ergebnis und denkst dir: "Läuft." Dann, drei Tage später, schreibst du einen ähnlichen Prompt für eine ähnliche Aufgabe – und das Ergebnis ist Müll. Du weißt nicht, was du beim ersten Mal anders gemacht hast. Du erinnerst dich nicht an die genaue Formulierung. Und dein Prompt-Protokoll? Hast du vielleicht doch nicht so konsequent geführt.

Das ist das Problem mit Intuition. Sie funktioniert – manchmal. Aber sie ist nicht reproduzierbar. Und in dem Moment, wo du KI regelmäßig nutzt, brauchst du Reproduzierbarkeit.

Frameworks lösen genau dieses Problem.

## Was ein Framework tut

Ein Prompt-Framework ist nichts anderes als eine Checkliste. Eine Vorlage, die dir sagt: "Denk an diesen Punkt. Und an diesen. Und an diesen." Es zwingt dich, bestimmte Elemente in deinen Prompt einzubauen, die du sonst vielleicht vergessen würdest.

Das klingt banal. Ist es auch. Aber die banalsten Dinge sind oft die effektivsten.

Piloten benutzen Checklisten. Nicht weil sie dumm sind, sondern weil Checklisten Fehler verhindern. Chirurgen benutzen Checklisten. Nicht weil sie ihr Handwerk nicht können, sondern weil in Stresssituationen selbst Profis Dinge vergessen.

Prompt-Frameworks sind deine Checklisten.

## Die drei Ebenen

Es gibt verschiedene Ebenen, auf denen Frameworks arbeiten:

### Ebene 1: Shot-Typen

Die grundlegendste Ebene. Hier geht es um eine einzige Frage: Gibst du dem Modell Beispiele oder nicht?

- **Zero-Shot:** Keine Beispiele. Du beschreibst nur die Aufgabe.
- **One-Shot:** Ein Beispiel.
- **Few-Shot:** Mehrere Beispiele.

Das klingt simpel, und das ist es auch. Aber die Wirkung ist enorm. Wir behandeln das ausführlich in den Kapiteln 2–4.

### Ebene 2: Struktur-Frameworks

Hier wird es interessanter. Struktur-Frameworks geben dir eine feste Reihenfolge vor, in der du deinen Prompt aufbaust:

- **CRAFT:** Context, Role, Action, Format, Tone
- **RTF:** Role, Task, Format
- **RISEN:** Role, Instructions, Steps, End goal, Narrowing

Jedes Framework hat seine Stärken. CRAFT ist am universellsten, RTF ist am schnellsten, RISEN ist am detailliertesten. In den Kapiteln 5–7 lernst du alle drei kennen, und Kapitel 8 zeigt dir, wann du welches nutzen solltest.

### Ebene 3: Template-Bibliothek

Die dritte Ebene ist deine persönliche Sammlung. Du nimmst die Frameworks, wendest sie auf wiederkehrende Aufgaben an und speicherst die besten Prompts als Vorlagen. Kapitel 9 zeigt dir, wie du das aufbaust.

## Frameworks sind keine Zwangsjacke

Ich muss das betonen, weil ich es in jeder Diskussion über Frameworks höre: "Aber dann wird doch alles so starr und formelhaft!"

Nein. Wird es nicht.

Ein Framework ist ein Startpunkt, kein Korsett. Du benutzt es als Grundlage und passt es an deine Bedürfnisse an. Manchmal lässt du Teile weg. Manchmal fügst du Elemente hinzu. Das ist nicht nur erlaubt, das ist gewünscht.

Denk an Musik. Professionelle Musiker lernen jahrelang Musiktheorie. Tonleitern, Harmonielehre, Rhythmik. Macht sie das steif und formelhaft? Nein. Es gibt ihnen das Fundament, auf dem sie improvisieren können.

Prompt-Frameworks funktionieren genauso. Sie geben dir Struktur, damit deine Kreativität nicht ins Leere läuft.

## Der Vorher-Nachher-Effekt

Lass mich dir ein konkretes Beispiel zeigen.

**Ohne Framework:**
```
Schreib mir einen Blogartikel über gesunde Ernährung.
```

Das Ergebnis? Generisch. Langweilig. Austauschbar. Könnte von jedem geschrieben worden sein, für niemanden bestimmt.

**Mit CRAFT-Framework:**
```
Context: Ich betreibe einen Blog über alltagstaugliche Gesundheitstipps
für berufstätige Eltern. Meine Leser haben wenig Zeit und wollen
praktische, sofort umsetzbare Ratschläge.

Role: Du bist ein erfahrener Ernährungsberater, der sich auf
Familienernährung spezialisiert hat. Du kommunizierst locker und
praxisnah, ohne erhobenen Zeigefinger.

Action: Schreibe einen Blogartikel über 5 einfache Wege, wie
berufstätige Eltern die Ernährung ihrer Familie verbessern können,
ohne stundenlang in der Küche zu stehen.

Format: 800-1000 Wörter. Einleitung, 5 nummerierte Tipps mit jeweils
einer konkreten Umsetzungsidee, Fazit. Verwende Zwischenüberschriften.

Tone: Locker, ermutigend, realistisch. Kein Schuldgefühl-Machen.
Kein "Du musst" – sondern "Du kannst".
```

Der Unterschied im Ergebnis ist dramatisch. Und das Beste: Du musst nicht jedes Mal von Null anfangen. Wenn du nächste Woche einen weiteren Blogartikel brauchst, nimmst du diesen Prompt, änderst das Thema, und fertig.

Das ist die Kraft von Frameworks.

## Ein Wort der Warnung

Frameworks machen dich nicht automatisch besser. Sie sind Werkzeuge, keine Wundermittel. Wenn dein Verständnis der Grundlagen fehlt – wenn du nicht weißt, warum Kontext wichtig ist oder wie Rollen funktionieren –, dann helfen dir auch die schicksten Frameworks nicht weiter.

Deshalb war Band 1 so wichtig. Und deshalb sage ich: Wenn du Band 1 übersprungen hast, geh zurück und lies ihn. Die Frameworks in diesem Band setzen voraus, dass du die Grundlagen draufhast.

Für alle anderen: Auf geht's.

---

## Übung

**Framework-Reflexion**

Nimm drei Prompts, die du in den letzten Tagen geschrieben hast (oder schreib drei neue für alltägliche Aufgaben). Für jeden Prompt:

1. Identifiziere, welche der 5 Bausteine (Aufgabe, Kontext, Format, Ton, Einschränkungen) du verwendet hast
2. Notiere, welche du vergessen hast
3. Überlege, ob ein vergessener Baustein das Ergebnis verbessert hätte

Du wirst merken: Die meisten Leute vergessen konsistent dieselben Bausteine. Das ist genau der Punkt, an dem Frameworks helfen.
