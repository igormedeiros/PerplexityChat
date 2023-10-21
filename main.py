import json
import os
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain.callbacks import get_openai_callback
from pplx import PerplexityChat

config_file = open('config.json')
config = json.load(config_file)

os.environ["SERPAPI_API_KEY"] = config['serpi_key']
os.environ["PPLX_API_KEY"] = config['pplx_api_key']

pplx_model_name = config['model_name']

# Instance of the PerplexityChatAI class
chat_perplexity_ai = PerplexityChat(model_name=pplx_model_name, temperature=0.7, verbose=True)

# Load the tools
tools = load_tools(["serpapi"], llm=chat_perplexity_ai)

# Initialize the agent
agent = initialize_agent(tools, chat_perplexity_ai, 
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                         verbose=True,
                         handle_parsing_errors=True
                         )

# Run the agent
with get_openai_callback() as cb:
    chat_answer = agent.run('Escreva um python que é um CRM')
    print('Answer: ', chat_answer)
