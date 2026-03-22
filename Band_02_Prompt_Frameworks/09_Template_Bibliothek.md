# Kapitel 9: Deine persönliche Template-Bibliothek

Du hast jetzt alle Werkzeuge. Shot-Typen, drei Frameworks, Vergleichswissen. Jetzt kommt der Schritt, der dich von einem guten Prompter zu einem effizienten Prompter macht: Du baust dir eine Template-Bibliothek auf.

## Was ist eine Template-Bibliothek?

Eine Sammlung von Prompt-Vorlagen, die du immer wieder verwenden kannst. Stell dir ein Kochbuch vor, aber statt Rezepten stehen da deine besten Prompts drin.

Jedes Template ist ein erprobter Prompt, bei dem du nur noch die variablen Teile ausfüllen musst. Alles andere – Rolle, Format, Ton, Struktur – ist fest definiert und bewährt.

## Warum Templates der entscheidende Vorteil sind

Drei Gründe:

### 1. Zeitersparnis

Ohne Template schreibst du jeden Prompt von Grund auf. Das dauert bei CRAFT 2-3 Minuten, bei RISEN 5-10 Minuten. Bei 20 Prompts am Tag ist das eine Stunde nur für Prompt-Schreiben.

Mit Templates füllst du nur die Lücken aus. Das dauert 30 Sekunden. Rechne das hoch auf eine Woche.

### 2. Konsistente Qualität

Deine Templates basieren auf Prompts, die funktioniert haben. Du weißt, dass sie gute Ergebnisse liefern. Ohne Template improvisierst du jedes Mal – und mal ist es gut, mal weniger.

### 3. Wissenstransfer

Wenn du deine Templates dokumentierst, können auch Kollegen oder Teammitglieder sie nutzen. Das ist besonders in Unternehmen Gold wert, wo verschiedene Leute mit KI arbeiten, aber nicht alle gleich erfahren sind.

## So baust du deine Bibliothek auf

### Schritt 1: Sammle deine wiederkehrenden Aufgaben

Geh eine typische Arbeitswoche durch und notiere jede Aufgabe, bei der du ein LLM benutzt oder benutzen könntest:

- E-Mails schreiben
- Texte zusammenfassen
- Präsentationen erstellen
- Berichte formulieren
- Social-Media-Posts erstellen
- Code überprüfen
- Brainstorming
- Recherche
- Übersetzungen
- Feedback formulieren

### Schritt 2: Priorisiere

Welche Aufgaben machst du am häufigsten? Die kommen zuerst. Du brauchst nicht 50 Templates. Fang mit 5-10 an.

### Schritt 3: Wähle das passende Framework

Für jede Aufgabe: Ist RTF genug? Braucht es CRAFT? Oder RISEN? Nutze die Entscheidungsmatrix aus Kapitel 8.

### Schritt 4: Schreibe das Template

Jedes Template hat feste und variable Teile. Die festen Teile bleiben immer gleich. Die variablen Teile markierst du mit Platzhaltern.

### Schritt 5: Teste und verbessere

Benutze jedes Template mindestens 3-5 Mal, bevor du es als "fertig" betrachtest. Passe es nach jedem Einsatz an, wenn nötig.

## Template-Beispiele

### Template 1: Professionelle E-Mail (RTF)

```
Role: Professioneller Business-Kommunikator mit Erfahrung in
[BRANCHE]

Task: Schreibe eine E-Mail an [EMPFÄNGER] zum Thema [THEMA].
Kernbotschaft: [KERNBOTSCHAFT].
Gewünschte Reaktion: [WAS SOLL DER EMPFÄNGER TUN?]

Format: Betreffzeile + E-Mail-Text. Maximal [LÄNGE] Wörter.
[ANZAHL] Absätze.
```

**Anwendung:**
```
Role: Professioneller Business-Kommunikator mit Erfahrung in
der IT-Branche

Task: Schreibe eine E-Mail an den Projektleiter zum Thema
Budgetüberschreitung. Kernbotschaft: Wir brauchen 15% mehr
Budget für Phase 3. Gewünschte Reaktion: Termin für Budget-
Meeting vereinbaren.

Format: Betreffzeile + E-Mail-Text. Maximal 150 Wörter.
3 Absätze.
```

### Template 2: Blog-Artikel (CRAFT)

```
Context: Blog über [THEMA] für [ZIELGRUPPE]. [ZUSÄTZLICHER KONTEXT].

Role: [EXPERTEN-ROLLE] mit [ERFAHRUNG/SPEZIALISIERUNG].

Action: Schreibe einen Blogartikel über [ARTIKELTHEMA].
Hauptpunkte: [PUNKT 1], [PUNKT 2], [PUNKT 3].

Format: [WORTANZAHL] Wörter. Struktur: Einleitung (Hook +
Problem), [ANZAHL] Hauptteile mit Zwischenüberschriften, Fazit
mit [CTA/ZUSAMMENFASSUNG]. Verwende [FORMATIERUNGSWÜNSCHE].

Tone: [TONBESCHREIBUNG]. [STIL-DETAILS].
```

### Template 3: Strategische Analyse (RISEN)

```
Role: [EXPERTEN-ROLLE] mit Spezialisierung auf [FACHGEBIET].

Instructions: Analysiere [ANALYSEOBJEKT] und entwickle
[GEWÜNSCHTES ERGEBNIS]. Berücksichtige [RAHMENBEDINGUNGEN].

Steps:
1. Fasse die Ausgangssituation zusammen
2. Identifiziere die [ANZAHL] wichtigsten [CHANCEN/PROBLEME/TRENDS]
3. Entwickle für jede/s [CHANCE/PROBLEM/TREND] konkrete
   Handlungsempfehlungen
4. Priorisiere nach [KRITERIEN]
5. Erstelle einen Maßnahmenplan mit Zeitrahmen

End Goal: [KONKRETES ERGEBNIS], das [WER] für [ZWECK] verwenden kann.

Narrowing:
- [EINSCHRÄNKUNG 1]
- [EINSCHRÄNKUNG 2]
- [EINSCHRÄNKUNG 3]
```

### Template 4: Social-Media-Post (CRAFT + One-Shot)

```
Context: [PLATTFORM]-Account für [UNTERNEHMEN/PERSON].
Zielgruppe: [ZIELGRUPPE]. Bisherige Tonalität: [STIL].

Role: Social-Media-Manager mit Erfahrung in [BRANCHE].

Action: Erstelle [ANZAHL] Posts zum Thema [THEMA].

Format: Jeweils: Post-Text (max. [ZEICHENLIMIT] Zeichen) +
Hashtag-Vorschläge (max. [ANZAHL]) + Bild-Beschreibung
(1 Satz).

Tone: [TONBESCHREIBUNG].

Beispiel für unseren Stil:
[BEISPIEL-POST EINFÜGEN]
```

### Template 5: Feedback geben (RTF)

```
Role: Empathischer aber ehrlicher Kommunikationsberater

Task: Formuliere konstruktives Feedback für [PERSON/ROLLE] zum
Thema [FEEDBACK-THEMA]. Positiv: [WAS GUT WAR]. Verbesserung:
[WAS BESSER WERDEN SOLL]. Konkreter Vorschlag: [IDEE].

Format: 3 Absätze (Positives – Verbesserungspotenzial – nächste
Schritte). Maximal [LÄNGE] Wörter. Direkte Ansprache.
```

## Wo speicherst du deine Templates?

Es gibt keine perfekte Lösung, aber hier sind die gängigsten:

### Option 1: Notion / Obsidian / Evernote
Flexibel, durchsuchbar, mit Tags organisierbar. Mein persönlicher Favorit ist Notion, weil ich Templates in Datenbanken organisieren kann.

### Option 2: Google Docs / Word
Einfach, überall zugänglich. Ein Dokument pro Kategorie (Marketing, Kommunikation, Analyse, etc.)

### Option 3: GitHub / GitLab
Für die Technisch-Affinen. Versionierung inklusive – du siehst, wie sich deine Templates über die Zeit verbessert haben.

### Option 4: Direkt im LLM
Manche Tools wie ChatGPT bieten "Custom Instructions" oder gespeicherte Prompts. Praktisch, aber an ein Tool gebunden.

## Template-Organisation

Egal wo du speicherst – organisiere deine Templates so, dass du sie in unter 10 Sekunden findest:

**Kategorien (Vorschlag):**
- Kommunikation (E-Mails, Nachrichten, Feedback)
- Content (Blog, Social Media, Newsletter)
- Analyse (Marktanalyse, Wettbewerb, Daten)
- Kreativ (Brainstorming, Texte, Ideen)
- Technisch (Code, Dokumentation, Debugging)

**Für jedes Template dokumentiere:**
- Name (kurz und beschreibend)
- Kategorie
- Framework (RTF/CRAFT/RISEN)
- Wann verwenden (1 Satz)
- Letzte Änderung
- Bewertung (funktioniert gut / muss verbessert werden)

## Die 80/20-Regel der Templates

Du wirst feststellen: 20% deiner Templates benutzt du 80% der Zeit. Das ist normal. Konzentriere deine Energie auf diese 20%. Mach sie perfekt. Die anderen Templates? Gut genug reicht.

Und noch was: Templates sind lebende Dokumente. Wenn ein Prompt nicht mehr funktioniert – weil das LLM aktualisiert wurde, weil sich deine Anforderungen geändert haben, weil du was Besseres gefunden hast –, dann aktualisiere das Template. Lösche alte, die du nicht mehr brauchst.

## Zusammenfassung

- Eine Template-Bibliothek spart Zeit und sichert Qualität
- Starte mit 5-10 Templates für deine häufigsten Aufgaben
- Markiere variable Teile als Platzhalter [IN GROSSBUCHSTABEN]
- Teste jedes Template 3-5 Mal bevor du es als fertig betrachtest
- Organisiere nach Kategorien und halte Templates aktuell
- 20% deiner Templates decken 80% deiner Aufgaben ab

---

## Übung

**Dein Starter-Kit**

Erstelle deine ersten 5 Templates:

1. Identifiziere 5 Aufgaben, die du regelmäßig mit KI erledigst (oder erledigen könntest)
2. Wähle für jede Aufgabe das passende Framework
3. Schreibe das Template mit Platzhaltern
4. Teste jedes Template einmal
5. Speichere sie an einem Ort, wo du sie schnell wiederfindest

Du hast damit den Grundstein für dein persönliches Prompt-System gelegt. Ab jetzt baust du es Stück für Stück aus.
