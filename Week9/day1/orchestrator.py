from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.answer_agent import AnswerAgent

class Orchestrator:
    def __init__(self):
        self.research = ResearchAgent()
        self.summarizer = SummarizerAgent()
        self.answer = AnswerAgent()

    def run(self, user_query):
        print("\n🔎 Research Agent running...")
        research_output = self.research.run(user_query)

        print("\n🧠 Summarizer Agent running...")
        summary = self.summarizer.run(research_output)

        print("\n🎯 Answer Agent running...")
        final_answer = self.answer.run(summary)

        return final_answer