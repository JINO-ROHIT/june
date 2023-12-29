from abc import ABC, abstractmethod
from typing import Any
from pydantic import BaseModel
from tools import Tools, Calculator

class Sum(Calculator):
    a: float
    b: float
    
    @property
    def result(self) -> float:
        return self.a + self.b

class Product(Calculator):
    a: float
    b: float
    
    @property
    def result(self) -> float:
        return self.a * self.b

# s = Product(a = 3, b = 3)
# print(s.result)

class CalculatorTool(Tools):
    tool_name: str = "Calculator"
    tool_description: str = "A calculator to do addition and multiplcation operations. The function calls are Sum() and Product()"
    tool_input: str = "Return the operation as a function call. Example : Sum(a = 2, b = 2) "

    def execute(self, input_text: str) -> float:
        return eval(input_text).result

if __name__ == '__main__':
    calc_tool = CalculatorTool()
    result = calc_tool.execute("Product(a = 10, b = 3)")
    print(result)