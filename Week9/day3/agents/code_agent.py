from tools.code_executor import execute_code


async def run_code_agent(task: str):

    try:
        result = execute_code(task)
        return result
    except Exception as e:
        return f"Error: {e}"