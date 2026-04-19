from agents.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Summarizer Agent",
            system_prompt="""
You are a Summarizer Agent.

TASK:
- Convert input into short structured summary
- Remove unnecessary details
- Keep meaning intact
"""
        )