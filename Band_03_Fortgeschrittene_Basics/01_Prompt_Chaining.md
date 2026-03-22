# Kapitel 1: Prompt-Chaining – Große Aufgaben in kleine Schritte zerlegen

Stell dir vor, du bittest jemanden: "Recherchiere das Thema Elektromobilität, analysiere die Vor- und Nachteile, schreib einen 2000-Wörter-Artikel darüber, formatiere ihn als Blogpost, füge passende Überschriften ein und achte darauf, dass der Ton informativ aber nicht langweilig ist."

In einem einzigen Satz. Ohne Pause.

Was würde passieren? Die Person würde wahrscheinlich Teile vergessen. Oder alles oberflächlich abarbeiten. Oder sich in den Details verlieren.

Genau das passiert auch mit LLMs, wenn du alles in einen einzigen Prompt packst. Sie können es – theoretisch. Aber die Qualität leidet. Und je komplexer die Aufgabe, desto mehr leidet sie.

Die Lösung heißt Prompt-Chaining.

## Was ist Prompt-Chaining?

Prompt-Chaining bedeutet: Du zerlegst eine komplexe Aufgabe in mehrere einzelne Prompts. Jeder Prompt hat eine klar definierte Aufgabe. Und das Ergebnis eines Prompts wird zum Input des nächsten.

Statt einem Mega-Prompt schreibst du eine Kette.

```
Prompt 1: Recherchiere → Ergebnis 1
Prompt 2: Analysiere Ergebnis 1 → Ergebnis 2
Prompt 3: Schreib einen Artikel basierend auf Ergebnis 2 → Ergebnis 3
Prompt 4: Überarbeite Ergebnis 3 → Fertiger Artikel
```

Das klingt nach mehr Arbeit. Ist es auch. Aber das Endergebnis ist fast immer besser. Warum?

## Warum Chaining funktioniert

### 1. Fokus

Ein Prompt, eine Aufgabe. Das Modell muss nicht jonglieren. Es kann sich voll und ganz auf einen Schritt konzentrieren. Das bedeutet weniger vergessene Details, weniger halbgare Ergebnisse.

### 2. Qualitätskontrolle

Nach jedem Schritt kannst du das Ergebnis prüfen. Stimmt die Recherche? Ist die Analyse sinnvoll? Passt der Ton? Du korrigierst Fehler, bevor sie sich durch die gesamte Aufgabe ziehen.

Bei einem Mega-Prompt merkst du den Fehler erst am Ende – und musst alles von vorne machen.

### 3. Kontext-Effizienz

Jeder Prompt bekommt genau den Kontext, den er braucht. Nicht mehr, nicht weniger. Das ist besonders wichtig, wenn du an die Grenzen des Kontext-Fensters kommst (dazu mehr in Kapitel 6).

### 4. Wiederverwendbarkeit

Einzelne Glieder der Kette kannst du wiederverwenden. Dein Recherche-Prompt funktioniert für jedes Thema. Dein Analyse-Prompt auch. Du baust dir quasi modulare Bauteile.

## Deine erste Kette

Lass uns das an einem konkreten Beispiel durchspielen. Aufgabe: Eine Produktbeschreibung für einen Online-Shop schreiben.

### Schritt 1: Informationen sammeln

```
Ich verkaufe einen kabellosen Bluetooth-Kopfhörer mit diesen Eigenschaften:
- Noise Cancelling (ANC)
- 30 Stunden Akku
- Schnellladefunktion (10 Min = 3 Stunden)
- Gewicht: 250g
- Preis: 79 Euro

Erstelle eine Liste der 5 wichtigsten Verkaufsargumente aus Kundensicht.
Sortiere sie nach Relevanz für den typischen Online-Käufer.
```

**Ergebnis:** Du bekommst eine priorisierte Liste. Prüfe sie. Passt die Reihenfolge? Fehlt etwas? Korrigiere, wenn nötig.

### Schritt 2: Zielgruppe definieren

```
Basierend auf diesen Verkaufsargumenten:
[Ergebnis aus Schritt 1 einfügen]

Beschreibe die ideale Zielgruppe für dieses Produkt.
Wer kauft einen 79-Euro-ANC-Kopfhörer?
Nenne: Alter, Beruf, Lebensstil, Kaufmotivation, Preiserwartung.
```

### Schritt 3: Produktbeschreibung schreiben

```
Schreibe eine Produktbeschreibung für einen Online-Shop.

Zielgruppe:
[Ergebnis aus Schritt 2 einfügen]

Verkaufsargumente (in dieser Reihenfolge):
[Ergebnis aus Schritt 1 einfügen]

Format:
- Überschrift (max. 10 Wörter, Nutzen betonen)
- Einleitungssatz (1 Satz, emotional)
- 3–4 Absätze mit je einem Verkaufsargument
- Technische Daten als Aufzählung am Ende
- Call-to-Action als letzter Satz

Ton: Direkt, ehrlich, nicht übertrieben. Kein "revolutionär", kein "einzigartig".
Länge: 200–250 Wörter.
```

### Schritt 4: Qualitätskontrolle

```
Prüfe diese Produktbeschreibung auf:
1. Faktische Korrektheit (stimmen alle Zahlen?)
2. Übertreibungen oder Marketing-Floskeln
3. Lesbarkeit (ist jeder Satz nötig?)
4. Call-to-Action (ist er überzeugend ohne aufdringlich zu sein?)

Produktbeschreibung:
[Ergebnis aus Schritt 3 einfügen]

Gib konkretes Feedback zu jedem Punkt.
Schreibe dann eine verbesserte Version.
```

Vier Prompts statt einem. Das dauert vielleicht fünf Minuten länger. Aber das Ergebnis ist durchdacht, zielgruppengerecht und frei von den typischen Schwächen eines Mega-Prompts.

## Wann Chaining und wann nicht

Nicht jede Aufgabe braucht eine Kette. Hier ist meine Faustregel:

**Chaining lohnt sich bei:**
- Aufgaben mit mehr als 3 verschiedenen Teilschritten
- Aufgaben, bei denen die Qualität wichtig ist (Kundenkommunikation, Berichte, Artikel)
- Aufgaben, bei denen du Zwischenergebnisse prüfen willst
- Aufgaben, die verschiedene Fähigkeiten erfordern (Recherche + Analyse + Schreiben)

**Ein einzelner Prompt reicht bei:**
- Einfachen, klar definierten Aufgaben
- Aufgaben, die du schnell brauchst und "gut genug" reicht
- Routineaufgaben, für die du schon ein Template hast

## Vier Ketten-Muster

### Muster 1: Linear (A → B → C → D)

Das einfachste Muster. Jeder Schritt baut auf dem vorherigen auf.

```
Recherche → Analyse → Entwurf → Überarbeitung
```

Nutze es für: Artikel, Berichte, Zusammenfassungen.

### Muster 2: Fächerförmig (A → B1, B2, B3 → C)

Ein Eingabe-Prompt erzeugt mehrere parallele Ergebnisse, die am Ende zusammengeführt werden.

```
Briefing → [Version sachlich, Version emotional, Version humorvoll] → Beste Elemente kombinieren
```

Nutze es für: Kreative Aufgaben, bei denen du Varianten brauchst.

### Muster 3: Prüfschleife (A → B → Prüfung → B korrigiert)

Ein Schritt wird wiederholt, bis das Ergebnis stimmt.

```
Entwurf → Prüfung → "Verbessere X, Y, Z" → Nochmal prüfen → Fertig
```

Nutze es für: Texte mit hohen Qualitätsanforderungen, Code-Generierung.

### Muster 4: Akkumulation (A + B + C → D)

Mehrere unabhängige Ergebnisse werden am Ende zusammengeführt.

```
[Recherche Markt] + [Recherche Wettbewerber] + [Recherche Zielgruppe] → Zusammenfassender Bericht
```

Nutze es für: Recherche-Projekte, Entscheidungsvorlagen.

## Häufige Fehler beim Chaining

### Fehler 1: Zu viele Schritte

Fünf bis sechs Schritte sind meist das Maximum. Mehr Schritte bedeuten mehr Übergaben, und bei jeder Übergabe kann Information verloren gehen. Wenn deine Kette zehn Schritte hat, überleg, ob du Schritte zusammenfassen kannst.

### Fehler 2: Zu wenig Kontext übergeben

"Basierend auf dem vorherigen Ergebnis..." ist kein guter Übergang. Kopiere das relevante Ergebnis explizit in den nächsten Prompt. Das Modell hat kein perfektes Gedächtnis – je klarer du bist, desto besser.

### Fehler 3: Keinen Prüfschritt einbauen

Die Versuchung ist groß, einfach von Schritt zu Schritt durchzuklicken. Aber der Prüfschritt ist der wichtigste Teil. Er fängt Fehler auf, bevor sie sich durch die Kette ziehen. Nimm dir die 30 Sekunden.

### Fehler 4: Die Kette nicht dokumentieren

Wenn du eine gute Kette gebaut hast, schreib sie auf. Speichere die Prompts. Notiere, welche Schritte du kombiniert oder angepasst hast. Dein zukünftiges Ich wird dir danken.

## Ein komplexes Beispiel: Bewerbungsanschreiben

Hier eine vollständige Kette für ein Bewerbungsanschreiben:

**Schritt 1: Stellenanzeige analysieren**
```
Analysiere diese Stellenanzeige. Extrahiere:
1. Die 5 wichtigsten Anforderungen
2. Die 3 wichtigsten Soft Skills
3. Die Unternehmenskultur (formell/locker/technisch)
4. Keywords, die im Anschreiben vorkommen sollten

Stellenanzeige:
"""
[Stellenanzeige einfügen]
"""
```

**Schritt 2: Qualifikationen abgleichen**
```
Hier sind die Anforderungen einer Stelle:
[Ergebnis Schritt 1]

Und hier ist mein Lebenslauf:
"""
[Lebenslauf einfügen]
"""

Erstelle eine Tabelle: Anforderung | Meine Qualifikation | Beweis/Beispiel
Markiere Lücken ehrlich.
```

**Schritt 3: Anschreiben entwerfen**
```
Schreibe ein Bewerbungsanschreiben basierend auf:

Anforderungen und Keywords:
[Ergebnis Schritt 1]

Mein Qualifikations-Match:
[Ergebnis Schritt 2]

Regeln:
- Maximal 1 Seite
- Kein "hiermit bewerbe ich mich"
- Erster Satz muss neugierig machen
- Jeder Absatz enthält ein konkretes Beispiel
- Ton: professionell aber nicht steif
- Schluss: Handlungsaufforderung ohne Floskeln
```

**Schritt 4: Feinschliff**
```
Prüfe dieses Anschreiben:
[Ergebnis Schritt 3]

Checkliste:
- Sind alle Keywords aus der Stellenanzeige eingebaut?
- Gibt es Floskeln? Ersetze sie durch konkrete Aussagen.
- Ist der Ton konsistent?
- Passt die Länge (max. 1 Seite)?
- Würde ein Personaler nach dem ersten Satz weiterlesen?

Schreibe die verbesserte Endversion.
```

Vier Schritte, und du hast ein Anschreiben, das besser ist als 90% dessen, was Leute mit einem einzelnen "Schreib mir ein Bewerbungsanschreiben"-Prompt bekommen.

---

## Übung

**Bau deine erste Kette**

Wähle eine dieser Aufgaben:
1. Einen Blogpost über ein Thema deiner Wahl schreiben
2. Eine Präsentation (5 Folien) zu einem Thema vorbereiten
3. Einen Newsletter für ein fiktives Unternehmen erstellen

Dann:
1. Zerlege die Aufgabe in mindestens 3 Schritte
2. Schreibe für jeden Schritt einen Prompt
3. Führe die Kette durch – und prüfe nach jedem Schritt das Ergebnis
4. Vergleiche das Endergebnis mit einem einzelnen Mega-Prompt für die gleiche Aufgabe

Notiere: Wo war das Chaining-Ergebnis besser? Wo hat der Mega-Prompt gereicht? Wie viel länger hat die Kette gedauert?
