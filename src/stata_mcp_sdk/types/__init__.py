"""Type definitions for stata-mcp-sdk."""

from __future__ import annotations

from typing import Any, Mapping, Union

from typing_extensions import Literal, TypeAlias

Timeout: TypeAlias = Union[float, Any]
NotGiven = object()
NOT_GIVEN = NotGiven()

Headers: TypeAlias = Mapping[str, str]
QueryParams: TypeAlias = Mapping[str, Any]

RequestOptions = Mapping[str, Any]

ResponseFormat = Literal["json", "text"]
