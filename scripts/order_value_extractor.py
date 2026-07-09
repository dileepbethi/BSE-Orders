"""
Order Value Extractor
Version: 1.1
"""

import re


class OrderValueExtractor:

    def __init__(self):
        pass

    def clean(self, value: str) -> str:

        value = re.sub(r"\s+", " ", value)

        return value.strip(" .:-")

    def extract(self, text: str) -> str:

        patterns = [

            r"Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?)?)",

            r"₹\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?)?)",

            r"INR\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?)?)",

            r"~\s*INR\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?)?)"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                return self.clean(
                    match.group(1)
                )

        return ""