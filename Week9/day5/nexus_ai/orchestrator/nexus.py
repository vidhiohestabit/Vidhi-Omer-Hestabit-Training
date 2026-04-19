import sys
import os

# -------------------------
# PATH FIX
# -------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.join(BASE_DIR, "day3"))
sys.path.append(os.path.join(BASE_DIR, "day4"))

# -------------------------
# IMPORTS
# -------------------------
import re
from datetime import datetime
from openai import OpenAI

# TOOLS
from tools.code_executor import execute_code
from tools.file_agent import write_txt, write_md

# MEMORY (your existing day4 files — untouched)
from memory.session_memory import SessionMemory
from memory.long_term import LongTermMemory

# CONFIG
from config import MODEL_NAME, API_KEY, BASE_URL


class NexusAI:

    def __init__(self):
        self.client = OpenAI(
            api_key=API_KEY,
            base_url=BASE_URL
        )

        self.session_memory = SessionMemory()
        self.long_term_memory = LongTermMemory()

    # -------------------------
    # MODEL CALL
    # -------------------------
    def call_model(self, prompt: str) -> str:
        try:
            resp = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )

            if not resp or not resp.choices:
                return "⚠️ No response from model"

            msg = resp.choices[0].message

            if msg and msg.content:
                return msg.content.strip()

            return f"(Fallback) {prompt[:100]}..."

        except Exception as e:
            return f"Error: {e}"

    # -------------------------
    # ROUTER
    # -------------------------
    def route(self, query: str):
        q = query.lower()

        # Personal memory questions — answered from memory, no model call needed
        personal_triggers = [
            "what is my name", "what's my name", "my name",
            "who am i", "do you know me", "do you remember me",
            "what do you know about me", "what is my age",
            "how old am i", "where am i from", "where do i live",
            "what is my job", "what do i do",
        ]
        if any(t in q for t in personal_triggers):
            return ["personal"]

        # Coding pipeline
        if any(w in q for w in ["write code", "write a function", "implement",
                                  "python script", "code for", "program to",
                                  "create a script", "generate code", "code"]):
            return ["researcher", "coder", "reporter"]

        # Planning pipeline
        if any(w in q for w in ["plan", "roadmap", "schedule", "startup",
                                  "strategy", "design a", "architect",
                                  "build a system", "steps to"]):
            return ["researcher", "optimizer", "reporter"]

        # Default — handles ALL general queries: "what is X", "explain X", "hello", anything
        return ["researcher", "reporter"]

    # -------------------------
    # PERSONAL QUERY HANDLER
    # -------------------------
    def handle_personal_query(self, query: str) -> str:
        """Answer user questions about themselves using stored long-term memory."""
        facts = self.long_term_memory.get_all_facts()

        if not facts:
            return (
                "I don't know anything about you yet!\n"
                "Tell me something like 'my name is ...' and I'll remember it."
            )

        q = query.lower()

        if any(w in q for w in ["name", "who am i", "called"]):
            name = facts.get("name")
            return f"Your name is **{name}**." if name else "I don't know your name yet. Tell me with 'my name is ...'"

        if any(w in q for w in ["age", "old"]):
            age = facts.get("age")
            return f"You are **{age}** years old." if age else "I don't know your age yet."

        if any(w in q for w in ["job", "work", "do"]):
            job = facts.get("job")
            return f"You work as a **{job}**." if job else "I don't know your job yet."

        if any(w in q for w in ["from", "live", "location"]):
            loc = facts.get("location")
            return f"You are from **{loc}**." if loc else "I don't know your location yet."

        # Dump everything known
        lines = "\n".join(f"  - **{k.title()}**: {v}" for k, v in facts.items())
        return f"Here's everything I know about you:\n{lines}"

    # -------------------------
    # AGENT PROMPTS
    # -------------------------
    def get_prompt(self, agent: str, query: str, pipeline_context: str) -> str:
        prompts = {
            "researcher": (
                f"You are a research agent. Answer the following clearly and thoroughly.\n\n"
                f"CONVERSATION CONTEXT:\n{pipeline_context}\n\n"
                f"USER QUERY: {query}\n\n"
                f"Provide well-structured, accurate information. "
                f"If the query is casual or conversational, respond naturally."
            ),

            "coder": (
                f"You are an expert Python developer.\n\n"
                f"TASK: {query}\n\n"
                f"BACKGROUND FROM RESEARCHER:\n{pipeline_context}\n\n"
                f"Instructions:\n"
                f"- Write COMPLETE, WORKING Python code\n"
                f"- Wrap ALL code in a single ```python ... ``` block\n"
                f"- Include a runnable example at the bottom\n"
                f"- Add clear inline comments\n"
                f"- Do NOT write any prose outside the code block"
            ),

            "optimizer": (
                f"You are a strategic planning agent.\n\n"
                f"ORIGINAL REQUEST: {query}\n\n"
                f"RESEARCH OUTPUT:\n{pipeline_context}\n\n"
                f"Restructure the above into a clear, step-by-step actionable plan "
                f"with milestones, priorities, and recommendations."
            ),

            "reporter": (
                f"You are the final reporting agent. Produce one clean, complete, final answer.\n\n"
                f"ORIGINAL USER REQUEST: {query}\n\n"
                f"CONTENT TO PRESENT:\n{pipeline_context}\n\n"
                f"Instructions:\n"
                f"- If code is present: keep it 100% intact, then add a plain-English explanation below it\n"
                f"- If no code: give a clear, well-structured answer\n"
                f"- Do NOT repeat yourself or add duplicate sections\n"
                f"- Be helpful, professional, and concise\n"
                f"- NEVER say 'I cannot answer' — always give the best response you can"
            ),
        }

        return prompts.get(agent, f"Answer this query helpfully:\n{query}")

    # -------------------------
    # RUN A SINGLE AGENT
    # -------------------------
    def run_agent(self, agent: str, query: str, pipeline_context: str) -> str:
        prompt = self.get_prompt(agent, query, pipeline_context)
        output = self.call_model(prompt)

        if not output or output.strip().lower() in ["", "none"]:
            return self.call_model(
                f"Context:\n{pipeline_context}\n\nAnswer this helpfully: {query}"
            )

        return output

    # -------------------------
    # SAVE CODE FILES
    # -------------------------
    def save_code_files(self, query: str, code_output: str, exec_output: str) -> tuple[str, str]:
        """Extract code block, save clean .py and full .md report."""

        code_match = re.search(r"```python(.*?)```", code_output, re.DOTALL)
        code = code_match.group(1).strip() if code_match else code_output.strip()

        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        py_file = f"outputs/code_{timestamp}.py"
        md_file = f"outputs/code_{timestamp}.md"

        # .py — clean code only
        write_txt(py_file, code)

        # .md — full report with properly closed code fences
        md_content = (
            "# Code Execution Report\n\n"
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"**Task:** {query}\n\n"
            "---\n\n"
            "## Generated Code\n\n"
            "```python\n"
            f"{code}\n"
            "```\n\n"
            "---\n\n"
            "## Execution Output\n\n"
            "```\n"
            f"{exec_output.strip() if exec_output and exec_output.strip() else 'No output captured.'}\n"
            "```\n\n"
            "---\n\n"
            "## Files\n\n"
            "| File | Purpose |\n"
            "|------|---------|\n"
            f"| `{py_file}` | Raw Python source |\n"
            f"| `{md_file}` | This report |\n"
        )

        write_md(md_file, md_content)
        return py_file, md_file

    # -------------------------
    # MAIN RUN
    # -------------------------
    def run(self, query: str) -> str:

        print("\n=== NEXUS AI ===\n")

        # Store user message in session memory
        # (your SessionMemory.add_message also auto-saves personal facts to long-term)
        self.session_memory.add_message("User", query)
        context = self.session_memory.get_context()

        # ROUTER
        print("[ROUTER]")
        agent_sequence = self.route(query)
        print("Pipeline:", " → ".join(agent_sequence))

        # -------------------------------------------------------
        # SHORT-CIRCUIT: personal memory query
        # -------------------------------------------------------
        if agent_sequence == ["personal"]:
            final_output = self.handle_personal_query(query)
            self.session_memory.add_message("Agent", final_output)
            print("\n=== FINAL OUTPUT ===")
            print("-" * 50)
            print(final_output)
            print("-" * 50)
            return final_output

        # -------------------------------------------------------
        # AGENT PIPELINE
        # -------------------------------------------------------
        # Seed with session context so every agent knows the user
        pipeline_context = f"Session context:\n{context}\n\nUser query:\n{query}"
        code_output = ""

        for agent in agent_sequence:
            print(f"\n[{agent.upper()}]")

            output = self.run_agent(agent, query, pipeline_context)

            if agent == "coder":
                code_output = output
                pipeline_context = output          # pass code to reporter

            elif agent == "reporter":
                pipeline_context = output          # reporter output = final answer, no labels

            else:
                pipeline_context = output

        # -------------------------------------------------------
        # CODE FILE SAVING (only if coder ran)
        # -------------------------------------------------------
        if "coder" in agent_sequence and code_output:
            print("\n[CODE PROCESSING]")

            exec_output = ""
            code_match = re.search(r"```python(.*?)```", code_output, re.DOTALL)
            if code_match:
                exec_output = execute_code(code_match.group(1).strip())

            py_file, md_file = self.save_code_files(query, code_output, exec_output)
            print(f"  ✅ Code saved  : {py_file}")
            print(f"  ✅ Report saved: {md_file}")

        # -------------------------------------------------------
        # FINAL SAFETY FALLBACK
        # -------------------------------------------------------
        final_output = pipeline_context

        if not final_output or str(final_output).strip().lower() in ["", "none"]:
            print("\n[FALLBACK TRIGGERED]")
            final_output = self.call_model(
                f"Context:\n{context}\n\nAnswer this helpfully: {query}"
            )

        # Store agent response in memory
        self.session_memory.add_message("Agent", final_output)

        # Print ONCE — do NOT print the return value in your entry point
        print("\n=== FINAL OUTPUT ===")
        print("-" * 50)
        print(final_output)
        print("-" * 50)

        return final_output