"""Exceptions for stata-mcp-sdk."""

from __future__ import annotations


class StataMCPError(Exception):
    """Base exception for all Stata MCP SDK errors."""


class APIError(StataMCPError):
    """Exception raised for API-related errors."""

    def __init__(
            self,
            message: str,
            status_code: int | None = None,
            response: str | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class AuthenticationError(APIError):
    """Exception raised for authentication errors."""


class ValidationError(StataMCPError):
    """Exception raised for validation errors."""


class ConnectionError(StataMCPError):
    """Exception raised for connection errors."""


class TimeoutError(StataMCPError):
    """Exception raised for timeout errors."""
