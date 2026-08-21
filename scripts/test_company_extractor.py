from pathlib import Path

from scripts.company_extractor import CompanyExtractor


def main():

    extractor = CompanyExtractor()

    txt_file = Path(
        "data/raw/114384fe-03c4-4321-b070-8cdf46e033c3.txt"
    )

    text = txt_file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    company = extractor.extract(text)

    print()
    print("=" * 60)
    print("COMPANY EXTRACTOR TEST")
    print("=" * 60)
    print()

    print("Extracted Company:")
    print(company)
    print()


if __name__ == "__main__":
    main()