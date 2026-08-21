"""
Date Extractor
Version: 3.0

Responsibilities

- Extract announcement date
- Normalize date
- Always return YYYY-MM-DD
"""

from ast import pattern
from pydoc import text
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
        # --------------------------------------------
        # Fix common OCR month errors
        # --------------------------------------------

        month_fixes = {

            "uly": "July",
            "anuar": "January",
            "ebruary": "February",
            "arch": "March",
            "pril": "April",
            "ay": "May",
            "une": "June",
            "ugust": "August",
            "eptember": "September",
            "ctober": "October",
            "ovember": "November",
            "ecember": "December",

        }

        for bad, good in month_fixes.items():

            value = re.sub(
                rf"\b{bad}\b",
                good,
                value,
                flags=re.IGNORECASE
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

        top_header = "\n".join(text.splitlines()[:10])
    
        print("=" * 40)
        body = "\n".join(text.splitlines()[10:50])

        patterns = [

            # Date: 24/07/2026
            r"Date\s*[:=\-]?\s*(\d{1,2}/\d{1,2}/\d{4})",

            # Date: 24-07-2026
            r"Date\s*[:=\-]?\s*(\d{1,2}-\d{1,2}-\d{4})",

            # Date: 24.07.2026
            r"Date\s*[:=\-]?\s*(\d{1,2}\.\d{1,2}\.\d{4})",

            # Date: 20th July 2026
            r"Date\s*[:=\-]?\s*(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,?\s*\d{4})",

            # Month Day Year
            r"([A-Za-z]+\s+\d{1,2},\s*\d{4})",

            # Day Month Year
            r"(\d{1,2}(?:st|nd|rd|th)?\s+[A-Za-z]+\s*,?\s*\d{4})",

            r"(\d{1,2}/\d{1,2}/\d{4})",

            r"(\d{1,2}-\d{1,2}-\d{4})",

            r"(\d{1,2}\.\d{1,2}\.\d{4})",

        ]
        # =====================================================
        # SEARCH HEADER FIRST
        # =====================================================

        for pattern in patterns:

            match = re.search(
                pattern,
                top_header,
                re.IGNORECASE
            )

            if not match:
                continue

            print()
            

            value = match.group(1)

            upper = value.upper()

            blocked = [
                "PLC",
                "ISO",
                "REGULATION",
                "YEARS",
                "SECTION",
                "ACT",
            ]

            if any(word in upper for word in blocked):
                continue

            return self.normalize(value)

        # =====================================================
        # SEARCH BODY ONLY IF HEADER FAILED
        # =====================================================

        for pattern in patterns:

            match = re.search(
                pattern,
                body,
                re.IGNORECASE
            )

            if not match:
                continue

            print()
            print("BODY MATCH:", match.group(1))

            value = match.group(1)

            upper = value.upper()

            blocked = [
                "PLC",
                "ISO",
                "REGULATION",
                "YEARS",
                "SECTION",
                "ACT",
            ]

            if any(word in upper for word in blocked):
                continue

            return self.normalize(value)

        return ""