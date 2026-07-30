"""
Field Parser Benchmark
Version: 1.0

Tests the FieldParser + FieldCleaner
on real BSE announcements.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.field_parser import FieldParser
from scripts.field_cleaner import FieldCleaner


RAW_FOLDER = PROJECT_ROOT / "data" / "raw"


def main():

    parser = FieldParser()
    cleaner = FieldCleaner()

    txt_files = sorted(RAW_FOLDER.glob("*.txt"))[:20]

    print("=" * 90)
    print("FIELD PARSER BENCHMARK")
    print("=" * 90)

    for index, txt_file in enumerate(txt_files, start=1):

        text = txt_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        raw = parser.parse(text)
        cleaned = cleaner.clean(raw)

        print()
        print("=" * 90)
        print(f"FILE {index}")
        print("=" * 90)
        print(txt_file.name)
        print()

        print("Entity Awarding")
        print("----------------------------")
        print(cleaned["entity_awarding"] or "(empty)")
        print()

        print("Order Value")
        print("----------------------------")
        print(cleaned["order_value"] or "(empty)")
        print()

        print("Domestic / International")
        print("----------------------------")
        print(cleaned["domestic"] or "(empty)")
        print()

        print("Execution Period")
        print("----------------------------")
        print(cleaned["execution_period"] or "(empty)")
        print()

        print("Order Type")
        print("----------------------------")
        print(cleaned["order_type"] or "(empty)")
        print()

        print("Terms")
        print("----------------------------")
        print(cleaned["terms"] or "(empty)")
        print()

    print("=" * 90)
    print("BENCHMARK COMPLETE")
    print("=" * 90)


if __name__ == "__main__":
    main()