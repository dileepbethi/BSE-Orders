"""
Date Extractor
Version: 1.0
"""

import re


class DateExtractor:

    def __init__(self):
        pass

    def clean(self, value: str) -> str:

        value = re.sub(r"\s+", " ", value)

        return value.strip()

    def extract(self, text: str) -> str:

        patterns = [

            r"Date\s*:\s*(\d{2}\.\d{2}\.\d{4})",

            r"Date\s*:\s*(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,\s*\d{4})",

            r"([A-Za-z]+\s+\d{1,2},\s*\d{4})"

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