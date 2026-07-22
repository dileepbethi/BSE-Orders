"""
BSE Orders PDF Parser
Version: 5.0

Pipeline:
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

from company_extractor import CompanyExtractor
from date_extractor import DateExtractor
from order_value_extractor import OrderValueExtractor
from entity_extractor import EntityExtractor
from field_parser import FieldParser
from field_cleaner import FieldCleaner
from table_parser_v2 import TableParserV2
from database_manager import DatabaseManager
from quality_classifier_v2 import QualityClassifierV2


RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")


class PDFParser:

    def __init__(self):

        self.company_extractor = CompanyExtractor()
        self.date_extractor = DateExtractor()
        self.order_value_extractor = OrderValueExtractor()
        self.entity_extractor = EntityExtractor()

        self.field_parser = FieldParser()
        self.field_cleaner = FieldCleaner()
        self.table_parser = TableParserV2()

        self.quality_classifier = QualityClassifierV2()

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

            self.files.append({
                "txt": txt_file,
                "pdf": pdf_file
            })

        return self.files

    def read_file(self, file_path):

        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    def build_record(self, file_path, text):

        raw_fields = self.field_parser.parse(text)

        fields = self.field_cleaner.clean(raw_fields)

        order_value = (
            fields["order_value"]
            if fields["order_value"]
            else self.order_value_extractor.extract(text)
        )

        return {

            "company": self.company_extractor.extract(text),

            "announcement_date": self.date_extractor.extract(text),

            "awarding_entity": fields["entity_awarding"],

            "order_value": order_value,

            "order_value_crore":
                self.order_value_extractor.convert_to_crore(order_value),

            "execution_period": fields["execution_period"],

            "order_type": fields["order_type"],

            "domestic": fields["domestic"],

            "project_description": fields["terms"],

            "source_file": file_path.name

        }
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
    def process_files(self, txt_files):

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER")
        print("=" * 60)
        print()

        print(f"Found {len(txt_files)} TXT files")
        print()

        success = 0

        for index, item in enumerate(txt_files, start=1):

            try:

                txt_file = item["txt"]

                text = self.read_file(txt_file)

                quality = self.quality_classifier.classify(text)

                if not quality["is_procurement"]:

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

                success += 1

                print(f"[{index:02}] {txt_file.name}")
                print("     JSON Saved")
                print("     Database Saved")

            except Exception as e:

                print(f"[ERROR] {item['txt'].name}")
                print(e)

        print()
        print("=" * 60)
        print("PIPELINE SUMMARY")
        print("=" * 60)
        print(f"Total Files       : {len(txt_files)}")
        print(f"Processed Records : {success}")
        print(f"Skipped Records   : {len(txt_files) - success}")
        print(f"Database Records  : {self.database.count()}")
        print("=" * 60)

        self.database.close()

        return success
    def run(self):

        txt_files = self.load_files()

        if not txt_files:

            print("No TXT files found in data/raw")
            return

        self.process_files(txt_files)
def main():

    parser = PDFParser()

    parser.run()


if __name__ == "__main__":
    main()