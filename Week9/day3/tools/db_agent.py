import sqlite3
import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage

DB = "data/sales.db"

# -------------------------------
#  LLM CLIENT — lazy init
# -------------------------------
_model_client = None  # NOT initialized at import time


def get_model_client():
    """Initialize only when first called — after load_dotenv() has run."""
    global _model_client

    if _model_client is None:
        model_name = os.getenv("MODEL_NAME")
        api_key = os.getenv("OPENAI_API_KEY")

        if not model_name or not api_key:
            raise ValueError(
                "❌ MODEL_NAME or OPENAI_API_KEY not set. "
                "Make sure load_dotenv() is called before using db_agent."
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
#  CREATE TABLE FROM CSV
# -------------------------------
def create_table_from_csv(data):

    if not data:
        raise ValueError("CSV file is empty or not loaded correctly")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS sales")

    columns = data[0].keys()
    col_str = ", ".join([f'"{c}" TEXT' for c in columns])

    cur.execute(f"CREATE TABLE sales ({col_str})")

    for row in data:
        cur.execute(
            f"INSERT INTO sales VALUES ({','.join(['?'] * len(row))})",
            list(row.values())
        )

    conn.commit()
    conn.close()
    print(f"[DB] Table 'sales' created with {len(data)} rows.")


# -------------------------------
#  GET TABLE SCHEMA
# -------------------------------
def get_schema():

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("PRAGMA table_info(sales)")
    columns = [col[1] for col in cur.fetchall()]

    conn.close()
    return columns


# -------------------------------
#  NL → SQL (ASYNC)
# -------------------------------
async def nl_to_sql(user_query: str) -> str:

    columns = get_schema()
    schema = ", ".join(columns)

    prompt = f"""
You are an expert SQLite query generator.

Convert the user request into a valid SQLite SQL query.

Table name: sales
Columns: {schema}

Rules:
- Only generate SELECT queries
- Use correct column names
- Do not explain anything
- Do not add markdown or code fences
- Return ONLY the raw SQL query

User Request: {user_query}
"""

    client = get_model_client()  # ✅ lazy — safe after load_dotenv()

    response = await client.create(
        messages=[UserMessage(content=prompt, source="user")]
    )

    sql_query = response.content.strip()

    # ✅ Strip markdown fences if LLM ignores instructions
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

    return sql_query


# -------------------------------
#  RUN QUERY (ASYNC)
# -------------------------------
async def run_query(user_query: str):

    print(f"[USER QUERY]: {user_query}")

    sql_query = await nl_to_sql(user_query)

    print(f"[GENERATED SQL]: {sql_query}")

    # 🔐 Safety check — only SELECT allowed
    if not sql_query.lower().startswith("select"):
        return "❌ Only SELECT queries are allowed"

    try:
        conn = sqlite3.connect(DB)
        cur = conn.cursor()

        cur.execute(sql_query)
        rows = cur.fetchall()

        col_names = [desc[0] for desc in cur.description] if cur.description else []

        conn.close()

        if not rows:
            return "No results found."

        return {"columns": col_names, "rows": rows}

    except Exception as e:
        return f"DB Error: {e}"