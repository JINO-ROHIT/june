from june.tools.schema import Tools

class Sum:
    a: float
    b: float
    
    @property
    def result(self) -> float:
        return self.a + self.b

class Product:
    a: float
    b: float
    
    @property
    def result(self) -> float:
        return self.a * self.b

class CalculatorTool(Tools):
    tool_name: str = "Calculator"
    tool_description: str = "A calculator to do addition and multiplcation operations. The function calls are Sum() and Product()"
    tool_input: str = "Return the operation as a function call. Example : Sum(a = 2, b = 2) "

    def execute(self, input_text: str) -> float:
        return eval(input_text).result