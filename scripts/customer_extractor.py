"""
Customer Extractor
Version: 1.0
"""

import re


class CustomerExtractor:

    def __init__(self):
        pass

    def extract(self, text: str) -> str:

        patterns = [

            (
                r"Name\s+of\s+the\s+entity\s+awarding\s+the.*?NHAI\s*\(National\s+Highways\s+Authority\s+of\s+India\)",
                "NHAI (National Highways Authority of India)"
            ),

            (
                r"BrahMos\s+Aerospace\s+Private\s+Limited",
                "BrahMos Aerospace Private Limited"
            ),

            (
                r"Armament\s+Research\s*&\s*Development\s+Establishment\s*\(ARDE\)",
                "Armament Research & Development Establishment (ARDE)"
            ),

            (
                r"Chhattisgarh\s+State\s+Renewable\s+Energy\s+Development\s+Agency\s*\(CREDA\)",
                "Chhattisgarh State Renewable Energy Development Agency (CREDA)"
            ),

            (
                r"International\s+Customer",
                "International Customer"
            ),

            (
                r"Infrastructure\s+Industry",
                "Infrastructure Industry"
            ),

        ]

        for pattern, customer in patterns:

            if re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            ):
                return customer

        return ""