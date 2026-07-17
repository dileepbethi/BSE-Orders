"""
Parser Utilities
Version: 2.0
"""

import re


def clean_text(text: str) -> str:

    text = re.sub(r"\s+", " ", text)

    return text.strip(" .:-")


def split_lines(text: str):

    return text.splitlines()


def is_meaningful(line: str) -> bool:

    line = clean_text(line)

    if not line:
        return False

    if len(line) < 3:
        return False

    skip = [

        "order(s)",
        "contract(s)",
        "particular",
        "response",
        "details",
        "entity;",
        "entity based",
        "nature",
        "domestic",
        "international",
        "whether",
        "time period"

    ]

    lower = line.lower()

    for word in skip:

        if word in lower:
            return False

    return True


def contains_any(text: str, words) -> bool:

    lower = text.lower()

    for word in words:

        if word.lower() in lower:

            return True

    return False


def find_field(lines, keywords, search_window=8):

    """
    Finds a field label and returns
    the first meaningful value below it.
    """

    for i, line in enumerate(lines):

        lower = line.lower()

        if not all(keyword.lower() in lower for keyword in keywords):
            continue

        for j in range(i + 1, min(i + search_window, len(lines))):

            candidate = clean_text(lines[j])

            if not is_meaningful(candidate):
                continue

            return candidate

    return ""