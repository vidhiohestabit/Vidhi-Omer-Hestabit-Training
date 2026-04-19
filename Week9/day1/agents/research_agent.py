from agents.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Research Agent",
            system_prompt="""
You are a Research Agent.

TASK:
- Collect factual information only
- Do NOT summarize
- Do NOT answer final question
- Provide detailed raw explanation
"""
        )