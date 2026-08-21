"""
============================================================
ORDERIQ VALUE EXTRACTOR
============================================================
Extracts monetary values from BSE/NSE order PDFs.

Examples

Rs. 31.49 Crores
INR 522.73 Crore
USD 54.81 Million
Rs. 29,87,844.86
EUR 12.5 Million

============================================================
"""

import re

from orderiq_parser.text_processor import TextProcessor


class ValueExtractor:

    def __init__(self):

        self.processor = TextProcessor()

        self.money_patterns = [

            # Rs. 31.49 Crores
            r"(?:rs\.?|inr|₹)\s*[:\-]?\s*([0-9][0-9,]*(?:\.\d+)?)\s*(crore|crores|lakh|lakhs|million|billion)?",

            # USD 54.81 Million
            r"(usd|eur|gbp|aed|sar)\s*([0-9][0-9,]*(?:\.\d+)?)\s*(million|billion|crore|crores)?",

            # 31.49 Crores
            r"([\d,]+(?:\.\d+)?)\s*(crore|crores|lakh|lakhs|million|billion)",

            # ₹29,87,844.86
            r"₹\s*([\d,]+(?:\.\d+)?)"

        ]
    # ========================================================
    # EXTRACT VALUE
    # ========================================================

    def extract(
        self,
        text: str
    ):

        text = self.processor.normalize(text)

        for pattern in self.money_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                print("=" * 80)
                print("VALUE MATCH")
                print(match.group(0))
                print("=" * 80)

                return self.normalize(
                    match.group(0)
                )

        return ""
    # ========================================================
    # NORMALIZE VALUE
    # ========================================================

    def normalize(
        self,
        value: str
    ) -> dict:

        if not value:

            return {}

        raw = value

        lower = value.lower()

        # ------------------------
        # Currency
        # ------------------------

        currency = "INR"

        if "usd" in lower:
            currency = "USD"

        elif "eur" in lower:
            currency = "EUR"

        elif "gbp" in lower:
            currency = "GBP"

        elif "aed" in lower:
            currency = "AED"

        elif "sar" in lower:
            currency = "SAR"

        # ------------------------
        # Unit
        # ------------------------

        unit = ""

        for u in [
            "crores",
            "crore",
            "lakhs",
            "lakh",
            "million",
            "billion"
        ]:

            if u in lower:
                unit = u.title()
                break

        # ------------------------
        # Amount
        # ------------------------

        amount = None

        number = re.search(
            r"([\d,]+(?:\.\d+)?)",
            value
        )

        if number:

            try:

                amount = float(
                    number.group(1).replace(",", "")
                )

            except ValueError:

                amount = None

        return {

            "raw": raw,
            "currency": currency,
            "amount": amount,
            "unit": unit

        }
# ========================================================
# STANDALONE TEST
# ========================================================
if __name__ == "__main__":

    from pathlib import Path

    extractor = ValueExtractor()

    txt_files = sorted(
        Path("data/raw").glob("*.txt")
    )

    print("=" * 60)
    print("VALUE EXTRACTOR TEST")
    print("=" * 60)

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

            value = extractor.extract(text)

            if value:

                print("SUCCESS")
                print(value)
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
    print("VALUE EXTRACTOR TEST COMPLETE")
    print("=" * 60)