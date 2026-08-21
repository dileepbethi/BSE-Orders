"""
Field Cleaner
Version: 1.0

Cleans raw fields extracted by FieldParser.
"""

import re
from datetime import datetime


class FieldCleaner:

    def __init__(self):
        pass

    def clean(self, fields: dict):

        cleaned = {}

        cleaned["entity_awarding"] = self.clean_entity(
            fields.get("entity_awarding", "")
        )

        cleaned["terms"] = self.clean_terms(
            fields.get("terms", "")
        )

        cleaned["domestic_entity"] = self.clean_domestic_entity(
            fields.get("domestic_entity", "")
        )

        cleaned["order_type"] = self.clean_order_type(
            fields.get("order_type", "")
        )

        cleaned["domestic"] = self.clean_domestic(
            fields.get("domestic", "")
        )

        cleaned["execution_period"] = self.clean_execution_period(
            fields.get("execution_period", "")
        )

        cleaned["order_value"] = self.clean_order_value(
            fields.get("order_value", "")
        )

        return cleaned

    def normalize(self, text):

        text = re.sub(r"\s+", " ", text)

        return text.strip(" ;,.-")

    def clean_entity(self, text):

        text = re.sub(
            r"order\(s\).*",
            "",
            text,
            flags=re.IGNORECASE
        )

        return self.normalize(text)

    def clean_terms(self, text):

        text = re.sub(
            r"order\(s\).*?brief",
            "",
            text,
            flags=re.IGNORECASE
        )

        return self.normalize(text)

    def clean_domestic_entity(self, text):

        if "domestic" in text.lower():
            return "Domestic Entity"

        if "international" in text.lower():
            return "International Entity"

        return self.normalize(text)

    def clean_order_type(self, text):

     text = re.sub(
        r"registered office.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"corp\.?\s*office.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"website:.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"email:.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"cin\s*no.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"\s+",
        " ",
        text
     )

     return self.normalize(text)

    def clean_domestic(self, text):

        lower = text.lower()

        if "domestic" in lower:
            return "Domestic"

        if "international" in lower:
            return "International"

        return self.normalize(text)

    def clean_execution_period(self, text):

     text = re.sub(
        r"order\(s\).*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"registered office.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"corp\.?\s*office.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"website:.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"email:.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"\s+",
        " ",
        text
     )

     return self.normalize(text)

    def clean_order_value(self, text):

     text = re.sub(
        r"order\(s\)\s*/?\s*contract\(s\)",
        "",
        text,
        flags=re.IGNORECASE
    ) 

     text = re.sub(
        r"\s+",
        " ",
        text
     )

     text = re.sub(
        r"\([^)]*GST[^)]*\)",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"\bexclusive of.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     text = re.sub(
        r"\bincluding.*",
        "",
        text,
        flags=re.IGNORECASE
     )

     return self.normalize(text)