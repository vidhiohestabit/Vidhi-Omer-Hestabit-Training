# 🚀 Local LLM API (Day 5 Capstone)

## 📌 Overview

This project implements a **local LLM inference API** using FastAPI/Flask, designed for:

* RAG systems
* Agent-based architectures
* Production-ready pipelines

---

## 🎯 Features

✔ Local quantized model (efficient & fast)
✔ `/generate` endpoint (single prompt)
✔ `/chat` endpoint (multi-turn conversation)
✔ Infinite chat memory support
✔ System + user prompt handling
✔ Sampling controls:

* temperature
* top-k
* top-p
  ✔ Streaming responses (optional)
  ✔ Request logging with unique request IDs
  ✔ Ready for RAG & agent integration

---

## 📁 Project Structure

```
/deploy
 ├── app.py              # FastAPI/Flask server
 ├── model_loader.py     # Model loading logic
 ├── config.py           # Configurations
 ├── utils.py            # Helpers (logging, ids)
 ├── logs/               # Request logs
 └── README.md
```

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone <repo-url>
cd deploy
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Server

```bash
uvicorn app:app --reload
```

Server runs at:

```
http://localhost:8000
```

---

## 🔌 API Endpoints

### 1. POST `/generate`

**Request:**

```json
{
  "prompt": "Explain LLMs",
  "temperature": 0.7,
  "top_k": 50,
  "top_p": 0.9
}
```

**Response:**

```json
{
  "request_id": "abc123",
  "output": "LLMs are..."
}
```

---

### 2. POST `/chat`

**Request:**

```json
{
  "messages": [
    {"role": "system", "content": "You are helpful"},
    {"role": "user", "content": "What is AI?"}
  ],
  "temperature": 0.7
}
```

**Response:**

```json
{
  "request_id": "xyz789",
  "reply": "AI stands for..."
}
```

---

## 🔄 Streaming (Optional)

Supports token streaming via:

* Server-Sent Events (SSE)
* WebSockets

---

## 🧠 Model Details

* Quantized model (GGUF / GPTQ / AWQ)
* Loaded via `model_loader.py`
* Cached in memory for performance

---

## ⚡ Performance Optimizations

* Model loaded once (singleton pattern)
* Token streaming reduces latency perception
* Efficient sampling controls
* Lightweight API layer

---

## 🔐 Logging

* Each request has a unique `request_id`
* Logs stored in `/logs`
* Tracks:

  * prompt
  * response
  * latency

---

## 🧪 Testing

* Test using Postman / curl
* Load testing recommended for production

---

## 🐳 Docker (Optional)

```bash
docker build -t local-llm .
docker run -p 8000:8000 local-llm
```

---

## 🧩 Future Improvements

* Redis caching
* Rate limiting
* Authentication (API keys)
* Multi-model routing
* GPU optimization

---

## 👨‍💻 Author

<your-name>

---
