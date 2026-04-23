# 📘 RAG Architecture — Local Pipeline (Day 1)

## 🔹 What is RAG?

**RAG (Retrieval-Augmented Generation)** is a system that improves LLM responses by retrieving relevant external data before generating answers.

Instead of relying only on training data, the model uses:

* 📂 Your documents
* 🔍 Semantic search
* 🤖 LLM for final response

---

## 🔹 High-Level Architecture

```
User Query
    ↓
Retriever (Vector Search)
    ↓
Relevant Chunks
    ↓
Prompt Builder
    ↓
Generator (LLM)
    ↓
Final Answer
```

---

## 🔹 System Components

### 1. 📥 Ingestion Pipeline

Responsible for loading and preprocessing documents.

**Supports:**

* PDF
* TXT
* CSV
* DOCX

**Steps:**

1. Load documents
2. Clean text (remove noise, extra spaces)
3. Normalize encoding

---

### 2. ✂️ Chunking Strategy

Documents are split into smaller chunks for better retrieval.

**Config:**

* Chunk size: `500–800 tokens`
* Overlap: `50–100 tokens`

**Why overlap?**

* Prevents loss of context between chunks
* Improves retrieval quality

---

### 3. 🏷 Metadata Tagging

Each chunk contains metadata:

```json
{
  "source": "file_name.pdf",
  "page": 3,
  "tags": ["finance", "report"]
}
```

**Purpose:**

* Better filtering
* Source tracing
* Explainability

---

### 4. 🧠 Embedding Generation

Convert text chunks into vectors using a local embedding model.

**Pipeline:**

```
Text Chunk → Embedding Model → Vector
```

**Output:**

* Dense vector representation of text

---

### 5. 🗄 Vector Store (FAISS / Qdrant)

Stores embeddings for fast similarity search.

**Index Types:**

* Flat (exact search, slow)
* IVF (faster, approximate)
* HNSW (best balance, graph-based)

**Stored Data:**

* Vector
* Metadata
* Chunk text

---

### 6. 🔍 Retriever Module

Handles query search.

**Steps:**

1. Convert query → embedding
2. Perform similarity search
3. Return top-k relevant chunks

---

### 7. 🧾 Prompt Builder

Combines:

* User query
* Retrieved chunks

**Example Prompt:**

```
Answer the question based only on the context below:

Context:
{retrieved_chunks}

Question:
{user_query}
```

---

### 8. 🤖 Generator (LLM)

Local LLM generates final response using:

* Retrieved context
* Prompt instructions

---

## 🔹 Folder Structure

```
src/
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── chunks/
│   ├── embeddings/
│
├── vectorstore/
├── retriever/
├── generator/
├── pipelines/
├── prompts/
├── models/
├── evaluation/
├── utils/
├── config/
├── logs/
```

---

## 🔹 End-to-End Flow

```
Documents → Cleaning → Chunking → Metadata
        → Embeddings → Vector DB

User Query → Embedding → Retrieval → Context
        → Prompt → LLM → Response
```

---

## 🔹 Key Concepts

### 🔸 Chunk Size vs Token Limit

* Too small → weak context
* Too large → retrieval noise

👉 Optimal: `500–800 tokens`

---

### 🔸 Overlap Strategy

* Maintains continuity
* Improves semantic recall

---

### 🔸 Semantic Search

Uses **vector similarity (cosine / dot product)** instead of keyword matching.

---

### 🔸 Embedding Pipeline

```
Raw Text → Clean → Chunk → Embed → Store
```

---

### 🔸 Index Selection

| Index Type | Speed | Accuracy | Use Case       |
| ---------- | ----- | -------- | -------------- |
| Flat       | Slow  | High     | Small datasets |
| IVF        | Fast  | Medium   | Large datasets |
| HNSW       | Fast  | High     | Production     |

---

## 🔹 Deliverables

* `/pipelines/ingest.py` → Data ingestion
* `/embeddings/embedder.py` → Embedding generation
* `/vectorstore/index.faiss` → Stored vectors
* `/retriever/query_engine.py` → Query search
* `RAG-ARCHITECTURE.md` → Documentation

---

## 🔹 Evaluation Metrics

* Retrieval Accuracy (Top-K relevance)
* Response Quality
* Latency
* Hallucination Reduction

---

## 🔹 Summary

RAG improves LLM performance by:

* Injecting real-time knowledge
* Reducing hallucinations
* Making answers explainable

---

## 🚀 Next Step

Build:

* Retrieval evaluation
* Multi-query retriever
* Re-ranking pipeline

---
