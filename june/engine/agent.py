from tools import Tools, CalculatorTool, PythonREPLTool
from typing import Type, Union, List, Any
from colorama import Fore, Style
from transformers import AutoModelForCausalLM, AutoTokenizer
import yaml
import os
from dotenv import load_dotenv 
load_dotenv()

class Agent:
    def __init__(self):
        self.tools: List[Type[Tools]] = []

    def register(self, tools: Union[Type[Tools], List[Type[Tools]]]):
        if isinstance(tools, list):
            self.tools.extend(tools)
        else:
            self.tools.append(tools)
        
        #print(self.tools)
    @property
    def tool_help(self):
        tool_info_list = [
            (
                f"Tool Name: {tool.tool_name}\n"
                f"Tool Description: {tool.tool_description}\n"
                f"Tool Input: {tool.tool_input}\n"
            )
            for tool in self.tools
        ]
        return '\n'.join(tool_info_list)
    
    def solve(self, question):
        with open(os.environ['PROMPT_PATH'], "r") as file:
            config_data = yaml.safe_load(file)
        config_data['agent_prompts']['tools'] = config_data['agent_prompts']['tools'].format(tool_description = self.tool_help)
        config_data['agent_prompts']['decision'] = config_data['agent_prompts']['decision'].format(question = question)
        print(config_data)
        

    def engine(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name,
                                                  use_fast = True)
        model = AutoModelForCausalLM.from_pretrained(model_name,  
                                                    load_in_8bit=True,
                                                    device_map="auto")
    


agent = Agent()
agent.register([CalculatorTool(), PythonREPLTool()])
#print(agent.tool_help)
agent.solve(question = "what is 10 + 10")


