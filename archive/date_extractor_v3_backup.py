"""
Date Extractor
Version: 3.0

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

        value = value.replace("–", "-")
        value = value.replace("—", "-")
        value = value.replace("'", "")

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

        value = re.sub(
            r"\s*,\s*",
            ", ",
            value
        )

        value = re.sub(
            r"\s+",
            " ",
            value
        )

        formats = [

            "%d.%m.%Y",

            "%d-%m-%Y",

            "%d/%m/%Y",

            "%d %B %Y",

            "%d %B, %Y",

            "%d %b %Y",

            "%d %b, %Y",

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

            # Date: 24/07/2026
            r"Date\s*[:=\-]?\s*(\d{1,2}/\d{1,2}/\d{4})",

            # Date: 24-07-2026
            r"Date\s*[:=\-]?\s*(\d{1,2}-\d{1,2}-\d{4})",

            # Date: 24.07.2026
            r"Date\s*[:=\-]?\s*(\d{1,2}\.\d{1,2}\.\d{4})",

            # Date: 20th July 2026
            r"Date\s*[:=\-]?\s*(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,?\s*\d{4})",

            # Standalone: 20th July 2026
            r"(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,?\s*\d{4})",

            # July 20, 2026
            r"([A-Za-z]+\s+\d{1,2},\s*\d{4})",

            # 09/07/2026 anywhere
            r"(\d{1,2}/\d{1,2}/\d{4})",

            # 09-07-2026 anywhere
            r"(\d{1,2}-\d{1,2}-\d{4})",

            # 09.07.2026 anywhere
            r"(\d{1,2}\.\d{1,2}\.\d{4})",

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