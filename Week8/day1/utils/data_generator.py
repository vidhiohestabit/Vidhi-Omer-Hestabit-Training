import json
import random
from tqdm import tqdm

def generate_qa():
    questions = [
        "What is Python?",
        "Explain REST API",
        "What is a database index?",
        "Define machine learning",
        "What is recursion?"
    ]
    q = random.choice(questions)
    return {
        "instruction": "Answer the question",
        "input": q,
        "output": f"This is a detailed answer about {q.lower()}."
    }

def generate_reasoning():
    problems = [
        "Write a function to reverse a string",
        "Find factorial of a number",
        "Check palindrome",
        "Sort a list",
        "Find prime numbers"
    ]
    p = random.choice(problems)
    return {
        "instruction": "Solve step-by-step",
        "input": p,
        "output": f"Step 1: Understand problem\nStep 2: Approach\nStep 3: Code for {p.lower()}"
    }

def generate_extraction():
    texts = [
        "John works at Google as a software engineer",
        "Alice joined Microsoft in 2020",
        "Bob is a data scientist at Amazon"
    ]
    t = random.choice(texts)
    return {
        "instruction": "Extract structured data",
        "input": t,
        "output": '{"name": "...", "company": "...", "role": "..."}'
    }

def generate_dataset(path, num_samples=1000):
    generators = [generate_qa, generate_reasoning, generate_extraction]

    with open(path, "w") as f:
        for _ in tqdm(range(num_samples)):
            sample = random.choice(generators)()
            f.write(json.dumps(sample) + "\n")

    print(f"Dataset saved to {path}")