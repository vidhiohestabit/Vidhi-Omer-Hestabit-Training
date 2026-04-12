from day1.utils.data_generator import generate_dataset
from day1.utils.data_cleaner import clean_dataset
from day1.utils.tokenizer_analysis import analyze_tokens
from day1.utils.splitter import split_dataset

RAW_PATH = "data/raw/generated_dataset.jsonl"
CLEAN_PATH = "data/raw/cleaned_dataset.jsonl"

def run_pipeline():
    print("Step 1: Generating dataset...")
    generate_dataset(RAW_PATH, num_samples=1200)

    print("Step 2: Cleaning dataset...")
    clean_dataset(RAW_PATH, CLEAN_PATH)

    print("Step 3: Token analysis...")
    analyze_tokens(CLEAN_PATH)

    print("Step 4: Splitting dataset...")
    split_dataset(CLEAN_PATH)

    print("✅ Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()