"""
Table Parser V2

Primary structured parser for BSE / SEBI Annexure tables.
"""

from pathlib import Path

import pdfplumber


class TableParserV2:
    """
    Extracts structured tables from BSE / SEBI Annexure PDFs.
    """

    def __init__(self):
        pass

    def extract_tables(self, pdf_path: Path):
        """
        Returns every detected table from every page.

        Output:
        [
            {
                "page": 1,
                "rows": [...]
            }
        ]
        """

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
                            "rows": table,
                        }
                    )

        return tables
    
    def table_to_dict(self, table):
        """
        Converts a SEBI Annexure table into a dictionary.

        Example:

        {
            "1": {
                "title": "...",
                "value": "..."
            }
        }
        """

        data = {}

        rows = table["rows"]

        for row in rows:

            if not row:
                continue

            if len(row) < 3:
                continue

            number = str(row[0]).strip()

            # Ignore header rows
            if not number.isdigit():
                continue

            title = str(row[1]).strip()

            value = str(row[2]).strip()

            data[number] = {
                "title": title,
                "value": value,
            }

        return data

    def build_record(self, table):
        """
        Converts the parsed table dictionary into the standard
        record format used by the rest of the pipeline.
        """

        data = self.table_to_dict(table)

        return {
            "awarding_entity": data.get("1", {}).get("value", ""),
            "terms": data.get("2", {}).get("value", ""),
            "domestic_entity": data.get("3", {}).get("value", ""),
            "order_type": data.get("4", {}).get("value", ""),
            "domestic": data.get("5", {}).get("value", ""),
            "execution_period": data.get("6", {}).get("value", ""),
            "order_value": data.get("7", {}).get("value", ""),
        }