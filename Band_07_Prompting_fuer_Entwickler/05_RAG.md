# Kapitel 5: RAG – Retrieval Augmented Generation

Das wichtigste Pattern für professionelle KI-Anwendungen. Punkt.

RAG löst das fundamentale Problem von LLMs: Sie wissen nur, was in ihren Trainingsdaten steht. Dein Unternehmens-Wiki? Deine Produktdokumentation? Deine Verträge? Davon weiß das Modell nichts.

RAG ändert das. Du reichst dem Modell die relevanten Informationen zusammen mit der Frage – und es antwortet basierend auf DEINEN Daten.

## Wie RAG funktioniert

```
1. INDEXIERUNG (einmalig):
   Dokumente → Chunks → Embeddings → Vektor-DB

2. ABFRAGE (bei jeder Frage):
   User-Frage → Embedding → Ähnlichkeitssuche in Vektor-DB
   → Top-K relevante Chunks abrufen

3. GENERATION (bei jeder Frage):
   System-Prompt + relevante Chunks + User-Frage
   → LLM generiert Antwort basierend auf den Chunks
```

### Visuell:

```
              ┌──────────────┐
              │ Deine Daten  │
              │ (PDFs, Docs, │
              │  Wiki, DB)   │
              └──────┬───────┘
                     │ Chunking + Embedding
                     ▼
              ┌──────────────┐
              │  Vektor-DB   │
              │ (Embeddings) │
              └──────┬───────┘
                     │ Similarity Search
    User-Frage ──────┤
                     ▼
              ┌──────────────┐
              │   Top-K      │
              │  Chunks      │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │     LLM      │
              │ (Claude etc.) │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   Antwort    │
              │ (mit Quellen)│
              └──────────────┘
```

## Schritt 1: Dokumente chunken

Chunking ist die wichtigste Entscheidung im RAG-Stack. Zu große Chunks = zu viel Noise. Zu kleine Chunks = fehlender Kontext.

### Chunking-Strategien

| Strategie | Beschreibung | Wann nutzen |
|---|---|---|
| **Fixed Size** | Alle 500 Tokens schneiden | Einfach, aber naiv |
| **Sentence-based** | An Satzgrenzen schneiden | Bessere semantische Einheiten |
| **Paragraph-based** | An Absatzgrenzen schneiden | Gut für strukturierte Dokumente |
| **Recursive** | Versuche große Teiler (§, \n\n, \n, .) | Standard-Empfehlung, flexibel |
| **Semantic** | Embedding-basiert, split bei Themenwechsel | Beste Qualität, teuerste Berechnung |
| **Document-aware** | Markdown-Header, HTML-Tags | Ideal für strukturierte Formate |

### Python-Beispiel: Recursive Chunking

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Zeichen pro Chunk
    chunk_overlap=200,      # Überlappung (Kontext-Brücke)
    separators=["\n\n", "\n", ". ", " ", ""],
    length_function=len
)

chunks = splitter.split_text(document_text)
# Ergebnis: Liste von Text-Chunks mit Überlappung
```

### Chunk-Optimierung

```python
# Metadata zu jedem Chunk hinzufügen
chunked_docs = []
for i, chunk in enumerate(chunks):
    chunked_docs.append({
        "text": chunk,
        "metadata": {
            "source": "handbuch_v2.pdf",
            "page": calculate_page(i),
            "chunk_index": i,
            "total_chunks": len(chunks),
            "section": extract_section_header(chunk)
        }
    })
```

## Schritt 2: Embeddings erstellen

Embeddings wandeln Text in Vektoren um – mathematische Repräsentationen der Bedeutung.

### Embedding-Modelle (Stand 2026)

| Modell | Anbieter | Dimensionen | Stärke | Kosten |
|---|---|---|---|---|
| `text-embedding-3-large` | OpenAI | 3072 | Bestes Allround | $0.13 / 1M Token |
| `text-embedding-3-small` | OpenAI | 1536 | Günstig, gut genug | $0.02 / 1M Token |
| `voyage-3-large` | Voyage AI | 1024 | Sehr gut für Code + Text | $0.18 / 1M Token |
| `embed-v4.0` | Cohere | 1024 | Multilingual stark | $0.10 / 1M Token |
| `nomic-embed-text` | Nomic | 768 | Open Source, lokal nutzbar | Kostenlos (lokal) |
| `mxbai-embed-large` | Mixedbread | 1024 | Deutsch besonders stark | Kostenlos (lokal) |

### Python: Embeddings erstellen (OpenAI)

```python
from openai import OpenAI

client = OpenAI()

def get_embeddings(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]

# Alle Chunks embedden
chunk_texts = [chunk["text"] for chunk in chunked_docs]
embeddings = get_embeddings(chunk_texts)
```

## Schritt 3: Vektor-Datenbank

Vektor-Datenbanken speichern Embeddings und ermöglichen schnelle Ähnlichkeitssuche.

### Vektor-DB-Vergleich

| DB | Typ | Stärke | Preis |
|---|---|---|---|
| **Pinecone** | Cloud (Managed) | Einfachste Setup, Serverless | Free Tier + Pay-per-use |
| **Weaviate** | Cloud + Self-hosted | Hybrid-Suche (Vektor + Keyword) | Free Tier + Managed |
| **Qdrant** | Cloud + Self-hosted | Performance, Rust-basiert | Free Tier + Self-hosted |
| **ChromaDB** | Lokal / Embedded | Einfachst für Prototypen | Kostenlos |
| **pgvector** | PostgreSQL Extension | In bestehende DB integriert | Kostenlos |
| **SQLite-vec** | SQLite Extension | Minimal, embedded | Kostenlos |

### Python: ChromaDB (einfachster Start)

```python
import chromadb

# Client erstellen (lokal, persistent)
client = chromadb.PersistentClient(path="./chroma_db")

# Collection erstellen
collection = client.get_or_create_collection(
    name="meine_docs",
    metadata={"hnsw:space": "cosine"}
)

# Dokumente hinzufügen
collection.add(
    documents=[chunk["text"] for chunk in chunked_docs],
    metadatas=[chunk["metadata"] for chunk in chunked_docs],
    ids=[f"chunk_{i}" for i in range(len(chunked_docs))]
)

# Suchen
results = collection.query(
    query_texts=["Wie funktioniert die Rückgabe?"],
    n_results=5
)
```

### Python: pgvector (in bestehender PostgreSQL)

```python
# SQL: Extension aktivieren
# CREATE EXTENSION vector;
# CREATE TABLE documents (
#     id SERIAL PRIMARY KEY,
#     content TEXT,
#     embedding vector(1536),
#     metadata JSONB
# );
# CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops);

import psycopg2

def search_similar(query_embedding, limit=5):
    conn = psycopg2.connect("postgresql://...")
    cur = conn.cursor()
    cur.execute("""
        SELECT content, metadata, 1 - (embedding <=> %s::vector) AS similarity
        FROM documents
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """, (query_embedding, query_embedding, limit))
    return cur.fetchall()
```

## Schritt 4: RAG-Pipeline zusammenbauen

```python
import anthropic
from openai import OpenAI

openai_client = OpenAI()
anthropic_client = anthropic.Anthropic()

def rag_query(question: str, collection, top_k: int = 5) -> str:
    # 1. Frage embedden
    q_embedding = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=[question]
    ).data[0].embedding

    # 2. Ähnliche Chunks finden
    results = collection.query(
        query_embeddings=[q_embedding],
        n_results=top_k
    )

    # 3. Kontext zusammenbauen
    context = "\n\n---\n\n".join(results["documents"][0])
    sources = [m["source"] for m in results["metadatas"][0]]

    # 4. LLM mit Kontext befragen
    message = anthropic_client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system="""Beantworte Fragen basierend auf dem bereitgestellten Kontext.
Wenn die Antwort nicht im Kontext steht, sag das ehrlich.
Zitiere relevante Stellen aus dem Kontext.""",
        messages=[{
            "role": "user",
            "content": f"""KONTEXT:
{context}

FRAGE: {question}

Beantworte die Frage basierend auf dem Kontext. Nenne die Quellen."""
        }]
    )

    return message.content[0].text
```

## Fortgeschrittene RAG-Techniken

### Hybrid Search (Vektor + Keyword)

Kombiniere semantische Suche mit klassischer Keyword-Suche:

```python
# Weaviate Hybrid Search
results = weaviate_client.query.get(
    "Document", ["content", "source"]
).with_hybrid(
    query="Rückgaberecht bei Online-Kauf",
    alpha=0.7  # 0 = nur Keyword, 1 = nur Vektor
).with_limit(5).do()
```

### Reranking

Nach der Suche: Sortiere die Ergebnisse mit einem Reranker-Modell:

```python
from cohere import Client

co = Client()

# Erste Suche: Vektor-DB (schnell, breit)
initial_results = collection.query(query_texts=[question], n_results=20)

# Reranking: Präzisere Sortierung
reranked = co.rerank(
    model="rerank-v3.5",
    query=question,
    documents=initial_results["documents"][0],
    top_n=5
)
# Ergebnis: Die 5 relevantesten Chunks, besser sortiert
```

### Query Expansion

Die User-Frage umformulieren für bessere Treffer:

```python
# LLM generiert alternative Suchanfragen
expansion = anthropic_client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    messages=[{
        "role": "user",
        "content": f"""Generiere 3 alternative Formulierungen für diese Suchanfrage:
"{question}"
Nur die Alternativen, eine pro Zeile."""
    }]
)

# Suche mit allen Varianten, dedupliziere Ergebnisse
queries = [question] + expansion.content[0].text.strip().split("\n")
```

### Contextual Retrieval (Anthropic)

Vor dem Embedden: Kontext zum Chunk hinzufügen:

```python
# Für jeden Chunk: LLM generiert einen Kontextsatz
context_prompt = f"""Hier ist das gesamte Dokument:
{full_document}

Hier ist ein Chunk daraus:
{chunk}

Schreibe einen kurzen Satz (max. 20 Wörter), der erklärt,
wo sich dieser Chunk im Gesamtdokument einordnet."""

# Der Kontextsatz wird dem Chunk vorangestellt:
# "Dieser Abschnitt beschreibt die Rückgabebedingungen für Online-Käufe."
# + Original-Chunk-Text
# → Bessere Embeddings, bessere Suchergebnisse
```

## RAG Anti-Patterns

### Anti-Pattern 1: Zu große Chunks
→ Das Modell bekommt irrelevante Informationen und wird verwirrt.

### Anti-Pattern 2: Kein Overlap
→ Informationen, die über Chunk-Grenzen gehen, werden nicht gefunden.

### Anti-Pattern 3: Blindes Vertrauen
→ Das Modell kann Informationen aus den Chunks falsch interpretieren. Immer Quellen angeben und verifizierbar machen.

### Anti-Pattern 4: Alles in den Kontext
→ 20 Chunks à 1000 Tokens = 20k Tokens Kontext. Das Modell findet die Nadel im Heuhaufen nicht. Top 3-5 reichen meist.

---

## Übungen

### Übung 1: Einfaches RAG
Nimm 3-5 PDF-Dokumente, chunke sie, erstelle Embeddings und baue eine RAG-Pipeline mit ChromaDB. Stelle Fragen an deine Dokumente.

### Übung 2: Chunking-Vergleich
Chunke dasselbe Dokument mit verschiedenen Strategien (500 vs. 1000 Zeichen, mit/ohne Overlap). Vergleiche die Suchergebnisse.

### Übung 3: Hybrid Search
Implementiere eine Hybrid-Suche, die Vektor-Suche mit Keyword-Suche kombiniert. Bei welchen Fragen ist Hybrid besser?

### Übung 4: Evaluierung
Erstelle 10 Frage-Antwort-Paare für deine Dokumente. Wie oft gibt das RAG-System die richtige Antwort? Wo scheitert es?
