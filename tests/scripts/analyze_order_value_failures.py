"""
Analyze Order Value Extractor Failures
"""

from pathlib import Path

from scripts.order_value_extractor_v2 import OrderValueExtractor


RAW_FOLDER = Path("data/raw")

extractor = OrderValueExtractor()

failed = []

for file in sorted(RAW_FOLDER.glob("*.txt")):

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    value = extractor.extract(text)

    if value.strip():
        continue

    failed.append(file)

print("=" * 80)
print("ORDER VALUE FAILURES")
print("=" * 80)

for file in failed:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    print("\n")
    print("=" * 80)
    print(file.name)
    print("=" * 80)

    print(text[:2500])

print("\n")
print("=" * 80)
print("Total Failures :", len(failed))
print("=" * 80)