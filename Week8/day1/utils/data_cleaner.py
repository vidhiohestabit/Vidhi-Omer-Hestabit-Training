import json

def is_valid(sample):
    return (
        isinstance(sample, dict) and
        "instruction" in sample and
        "input" in sample and
        "output" in sample and
        len(sample["instruction"]) > 3 and
        len(sample["output"]) > 3
    )

def clean_dataset(input_path, output_path):
    cleaned = []

    with open(input_path, "r") as f:
        for i, line in enumerate(f):
            try:
                sample = json.loads(line)

                if is_valid(sample):
                    cleaned.append(sample)
                else:
                    print(f"⚠️ Invalid sample at line {i}")

            except:
                print(f"⚠️ Skipping invalid JSON at line {i}")

    with open(output_path, "w") as f:
        for sample in cleaned:
            f.write(json.dumps(sample) + "\n")

    print(f"✅ Cleaned dataset saved: {output_path}")
    print(f"Total valid samples: {len(cleaned)}")