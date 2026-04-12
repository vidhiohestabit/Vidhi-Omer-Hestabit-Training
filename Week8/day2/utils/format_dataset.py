import json
import os

INPUT_PATH = "../day1/data/processed/train.jsonl"
OUTPUT_PATH = "data/chat_train.jsonl"

os.makedirs("data", exist_ok=True)

with open(INPUT_PATH, "r") as f_in, open(OUTPUT_PATH, "w") as f_out:
    for line in f_in:
        sample = json.loads(line)

        chat = {
            "messages": [
                {
                    "role": "user",
                    "content": sample["instruction"] + " " + sample["input"]
                },
                {
                    "role": "assistant",
                    "content": sample["output"]
                }
            ]
        }

        f_out.write(json.dumps(chat) + "\n")

print("✅ Dataset ready")