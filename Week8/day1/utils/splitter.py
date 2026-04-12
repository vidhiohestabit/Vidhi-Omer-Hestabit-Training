import json
from sklearn.model_selection import train_test_split

def split_dataset(path, train_ratio=0.9):
    data = []

    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))

    train, val = train_test_split(data, test_size=1-train_ratio, random_state=42)

    with open("data/processed/train.jsonl", "w") as f:
        for sample in train:
            f.write(json.dumps(sample) + "\n")

    with open("data/processed/val.jsonl", "w") as f:
        for sample in val:
            f.write(json.dumps(sample) + "\n")

    print(f"Train samples: {len(train)}")
    print(f"Validation samples: {len(val)}")