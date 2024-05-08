#!/usr/bin/python3
"""Markdown to HTML Converter with Simplified List Handling"""
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
    html_text = ""
    lines = markdown_text.splitlines()
    in_list = False
    list_type = None
    for line in lines:
        if line.startswith("# "):
            html_text += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith("## "):
            html_text += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith("### "):
            html_text += f"<h3>{line[4:]}</h3>\n"
        elif line.startswith("#### "):
            html_text += f"<h4>{line[5:]}</h4>\n"
        elif line.startswith("##### "):
            html_text += f"<h5>{line[6:]}</h5>\n"
        elif line.startswith("###### "):
            html_text += f"<h6>{line[7:]}</h6>\n"
        elif (line.startswith("-") or
              (str(x) + "* " for x in range(1, 10))):
            if not in_list:
                html_text += "<" + \
                    ("ul" if line.startswith("-") else "ol") + ">\n"
                in_list = True
            html_text += f"  <li>{line[2:] if line.startswith('-') else line[2:]}</li>\n"
        else:
            if in_list:
                html_text += "</" + ("ul" if list_type ==
                                     "UL" else "ol") + ">\n"
                in_list = False
            html_text += line + "\n"
    if in_list:
        html_text += "</" + ("ul" if list_type == "UL" else "ol") + ">\n"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html_text)
    sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write(
            "Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)
    markdown_to_html(sys.argv[1], sys.argv[2])
