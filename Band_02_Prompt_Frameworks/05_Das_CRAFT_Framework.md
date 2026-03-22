# Kapitel 5: Das CRAFT-Framework – Dein Allrounder

Jetzt wird's ernst. Wir verlassen die Shot-Typen und steigen in die Struktur-Frameworks ein. Und wir fangen mit dem vielseitigsten an: CRAFT.

CRAFT steht für:

- **C** – Context (Kontext)
- **R** – Role (Rolle)
- **A** – Action (Aufgabe/Aktion)
- **F** – Format (Ausgabeformat)
- **T** – Tone (Tonalität)

Kommt dir bekannt vor? Sollte es. Das sind im Grunde die 5 Bausteine aus Band 1, nur anders sortiert und unter einem einprägsamen Namen verpackt.

## Warum CRAFT?

Weil es funktioniert. Und weil es leicht zu merken ist.

Ich habe dutzende Frameworks getestet. Manche hatten 8 Buchstaben, manche 3. CRAFT ist der Sweet Spot. Es ist detailliert genug, um fast jede Aufgabe abzudecken, und kompakt genug, um es sich tatsächlich zu merken.

Außerdem passt der Name: CRAFT bedeutet auf Englisch "Handwerk". Und genau das ist Prompting – ein Handwerk.

## Die fünf Elemente im Detail

### C – Context (Kontext)

Der Kontext beantwortet die Frage: Was ist die Ausgangssituation?

Hier gibst du dem Modell alle Hintergrundinformationen, die es braucht, um deine Aufgabe zu verstehen. Wer bist du? Wofür brauchst du das Ergebnis? Welche Rahmenbedingungen gibt es?

**Beispiele:**
- "Ich bin Teamleiterin in einem mittelständischen IT-Unternehmen mit 50 Mitarbeitern."
- "Wir planen ein Webinar zum Thema Datenschutz für kleine Unternehmen."
- "Der Kunde hat sich dreimal beschwert und droht mit Kündigung."

### R – Role (Rolle)

Die Rolle beantwortet die Frage: Wer soll das Modell sein?

In Band 1 hast du gelernt, dass Rollen die Qualität der Antwort massiv beeinflussen. In CRAFT ist die Rolle fest im Framework verankert – du vergisst sie nicht mehr.

**Beispiele:**
- "Du bist ein erfahrener HR-Manager mit 15 Jahren Erfahrung."
- "Du bist eine Marketingexpertin, die sich auf B2B-SaaS spezialisiert hat."
- "Du bist ein geduldiger Nachhilfelehrer für Mathematik."

### A – Action (Aktion)

Die Aktion beantwortet die Frage: Was genau soll das Modell tun?

Das ist der Kern deines Prompts. Klare, eindeutige Anweisung. Kein "Hilf mir mal" oder "Mach was Schönes". Sondern: "Schreibe", "Analysiere", "Erstelle", "Vergleiche".

**Beispiele:**
- "Schreibe eine Einladungs-E-Mail für das Webinar."
- "Erstelle eine Pro-Contra-Liste für die Einführung von Remote Work."
- "Analysiere diese drei Bewerbungen und erstelle eine Ranking-Liste."

### F – Format (Format)

Das Format beantwortet die Frage: Wie soll das Ergebnis aussehen?

Ohne Format-Vorgabe entscheidet das Modell selbst – und die Entscheidung ist selten optimal. Mit Format-Vorgabe bekommst du genau das, was du brauchst.

**Beispiele:**
- "Bullet-Point-Liste mit maximal 7 Punkten"
- "Tabelle mit Spalten: Name, Stärken, Schwächen, Gesamtbewertung"
- "Fließtext, 300-400 Wörter, mit Zwischenüberschriften"
- "JSON-Objekt mit den Feldern: Titel, Zusammenfassung, Keywords"

### T – Tone (Tonalität)

Der Ton beantwortet die Frage: Wie soll es klingen?

Der am meisten unterschätzte Baustein. Viele Leute denken, der Ton sei egal, weil es "nur eine KI" ist. Aber der Ton bestimmt, ob dein Ergebnis nach Pressemitteilung klingt oder nach Gespräch unter Freunden.

**Beispiele:**
- "Professionell aber zugänglich, keine Fachsprache"
- "Freundlich und ermutigend, wie ein guter Coach"
- "Direkt und sachlich, ohne Floskeln"
- "Humorvoll und leicht, wie ein Podcast-Gespräch"

## CRAFT in der Praxis: Vollständige Beispiele

### Beispiel 1: Blog-Artikel

```
Context: Ich betreibe einen Karriere-Blog für Young Professionals
(25-35 Jahre) in der DACH-Region. Der Blog hat monatlich ca.
15.000 Leser. Thema dieses Monats: Gehaltsverhandlung.

Role: Du bist ein erfahrener Karrierecoach, der seit 10 Jahren
Young Professionals bei Gehaltsverhandlungen berät. Du kennst die
typischen Fehler und hast ein Händchen für praxisnahe Tipps.

Action: Schreibe einen Blogartikel über die 5 größten Fehler bei
der ersten Gehaltsverhandlung und wie man sie vermeidet.

Format: 1200-1500 Wörter. Einleitung (Hook + Problemstellung),
5 Fehler als nummerierte Abschnitte (je mit Beispielsituation und
konkretem Tipp), Fazit mit Ermutigung. Verwende Zwischenüberschriften
(H2 für jeden Fehler).

Tone: Locker aber kompetent. Du-Ansprache. Konkrete Beispiele statt
abstrakte Ratschläge. Kein "Sei einfach selbstbewusst"-Gelaber.
```

### Beispiel 2: Kundenservice-Antwort

```
Context: Ich arbeite im Kundenservice eines Online-Möbelhauses.
Ein Kunde hat einen Schreibtisch bestellt, der mit einer verkratzten
Oberfläche ankam. Es ist sein zweiter Reklamationsfall in 3 Monaten.

Role: Du bist ein erfahrener Kundenservice-Mitarbeiter, der
Eskalationen mit Empathie und konkreten Lösungen entschärft.

Action: Verfasse eine Antwort-E-Mail, die das Problem anerkennt,
sich entschuldigt und eine Lösung anbietet (Austauschlieferung +
15% Gutschein auf die nächste Bestellung als Wiedergutmachung).

Format: Maximal 200 Wörter. Anrede, 3-4 kurze Absätze, Grußformel.
Keine Standard-Textbausteine wie "Ihr Anliegen ist uns wichtig".

Tone: Aufrichtig entschuldigend, ohne übertrieben unterwürfig zu sein.
Lösungsorientiert. Der Kunde soll das Gefühl haben, gehört zu werden.
```

### Beispiel 3: Technische Dokumentation

```
Context: Wir haben gerade eine neue REST-API für unser
Projektmanagement-Tool gelauncht. Die Dokumentation soll
Entwicklern helfen, die API schnell zu integrieren.

Role: Du bist ein Technical Writer mit Erfahrung in API-Dokumentation.
Du schreibst für Entwickler, die wenig Zeit haben und schnell
funktionierende Beispiele brauchen.

Action: Schreibe die Dokumentation für den Endpunkt
POST /api/v1/projects. Decke ab: Beschreibung, Authentifizierung,
Request-Parameter, Beispiel-Request, Beispiel-Response, Fehlercodes.

Format: Markdown. Klare Überschriften, Code-Blöcke für Beispiele
(curl + Python), Tabelle für Parameter und Fehlercodes.

Tone: Sachlich und präzise. Kein Marketing-Sprech. Direkt und
technisch korrekt, aber nicht trocken.
```

## CRAFT muss nicht immer vollständig sein

Wichtiger Punkt: Du musst nicht immer alle fünf Elemente verwenden. CRAFT ist eine Checkliste, kein Formular, das komplett ausgefüllt werden muss.

- Schnelle Frage an die KI? Vielleicht reicht A + F.
- Kreativer Text? C + R + A + T ist wichtiger als F.
- Datenaufgabe? C + A + F, ohne R und T.

Die Faustregel: Je komplexer die Aufgabe, desto mehr CRAFT-Elemente brauchst du.

| Komplexität | Empfohlene Elemente |
|---|---|
| Einfach (Übersetzung, Zusammenfassung) | A, F |
| Mittel (E-Mail, Blogartikel) | C, R, A, F, T |
| Komplex (Strategie, Analyse) | Alle + Einschränkungen |

## CRAFT kombiniert mit Shot-Typen

Und hier wird's richtig mächtig: Du kannst CRAFT mit Zero-Shot, One-Shot oder Few-Shot kombinieren.

**CRAFT + Zero-Shot:** Der Prompt oben. Klare Struktur, keine Beispiele.

**CRAFT + One-Shot:** Du fügst nach der CRAFT-Beschreibung ein Beispiel hinzu.

```
[CRAFT-Prompt wie oben]

Hier ist ein Beispiel für den gewünschten Stil:
[Beispiel einfügen]

Jetzt schreibe den Text für das neue Thema:
[Thema]
```

**CRAFT + Few-Shot:** Mehrere Beispiele nach dem CRAFT-Block.

Das ist die Profi-Variante. Und ja, die Prompts werden dabei lang. Das ist okay. Ein langer, strukturierter Prompt schlägt einen kurzen, vagen Prompt jedes Mal.

## Zusammenfassung

- CRAFT = Context, Role, Action, Format, Tone
- Das vielseitigste Framework – funktioniert für fast jede Aufgabe
- Nicht immer alle 5 Elemente nötig – anpassen je nach Komplexität
- Kombinierbar mit Shot-Typen für maximale Kontrolle
- CRAFT ist der logische nächste Schritt nach den 5 Bausteinen aus Band 1

---

## Übung

**CRAFT-Marathon**

Schreibe drei vollständige CRAFT-Prompts für folgende Szenarien:

1. **Bewerbung:** Du willst ein Motivationsschreiben für deinen Traumjob erstellen lassen
2. **Präsentation:** Du brauchst eine Gliederung für einen Vortrag vor dem Management
3. **Social Media:** Du willst eine Woche Instagram-Posts für ein kleines Café planen

Für jeden Prompt: Fülle alle 5 CRAFT-Elemente aus. Teste sie. Bewerte die Ergebnisse. Welches Element hat den größten Einfluss auf die Qualität?
