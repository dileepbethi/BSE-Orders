"""
Announcement Classifier Gold Test

Uses the gold dataset stored in:

tests/database/announcement_classifier_gold.csv
"""

import csv
from pathlib import Path

from scripts.announcement_classifier import AnnouncementClassifier


classifier = AnnouncementClassifier()

gold_file = Path(
    "tests/database/announcement_classifier_gold.csv"
)

with open(
    gold_file,
    newline="",
    encoding="utf-8"
) as f:

    reader = csv.DictReader(f)

    print("=" * 70)
    print("ANNOUNCEMENT CLASSIFIER GOLD TEST")
    print("=" * 70)
    print()

    passed = 0
    total = 0

    for row in reader:

        total += 1

        filename = row["filename"]
        expected = row["expected_category"]

        text = Path(
            "data/raw",
            filename
        ).read_text(
            encoding="utf-8",
            errors="ignore"
        )

        actual = classifier.classify(text)

        print("File     :", filename)
        print("Expected :", expected)
        print("Actual   :", actual)

        if expected == actual:

            passed += 1
            print("Result   : PASS")

        else:

            print("Result   : FAIL")

        print("-" * 60)

print()
print("=" * 70)
print(f"Passed : {passed}/{total}")
print("=" * 70)