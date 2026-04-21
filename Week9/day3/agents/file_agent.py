import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from tools.file_agent import read_csv, write_csv, read_txt, write_txt

# -------------------------------
# 🔹 LLM CLIENT — lazy init
# -------------------------------
_model_client = None

def get_model_client():
    global _model_client
    if _model_client is None:
        model_name = os.getenv("MODEL_NAME")
        api_key = os.getenv("OPENAI_API_KEY")

        if not model_name or not api_key:
            raise ValueError("❌ MODEL_NAME or OPENAI_API_KEY not set.")

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
# 🔹 NL → FILE INTENT (ASYNC)
# -------------------------------
async def nl_to_file_intent(user_query: str) -> dict:
    """Use LLM to understand what file operation the user wants."""

    prompt = f"""
You are a file operation classifier.

Classify the user request into a JSON object with these fields:
- "action": one of "read_csv", "read_txt", "write_csv", "write_txt"
- "filename": the file mentioned (default to "sales.csv" if CSV, "sample.txt" if TXT)
- "content": content to write (only if action is write, else null)

Rules:
- Return ONLY valid JSON, no explanation, no markdown
- If user says "give me data", "show csv", "display file", "get csv" → action = "read_csv"
- If user says "show txt", "read text file" → action = "read_txt"
- If user says "write" or "save" → action = "write_txt" or "write_csv"
- Default file is "sales.csv" unless user mentions .txt

User Request: {user_query}

JSON:
"""

    client = get_model_client()
    response = await client.create(
        messages=[UserMessage(content=prompt, source="user")]
    )

    raw = response.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    import json
    try:
        return json.loads(raw)
    except Exception:
        # ✅ Safe fallback — if JSON parse fails, default to read_csv
        return {"action": "read_csv", "filename": "sales.csv", "content": None}


# -------------------------------
# 🔹 MAIN FILE AGENT (ASYNC)
# -------------------------------
async def run_file_agent(task: str):

    print(f"[FILE AGENT] Task: {task}")

    intent = await nl_to_file_intent(task)
    action = intent.get("action", "read_csv")
    filename = intent.get("filename", "sales.csv")
    content = intent.get("content", None)

    print(f"[FILE AGENT] Intent → action={action}, file={filename}")

    # ✅ Build correct path
    filepath = f"data/{filename}"

    if action == "read_csv":
        try:
            data = read_csv(filepath)
            return data
        except FileNotFoundError:
            return f"❌ File not found: {filepath}"

    elif action == "read_txt":
        try:
            return read_txt(filepath)
        except FileNotFoundError:
            return f"❌ File not found: {filepath}"

    elif action == "write_txt":
        write_txt(filepath, content or "Hello from agent")
        return f"✅ Written to {filepath}"

    elif action == "write_csv":
        write_csv(filepath, content or [])
        return f"✅ CSV written to {filepath}"

    else:
        return f"❌ Unknown file action: {action}"