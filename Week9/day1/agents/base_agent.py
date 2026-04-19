import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))
print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))
print("DEBUG MODEL:", os.getenv("MODEL_NAME"))

class BaseAgent:
    def __init__(self, role, system_prompt):
        self.role = role
        self.system_prompt = system_prompt
        self.memory = []

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("BASE_URL")
        )

        self.model = os.getenv("MODEL_NAME")
        self.max_tokens = int(os.getenv("MAX_TOKENS", 200))
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))

    def add_to_memory(self, msg):
        self.memory.append(msg)
        if len(self.memory) > 10:
            self.memory.pop(0)

    def run(self, user_input):
        # only pass current input (IMPORTANT FIX)
        self.add_to_memory(f"User: {user_input}")

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        output = response.choices[0].message.content

        # SAFETY CHECK (prevents blank output issues)
        if not output or output.strip() == "":
            output = f"[{self.role}] No response generated."

        self.add_to_memory(f"{self.role}: {output}")
        return output