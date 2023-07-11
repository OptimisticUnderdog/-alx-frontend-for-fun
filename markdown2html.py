#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import os
import re

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML and writes the output to a file.
    """
    # Check that the Markdown file exists and is a file
    if not (os.path.exists(input_file) and os.path.isfile(input_file)):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file and convert it to HTML
    with open(input_file, encoding="utf-8") as f:
        html_lines = []
        for line in f:

