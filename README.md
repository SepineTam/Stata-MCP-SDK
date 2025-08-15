# Stata-MCP SDK (Python)

[![PyPI version](https://img.shields.io/pypi/v/stata-mcp-sdk.svg)](https://pypi.org/project/stata-mcp-sdk/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Issue](https://img.shields.io/badge/Issue-report-green.svg)](https://github.com/sepinetam/stata-mcp-sdk/issues/new)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/SepineTam/stata-mcp-sdk)

Let everyone make Stata-MCP powerful.

## Quickly Start

### Installation
You can install it with pip
```bash
pip install stata-mcp-sdk
```

or, if you use `uv`

```bash
uv add stata-mcp-sdk
```

### Basic Usage
```python
from stata_mcp_sdk import StataMCPClient

api_key = "<YOUR_STATA_MCP_API_KEY>"
base_url = "https://api.statamcp.com"
sm_client = StataMCPClient(api_key, base_url)

balance: float = sm_client.credits()
print(f"Your balance is ${balance:.2f}")

# regression stata code
code = """
sysuse auto
reg price mpg
reg price mpg weight
"""
reviewed_code = sm_client.code_review(code, "stata")
print("Reviewed Code:\n" + reviewed_code)
```

## Project Structure
```
./src
└── stata_mcp_sdk
    ├── __init__.py
    ├── __main__.py
    ├── _client.py
    ├── _version.py
    ├── cli
         ├── __init__.py
         └── _cli.py
    ├── exceptions
         └── __init__.py
    └── types
        └── __init__.py
```

## License
[Apache License 2.0](LICENSE)

