"""
Date Extractor
Version: 2.0

Responsibilities

- Extract announcement date
- Normalize date
- Always return YYYY-MM-DD
"""

import re
from datetime import datetime


class DateExtractor:

    def __init__(self):
        pass

    # =====================================================
    # CLEAN
    # =====================================================

    def clean(self, value: str) -> str:

        value = re.sub(r"\s+", " ", value)

        return value.strip()

    # =====================================================
    # NORMALIZE
    # =====================================================

    def normalize(self, value: str) -> str:

        value = self.clean(value)

        value = re.sub(
            r"(\d+)(st|nd|rd|th)",
            r"\1",
            value,
            flags=re.IGNORECASE
        )

        formats = [

            "%d.%m.%Y",

            "%d %B, %Y",

            "%d %B %Y",

            "%B %d, %Y",

            "%b %d, %Y",

        ]

        for fmt in formats:

            try:

                return datetime.strptime(
                    value,
                    fmt
                ).strftime("%Y-%m-%d")

            except ValueError:

                pass

        return value

    # =====================================================
    # EXTRACT
    # =====================================================

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

                return self.normalize(
                    match.group(1)
                )

        return ""