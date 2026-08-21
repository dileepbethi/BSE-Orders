"""
============================================================
ORDERIQ
Customer Extractor
Version : 3.0
============================================================

Purpose
-------
Extract the customer / client / awarding authority from
BSE order announcements.

This extractor depends on TextProcessor and works only on
relevant sentences instead of scanning the entire document.

============================================================
"""

from __future__ import annotations

import re

from orderiq_parser.text_processor import TextProcessor


class CustomerExtractor:

    def __init__(self):

        self.processor = TextProcessor()

        self.order_keywords = [

            "order",

            "contract",

            "work order",

            "purchase order",

            "letter of award",

            "awarded",

            "bagged",

            "secured",

            "received",

            "accept",

            "accepted"

        ]

        self.stop_words = [

            "company",

            "board",

            "director",

            "shareholder",

            "regulation",

            "sebi",

            "listing",

            "domestic",

            "international",

            "entity",

            "annexure",

            "schedule"

        ]
    # ========================================================
    # PUBLIC API
    # ========================================================

    def extract(
        self,
        text: str
    ) -> str:

        text = self.processor.normalize(text)

        candidate_sentences = self.collect_candidate_sentences(text)

        for sentence in candidate_sentences:

            customer = self.extract_from_sentence(sentence)

            if customer:

                print("=" * 80)
                print("EXTRACTED CUSTOMER")
                print(customer)
                print("=" * 80)

                return customer

        return ""


    # ========================================================
    # SENTENCE COLLECTION
    # ========================================================

    def collect_candidate_sentences(
        self,
        text: str
    ) -> list[str]:

        candidates = []

        sentences = self.processor.sentences(text)

        for sentence in sentences:

            lower = sentence.lower()

            for keyword in self.order_keywords:

                if keyword in lower:

                    candidates.append(sentence)

                    break

        return candidates
    # ========================================================
    # CUSTOMER EXTRACTION
    # ========================================================

    def extract_from_sentence(
        self,
        sentence: str
    ) -> str:

        patterns = [

            r"order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"contract\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"received\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"accepted\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"awarded\s+by\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"bagged\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"purchase\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"work\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"letter\s+of\s+award\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                sentence,
                re.IGNORECASE
            )

            if not match:

                continue

            customer = self.clean_customer(
                match.group(1)
            )

            if customer:

                return customer

        return ""


    # ========================================================
    # CLEANUP
    # ========================================================

    def clean_customer(
        self,
        customer: str
    ) -> str:

        customer = re.sub(
            r"\s+",
            " ",
            customer
        ).strip()

        customer = customer.strip(
            " .,:;()-"
        )

        customer = re.sub(
            r"\(.*?\)",
            "",
            customer
        ).strip()

        lower = customer.lower()

        for word in self.stop_words:

            if lower == word:

                return ""

        return customer
    # ========================================================
    # VALIDATION
    # ========================================================

    def is_valid_customer(
        self,
        customer: str
    ) -> bool:

        if not customer:

            return False

        customer = customer.strip()

        if len(customer) < 4:

            return False

        lower = customer.lower()

        for word in self.stop_words:

            if lower == word:

                return False

        invalid_patterns = [

            r"^rs\.?$",
            r"^crore$",
            r"^lakh$",
            r"^million$",
            r"^\d+$",
            r"^yes$",
            r"^no$",
            r"^nil$"

        ]

        for pattern in invalid_patterns:

            if re.fullmatch(pattern, lower):

                return False

        return True


    def extract_from_sentence(
        self,
        sentence: str
    ) -> str:

        patterns = [

            r"order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"contract\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"received\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"accepted\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"awarded\s+by\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"bagged\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"purchase\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"work\s+order\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)",

            r"letter\s+of\s+award\s+from\s+([A-Z][A-Za-z0-9&.,()/\- ]+)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                sentence,
                re.IGNORECASE
            )

            if not match:

                continue

            customer = self.clean_customer(
                match.group(1)
            )

            if self.is_valid_customer(customer):

                return customer

        return ""
# ========================================================
# STANDALONE TEST
# ========================================================

if __name__ == "__main__":

    from pathlib import Path

    extractor = CustomerExtractor()

    txt_files = sorted(
        Path("data/raw").glob("*.txt")
    )

    print("=" * 60)
    print("CUSTOMER EXTRACTOR TEST")
    print("=" * 60)

    if not txt_files:

        print("No TXT files found.")

    else:

        success = 0
        failed = 0

        for txt_file in txt_files[:10]:

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
                    success += 1

                else:

                    print("NOT FOUND")
                    failed += 1

            except Exception as e:

                print("ERROR")
                print(e)
                failed += 1

        print()
        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(f"SUCCESS : {success}")
        print(f"FAILED  : {failed}")

    print()
    print("=" * 60)
    print("CUSTOMER EXTRACTOR TEST COMPLETE")
    print("=" * 60)