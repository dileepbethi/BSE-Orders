"""
Quality Classifier V1

Classifies whether a PDF is a genuine procurement announcement.
"""

import re


class QualityClassifier:

    def __init__(self):

        self.procurement_keywords = [

            "award of order",
            "receipt of order",
            "work order",
            "purchase order",
            "letter of award",
            "letter of intent",
            "loi",
            "contract award",
            "contract received",
            "project award",
            "tender",
            "contract"

        ]

        self.reject_keywords = [

            "shareholder meeting",
            "postal ballot",
            "agm",
            "egm",
            "voting results",
            "scrutinizer",
            "board meeting",
            "financial results",
            "quarterly results",
            "annual report",
            "brsr",
            "business responsibility",
            "investor presentation",
            "newspaper advertisement",
            "credit rating",
            "dividend"

        ]

    def classify(self, header: str, description: str, text: str):

        content = " ".join([
            header or "",
            description or "",
            text or ""
        ]).lower()

        # Reject first

        for keyword in self.reject_keywords:

            if keyword in content:

                return {

                    "is_valid": False,
                    "category": "NON_PROCUREMENT",
                    "subtype": keyword,
                    "confidence": 0.99,
                    "reason": f"Matched reject keyword: {keyword}"

                }

        # Procurement

        for keyword in self.procurement_keywords:

            if keyword in content:

                return {

                    "is_valid": True,
                    "category": "PROCUREMENT",
                    "subtype": keyword,
                    "confidence": 0.99,
                    "reason": f"Matched procurement keyword: {keyword}"

                }

        return {

            "is_valid": False,
            "category": "UNKNOWN",
            "subtype": "",
            "confidence": 0.50,
            "reason": "No matching keyword"

        }