#!/usr/bin/env python3
"""Markdown to HTML Converter"""
import sys
import os


def markdown_to_html():
    """Converts Markdown file to HTML, handling errors and simplified list handling.

    Args:
        input_filename (str): Path to the Markdown file.
        output_filename (str): Path to the output HTML file.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print("Missing " + sys.argv[1], file=sys.stderr)
        exit(1)

    exit(0)


if __name__ == "__main__":
    markdown_to_html()
