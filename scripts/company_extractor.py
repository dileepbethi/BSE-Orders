"""
Company Extractor
Version: 1.1
"""

import re


class CompanyExtractor:

    def __init__(self):
        pass

    def clean(self, value: str) -> str:

        value = re.sub(r"\s+", " ", value)

        return value.strip(" :-\t\r\n")

    def extract(self, text: str) -> str:

        patterns = [

            # NEW PATTERN
            r"For\s*&\s*on\s*behalf\s*of\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

            # NEW PATTERN
            r"For,\s*([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

            # Existing patterns
            r"FOR\s+([A-Z][A-Z0-9&.,()'\/\- ]+(?:LIMITED|LTD))",

            r"For\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

            r"for\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

            r"Company has been awarded.*?\n.*?For\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.MULTILINE | re.IGNORECASE
            )

            if match:

                return self.clean(
                    match.group(1)
                )

        return ""