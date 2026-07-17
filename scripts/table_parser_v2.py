"""
Table Parser V2

Primary structured parser for BSE / SEBI Annexure tables.
"""

from pathlib import Path

import pdfplumber


class TableParserV2:

    def __init__(self):
        pass

    def extract_tables(self, pdf_path: Path):

        tables = []

        with pdfplumber.open(pdf_path) as pdf:

            for page_number, page in enumerate(pdf.pages, start=1):

                page_tables = page.extract_tables()

                if not page_tables:
                    continue

                for table in page_tables:

                    tables.append(
                        {
                            "page": page_number,
                            "rows": table
                        }
                    )

        return tables


    def table_to_dict(self, table):

        data = {}

        rows = table["rows"]

        for row in rows:

            if not row:
                continue

            if len(row) < 3:
                continue

            number = str(row[0]).strip()

            # Skip header row (Sr. No.)
            if not number.isdigit():
                continue

            key = str(row[1]).strip()

            value = str(row[2]).strip()

            data[number] = {
                "title": key,
                "value": value
            }

        return data


    def build_record(self, table):

        data = self.table_to_dict(table)

        return {

            "awarding_entity":
                data.get("1", {}).get("value", ""),

            "terms":
                data.get("2", {}).get("value", ""),

            "domestic_entity":
                data.get("3", {}).get("value", ""),

            "order_type":
                data.get("4", {}).get("value", ""),

            "domestic":
                data.get("5", {}).get("value", ""),

            "execution_period":
                data.get("6", {}).get("value", ""),

            "order_value":
                data.get("7", {}).get("value", "")

        }