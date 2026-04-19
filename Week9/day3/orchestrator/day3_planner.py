import os
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from agents.code_agent import run_code_agent
from agents.file_agent import run_file_agent
from agents.db_agent import run_db_agent

from tools.file_agent import read_csv
from tools.db_agent import create_table_from_csv


def create_router():

    system_prompt = """
You are a Router Agent.

Classify user request into ONE category:

- code → Python execution, analysis, calculations
- file → reading/writing .txt or .csv
- db → SQL queries, analytics on structured data

Reply ONLY: code OR file OR db
"""

    model_client = OpenAIChatCompletionClient(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    temperature=0.0,
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

    return AssistantAgent(
        name="router",
        system_message=system_prompt,
        model_client=model_client,
    )


class Day3Planner:

    def __init__(self):
        self.router = create_router()

        print("[INIT] Loading CSV → SQLite...")
        data = read_csv("data/sales.csv")
        create_table_from_csv(data)
        print("[INIT] Ready.\n")

    async def route(self, user_message):

        response = await self.router.on_messages(
            [TextMessage(content=user_message, source="user")],
            cancellation_token=None,
        )

        decision = response.chat_message.content.strip().lower()
        print(f"[ROUTER]: {decision}")
        return decision

    async def chat(self, user_input):

        decision = await self.route(user_input)

        if decision == "code":
            await self.handle_code(user_input)

        elif decision == "file":
            await self.handle_file(user_input)

        elif decision == "db":
            await self.handle_db(user_input)

        else:
            print("❌ Could not classify request")

    async def handle_code(self, user_input):

        result = await run_code_agent(user_input)

        print("\n[CODE OUTPUT]\n")
        print(result)

    async def handle_file(self, user_input):

        result = await run_file_agent(user_input)

        print("\n[FILE OUTPUT]\n")
        print(result)

    async def handle_db(self, user_input):

        result = await run_db_agent(user_input)

        print("\n[DB OUTPUT]\n")
        print(result)