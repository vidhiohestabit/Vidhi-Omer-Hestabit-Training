import os
import asyncio
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

from memory.session_memory import SessionMemory
from memory.vector_store import VectorStore
from memory.long_term import LongTermMemory

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))
print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))
print("DEBUG MODEL:", os.getenv("MODEL_NAME"))

class MemoryAgentSystem:

    def __init__(self):

        self.session_memory = SessionMemory()
        self.vector_store = VectorStore()
        self.long_term_memory = LongTermMemory()

        self.model_client = OpenAIChatCompletionClient(
            model=os.getenv("MODEL_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
            temperature=0.4,
            model_info={
                "provider": "groq",
                "family": "llama",
                "context_length": 8192,
                "vision": False,
                "function_calling": False,
                "json_output": False,
                "structured_output": False,
            },
        
        )

    # -------------------------
    # LLM decides memory importance
    # -------------------------
    async def should_store_in_long_term(self, user_query, answer):

        prompt = f"""
Decide if this contains important personal info (name, preferences, facts).

User: {user_query}
Assistant: {answer}

Reply only: yes or no
"""

        try:
            response = await self.model_client.create(
                messages=[UserMessage(content=prompt, source="user")]
            )
            return "yes" in response.content.lower()
        except:
            return False

    # -------------------------
    # MAIN RESPONSE FUNCTION
    # -------------------------
    async def generate_response(self, user_query):

        self.session_memory.add_message("User", user_query)

        # Vector memory
        similar = self.vector_store.search(user_query)
        vector_context = "\n".join(similar) if similar else ""

        # Session memory
        session_context = self.session_memory.get_context()

        # Long term memory
        past = self.long_term_memory.retrieve_all()
        long_term_context = "\n".join(past[-5:]) if past else ""

        # CLEAN PROMPT
        prompt = f"""
You are a helpful conversational AI.

Use memory naturally if relevant.

Conversation:
{session_context}

Known user facts:
{long_term_context}

Similar past:
{vector_context}

User: {user_query}
Assistant:
"""

        try:
            response = await self.model_client.create(
                messages=[UserMessage(content=prompt, source="user")]
            )

            answer = response.content.strip()

        except Exception as e:
            return f"Error: {e}"

        # Update memory
        self.session_memory.add_message("Agent", answer)
        self.vector_store.add(user_query)

        # LLM decides long-term memory
        if await self.should_store_in_long_term(user_query, answer):
            self.long_term_memory.store(user_query)
            print("[Memory Stored]")

        return answer


# -------------------------
# CLI
# -------------------------
async def main():
    system = MemoryAgentSystem()

    print("\n=== Memory Agent System ===\n")

    while True:
        user = input("User: ")

        if user.lower() == "exit":
            break

        response = await system.generate_response(user)

        print(f"\nAgent: {response}\n")


if __name__ == "__main__":
    asyncio.run(main())