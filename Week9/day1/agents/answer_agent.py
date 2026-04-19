from agents.base_agent import BaseAgent

class AnswerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Answer Agent",
            system_prompt="""
You are an Answer Agent.

TASK:
- Give final user-ready answer
- Make it clear and structured
- Add simple explanation if needed
"""
        )