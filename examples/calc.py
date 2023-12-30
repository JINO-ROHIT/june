from june import CalculatorTool, PythonREPLTool, Agent

agent = Agent()
agent.register([CalculatorTool(), PythonREPLTool()])
#print(agent.tool_help)
agent.engine(model_name = "meta-llama/Llama-2-7b-chat-hf")
agent.solve(question = "what is 10 * 10")