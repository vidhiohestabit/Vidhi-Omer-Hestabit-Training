# DAY 3 — QUANTISATION (8-bit → 4-bit → GGUF)

## 📌 Overview

This project demonstrates post-training quantisation of a fine-tuned LLM using multiple techniques:

* 8-bit quantisation (INT8)
* 4-bit quantisation (INT4 - NF4)
* GGUF conversion + q4_0 quantisation using llama.cpp

The base model used:
**TinyLlama-1.1B-Chat-v1.0 (with LoRA merged weights)**

---

## 🎯 Learning Objectives

* Understand why quantisation is required for LLMs
* Compare memory vs performance trade-offs
* Learn practical implementation of:

  * BitsAndBytes quantisation
  * GGUF conversion
  * llama.cpp inference

---

## 🧠 Key Concepts

### 🔹 What is Quantisation?

Quantisation reduces model size by lowering numerical precision of weights.

| Format | Precision | Memory | Speed      | Quality       |
| ------ | --------- | ------ | ---------- | ------------- |
| FP16   | 16-bit    | High   | Medium     | Best          |
| INT8   | 8-bit     | Medium | Faster     | Slight loss   |
| INT4   | 4-bit     | Low    | Fastest    | Moderate loss |
| GGUF   | Optimized | Lowest | Fast (CPU) | Depends       |

---

### 🔹 Types of Quantisation

#### 1. Post-Training Quantisation (PTQ)

* Applied after training
* No retraining required

#### 2. Static vs Dynamic

* Static: Pre-calibrated ranges
* Dynamic: Computed during inference

---

## ⚙️ Implementation Steps

---

## 🔹 Step 1 — Merge LoRA into Base Model

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("/content/base_model")

model = PeftModel.from_pretrained(model, "/content/adapters")
model = model.merge_and_unload()

model.save_pretrained("/content/merged_model")
```

Output directory:

```
/content/merged_model
```

---

## 🔹 Step 2 — INT8 Quantisation

```python
from transformers import BitsAndBytesConfig, AutoModelForCausalLM

bnb8 = BitsAndBytesConfig(load_in_8bit=True)

model8 = AutoModelForCausalLM.from_pretrained(
    "/content/merged_model",
    quantization_config=bnb8,
    device_map="auto"
)

model8.save_pretrained("/content/quantized/model-int8")
```

Saved at:

```
/content/quantized/model-int8
```

---

## 🔹 Step 3 — INT4 Quantisation (NF4)

```python
import torch
from transformers import BitsAndBytesConfig, AutoModelForCausalLM

bnb4 = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4"
)

model4 = AutoModelForCausalLM.from_pretrained(
    "/content/merged_model",
    quantization_config=bnb4,
    device_map="auto"
)

model4.save_pretrained("/content/quantized/model-int4")
```

Saved at:

```
/content/quantized/model-int4
```

---

## 🔹 Step 4 — GGUF Conversion

### Convert HF → GGUF

```bash
python3 /content/llama.cpp/convert_hf_to_gguf.py \
/content/merged_model \
--outfile /content/quantized/model.gguf \
--outtype f16
```

---

### Quantise GGUF → q4_0

```bash
/content/llama.cpp/build/bin/llama-quantize \
/content/quantized/model.gguf \
/content/quantized/model-q4.gguf \
q4_0
```

Saved at:

```
/content/quantized/model-q4.gguf
```

---

## 🔹 Step 5 — Inference using llama.cpp

```bash
/content/llama.cpp/build/bin/llama-cli \
-m /content/quantized/model-q4.gguf \
-p "Explain random choice in Python"
```

---

## 📊 Results

### 🔹 Model Size Comparison

| Format      | Approx Size |
| ----------- | ----------- |
| FP16        | ~2.2 GB     |
| INT8        | ~1.1 GB     |
| INT4        | ~0.6 GB     |
| GGUF (q4_0) | ~0.5 GB     |

---

### 🔹 Performance Comparison

| Format | Speed           | Memory Usage | Quality |
| ------ | --------------- | ------------ | ------- |
| FP16   | Slow            | High         | ⭐⭐⭐⭐⭐   |
| INT8   | Medium          | Medium       | ⭐⭐⭐⭐    |
| INT4   | Fast            | Low          | ⭐⭐⭐     |
| GGUF   | Very Fast (CPU) | Very Low     | ⭐⭐⭐     |

---

## 📁 Deliverables

```
quantized/
├── model-int8/
├── model-int4/
├── model.gguf
├── model-q4.gguf
```

---

## ⚖️ Observations

### ✅ INT8

* Good balance between size and accuracy
* Works efficiently on GPUs

### ✅ INT4 (NF4)

* Huge memory reduction
* Slight drop in response quality
* Best for low VRAM environments

### ✅ GGUF (q4_0)

* Designed for CPU inference
* Very fast and lightweight
* Ideal for local deployment

---

## 🚀 Key Takeaways

* Quantisation reduces model size drastically
* Enables running LLMs on limited hardware
* Trade-off exists:

  * Memory ↓
  * Speed ↑
  * Accuracy ↓

---

## 🔮 Future Improvements

* Try q8_0 GGUF for better accuracy
* Benchmark tokens/sec speed
* Compare real prompt outputs
* Deploy via local chatbot UI

---

## ✅ Conclusion

This project successfully demonstrates:

* End-to-end quantisation pipeline
* Model compression techniques
* Deployment using llama.cpp

Quantisation is essential for efficient and scalable LLM deployment 🚀
