"""
Order Value Failure Report

Prints the failed files along with the
last section of each document for analysis.
"""

from pathlib import Path

from scripts.order_value_extractor_v2 import OrderValueExtractor


extractor = OrderValueExtractor()

files = sorted(Path("data/raw").glob("*.txt"))

print("=" * 80)

for file in files:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    value = extractor.extract(text)

    if value.strip():
        continue

    print("\n")
    print("=" * 80)
    print(file.name)
    print("=" * 80)

    print(text[-1000:])

print("\n")
print("=" * 80)