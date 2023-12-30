from june.tools.schema import Tools
from typing import Type, Union, List
from colorama import Fore, Style
from transformers import AutoModelForCausalLM, AutoTokenizer
import yaml
import os
import re
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
        return tool_info_list
    
    def engine(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name,
                                                  use_fast = True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name,  
                                                    load_in_8bit=True,
                                                    device_map="auto")
        
    def solve(self, question):
        with open(os.environ['PROMPT_PATH'], "r") as file:
            config_data = yaml.safe_load(file)
        config_data['agent_prompts']['tools'] = config_data['agent_prompts']['tools'].format(tool_description = '\n'.join(self.tool_help))
        config_data['agent_prompts']['decision'] = config_data['agent_prompts']['decision'].format(question = question)
        messages=[{"role": "user", 
                   "content": config_data['agent_prompts']['system'] + config_data['agent_prompts']['tools'] + config_data['agent_prompts']['decision']}]
        print(f"{Fore.BLUE} {messages}.{Style.RESET_ALL}")

        tokenized_chat = self.tokenizer.apply_chat_template(messages, 
                                                            tokenize = True, 
                                                            add_generation_prompt = True,
                                                            return_tensors = "pt")
        generated_ids = self.model.generate(tokenized_chat.to("cuda"), max_new_tokens=1000, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)

        tool_pattern = re.compile(r"Tool: (.+?)\n")
        action_pattern = re.compile(r"Action: (.+?)</s>")

        tool_match = tool_pattern.findall(decoded[0])
        action_match = action_pattern.findall(decoded[0])

        tool_chosen, action_chosen = tool_match[-1], action_match[-1]

        print(f"{Fore.YELLOW} Tool Chosen : {tool_chosen}.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW} Action Chosen : {action_chosen}.{Style.RESET_ALL}")

        action_executor = None
        for idx, _t in enumerate(self.tools):
            if getattr(_t, 'tool_name', None) == tool_chosen:
                action_executor = _t

        answer = action_executor.execute(action_chosen)
        print(f"{Fore.GREEN} Answer : {answer}.{Style.RESET_ALL}")


