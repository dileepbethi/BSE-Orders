"""
Entity Extractor Benchmark
Version: 1.0

Compares:
- EntityExtractor (V5)
- EntityExtractorV6
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.entity_extractor import EntityExtractor
from scripts.entity_extractor_v6 import EntityExtractorV6


RAW_FOLDER = Path("data/raw")


def main():

    v5 = EntityExtractor()
    v6 = EntityExtractorV6()

    txt_files = sorted(RAW_FOLDER.glob("*.txt"))[:20]

    print("=" * 80)
    print("ENTITY EXTRACTOR BENCHMARK")
    print("=" * 80)
    print()

    for index, txt_file in enumerate(txt_files, start=1):

        text = txt_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        result_v5 = v5.extract(text)
        result_v6 = v6.extract(text)

        print("=" * 80)
        print(f"FILE {index}")
        print("=" * 80)
        print(txt_file.name)
        print()

        print("V5")
        print("-" * 40)
        print(result_v5 if result_v5 else "(empty)")
        print()

        print("V6")
        print("-" * 40)
        print(result_v6 if result_v6 else "(empty)")
        print()

    print("=" * 80)
    print("BENCHMARK COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()