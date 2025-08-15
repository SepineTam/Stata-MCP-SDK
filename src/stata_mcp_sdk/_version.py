from importlib.metadata import version

__version__ = version("stata-mcp-sdk")


if __name__ == "__main__":
    print(f"Welcome to Stata MCP SDK v{__version__}")
