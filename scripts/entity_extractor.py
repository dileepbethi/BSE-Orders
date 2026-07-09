"""
Entity Extractor
Version: 5.0
"""

import re


class EntityExtractor:

    def __init__(self):
        pass

    def clean(self, value: str):

        value = re.sub(r"\s+", " ", value)

        return value.strip(" .:-")

    def extract(self, text: str):

        patterns = [

            r"entity\s+awarding\s+the\s+(.*)",

            r"entity\s+awardinq\s+the\s+(.*)",

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            value = self.clean(
                match.group(1)
            )

            value = re.sub(
                r"order.*",
                "",
                value,
                flags=re.IGNORECASE
            )

            value = self.clean(value)

            if value:

                return value

        return ""