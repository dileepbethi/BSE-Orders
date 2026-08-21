from pathlib import Path

from scripts.date_extractor import DateExtractor


def main():

    extractor = DateExtractor()

    text = Path(
        "data/raw/12b5bd2d-dfcb-4a1f-8218-9a81b1bed944.txt"
    ).read_text(
        encoding="utf-8",
        errors="ignore"
    )

    print("=" * 60)
    print("REAL DATE TEST")
    print("=" * 60)
    print()

    result = extractor.extract(text)

    print("Extracted Date:")
    print(result)
    print()


if __name__ == "__main__":
    main()