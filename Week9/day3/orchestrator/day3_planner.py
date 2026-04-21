import os
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

from agents.code_agent import run_code_agent
from agents.file_agent import run_file_agent
from agents.db_agent import run_db_agent

from tools.file_agent import read_csv
from tools.db_agent import create_table_from_csv


def make_model_client():
    return OpenAIChatCompletionClient(
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


def create_router():
    system_prompt = """
You are a Router Agent.

Classify the user request into ONE or MORE categories:

- code  → Python execution, calculations, statistics
- file  → reading/writing .txt or .csv files
- db    → SQL queries, analytics on structured data
- combined → requires file + db + code together (e.g., "analyze sales.csv and give insights")

Reply ONLY with one of: code | file | db | combined
"""
    return AssistantAgent(
        name="router",
        system_message=system_prompt,
        model_client=make_model_client(),
    )


def create_analyst():
    system_prompt = """
You are a Senior Data Analyst Agent.

You will receive raw outputs from multiple agents (file reader, database queries, code execution).
Synthesize them into a clear, structured final answer with insights, bullet points, and a summary.
"""
    return AssistantAgent(
        name="analyst",
        system_message=system_prompt,
        model_client=make_model_client(),
    )


class Day3Planner:

    def __init__(self):
        self.router = create_router()
        self.analyst = create_analyst()

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
        print(f"[ROUTER] → {decision}")
        return decision

    async def chat(self, user_input):
        decision = await self.route(user_input)

        if decision == "code":
            await self.handle_code(user_input)

        elif decision == "file":
            await self.handle_file(user_input)

        elif decision == "db":
            await self.handle_db(user_input)

        elif decision == "combined":
            await self.handle_combined(user_input)

        else:
            print("❌ Could not classify request.")

    # ── Individual handlers ──────────────────────────────────────

    async def handle_code(self, user_input):
        result = await run_code_agent(user_input)
        print("\n[CODE OUTPUT]\n", result)

    async def handle_file(self, user_input):
        result = await run_file_agent(user_input)
        print("\n[FILE OUTPUT]\n", result)

    async def handle_db(self, user_input):
        result = await run_db_agent(user_input)
        print("\n[DB OUTPUT]\n", result)

    # ── Combined multi-agent handler ─────────────────────────────

    async def handle_combined(self, user_input):
        """
        Runs File + DB + Code agents in parallel (conceptually),
        then passes all results to an Analyst Agent for synthesis.
        """
        print("\n[COMBINED] Running all agents...\n")

        # Step 1: File Agent — load raw CSV data
        file_result = await run_file_agent("read sales.csv")
        print(f"[FILE AGENT] ✅ Got {len(file_result)} rows")

        # Step 2: DB Agent — run analytics query
        db_result = await run_db_agent(user_input)
        print(f"[DB AGENT] ✅ Query complete")

        # Step 3: Code Agent — compute stats
        code_task = f"""
import csv

data = {file_result}

# Basic stats
if data:
    try:
        amounts = [float(row.get('amount', row.get('sales', row.get('revenue', 0)))) for row in data]
        print(f"Total rows: {{len(amounts)}}")
        print(f"Total revenue: {{sum(amounts):.2f}}")
        print(f"Average: {{sum(amounts)/len(amounts):.2f}}")
        print(f"Max: {{max(amounts):.2f}}")
        print(f"Min: {{min(amounts):.2f}}")
    except Exception as e:
        print(f"Stats error: {{e}}")
"""
        code_result = await run_code_agent(code_task)
        print(f"[CODE AGENT] ✅ Stats computed")

        # Step 4: Analyst Agent synthesizes everything
        synthesis_prompt = f"""
User asked: "{user_input}"

Here are results from 3 agents:

=== FILE AGENT (raw CSV sample) ===
{str(file_result[:5])}

=== DB AGENT (query results) ===
{str(db_result)}

=== CODE AGENT (statistics) ===
{code_result}

Please synthesize these into the top 5 insights with a brief summary.
"""

        analysis = await self.analyst.on_messages(
            [TextMessage(content=synthesis_prompt, source="user")],
            cancellation_token=None,
        )

        print("\n" + "="*60)
        print("📊 FINAL COMBINED ANALYSIS")
        print("="*60)
        print(analysis.chat_message.content)
        print("="*60 + "\n")