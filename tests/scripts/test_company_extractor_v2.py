"""
Company Extractor V2 Tests
"""

from pathlib import Path

from scripts.company_extractor_v2 import CompanyExtractor


extractor = CompanyExtractor()

RAW_FOLDER = Path("data/raw")

TEST_FILES = [
    (
        "7e9845c6-6a7b-4826-ad0b-2db207a7dc15.txt",
        "BPL Limited"
    ),
    (
        "75e30e05-48d5-43b2-b1fd-e847005e67cf.txt",
        "COSMIC CRF LIMITED"
    ),
    (
        "14205c43-30e5-4de5-9033-a545b8c01319.txt",
        "Monarch Surveyors and Engineering Consultants Limited"
    ),
    (
        "defe0439-7b26-4998-bae5-2c796a4619da.txt",
        "Lord's Mark Industries Limited"
    ),
    (
        "8d217589-04c2-4237-ab71-f435b687f54b.txt",
        "HFCL Limited"
    ),
]


for filename, expected in TEST_FILES:

    text = (RAW_FOLDER / filename).read_text(
        encoding="utf-8",
        errors="ignore"
    )

    actual = extractor.extract(text)

    print(f"File     : {filename}")
    print(f"Expected : {expected}")
    print(f"Actual   : {actual}")

    if actual == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")

    print("-" * 60)