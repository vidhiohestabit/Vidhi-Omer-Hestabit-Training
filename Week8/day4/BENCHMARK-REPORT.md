# DAY 4 — INFERENCE OPTIMISATION + BENCHMARKING

## Objective

To compare inference performance between base and quantized LLM models.

## Models Tested

* Base Model (TinyLlama - GPU)
* Quantized Model (GGUF via llama.cpp - CPU)

## Prompt Used

Explain AI in simple terms

## Results

| Model     | Tokens/sec | Latency  |
| --------- | ---------- | -------- |
| Base      | 29.22      | 3.42 sec |
| Quantized | 10.30      | 9.00 sec |

## Observations

* Base model is significantly faster due to GPU acceleration
* Quantized model runs on CPU with much lower memory usage (~700MB)
* GGUF models are slower but highly efficient for low-resource environments
* Latency for GGUF is approximate since llama.cpp provides tokens/sec directly

## Conclusion

Quantization enables running large language models on CPU with reduced memory usage. While performance (tokens/sec) decreases compared to GPU-based inference, GGUF models provide practical deployment options for systems without GPUs.
