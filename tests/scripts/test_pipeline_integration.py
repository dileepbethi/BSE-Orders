"""
Pipeline Integration Test

Runs the complete OrderIQ extraction pipeline
on a few sample announcement files.
"""

from pathlib import Path

from scripts.company_extractor_v2 import CompanyExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor_v2 import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.record_validator import RecordValidator


company_extractor = CompanyExtractor()
date_extractor = DateExtractor()
order_value_extractor = OrderValueExtractor()
classifier = AnnouncementClassifier()
validator = RecordValidator()


sample_files = [

    "12fc86a8-feeb-4550-93a1-7acf05fa0497.txt",

    "75e30e05-48d5-43b2-b1fd-e847005e67cf.txt",

    "183582ac-c542-404a-8659-ebfe72e55830.txt",

]


print("=" * 80)
print("ORDERIQ PIPELINE INTEGRATION TEST")
print("=" * 80)

for filename in sample_files:

    text = Path(
        "data/raw",
        filename
    ).read_text(
        encoding="utf-8",
        errors="ignore"
    )

    record = {

        "company": company_extractor.extract(text),

        "announcement_date": date_extractor.extract(text),

        "announcement_type": classifier.classify(text),

        "order_value": order_value_extractor.extract(text),

        "source_file": filename,

    }

    result = validator.validate(record)

    print()

    print("=" * 80)

    print("File :", filename)

    print("=" * 80)

    for key, value in record.items():

        print(f"{key:20}: {value}")

    print()

    print("Valid :", result["valid"])

    print("Errors:", result["errors"])

print()

print("=" * 80)
print("Integration Test Completed")
print("=" * 80)