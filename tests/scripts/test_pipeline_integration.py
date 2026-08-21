"""
Pipeline Integration Test

Runs the complete OrderIQ extraction pipeline
on a few sample announcement files.
"""

from pathlib import Path

from scripts.company_extractor import CompanyExtractor
from scripts.customer_extractor import CustomerExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor_v2 import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.record_validator import RecordValidator


company_extractor = CompanyExtractor()
customer_extractor = CustomerExtractor()
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

        "customer": customer_extractor.extract(text),

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

    print(f"{'company':20}: {record['company']}")
    print(f"{'customer':20}: {record['customer']}")
    print(f"{'announcement_date':20}: {record['announcement_date']}")
    print(f"{'announcement_type':20}: {record['announcement_type']}")
    print(f"{'order_value':20}: {record['order_value']}")
    print(f"{'source_file':20}: {record['source_file']}")

    print()
    print("Valid :", result["valid"])
    print("Errors:", result["errors"])

print()
print("=" * 80)
print("Integration Test Completed")
print("=" * 80)