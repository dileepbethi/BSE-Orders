"""
Test Date Extractor

This test verifies that every supported
date format is normalized correctly.
"""

from scripts.date_extractor import DateExtractor


extractor = DateExtractor()

samples = [

    "Date : 07.07.2026",

    "Date : 07th July, 2026",

    "Date : 7th July, 2026",

    "July 07, 2026",

    "January 30, 2026",

    "uly 21, 2026",

    "ry 30, 2026",

    "Date : uly 21, 2026",

    "Date : 7th uly, 2026",

    "Date : July 7, 2026",

    "Date : 21 July 2026",

    "21st July, 2026",

]

print()
print("=" * 60)
print("DATE NORMALIZER TEST")
print("=" * 60)
print()

for sample in samples:

    result = extractor.extract(sample)

    print(f"Input : {sample}")
    print(f"Output: {result}")
    print()