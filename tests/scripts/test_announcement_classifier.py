"""
Announcement Classifier Tests
"""

from pathlib import Path

from scripts.announcement_classifier import AnnouncementClassifier


classifier = AnnouncementClassifier()

RAW_FOLDER = Path("data/raw")

TEST_CASES = [

    (
        "0d2c51ca-ad5b-4a5c-ba6d-f7b0a60f4944.txt",
        "ORDER"
    ),

    (
        "12fc86a8-feeb-4550-93a1-7acf05fa0497.txt",
        "ORDER"
    ),

    (
        "183582ac-c542-404a-8659-ebfe72e55830.txt",
        "ORDER"
    ),

]

for filename, expected in TEST_CASES:

    text = (RAW_FOLDER / filename).read_text(
        encoding="utf-8",
        errors="ignore"
    )

    actual = classifier.classify(text)

    print(f"File     : {filename}")
    print(f"Expected : {expected}")
    print(f"Actual   : {actual}")

    if actual == expected:
        print("Result   : PASS")
    else:
        print("Result   : FAIL")

    print("-" * 60)