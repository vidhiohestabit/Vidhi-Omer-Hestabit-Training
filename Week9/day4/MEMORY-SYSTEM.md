# MEMORY SYSTEM

## Overview
This system implements 3 types of memory:

### 1. Short-Term Memory
- Stores last few interactions
- Maintains conversational context

### 2. Long-Term Memory (SQLite)
- Stores important facts
- Persistent across sessions

### 3. Vector Memory (FAISS)
- Stores embeddings
- Enables similarity-based retrieval

---

## Flow

User Input
→ Search Vector Memory
→ Retrieve Similar Context
→ Add Session Context
→ Add Long-Term Facts
→ Generate Response
→ Store in Memory

---

## Design Choices

- FAISS for fast similarity search
- SQLite for persistence
- Session buffer for recent context

---

## Limitations

- Basic importance detection
- No summarization
- No memory pruning

---

## Future Improvements

- LLM-based summarization
- Better importance scoring
- Hybrid search