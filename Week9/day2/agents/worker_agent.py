from autogen_core.models import UserMessage
class WorkerAgent:

    def __init__(self, model):
        self.model = model

    async def run(self, task, query):

        prompt = f"""
User Question: {query}

Your Task: {task}

Rules:
- Stay strictly relevant to the user question
- Do NOT introduce unrelated topics
- Keep it short and useful

Answer:
"""

        response = await self.model.create(
            messages=[UserMessage(content=prompt, source="user")]
        )

        return response.content.strip()