from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import List

model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name,
                                          use_fast = True)
model = AutoModelForCausalLM.from_pretrained(model_name,  
                                            load_in_8bit=True,
                                            device_map="auto")