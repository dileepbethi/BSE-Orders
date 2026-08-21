"""
Announcement Classifier
Version: 1.1
"""

import re


class AnnouncementClassifier:

    ORDER = "ORDER"

    FINANCIAL_RESULTS = "FINANCIAL_RESULTS"

    AGM = "AGM"

    ESG = "ESG"

    COURT_ORDER = "COURT_ORDER"

    PRESS_RELEASE = "PRESS_RELEASE"

    OTHER = "OTHER"

    def __init__(self):
        pass

    def classify(self, text: str) -> str:

        text = text.lower()

        order_keywords = [

            "receipt of order",

            "bagged",

            "bagging",

            "work order",

            "letter of award",

            "loa",

            "contract",

            "purchase order",

            "received an order",

            "order secured",

            "order received",

        ]

        financial_keywords = [

            "financial results",

            "quarter ended",

            "standalone results",

            "consolidated results",

            "unaudited financial",

            "audited financial",

        ]

        agm_keywords = [

            "annual general meeting",

            "agm",

            "e-voting",

            "video conferencing",

        ]

        esg_keywords = [

            "esg",

            "environmental",

            "social",

            "governance score",

        ]

        court_keywords = [

            "securities appellate tribunal",

            "sat",

            "court order",

            "appeal",

        ]

        press_keywords = [

            "press release",

            "newspaper",

            "advertisement",

        ]

        # More specific categories first

        if self._contains(text, financial_keywords):

            if not self._contains(text, agm_keywords):

                return self.FINANCIAL_RESULTS

        if self._contains(text, agm_keywords):
            return self.AGM

        if self._contains(text, esg_keywords):
            return self.ESG

        if self._contains(text, court_keywords):
            return self.COURT_ORDER

        # Press Release should only win if the
        # announcement is NOT also an order.

        if self._contains(text, press_keywords):

            if not self._contains(text, order_keywords):

                return self.PRESS_RELEASE
            
        # ORDER is evaluated last because many
        # announcements contain generic words
        # like "order" or "contract".

        if self._contains(text, order_keywords):
            return self.ORDER

        return self.OTHER

    def _contains(self, text: str, keywords):

        for keyword in keywords:

            # Phrase -> substring search
            if " " in keyword:

                if keyword in text:
                    return True

            # Single word -> whole-word search
            else:

                pattern = r"\b" + re.escape(keyword) + r"\b"

                if re.search(
                    pattern,
                    text,
                    re.IGNORECASE
                ):
                    return True

        return False