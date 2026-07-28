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

            # BODY SENTENCE STRATEGY
            r"The\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))\s+is\s+pleased",

            r"([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))\s+has\s+secured",

            r"([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))\s+has\s+received",

            r"([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))\s+has\s+been\s+awarded",

            # COMPANY NAME FIELD

            r"Company\s+Name\s*:\s*([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

            # REFERENCE FIELD

            r"Ref:.*?(?:M/s\.?\s*)?([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",
 
            # THE COMPANY PATTERN
            
            r"([A-Z][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))\s*\(\"the Company\"\)\s*has\s+received",

            # Existing patterns
            
            r"FOR\s+([A-Z][A-Z0-9&.,()'\/\- ]+(?:LIMITED|LTD))",

            r"For\s+([A-Za-z0-9][A-Za-z0-9&.,()'\/\- ]+(?:Limited|LIMITED|Ltd|LTD))",

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