# Kapitel 5: RAG – Retrieval Augmented Generation

Das wichtigste Pattern für professionelle KI-Anwendungen. Punkt.

RAG löst das fundamentale Problem von LLMs: Sie wissen nur, was in ihren Trainingsdaten steht. Dein Unternehmens-Wiki? Deine Produktdokumentation? Deine Verträge? Davon weiß das Modell nichts.

RAG ändert das. Du reichst dem Modell die relevanten Informationen zusammen mit der Frage – und es antwortet basierend auf DEINEN Daten.

## Wie RAG funktioniert

Drei Phasen:

1. **Indexierung** (einmalig): Dokumente → Chunks → Embeddings → Vektor-DB
2. **Abfrage** (bei jeder Frage): User-Frage → Embedding → Ähnlichkeitssuche → Top-K Chunks
3. **Generation** (bei jeder Frage): System-Prompt + Chunks + Frage → LLM → Antwort

Organisationen berichten von 60-80% weniger Halluzinationen und 3x besserer Antwortgenauigkeit bei domain-spezifischen Fragen.

## Schritt 1: Dokumente chunken

Chunking ist die wichtigste Entscheidung im RAG-Stack. **80% aller RAG-Fehler liegen im Chunking-Layer, nicht beim LLM.**

### Chunking-Strategien

| Strategie | Beschreibung | Wann nutzen |
|---|---|---|
| **Fixed Size** | Alle 500 Tokens schneiden | Einfach, aber naiv |
| **Recursive** | Versuche große Teiler (§, \n\n, \n, .) | **Standard-Empfehlung** |
| **Semantic** | Split bei Themenwechsel per Embedding | Beste Qualität, teuerste Berechnung |
| **Document-aware** | Markdown-Header, HTML-Tags | Ideal für strukturierte Formate |

**Empfohlener Standard:** Recursive Character Splitting, **512 Tokens**, 50-100 Tokens Overlap. Erzielte 69% Accuracy im größten Real-Document-Test 2026.

**Häufige Fehler:**
- Zu kleine Chunks (unter 100 Tokens) verlieren Kontext
- Zu große Chunks (über 2.500 Tokens) verwässern die Relevanz
- Semantisches Chunking klingt besser als es ist – rechtfertigt selten die höheren Kosten

Die Implementierung ist einfach: `RecursiveCharacterTextSplitter` aus LangChain mit `chunk_size`, `chunk_overlap` und einer Liste von Separatoren. Metadata pro Chunk hinzufügen (Quelle, Seite, Abschnitt).

## Schritt 2: Embeddings erstellen

Embeddings wandeln Text in Vektoren um – mathematische Repräsentationen der Bedeutung. Ähnliche Texte haben ähnliche Vektoren.

### Embedding-Modelle (Stand 2026)

| Modell | Anbieter | Stärke | Kosten |
|---|---|---|---|
| `text-embedding-3-large` | OpenAI | Bestes Allround | $0.13 / 1M Token |
| `voyage-3-large` | Voyage AI | #1 MTEB Retrieval | $0.18 / 1M Token |
| Gemini Embedding 2 | Google | #1 ELO-Ranking | Kostenlos (Free Tier) |
| `embed-v4.0` | Cohere | Multilingual stark | $0.10 / 1M Token |
| BGE-M3 | Open Source | Bestes Budget/Self-Hosted | Kostenlos (lokal) |

**Kritisch:** Query und Chunks müssen das gleiche Embedding-Modell verwenden. Modell-Upgrades erfordern Re-Embedding des gesamten Corpus.

Die Implementierung: OpenAI-Client, `client.embeddings.create(model="text-embedding-3-small", input=texts)` – gibt eine Liste von Vektoren zurück.

## Schritt 3: Vektor-Datenbank

| DB | Typ | Stärke | Wann nutzen |
|---|---|---|---|
| **Pinecone** | Cloud | Sub-10ms Latenz, SOC2/HIPAA | Enterprise, Skalierung |
| **Weaviate** | Cloud + Self-hosted | Hybrid-Suche, Multi-Modal | Wenn Hybrid Search wichtig |
| **Qdrant** | Cloud + Self-hosted | Performance (Rust), Filter | Hohe Anforderungen an Filter |
| **ChromaDB** | Lokal / Embedded | Einfachster Start | **Prototypen** |
| **pgvector** | PostgreSQL Extension | In bestehende DB integriert | Wenn du Postgres hast |

**Für den Start:** ChromaDB. Collection erstellen, Dokumente mit `collection.add()` hinzufügen, mit `collection.query()` suchen. Drei Zeilen Setup, sofort einsatzbereit.

**Für Produktion:** pgvector (75% günstiger als Pinecone bei bestehender Postgres-Infrastruktur) oder Weaviate (wenn Hybrid Search nötig).

## Schritt 4: RAG-Pipeline zusammenbauen

Die Pipeline in vier Schritten:

1. Frage embedden
2. Ähnliche Chunks finden (Top-K, typisch 3-5)
3. Kontext zusammenbauen (Chunks als String)
4. LLM mit System-Prompt + Kontext + Frage befragen

Der System-Prompt ist entscheidend: *"Beantworte Fragen basierend auf dem bereitgestellten Kontext. Wenn die Antwort nicht im Kontext steht, sag das ehrlich. Zitiere relevante Stellen."*

## Fortgeschrittene RAG-Techniken

### Hybrid Search (Vektor + Keyword)

**Pflicht für Produktion.** Reine Vektor-Suche verpasst exakte Treffer (z.B. "RFC 7231"). BM25 verpasst semantische Queries. Produktion braucht beides. Weaviate bietet das nativ mit einem `alpha`-Parameter (0 = nur Keyword, 1 = nur Vektor).

### Reranking

**Höchster ROI-Upgrade in RAG.** Erst breit suchen (Top 20), dann mit einem Reranker-Modell (z.B. Cohere `rerank-v3.5`) auf Top 5 sortieren. Deutlich bessere Ergebnisqualität.

### Query Expansion

Die User-Frage umformulieren für bessere Treffer. Ein schnelles LLM (Haiku) generiert 3 alternative Formulierungen. Suche mit allen Varianten, dedupliziere Ergebnisse.

### Contextual Retrieval

Vor dem Embedden: Jedem Chunk einen Kontextsatz voranstellen, der erklärt, wo sich der Chunk im Gesamtdokument einordnet. Bessere Embeddings, bessere Suchergebnisse.

## RAG Anti-Patterns

1. **Zu große Chunks** → Modell wird von irrelevanter Information verwirrt
2. **Kein Overlap** → Informationen über Chunk-Grenzen gehen verloren
3. **Blindes Vertrauen** → Modell kann Chunks falsch interpretieren – immer Quellen angeben
4. **Zu viel Kontext** → 20 Chunks à 1000 Tokens = Nadel im Heuhaufen. Top 3-5 reichen

---

## Übungen

### Übung 1: Einfaches RAG
Nimm 3-5 PDFs, chunke sie, erstelle Embeddings und baue eine RAG-Pipeline mit ChromaDB.

### Übung 2: Chunking-Vergleich
Chunke dasselbe Dokument mit verschiedenen Strategien. Vergleiche die Suchergebnisse.

### Übung 3: Hybrid Search
Implementiere Hybrid-Suche (Vektor + Keyword). Bei welchen Fragen ist Hybrid besser?

### Übung 4: Evaluierung
Erstelle 10 Frage-Antwort-Paare für deine Dokumente. Wie oft gibt das RAG-System die richtige Antwort?
