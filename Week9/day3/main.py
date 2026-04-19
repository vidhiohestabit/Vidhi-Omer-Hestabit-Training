import os
import asyncio
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))
print("DEBUG KEY:", os.getenv("OPENAI_API_KEY"))
print("DEBUG MODEL:", os.getenv("MODEL_NAME"))

from orchestrator.day3_planner import Day3Planner


async def main():
    planner = Day3Planner()

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            break

        await planner.chat(user_input)


if __name__ == "__main__":
    asyncio.run(main())