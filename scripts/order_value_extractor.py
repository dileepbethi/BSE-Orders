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

            r"Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakhs|Lakh|Crores?|Crore|Cr)?)",

            r"₹\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakh|Crores?|Crore|Cr)?)",

            r"INR\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakh|Crores?|Crore|Cr)?)",

            r"USD\s*\$?\s*([0-9][0-9,]*\.?[0-9]*)",

            r"\$\s*([0-9][0-9,]*\.?[0-9]*)",

            r"EUR\s*([0-9][0-9,]*\.?[0-9]*)",

            r"GBP\s*([0-9][0-9,]*\.?[0-9]*)",

            r"value\s*of\s*Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?|Cr)?)",

            r"worth\s*Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?|Cr)?)"

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