"""
SEBI Field Parser
Version: 5.0
Supports multi-line field extraction
"""

from dataclasses import fields
import re


class FieldParser:

    def __init__(self):
        pass

    def clean(self, text):

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def after(self, text, keyword):

        index = text.lower().find(keyword.lower())

        if index == -1:
            return ""

        value = text[index + len(keyword):]

        return self.clean(value)


    def extract_sections(self, text):

        """
        Split SEBI Annexure-I into numbered sections.
        """

        text = text.replace("\r", "")

        pattern = r"(?m)^(\d+)\.\s"

        matches = list(
            re.finditer(pattern, text)
        )

        sections = {}

        for i, match in enumerate(matches):

            number = match.group(1)

            start = match.end()

            if i + 1 < len(matches):
                end = matches[i + 1].start()
            else:
                end = len(text)

            sections[number] = text[start:end].strip()

        return sections
    def parse(self, text):
        fields = {
            "entity_awarding": "",
            "terms": "",
            "domestic_entity": "",
            "order_type": "",
            "domestic": "",
            "execution_period": "",
            "order_value": ""
        }

        lines = text.splitlines()

        current_field = None

        for raw_line in lines:

            line = self.clean(raw_line)

            if not line:
                continue

            lower = line.lower()

            # ---------- Detect new field ----------

            if "name of the entity awarding" in lower or "name of the entity awardinq" in lower:

                current_field = "entity_awarding"
                fields[current_field] = self.after(
                    line,
                    "name of the entity awarding the"
                )

                if not fields[current_field]:
                    fields[current_field] = self.after(
                        line,
                        "name of the entity awardinq the"
                    )

                continue

            if "significant terms and conditions" in lower:

                current_field = "terms"
                fields[current_field] = self.after(
                    line,
                    "significant terms and conditions of"
                )
                continue

            if "nature of order" in lower:

                current_field = "order_type"

                if ";" in line:
                    fields[current_field] = self.clean(
                        line.split(";", 1)[1]
                    )
                else:
                    fields[current_field] = self.after(
                        line,
                        "nature of order(s) / contract(s)"
                    )

                continue

            if "whether domestic or international" in lower:

                current_field = "domestic"

                if ";" in line:
                    fields[current_field] = self.clean(
                        line.split(";", 1)[1]
                    )
                else:
                    fields[current_field] = self.after(
                        line,
                        "whether domestic or international"
                    )

                continue

            if "time period" in lower:

                current_field = "execution_period"
                fields[current_field] = self.after(
                    line,
                    "time period by which the"
                )
                continue

            if "broad consideration" in lower:

                current_field = "order_value"
                fields[current_field] = self.after(
                    line,
                    "broad consideration or size of the"
                )
                continue

            # ---------- Append wrapped lines ----------

            if current_field:

                # Next numbered field
                if re.match(r"^\d+\.", line):
                    current_field = None
                    continue

                if re.match(r"^\d+\s", line):
                    current_field = None
                    continue

                # Bullet
                if re.match(r"^[A-Za-z]\)", line):
                    current_field = None
                    continue

                # Known SEBI field headers
                stop_headers = [
                    "name of the entity",
                    "significant terms",
                    "whether domestic",
                    "nature of order",
                    "time period",
                    "broad consideration",
                    "whether the promoter",
                    "whether the order",
                    "nature of interest",
                    "additional disclosure",
                    "brief details",
                    "name of parties"
                ]

                if any(header in lower for header in stop_headers):
                    current_field = None
                    continue

                # Company footer
                footer_headers = [
                    "registered office",
                    "corp. office",
                    "website",
                    "email",
                    "cin",
                    "telephone",
                    "tel:",
                    "fax",
                    "www."
                ]

                if any(footer in lower for footer in footer_headers):
                    current_field = None
                    continue

                fields[current_field] += " " + line
                fields[current_field] = self.clean(
                    fields[current_field]
                )

        return fields