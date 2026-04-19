from tools.file_agent import read_csv, write_csv, read_txt, write_txt


async def run_file_agent(task: str):

    task = task.lower()

    if "read" in task and ".csv" in task:
        return read_csv("data/sales.csv")[:5]

    if "read" in task and ".txt" in task:
        return read_txt("data/sample.txt")

    if "write" in task:
        write_txt("data/output.txt", "Hello from agent")
        return "File written successfully"

    return "File task not understood"