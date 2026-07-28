"""
Order Value Extractor Tests
"""

from pathlib import Path

from scripts.order_value_extractor_v2 import OrderValueExtractor


extractor = OrderValueExtractor()

RAW_FOLDER = Path("data/raw")

TEST_CASES = [

    (
        "9ff4d4f2-f882-4d72-b7cd-a6d8ac193bf1.txt",
        "18,53,66,820"
    ),

    (
        "75e30e05-48d5-43b2-b1fd-e847005e67cf.txt",
        "157.97 Lakhs"
    ),

    (
        "0d2c51ca-ad5b-4a5c-ba6d-f7b0a60f4944.txt",
        ""
    ),

]

for filename, expected in TEST_CASES:

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