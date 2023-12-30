from june import Tools, Agent

class Sum:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    @property
    def result(self) -> float:
        return self.a + self.b

class Product:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    @property
    def result(self) -> float:
        return self.a * self.b

class CalculatorTool(Tools):
    tool_name: str = "Calculator"
    tool_description: str = "A calculator to do addition and multiplcation operations. The function calls are Sum() and Product()"
    tool_input: str = "Only return the function call for the given inputs. Example : Sum(a = 2, b = 2) "

    def execute(self, input_text: str) -> float:
        return eval(input_text).result

agent = Agent()
agent.register([CalculatorTool()])
#print(agent.tool_help)
agent.engine(model_name = "meta-llama/Llama-2-7b-chat-hf")
agent.solve(question = "what is 20 * 10")