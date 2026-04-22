from tools.code_executor import run_code_executor


async def run_code_agent(task: str):
    try:
        result = await run_code_executor(task)   
        return result
    except Exception as e:
        return f"Error: {e}"