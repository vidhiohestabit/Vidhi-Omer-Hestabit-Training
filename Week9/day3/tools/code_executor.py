import io
import os
import contextlib
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage


# -------------------------------
#  LLM CLIENT — lazy init (fixes import-time crash)
# -------------------------------
_model_client = None  


def get_model_client():
    """Initialize model client only when first needed — after .env is loaded."""
    global _model_client

    if _model_client is None:
        model_name = os.getenv("MODEL_NAME")
        api_key = os.getenv("OPENAI_API_KEY")

        if not model_name or not api_key:
            raise ValueError(
                "❌ MODEL_NAME or OPENAI_API_KEY not set. "
                "Make sure load_dotenv() is called before using code_executor."
            )

        _model_client = OpenAIChatCompletionClient(
            model=model_name,
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
            temperature=0.0,
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

    return _model_client


# -------------------------------
# 🔹 NL → PYTHON CODE (ASYNC)
# -------------------------------
async def nl_to_code(user_query: str) -> str:

    client = get_model_client()  
    prompt = f"""
You are an expert Python code generator.

Convert the user request into a valid Python code snippet.

Rules:
- Only use Python standard library (no pandas, numpy, matplotlib)
- Always use print() to show the output
- Do not explain anything
- Do not add markdown or code fences
- Return ONLY raw executable Python code

User Request: {user_query}
"""

    response = await client.create(
        messages=[UserMessage(content=prompt, source="user")]
    )

    code = response.content.strip()

    # Strip markdown fences if LLM ignores instructions
    code = code.replace("```python", "").replace("```", "").strip()

    return code


# -------------------------------
#  EXECUTE PYTHON CODE (SYNC)
# -------------------------------
def execute_code(code: str) -> str:
    """Directly execute a raw Python code string. Used by nexus.py."""

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        result = output.getvalue()
        return result if result else "✅ Code executed successfully (no output)"

    except Exception as e:
        return f"Execution Error: {e}"


# -------------------------------
#  MAIN ENTRY — NL → CODE → EXECUTE (ASYNC)
# -------------------------------
async def run_code_executor(user_query: str) -> str:
    """Full pipeline: natural language → generate code → execute it."""

    print(f"[USER QUERY]: {user_query}")

    # Step 1: NL → Python code via LLM
    code = await nl_to_code(user_query)
    print(f"[GENERATED CODE]:\n{code}\n")

    # Step 2: Execute the generated code
    result = execute_code(code)
    print(f"[EXECUTION RESULT]: {result}")

    return result