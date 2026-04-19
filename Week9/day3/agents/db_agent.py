from tools.db_agent import run_query


async def run_db_agent(task: str):

    try:
        result = run_query(task)
        return result
    except Exception as e:
        return f"DB Error: {e}"