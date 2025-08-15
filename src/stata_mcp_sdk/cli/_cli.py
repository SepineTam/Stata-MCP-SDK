#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : _cli.py

import argparse
import sys

from .._version import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="Stata-MCP-SDK",
        description="Let everyone make Stata-MCP powerful.",
        add_help=True,
    )

    parser.add_argument(
        "-v", "-V", "--version",
        action="version",
        version=f"Stata-MCP-SDK version is {__version__}",
        help="show version information",
    )

    parser.add_argument(
        "-w", "-W", "--website",
        action="store_true",
        help="open the website",
    )

    args = parser.parse_args()

    if args.website:
        import webbrowser
        webbrowser.open("https://github.com/sepinetam/stata-mcp-sdk")
        sys.exit(0)


if __name__ == "__main__":
    main()
