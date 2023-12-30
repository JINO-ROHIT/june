from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Any

class AbstractMethodNotImplementedError(Exception):
    pass

class Tools(BaseModel):
    tool_name: str
    tool_description: str
    tool_input: str

    @abstractmethod
    def execute(self, input_text: str) -> Any:
        raise AbstractMethodNotImplementedError("Abstract method must be implemented in the subclass")