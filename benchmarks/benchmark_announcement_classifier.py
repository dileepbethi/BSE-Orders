"""
Announcement Classifier Benchmark
"""

from collections import Counter
from pathlib import Path

from scripts.announcement_classifier import AnnouncementClassifier


RAW_FOLDER = Path("data/raw")

classifier = AnnouncementClassifier()

counter = Counter()

files = sorted(RAW_FOLDER.glob("*.txt"))

for file in files:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    category = classifier.classify(text)

    counter[category] += 1


print("=" * 60)
print("Announcement Classifier Benchmark")
print("=" * 60)

print(f"Total Files : {len(files)}")

print()

for category in sorted(counter):
    print(f"{category:20} : {counter[category]}")

print("=" * 60)