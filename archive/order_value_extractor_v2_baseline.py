"""
Order Value Extractor
Version: 2.0 (Baseline)
"""

import re


class OrderValueExtractor:

    def __init__(self):
        pass

    def clean(self, value: str) -> str:
        value = re.sub(r"\s+", " ", value)
        return value.strip(" .:-")

    def extract(self, text: str) -> str:

        priority_patterns = [

            r"Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakh|Crores?|Crore|Cr)?)",

            r"₹\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakh|Crores?|Crore|Cr)?)",

            r"INR\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Lakh|Crores?|Crore|Cr)?)",

            r"USD\s*\$?\s*([0-9][0-9,]*\.?[0-9]*)",

            r"\$\s*([0-9][0-9,]*\.?[0-9]*)",

            r"EUR\s*([0-9][0-9,]*\.?[0-9]*)",

            r"GBP\s*([0-9][0-9,]*\.?[0-9]*)",

            r"value\s*of\s*Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?|Crore|Cr)?)",

            r"worth\s*Rs\.?\s*([0-9][0-9,]*\.?[0-9]*\s*(?:Lakhs?|Crores?|Crore|Cr)?)",

        ]

        fallback_patterns = [
            # Future OCR-friendly patterns will go here.
        ]

        for pattern in priority_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:
                return self.clean(match.group(1))

        for pattern in fallback_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:
                return self.clean(match.group(1))

        return ""

    def convert_to_crore(self, value: str):

        if not value:
            return None

        text = value.lower()

        # Crore
        m = re.search(r"([\d,.]+)\s*(crore|cr)", text)
        if m:
            try:
                return round(float(m.group(1).replace(",", "")), 4)
            except ValueError:
                return None

        # Lakh
        m = re.search(r"([\d,.]+)\s*lakh", text)
        if m:
            try:
                lakhs = float(m.group(1).replace(",", ""))
                return round(lakhs / 100, 4)
            except ValueError:
                return None

        # Plain Rupees
        m = re.search(r"([\d,]+)", text)
        if m:
            try:
                rupees = float(m.group(1).replace(",", ""))
                return round(rupees / 10000000, 4)
            except ValueError:
                return None

        return None