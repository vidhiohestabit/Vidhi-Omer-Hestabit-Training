import io
import contextlib


def execute_code(code: str):

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        return output.getvalue()

    except Exception as e:
        return f"Execution Error: {e}"