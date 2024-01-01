# June 
### A LLM Agent 🤖

## Overview
June is a Language Model (LLM) Agent designed to execute actions using custom tools. Using a LLM as the central brain to make decisions, june leverages its power with the tools it has access to make the final decision.

## Installation[package publish in progress]

You can run the examples 
```bash
python -m examples.calc
```

## Features
- Model Compatibility: June supports loading various Hugging Face models seamlessly. Users can specify the LLM's name when calling the agent, providing flexibility and the ability to leverage different models based on their needs.
- Custom Tools: Users can extend June's functionality by creating custom tools inheriting from the Tool base class, allowing for easy integration and expansion of the agent's capabilities.
- Strong data validation: June leverages Pydantic for data validation and configuration. Pydantic allows for easy definition of data models and automatic validation, making it a powerful tool for handling input data and configurations.

## Usage

### Define custom functions and tools

Define a custom tool by inheriting from the Tools class with a **tool_name, tool_description and tool_input**. Overide the **execute()** method to perform the type of action.

```python
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
```

### Agent Execution

1. Instantiate the agent.
2. Register your custom tool/tools.
3. You can use the **tool_help** property to check the tool details.
4. Define the LLM model by pasing the model name.
5. Invoke the **solve()** method with your task.

```python
agent = Agent()
agent.register([CalculatorTool()])
#print(agent.tool_help)
agent.engine(model_name = "meta-llama/Llama-2-7b-chat-hf")
agent.solve(question = "what is 20 * 10")
```

Example Output:

```
prompt:
{
    'role': 'user', 
    'content': 'You are an intelligent AI agent that can understand what the user is asking for by making use of the tools available to you.
    The following tools are available:
       Tool Name: Calculator
       Tool Description: A calculator to do addition and multiplcation operations. The function calls are Sum() and Product()
       Tool Input: Only return the function call for the given inputs. Example : Sum(a = 2, b = 2) 

    Use the following format:
       Question: the input question you must answer
       Tool: the action to take, exactly one tool from the provided list above and return the tool name here.
       Action: generate the input to be passed to the tool chosen.
       Question: what is 20 * 10
}

June's Output :

  Tool Chosen : Calculator.
  Action Chosen : Product(a = 20, b = 10).
  Answer : 200.
```

## Examples

You can find more examples in the [examples](./examples/) directory.

