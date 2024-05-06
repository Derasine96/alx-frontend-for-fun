#!/usr/bin/python3
"""Markdown to HTML Converter"""
import sys
import os
import markdown


def markdown_to_html(input_filename, output_filename):
    """Convert Markdown file to HTML"""
    # if len(sys.argv) < 2:
    #     sys.stderr.write(
    #         "Usage: ./markdown2html.py <input_file> <output_file>\n")
    #     sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    if not os.path.exists(input_filename):
        sys.stderr.write(f"Missing {input_filename}\n")
        sys.exit(1)
    with open(input_filename, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    html_text = markdown.markdown(markdown_text)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_text)
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write(
            "Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    markdown_to_html(sys.argv[1], sys.argv[2])
