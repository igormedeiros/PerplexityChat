
# PerplexityChat Model Wrapper for Langchain

## Overview

The `pplx.py` module acts as a wrapper for handling perplexity chat model in Langchain projects.

## Requirements

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuration

1. Add the following import in your main Langchain application:
    ```python
    from pplx import PerplexityChat
    ```

2. Update your `config.json` to include any specific settings required for the `pplx` module.

3. In your main Langchain application, initialize the `PerplexityChat` class and use it as per your needs.

## Usage

Here's a simple example using `pplx.py` in a Langchain application:

from langchain.agents import initialize_agent, AgentType, load_tools
from langchain.callbacks import get_openai_callback
from pplx import PerplexityChat

# Instance of the PerplexityChatAI class
chat_perplexity_ai = PerplexityChat(model_name="mistral-7b-instruct", temperature=0.7, verbose=True)

# Load the tools
tools = load_tools(["serpapi"], llm=chat_perplexity_ai)

# Initialize the agent
agent = initialize_agent(tools, chat_perplexity_ai, 
                         agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
                         verbose=True,
                         handle_parsing_errors=True
                         )

# Run the agent
chat_answer = agent.run('Qual a cor do cavalo branco de Napoleão?')
print('Answer: ', chat_answer)

For more details, refer to the comments and documentation within the `pplx.py` module itself.

## Troubleshooting

For any issues, refer to the logs or debug the `pplx.py` module directly.
