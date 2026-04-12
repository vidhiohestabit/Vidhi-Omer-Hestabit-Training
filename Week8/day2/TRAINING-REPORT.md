# 🧠 QLoRA Fine-Tuning Report

## 📌 Project: Parameter-Efficient Fine-Tuning (QLoRA)

This project demonstrates efficient fine-tuning of a Large Language Model (LLM) using QLoRA (Quantized Low-Rank Adaptation). The goal is to reduce memory usage while maintaining performance by training only a small fraction of parameters.

---

## 🚀 Objectives

* Fine-tune an LLM using QLoRA
* Reduce memory usage with 4-bit quantization
* Train only ~1% parameters
* Save adapter weights instead of full model
* Optimize training loss

---

## 🧩 Dataset Preparation

The dataset was converted into chat format using a custom script.

### 🔧 format_dataset.py

* Input: JSONL with instruction, input, output
* Output: Chat-style JSONL with messages format

Example format:

```
{
  "messages": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

✔ Ensures compatibility with chat-based LLMs
✔ Structured for supervised fine-tuning

---

## ⚙️ Training Configuration

| Parameter     | Value             |
| ------------- | ----------------- |
| Method        | QLoRA             |
| Rank (r)      | 16                |
| Learning Rate | 2e-4              |
| Batch Size    | 4                 |
| Epochs        | 3                 |
| Quantization  | 4-bit             |
| Precision     | Mixed (FP16/BF16) |
| Optimizer     | AdamW             |

---

## 🧠 Key Techniques Used

### 🔹 QLoRA

* Combines LoRA with 4-bit quantization
* Reduces GPU memory usage drastically
* Enables training on low-resource systems

### 🔹 PEFT (Parameter Efficient Fine-Tuning)

* Only small adapter matrices are trained
* Base model remains frozen

### 🔹 BitsAndBytes

* Loads model in 4-bit precision
* Significantly reduces VRAM usage

### 🔹 Gradient Checkpointing

* Saves memory by recomputing activations
* Useful for large models

### 🔹 Mixed Precision

* Faster computation
* Lower memory consumption

---

## 📊 Training Results

* Trainable Parameters: ~1% of total model
* Memory Efficient Training achieved using 4-bit loading
* Loss decreased consistently across epochs
* Training remained stable

---

## 💾 Outputs

| File                        | Description             |
| --------------------------- | ----------------------- |
| /notebooks/lora_train.ipynb | Training notebook       |
| /adapters/adapter_model.bin | Trained adapter weights |
| /TRAINING-REPORT.md         | This report             |

---

## 📈 Observations

* QLoRA enables fine-tuning of large models on limited hardware
* Training only adapters reduces compute requirements
* Performance improves steadily without heavy resource usage
* Suitable for real-world GenAI applications

---

## ⚠️ Challenges Faced

* Initial setup issues with quantization libraries
* GPU memory constraints
* Hyperparameter tuning required for stability

---

## 🏁 Conclusion

QLoRA is an effective and efficient approach for LLM fine-tuning. By combining parameter-efficient training with quantization, it achieves:

* Faster training
* Lower memory usage
* Scalable deployment

This makes it highly suitable for production-level AI systems.

---

