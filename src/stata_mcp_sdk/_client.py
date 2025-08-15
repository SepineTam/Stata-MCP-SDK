#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : _client.py

from __future__ import annotations

from typing import Any

import httpx

from .exceptions import APIError, AuthenticationError, ConnectionError, ValidationError
from .types import Headers, QueryParams, Timeout


class StataMCPClient:
    def __init__(self,
                 api_key: str,
                 *,
                 base_url: str = "https://api.statamcp.com/v1",
                 timeout: float | Timeout | None = 30.0,
                 max_retries: int = 3,
                 default_headers: Headers | None = None,
                 http_client: httpx.Client | None = None) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

        # Create HTTP client
        if http_client is not None:
            self._client = http_client
        else:
            headers = {
                "Authorization": f"Bearer {api_key}",
                "User-Agent": "stata-mcp-sdk/0.1.0",
                "Content-Type": "application/json",
            }
            if default_headers:
                headers.update(default_headers)

            self._client = httpx.Client(
                base_url=self.base_url,
                timeout=timeout,
                headers=headers,
            )

        # Validate API key on initialization
        self._validate_api_key()

    def _validate_api_key(self):
        """Validate the API key by making a test request."""
        try:
            response = self._client.get("/health")
            if response.status_code == 401:
                raise AuthenticationError("Invalid API key")
            elif response.status_code == 403:
                raise AuthenticationError("API key lacks required permissions")
            elif response.status_code >= 400:
                raise APIError(
                    f"API validation failed: {response.status_code}")
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Invalid API key") from e
            raise APIError(f"API validation failed: {e}") from e
        except httpx.ConnectError as e:
            raise ConnectionError(f"Failed to connect to API: {e}") from e
        except httpx.TimeoutException as e:
            from .exceptions import TimeoutError
            raise TimeoutError(f"API validation timed out: {e}") from e

    def credits(self) -> float:
        """Get the number of credits available for the API key."""
        resp = self._get("/credits")  # json format
        if "credits" in resp:
            return resp["credits"]
        else:
            return 0.0

    def code_review(self, code: str) -> str:
        """Get the code review of the given code."""
        return self._get(endpoint="/review", params={"code": code})

    def _get(self, endpoint: str, **kwargs: Any) -> Any:
        """Make a GET request to the API."""
        return self._request("GET", endpoint, **kwargs)

    def _post(self, endpoint: str, **kwargs: Any) -> Any:
        """Make a POST request to the API."""
        return self._request("POST", endpoint, **kwargs)

    def _put(self, endpoint: str, **kwargs: Any) -> Any:
        """Make a PUT request to the API."""
        return self._request("PUT", endpoint, **kwargs)

    def _delete(self, endpoint: str, **kwargs: Any) -> Any:
        """Make a DELETE request to the API."""
        return self._request("DELETE", endpoint, **kwargs)

    def _request(self,
                 method: str,
                 endpoint: str,
                 *,
                 params: QueryParams | None = None,
                 json: Any | None = None,
                 headers: Headers | None = None,
                 timeout: float | Timeout | None = None) -> Any:
        """Make an HTTP request to the API."""
        try:
            response = self._client.request(
                method=method,
                url=endpoint,
                params=params,
                json=json,
                headers=headers,
                timeout=timeout,
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthenticationError("Invalid API key") from e
            elif e.response.status_code == 422:
                raise ValidationError(
                    f"Validation error: {e.response.text}") from e
            raise APIError(f"API request failed: {e}") from e
        except httpx.ConnectError as e:
            raise ConnectionError(f"Failed to connect to API: {e}") from e
        except httpx.TimeoutException as e:
            from .exceptions import TimeoutError
            raise TimeoutError(f"Request timed out: {e}") from e
        except Exception as e:
            raise APIError(f"Unexpected error: {e}") from e

    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self) -> StataMCPClient:
        """Enter the context manager."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Exit the context manager."""
        self.close()
