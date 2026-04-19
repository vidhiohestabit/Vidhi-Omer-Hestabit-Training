import os
import asyncio

from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

from agents.worker_agent import WorkerAgent
from agents.reflection_agent import ReflectionAgent
from agents.validator import ValidatorAgent


class Planner:

    def __init__(self):

        self.model = OpenAIChatCompletionClient(
            model=os.getenv("MODEL_NAME"),
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
            temperature=0.3,
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

        self.worker = WorkerAgent(self.model)
        self.reflection = ReflectionAgent(self.model)
        self.validator = ValidatorAgent(self.model)

    # -------------------------
    # Step 1: Create Plan
    # -------------------------
    async def create_plan(self, query):

        prompt = f"""
Break this user query into 2-4 clear steps.

User Query: {query}

Return ONLY steps like:
Step 1: ...
Step 2: ...
"""

        response = await self.model.create(
            messages=[UserMessage(content=prompt, source="user")]
        )

        steps = response.content.strip().split("\n")
        return [s for s in steps if s.strip()]

    # -------------------------
    # Step 2: Execute Workers
    # -------------------------
    async def execute_workers(self, steps, query):

        tasks = []

        for step in steps:
            # ✅ PASS query ALSO
            tasks.append(self.worker.run(step, query))

        results = await asyncio.gather(*tasks)
        return results

    # -------------------------
    # MAIN PIPELINE
    # -------------------------
    async def run(self, query):

        print("\n[PLANNER] Creating plan...\n")

        steps = await self.create_plan(query)

        for s in steps:
            print(f"→ {s}")

        print("\n[WORKERS] Executing in parallel...\n")

        worker_outputs = await self.execute_workers(steps, query)

        combined = "\n".join(worker_outputs)

        print("\n[REFLECTION] Improving answer...\n")

        improved = await self.reflection.run(combined, query)

        print("\n[VALIDATOR] Checking answer...\n")

        final = await self.validator.run(improved, query)

        return final