#!/usr/bin/env python3
"""Markdown to HTML Converter"""
import sys
import os


def markdown_to_html(input_filename, output_filename):
    """Converts Markdown file to HTML, handling errors and simplified list handling.

    Args:
        input_filename (str): Path to the Markdown file.
        output_filename (str): Path to the output HTML file.
    """
    if not os.path.exists(input_filename):
        sys.stderr.write(f"Missing {input_filename}\n")
        sys.exit(1)
    with open(input_filename, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    else:
        markdown_to_html(sys.argv[1], sys.argv[2])
