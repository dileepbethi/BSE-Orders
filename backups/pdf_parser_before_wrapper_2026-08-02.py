"""
OrderIQ PDF Parser
Production Version

Pipeline

TXT
 ↓
Quality Check
 ↓
Field Parser
 ↓
Field Cleaner
 ↓
Extractors
 ↓
JSON
 ↓
SQLite
"""

from pathlib import Path
import json

from scripts.company_extractor import CompanyExtractor
from scripts.customer_extractor import CustomerExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.entity_extractor import EntityExtractor
from scripts.field_parser import FieldParser
from scripts.field_cleaner import FieldCleaner
from scripts.table_parser_v2 import TableParserV2
from scripts.quality_classifier_v2 import QualityClassifierV2
from scripts.record_validator import RecordValidator

from database.database_manager import DatabaseManager


RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")


class PDFParser:

    def __init__(self):

        self.company_extractor = CompanyExtractor()

        self.customer_extractor = CustomerExtractor()

        self.date_extractor = DateExtractor()

        self.order_value_extractor = OrderValueExtractor()

        self.announcement_classifier = AnnouncementClassifier()

        self.entity_extractor = EntityExtractor()

        self.field_parser = FieldParser()

        self.field_cleaner = FieldCleaner()

        self.table_parser = TableParserV2()

        self.quality_classifier = QualityClassifierV2()

        self.record_validator = RecordValidator()

        self.database = DatabaseManager()

        self.files = []

        PROCESSED_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_files(self):

        self.files = []

        for txt_file in sorted(RAW_FOLDER.glob("*.txt")):

            pdf_file = txt_file.with_suffix(".pdf")

            self.files.append(
                {
                    "txt": txt_file,
                    "pdf": pdf_file
                }
            )

        return self.files

    def read_file(self, file_path):

        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def save_json(self, file_path, record):

        output = PROCESSED_FOLDER / f"{file_path.stem}.json"

        output.write_text(

            json.dumps(

                record,

                indent=4,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )
    def build_record(self, file_path, text):

        print()
        print("=" * 70)
        print(f"PROCESSING : {file_path.name}")
        print("=" * 70)

        raw_fields = self.field_parser.parse(text)

        print("[1/8] Field Parser")

        fields = self.field_cleaner.clean(raw_fields)

        print("[2/8] Field Cleaner")

        print("[3/8] Company Extractor")

        company = self.company_extractor.extract(text)

        print(company)

        print("[4/8] Customer Extractor")

        customer = self.customer_extractor.extract(text)

        print(customer)

        print("[5/8] Date Extractor")

        announcement_date = self.date_extractor.extract(text)

        print(announcement_date)

        print("[6/8] Order Value Extractor")

        if fields.get("order_value"):

            order_value = fields["order_value"]

        else:

            order_value = self.order_value_extractor.extract(text)

        print(order_value)

        print("[7/8] Announcement Classifier")

        announcement_type = self.announcement_classifier.classify(text)

        print(announcement_type)

        print("[8/8] Record Built")

        record = {

            "company": company,

            "customer": customer,

            "announcement_date": announcement_date,

            "announcement_type": announcement_type,

            "awarding_entity": fields.get("entity_awarding", ""),

            "order_value": order_value,

            "order_value_crore":
                self.order_value_extractor.convert_to_crore(order_value),

            "execution_period":
                fields.get("execution_period", ""),

            "order_type":
                fields.get("order_type", ""),

            "domestic":
                fields.get("domestic", ""),

            "project_description":
                fields.get("terms", ""),

            "source_file":
                file_path.name,

            "exchange":
                "BSE",

            "confidence_score":
                1.0,

            "processing_status":
                "SUCCESS"

        }

        return record
    def run(self, txt_files):

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER")
        print("=" * 60)

        processed = 0
        skipped = 0

        print()
        print(f"Found {len(txt_files)} TXT files")

        for txt_file in txt_files:

            print()
            print("-" * 60)

            try:

                file_path = Path(txt_file)

                text = self.read_file(file_path)

                record = self.build_record(
                    file_path=file_path,
                    text=text
                )

                validation = self.record_validator.validate(record)

                record["valid"] = validation["valid"]
                record["errors"] = validation["errors"]

                self.save_json(
                    file_path=file_path,
                    record=record
                )

                print("JSON Saved")

                if record["valid"]:

                    self.database.insert_record(record)

                    print("Database Saved")

                else:

                    print("Validation Failed")

                processed += 1

            except Exception as e:

                import traceback

                skipped += 1

                print()
                print("=" * 80)
                print("FULL ERROR")
                print("=" * 80)

                traceback.print_exc()

                print("=" * 80)

        print()
        print("=" * 60)
        print("PIPELINE SUMMARY")
        print("=" * 60)
        print(f"Processed Records : {processed}")
        print(f"Skipped Records   : {skipped}")
        print("=" * 60)

        return processed


if __name__ == "__main__":

    from scripts.pdf_reader import process_pdfs

    pdfs = sorted(Path("data/downloads").glob("*.pdf"))

    txts = process_pdfs(pdfs)

    parser = PDFParser()

    parser.run(txts)