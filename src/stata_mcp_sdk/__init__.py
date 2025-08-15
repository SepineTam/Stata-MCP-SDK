#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : __init__.py

from typing import Any

from _client import StataMCPClient
from _version import __version__

__all__ = [
    "__version__",
    "StataMCPClient"
]


_client: StataMCPClient | None = None


def client(api_key: str | None = None,
           base_url: str | None = None,
           **kwargs: Any) -> StataMCPClient:
    """Get the global client instance."""
    global _client

    if _client is None:
        _client = StataMCPClient(
            api_key=api_key,
            base_url=base_url,
            **kwargs,
        )

    return _client


def reset_client() -> None:
    """Reset the global client instance."""
    global _client
    _client = None
