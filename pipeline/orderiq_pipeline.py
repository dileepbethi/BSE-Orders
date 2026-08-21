"""
OrderIQ Pipeline

Sprint 3
Version: 2.0
"""

from pathlib import Path

from scripts.company_extractor import CompanyExtractor
from scripts.customer_extractor import CustomerExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor_v2 import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.record_validator import RecordValidator
from database.database_manager import DatabaseManager


class OrderIQPipeline:

    def __init__(self, auto_save: bool = False):

        self.company_extractor = CompanyExtractor()

        self.customer_extractor = CustomerExtractor()

        self.date_extractor = DateExtractor()

        self.order_value_extractor = OrderValueExtractor()

        self.classifier = AnnouncementClassifier()

        self.validator = RecordValidator()

        self.auto_save = auto_save

        if self.auto_save:

            self.db = DatabaseManager()

            self.db.create_tables()

    def process(self, text: str, source_file: str = "") -> dict:

        record = {

            "company": self.company_extractor.extract(text),

            "customer": self.customer_extractor.extract(text),

            "announcement_date": self.date_extractor.extract(text),

            "announcement_type": self.classifier.classify(text),

            "order_value": self.order_value_extractor.extract(text),

            "source_file": source_file,

            "exchange": "BSE",

            "confidence_score": 1.0,

            "processing_status": "SUCCESS",

        }

        validation = self.validator.validate(record)

        record["valid"] = validation["valid"]

        record["errors"] = validation["errors"]

        if self.auto_save and record["valid"]:

            self.db.insert_record(record)

        return record

    def process_file(self, file_path: str) -> dict:

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

        records = []

        folder = Path(folder_path)

        for file in sorted(folder.glob("*.txt")):

            try:

                record = self.process_file(file)

                records.append(record)

            except Exception as e:

                print(f"Error processing {file.name}: {e}")

        return records

    def close(self):

        if self.auto_save:

            self.db.close()