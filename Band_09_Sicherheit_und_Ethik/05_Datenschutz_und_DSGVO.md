# Kapitel 5: Datenschutz und DSGVO – Was du darfst und was nicht

Das ist das Kapitel, das niemand lesen will und jeder lesen muss. Datenschutz klingt nach Bürokratie, nach Paragraphen und Formularen. Aber in einer Welt, in der KI-Tools Daten verarbeiten, die durch dutzende Systeme fließen, ist Datenschutz keine Formalie – es ist ein existenzielles Risiko.

Ein DSGVO-Verstoß kann dein Unternehmen Millionen kosten. Nicht theoretisch. Real.

## Die Grundfrage: Welche Daten gibst du in die KI?

Jedes Mal, wenn du Text in ein KI-Tool einfügst, verarbeitest du Daten. Und wenn diese Daten personenbezogen sind, greift die DSGVO. Die entscheidende Frage ist nicht "Ist KI erlaubt?" sondern "Welche Daten darf ich in welches KI-Tool eingeben?"

### Was sind personenbezogene Daten?

Alles, was eine natürliche Person identifiziert oder identifizierbar macht:

- **Direkt:** Name, E-Mail, Telefonnummer, Adresse
- **Indirekt:** Personalnummer, Kundennummer, IP-Adresse
- **Besondere Kategorien (Art. 9 DSGVO):** Gesundheitsdaten, politische Meinungen, ethnische Herkunft, biometrische Daten, Gewerkschaftszugehörigkeit

Besondere Kategorien sind der Hochrisikobereich. Gesundheitsdaten in ein Cloud-LLM einzugeben, ohne Rechtsgrundlage und technisch-organisatorische Maßnahmen, ist nicht nur ein Compliance-Problem – es ist potenziell strafbar.

### Die Anonymisierungs-Illusion

"Ich entferne einfach den Namen" reicht nicht. Eine Kombination aus Alter, Diagnose, Wohnort und Behandlungsdatum kann eine Person eindeutig identifizieren. Echte Anonymisierung ist schwieriger, als die meisten denken.

**Pseudonymisierung** (Name durch Code ersetzen) ist besser, aber die Daten bleiben personenbezogen im Sinne der DSGVO – sie sind nur schwerer zuzuordnen.

**Echte Anonymisierung** bedeutet: Die Daten können unter keinen Umständen einer Person zugeordnet werden. Dann greift die DSGVO nicht mehr. Aber das ist in der Praxis oft nicht erreichbar.

## DSGVO-Grundlagen für KI-Nutzung

### Rechtsgrundlage (Art. 6 DSGVO)

Für jede Verarbeitung personenbezogener Daten brauchst du eine Rechtsgrundlage:

**1. Einwilligung (Art. 6 Abs. 1 lit. a):** Die Person hat zugestimmt. Muss freiwillig, informiert, spezifisch und unmissverständlich sein. Und jederzeit widerrufbar. Für KI-Nutzung: Der Betroffene muss wissen, dass seine Daten in ein KI-System eingegeben werden.

**2. Vertrag (Art. 6 Abs. 1 lit. b):** Die Verarbeitung ist für die Erfüllung eines Vertrags nötig. Wenn ein Kunde dich beauftragt und du KI zur Auftragserfüllung nutzt, kann das eine Grundlage sein – aber nur für den konkreten Zweck.

**3. Berechtigtes Interesse (Art. 6 Abs. 1 lit. f):** Dein Interesse überwiegt das des Betroffenen. Für interne Effizienzsteigerung durch KI oft anwendbar, aber nur nach Abwägung. Und nicht für sensible Daten.

### Auftragsverarbeitung (Art. 28 DSGVO)

Wenn du Cloud-LLMs nutzt (Claude, ChatGPT, Gemini), ist der Anbieter ein Auftragsverarbeiter. Du brauchst einen **Auftragsverarbeitungsvertrag (AVV)**. Die großen Anbieter bieten das an:

- **Anthropic (Claude):** AVV verfügbar, EU-Rechenzentren (über GCP/AWS)
- **OpenAI (ChatGPT):** AVV verfügbar (Data Processing Agreement), ChatGPT Enterprise mit verstärkten Garantien
- **Google (Gemini):** AVV über Google Workspace, EU-Rechenzentren
- **Microsoft (Copilot):** Integriert in bestehende Microsoft 365 AVV

**Enterprise-Versionen** (Claude for Enterprise, ChatGPT Enterprise, Microsoft Copilot) bieten in der Regel: Keine Nutzung der Daten zum Training, SOC-2-Zertifizierung, regionale Datenverarbeitung, Audit-Trails.

**Kostenlose Versionen und Standard-Abos** können Nutzerdaten für Modellverbesserung verwenden (je nach Anbieter und Einstellung). Prüfe die Datenschutzrichtlinien deines Anbieters genau.

### Drittlandtransfer

Wenn Daten in die USA übermittelt werden (was bei den meisten Cloud-LLMs der Fall ist), brauchst du eine Grundlage für den Drittlandtransfer. Seit dem EU-US Data Privacy Framework (Juli 2023) ist das für zertifizierte US-Unternehmen wieder möglich. Anthropic, OpenAI und Google sind zertifiziert. Aber: Das Framework könnte erneut angefochten werden (wie Safe Harbor und Privacy Shield davor).

**Sicherste Option:** EU-Rechenzentren nutzen, wenn verfügbar. Oder lokale Modelle (Ollama, vLLM), die das Unternehmen nicht verlassen.

## Praktische Regeln für den Arbeitsalltag

### Die Daten-Ampel

Erstelle für dein Team eine klare Klassifizierung:

**🟢 Grün – Darf in jedes KI-Tool:**
- Öffentlich verfügbare Informationen
- Anonymisierte Daten (wirklich anonymisiert)
- Allgemeine Fragen ohne Personenbezug
- Fiktive Beispiele

**🟡 Gelb – Nur in freigegebene Enterprise-Tools:**
- Interne Geschäftsdaten (nicht personenbezogen)
- Aggregierte Kennzahlen
- Pseudonymisierte Daten mit AVV

**🔴 Rot – Niemals in Cloud-KI:**
- Echte Kundendaten mit Namen
- Personaldaten (Gehälter, Bewertungen, Gesundheit)
- Vertrauliche Verträge mit Personenbezug
- Gesundheitsdaten
- Finanzdaten einzelner Personen

### Was tun, wenn du personenbezogene Daten verarbeiten musst?

1. **Anonymisiere** so weit wie möglich, bevor du an die KI gehst
2. **Nutze Enterprise-Versionen** mit AVV und Nicht-Trainings-Garantie
3. **Dokumentiere** die Rechtsgrundlage und den Zweck
4. **Informiere** die Betroffenen (Datenschutzerklärung aktualisieren)
5. **Lösche** die Daten aus dem KI-Tool nach Gebrauch, wenn möglich

### Die häufigsten DSGVO-Fehler mit KI

1. **Kundenmails in ChatGPT kopieren** – ohne AVV, ohne Rechtsgrundlage
2. **Bewerbungen durch KI bewerten lassen** – ohne Information der Bewerber
3. **Support-Transkripte als Trainingsdaten nutzen** – ohne Einwilligung
4. **Mitarbeiter-Feedback in KI analysieren** – besondere Kategorie, Art. 9
5. **"Ist ja nur intern"** – auch interne Verarbeitung ist Verarbeitung

## Datenschutz-Folgenabschätzung (DSFA)

Wenn du KI-Systeme einführst, die personenbezogene Daten verarbeiten, ist wahrscheinlich eine Datenschutz-Folgenabschätzung nötig (Art. 35 DSGVO). Das gilt besonders für:

- Systematische Bewertung persönlicher Aspekte (Scoring, Profiling)
- Verarbeitung besonderer Datenkategorien in großem Umfang
- Systematische Überwachung öffentlich zugänglicher Bereiche

Eine DSFA beschreibt: Was wird verarbeitet, warum, welche Risiken bestehen und welche Maßnahmen werden ergriffen. Klingt nach Aufwand – ist aber Pflicht und schützt dich im Ernstfall.

## Der Datenschutzbeauftragte

Ab 20 Mitarbeitern, die regelmäßig personenbezogene Daten verarbeiten, ist ein Datenschutzbeauftragter Pflicht (§ 38 BDSG). Wenn du KI einführst, involviere ihn von Anfang an. Nicht als Bremse, sondern als Berater. Ein guter DSB findet Wege, KI DSGVO-konform zu nutzen – statt sie zu verbieten.

---

## Übungen

### Übung 1: Daten-Ampel erstellen
Erstelle eine Daten-Ampel (grün/gelb/rot) für die Datentypen in deinem Unternehmen. Welche Daten fallen in welche Kategorie?

### Übung 2: AVV prüfen
Prüfe, ob für dein KI-Tool ein Auftragsverarbeitungsvertrag existiert. Was steht drin? Werden Daten zum Training genutzt?

### Übung 3: DSGVO-Schnellcheck
Nimm 3 konkrete KI-Anwendungsfälle in deinem Team. Prüfe für jeden: Rechtsgrundlage? Personenbezug? Drittlandtransfer? Information der Betroffenen?

### Übung 4: Anonymisierung testen
Nimm einen echten Datensatz und versuche, ihn zu anonymisieren. Ist er wirklich anonym, oder kannst du Personen rekonstruieren?
