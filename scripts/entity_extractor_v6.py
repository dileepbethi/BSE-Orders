"""
OrderIQ Entity Extractor
Version: 6.0

Purpose:
Extract the awarding entity / customer from
BSE & NSE procurement announcements.
"""

import re


class EntityExtractorV6:

    def __init__(self):
        pass

    # ==========================================
    # CLEAN TEXT
    # ==========================================

    def clean(self, text: str) -> str:

        if not text:
            return ""

        text = re.sub(r"\s+", " ", text)

        return text.strip(" .,:;-")

    # ==========================================
    # EXTRACT
    # ==========================================

    def extract(self, text: str):

        if not text:
            return ""

        patterns = [

            r"Letter of Award.*?from\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"received (?:a|an)?\s*landmark order from\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"received (?:a|an)?\s*order from\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"Purchase Order.*?from\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"Work Order.*?from\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"contract awarded by\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"awarded by\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"client[:\-]?\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"customer[:\-]?\s+([A-Z][A-Za-z0-9&.,()'\/\- ]+)",

            r"Name of parties.*?([A-Z][A-Za-z0-9&.,()'\/\- ]+Limited)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if not match:
                continue

            value = self.clean(match.group(1))

            if len(value) < 4:
                continue

            return value

        return ""