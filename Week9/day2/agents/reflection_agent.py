from autogen_core.models import UserMessage


class ReflectionAgent:

    def __init__(self, model):
        self.model = model

    async def run(self, text, query):

        prompt = f"""
User Question: {query}

Combine the following into ONE correct answer.

Rules:
- MUST answer the user question
- Remove unrelated content
- Keep it simple
- Add example if needed

Content:
{text}
"""

        response = await self.model.create(
            messages=[UserMessage(content=prompt, source="user")]
        )

        return response.content.strip()