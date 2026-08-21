"""
Customer Extractor
Version : 2.0

Purpose
-------
Extract the customer / awarding authority from BSE order PDFs.

Examples

Hindustan Aeronautics Limited
Integral Coach Factory
NHAI
Indian Railways
NTPC
PGCIL
ONGC
Indian Oil Corporation

The extractor is intentionally pattern-based instead of
hardcoded for specific PDFs.
"""

import re


class CustomerExtractor:

    def __init__(self):

        self.ignore = [

            "company",

            "board",

            "directors",

            "shareholders",

            "bse limited",

            "national stock exchange",

            "listing department",

            "dear sir",

            "dear madam",

            "sebi",

            "regulation 30",

            "company secretary"

        ]
    def clean_customer(
        self,
        customer: str
    ) -> str:

        if not customer:
            return ""

        customer = re.sub(
            r"\s+",
            " ",
            customer
        ).strip()

        customer = customer.strip(
            " .,:;()-"
        )

        customer = re.sub(
            r"^(the)\s+",
            "",
            customer,
            flags=re.IGNORECASE
        )

        customer = re.sub(
            r"\s+\(.*?$",
            "",
            customer
        ).strip()

        lower = customer.lower()

        for item in self.ignore:

            if item in lower:

                return ""

        return customer


    def extract_using_patterns(
        self,
        text: str
    ) -> str:

        patterns = [

            r"received\s+(?:an\s+)?order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"received\s+(?:the\s+)?contract\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"bagged\s+(?:an\s+)?order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"bagged\s+(?:a\s+)?contract\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"awarded\s+by\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"purchase\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"work\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"letter\s+of\s+award\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"customer\s*:\s*([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"client\s*:\s*([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"entity\s+awarding\s+the\s+order\s*[:\-]?\s*([A-Z][A-Za-z0-9&.,()/\- ]+)"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                customer = self.clean_customer(
                    match.group(1)
                )

                if customer:

                    print("=" * 80)
                    print("EXTRACTED CUSTOMER")
                    print(customer)
                    print("=" * 80)

                    return customer

        return ""
    def extract_using_known_entities(
        self,
        text: str
    ) -> str:

        entities = [

            "Hindustan Aeronautics Limited",
            "Integral Coach Factory",
            "Indian Railways",
            "Rail Vikas Nigam Limited",
            "National Highways Authority of India",
            "National Thermal Power Corporation",
            "Power Grid Corporation of India",
            "Oil and Natural Gas Corporation",
            "Indian Oil Corporation",
            "Bharat Petroleum Corporation",
            "Hindustan Petroleum Corporation",
            "Coal India Limited",
            "Steel Authority of India",
            "Airport Authority of India",
            "Airports Authority of India",
            "Bharat Electronics Limited",
            "BrahMos Aerospace",
            "Defence Research and Development Organisation",
            "Indian Navy",
            "Indian Army",
            "Indian Air Force",
            "South Central Railway",
            "Northern Railway",
            "Western Railway",
            "Eastern Railway",
            "Southern Railway",
            "Metro Railway",
            "Delhi Metro Rail Corporation",
            "Chennai Metro Rail Limited",
            "Bangalore Metro Rail Corporation",
            "Gujarat Metro Rail Corporation"

        ]

        lower = text.lower()

        for entity in entities:

            if entity.lower() in lower:

                print("=" * 80)
                print("KNOWN CUSTOMER")
                print(entity)
                print("=" * 80)

                return entity

        return ""


    def extract(
        self,
        text: str
    ) -> str:

        customer = self.extract_using_patterns(text)

        if customer:

            return customer

        customer = self.extract_using_known_entities(text)

        if customer:

            return customer

        return ""

if __name__ == "__main__":

    from pathlib import Path

    txt_files = sorted(
        Path("data/raw").glob("*.txt")
    )

    extractor = CustomerExtractor()

    print("=" * 60)
    print("CUSTOMER EXTRACTOR TEST")
    print("=" * 60)

    for txt_file in txt_files[:5]:

        print()
        print("-" * 60)
        print(txt_file.name)

        try:

            text = txt_file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            customer = extractor.extract(text)

            if customer:

                print("SUCCESS")
                print(customer)

            else:

                print("NOT FOUND")

        except Exception as e:

            print("ERROR")
            print(e)

    print()
    print("=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)