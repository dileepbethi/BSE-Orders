"""
BSE Orders PDF Parser V2

Clean orchestration layer.

Pipeline:

TXT
 ↓
Quality Classifier
 ↓
Field Parser
 ↓
Field Cleaner
 ↓
Company Extractor
 ↓
Date Extractor
 ↓
Order Value Extractor
 ↓
JSON
 ↓
Database
"""

from pathlib import Path
import json

from company_extractor import CompanyExtractor
from date_extractor import DateExtractor
from order_value_extractor import OrderValueExtractor
from field_parser import FieldParser
from field_cleaner import FieldCleaner
from quality_classifier_v2 import QualityClassifierV2
from database_manager import DatabaseManager


RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")


class PDFParserV2:

    def __init__(self):

        self.company_extractor = CompanyExtractor()
        self.date_extractor = DateExtractor()
        self.order_value_extractor = OrderValueExtractor()

        self.field_parser = FieldParser()
        self.field_cleaner = FieldCleaner()
        self.quality_classifier = QualityClassifierV2()

        self.database = DatabaseManager()

        PROCESSED_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )
    def load_files(self):
        """
        Returns all TXT files found in data/raw.
        """

        return sorted(RAW_FOLDER.glob("*.txt"))

    def read_file(self, file_path: Path) -> str:
        """
        Reads a TXT file.
        """

        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def build_record(self, file_path: Path, text: str):

        raw_fields = self.field_parser.parse(text)

        fields = self.field_cleaner.clean(raw_fields)

        order_value = fields.get("order_value")

        if not order_value:
            order_value = self.order_value_extractor.extract(text)

        return {

            "company": self.company_extractor.extract(text),

            "announcement_date":
                self.date_extractor.extract(text),

            "awarding_entity":
                fields.get("entity_awarding"),

            "order_value":
                order_value,

            "execution_period":
                fields.get("execution_period"),

            "order_type":
                fields.get("order_type"),

            "domestic":
                fields.get("domestic"),

            "project_description":
                fields.get("terms"),

            "source_file":
                file_path.name
        }
    def save_json(self, file_path: Path, record: dict):

        output_file = PROCESSED_FOLDER / f"{file_path.stem}.json"

        output_file.write_text(
            json.dumps(
                record,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

    def process_files(self):

        txt_files = self.load_files()

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER V2")
        print("=" * 60)
        print()

        print(f"Found {len(txt_files)} TXT files")
        print()

        processed = 0
        skipped = 0

        for index, txt_file in enumerate(txt_files, start=1):

            try:

                text = self.read_file(txt_file)

                quality = self.quality_classifier.classify(text)

                if not quality["is_procurement"]:

                    skipped += 1

                    print(f"[{index:02}] {txt_file.name}")
                    print("     Skipped (Not a procurement announcement)")
                    continue

                record = self.build_record(
                    txt_file,
                    text
                )

                self.save_json(
                    txt_file,
                    record
                )

                self.database.insert(
                    record
                )

                processed += 1

                print(f"[{index:02}] {txt_file.name}")
                print("     JSON Saved")
                print("     Database Saved")

            except Exception as e:

                print(f"[ERROR] {txt_file.name}")
                print(e)

        return processed, skipped
    def run(self):

        processed, skipped = self.process_files()

        print()
        print("=" * 60)
        print("PIPELINE SUMMARY")
        print("=" * 60)
        print(f"Processed Records : {processed}")
        print(f"Skipped Records   : {skipped}")
        print(f"Database Records  : {self.database.count()}")
        print("=" * 60)

        self.database.close()

        return processed


def main():

    parser = PDFParserV2()

    parser.run()


if __name__ == "__main__":

    main()        