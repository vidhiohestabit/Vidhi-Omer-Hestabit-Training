import json
import matplotlib.pyplot as plt
from transformers import AutoTokenizer

def analyze_tokens(path):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")

    lengths = []

    with open(path, "r") as f:
        for line in f:
            sample = json.loads(line)

            text = (
                sample["instruction"] +
                sample["input"] +
                sample["output"]
            )

            tokens = tokenizer.encode(text)
            lengths.append(len(tokens))

    print(f"Avg tokens: {sum(lengths)/len(lengths)}")
    print(f"Max tokens: {max(lengths)}")
    print(f"Min tokens: {min(lengths)}")

    # Plot
    plt.hist(lengths, bins=50)
    plt.title("Token Length Distribution")
    plt.xlabel("Tokens")
    plt.ylabel("Frequency")
    plt.savefig("token_distribution.png")

    print("📊 Token distribution saved as token_distribution.png")