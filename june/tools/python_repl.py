import sys
from io import StringIO
from typing import Any
from june.tools.schema import Tools

def PythonREPL(user_input):
    repl_locals = {}
    repl_globals = {}

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    try:
        exec(user_input, repl_globals, repl_locals)
    except Exception as e:
        return f"Error: {e}"

    sys.stdout = old_stdout
    output = mystdout.getvalue()

    return output

class PythonREPLTool(Tools):
    tool_name: str = "Python REPL"
    tool_description: str = "A python execution tool where you can execute valid python code."
    tool_input: str = "Return the python code that can be executed by a python shell."

    def execute(self, input_text: str) -> Any:
        return PythonREPL(input_text)

if __name__ == '__main__':
    repl_tool = PythonREPLTool()
    result = repl_tool.execute("print('hello')")
    print(result)



