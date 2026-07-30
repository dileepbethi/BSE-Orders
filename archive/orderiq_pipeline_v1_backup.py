"""
OrderIQ Pipeline

Sprint 2
Version: 1.0
"""

from scripts.company_extractor import CompanyExtractor
from scripts.customer_extractor import CustomerExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor_v2 import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.record_validator import RecordValidator


class OrderIQPipeline:

    def __init__(self):

        self.company_extractor = CompanyExtractor()

        self.customer_extractor = CustomerExtractor()

        self.date_extractor = DateExtractor()

        self.order_value_extractor = OrderValueExtractor()

        self.classifier = AnnouncementClassifier()

        self.validator = RecordValidator()
    def process(self, text: str, source_file: str = "") -> dict:

        record = {

            "company": self.company_extractor.extract(text),

            "customer": self.customer_extractor.extract(text),

            "announcement_date": self.date_extractor.extract(text),

            "announcement_type": self.classifier.classify(text),

            "order_value": self.order_value_extractor.extract(text),

            "source_file": source_file,

        }

        validation = self.validator.validate(record)

        record["valid"] = validation["valid"]

        record["errors"] = validation["errors"]

        return record
    def process_file(self, file_path: str) -> dict:

        from pathlib import Path

        path = Path(file_path)

        text = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return self.process(
            text=text,
            source_file=path.name
        )
    def process_directory(self, folder_path: str) -> list:

        from pathlib import Path

        records = []

        folder = Path(folder_path)

        for file in sorted(folder.glob("*.txt")):

            try:

                record = self.process_file(file)

                records.append(record)

            except Exception as e:

                print(f"Error processing {file.name}: {e}")

        return records