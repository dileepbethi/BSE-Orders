"""
Order Value Extractor
Version: 2.0 (Baseline)
"""

import re


class OrderValueExtractor:

    def __init__(self):

        self.priority_keywords = [

        "broad consideration",

        "size of the order",

        "gross order value",

        "order value",

        "contract value",

        "aggregating to",

        "worth",

        "value of",

        "commercial consideration",

    ]

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
        # -----------------------------
        # RailTel multiline INR pattern
        # Example:
        #
        # Rs.
        # (in INR);
        # 18,53,66,820
        # -----------------------------

        railtel = re.search(

            r"Rs\.?\s*\n?\s*\(?.{0,40}?INR.*?\)?\s*[:;]?\s*\n?\s*([0-9,]{5,})",

            text,

            re.IGNORECASE | re.DOTALL

        )

        if railtel:

            return self.clean(railtel.group(1))

        # -----------------------------
        # Cosmic OCR pattern
        # Example:
        # aggregating to 2.157.97 Lakhs
        # -----------------------------

        cosmic = re.search(

            r"aggregating\s+to\s+\d+\.(\d+\.\d+\s*Lakhs?)",

            text,

            re.IGNORECASE

        )

        if cosmic:

            return self.clean(cosmic.group(1))

        # -----------------------------
        # Indian currency format
        # Example:
        # 9,23,44,635/-
        # -----------------------------

        indian_amount = re.search(
            r"([0-9][0-9,]{5,})\s*/-",
            text
        )

        if indian_amount:
            return self.clean(indian_amount.group(1))
        
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
    def normalize_text(self, text: str) -> str:
        """
        Normalize OCR text before extraction.
        """

        if not text:
            return ""

        # Normalize newlines
        text = text.replace("\r", "\n")

        # Collapse multiple spaces
        text = re.sub(r"[ \t]+", " ", text)

        # Normalize blank lines
        text = re.sub(r"\n{2,}", "\n", text)

        return text

    def find_context(self, text: str, keywords, window=120):

        lower = text.lower()

        for keyword in keywords:

            index = lower.find(keyword.lower())

            if index == -1:
                continue

            start = max(0, index - window)

            end = min(len(text), index + window)

            return text[start:end]

        return ""
    def extract_from_context(self, text: str) -> str:

        keywords = [

            "broad consideration",

            "size of order",

            "gross order value",

            "order value",

            "contract value",

            "aggregating to",

            "worth",

            "value of",

        ]

        context = self.find_context(text, keywords)

        if not context:
            return ""

        patterns = [

            r"([0-9][0-9,]*\.?[0-9]*)\s*(Lakhs?|Lakh|Crores?|Crore|Cr)",

            r"₹\s*([0-9][0-9,]*\.?[0-9]*)",

            r"Rs\.?\s*([0-9][0-9,]*\.?[0-9]*)",

            r"INR\s*([0-9][0-9,]*\.?[0-9]*)",

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                context,
                re.IGNORECASE
            )

            if not match:
                continue

            if len(match.groups()) >= 2:
                return self.clean(
                    f"{match.group(1)} {match.group(2)}"
                )

            return self.clean(match.group(1))

        return ""