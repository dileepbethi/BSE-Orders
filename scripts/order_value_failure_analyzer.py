"""
Order Value Failure Analyzer

Classifies remaining extraction failures into categories.
"""

from pathlib import Path

from scripts.order_value_extractor_v2 import OrderValueExtractor


extractor = OrderValueExtractor()

files = sorted(Path("data/raw").glob("*.txt"))

categories = {
    "NOT_DISCLOSED": [],
    "HAS_VALUE_BUT_MISSED": [],
}

for file in files:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    value = extractor.extract(text)

    if value.strip():
        continue

    lower = text.lower()

    if (
        "not disclosed" in lower
        or "confidentiality" in lower
    ):
        categories["NOT_DISCLOSED"].append(file.name)

    else:
        categories["HAS_VALUE_BUT_MISSED"].append(file.name)


print("=" * 70)

for name, items in categories.items():

    print(name)

    print(len(items))

    print()

print("=" * 70)