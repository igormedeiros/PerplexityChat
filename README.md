
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

```python
from pplx import PerplexityChat

# Initialize
pplx_chat = PerplexityChat()

# Use in your Langchain logic
result = pplx_chat.calculate(text_input)
```

For more details, refer to the comments and documentation within the `pplx.py` module itself.

## Troubleshooting

For any issues, refer to the logs or debug the `pplx.py` module directly.
