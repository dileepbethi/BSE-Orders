"""
SEBI Table Parser
Version: 1.0
"""

import re


class TableParser:

    def __init__(self):
        pass

    def clean(self, text: str):

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def parse(self, text: str):

        rows = []

        for line in text.splitlines():

            line = self.clean(line)

            if not line:
                continue

            rows.append(line)

        return rows