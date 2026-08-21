"""
Customer Extractor Gold Test
"""

import csv
from pathlib import Path

from scripts.customer_extractor import CustomerExtractor

extractor = CustomerExtractor()

print("=" * 70)
print("CUSTOMER EXTRACTOR GOLD TEST")
print("=" * 70)
print()

passed = 0
total = 0

with open(
    "tests/database/customer_gold.csv",
    newline="",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    for row in reader:

        total += 1

        filename = row["filename"]

        expected = row["expected_customer"]

        text = Path(
            "data/raw",
            filename
        ).read_text(
            encoding="utf-8",
            errors="ignore"
        )

        actual = extractor.extract(text)

        result = "PASS" if actual == expected else "FAIL"

        if result == "PASS":
            passed += 1

        print(f"File     : {filename}")
        print(f"Expected : {expected}")
        print(f"Actual   : {actual}")
        print(f"Result   : {result}")
        print("-" * 60)

print()
print("=" * 70)
print(f"Passed : {passed}/{total}")
print("=" * 70)