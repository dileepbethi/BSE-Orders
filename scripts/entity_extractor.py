"""
Entity Extractor
Version: 4.0
"""

import re


class EntityExtractor:

    def __init__(self):
        pass

    def clean(self, value: str) -> str:

        value = re.sub(r"\s+", " ", value)

        return value.strip(" .:-")

    def extract(self, text: str) -> str:

        patterns = [

            r"Name\s+of\s+the\s+entity\s+awarding.*?\n\s*([^\n]+)",

            r"name\s+of\s+the\s+entity\s+awarding.*?\n\s*([^\n]+)",

            r"1\s+Name\s+of\s+the\s+entity\s+awarding.*?\n\s*([^\n]+)",

            r"a\)\s*name\s+of\s+the\s+entity\s+awarding.*?\n\s*([^\n]+)",

        ]

        skip_words = [

            "significant",
            "terms",
            "conditions",
            "particulars",
            "response",
            "details",
            "order(s)",
            "contract(s)",
            "awarded in brief"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if not match:
                continue

            candidate = self.clean(match.group(1))

            lower = candidate.lower()

            if any(word in lower for word in skip_words):
                continue

            return candidate

        return ""