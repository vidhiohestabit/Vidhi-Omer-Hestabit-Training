from autogen_core.models import UserMessage

class ValidatorAgent:

    def __init__(self, model):
        self.model = model

    async def run(self, answer, query):   # FIXED (added query)

        prompt = f"""
You are a validator.

User Query: {query}

Answer:
{answer}

Check:
- Is it correct?
- Is it relevant?

If correct → return final clean answer
If wrong → fix and return improved answer
"""

        response = await self.model.create(
            messages=[UserMessage(content=prompt, source="user")]
        )

        return response.content.strip()