"""
BSE Orders PDF Parser
Version: 4.0

JSON + SQLite Pipeline
"""

from pathlib import Path
import json

from company_extractor import CompanyExtractor
from date_extractor import DateExtractor
from order_value_extractor import OrderValueExtractor
from entity_extractor import EntityExtractor
from field_parser import FieldParser
from field_cleaner import FieldCleaner
from database_manager import DatabaseManager


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

        self.database = DatabaseManager()

        self.files = []

        PROCESSED_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

    def load_files(self):

        self.files = sorted(
            RAW_FOLDER.glob("*.txt")
        )

        return self.files

    def read_file(self, file_path):

        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def build_record(self, file_path, text):

        raw_fields = self.field_parser.parse(text)

        fields = self.field_cleaner.clean(raw_fields)

        return {

            "company": self.company_extractor.extract(text),

            "announcement_date": self.date_extractor.extract(text),

            "awarding_entity": fields["entity_awarding"],

            "order_value": self.order_value_extractor.extract(text),

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

    for index, file in enumerate(txt_files, start=1):

        text = self.read_file(file)

        record = self.build_record(
            file,
            text
        )

        self.save_json(
            file,
            record
        )

        self.database.insert(
            record
        )

        print(f"[{index:02}] {file.name}")
        print("     JSON Saved")
        print("     Database Saved")

    print()
    print("=" * 60)
    print(
        f"Database Records : {self.database.count()}"
    )
    print("=" * 60)

    self.database.close()
    def run(self):

        txt_files = self.load_files()

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER")
        print("=" * 60)
        print()

        print(f"Found {len(files)} TXT files")
        print()

        for index, file in enumerate(txt_files, start=1):

            text = self.read_file(file)

            record = self.build_record(
                file,
                text
            )

            self.save_json(
                file,
                record
            )

            self.database.insert(
                record
            )

            print(f"[{index:02}] {file.name}")
            print(f"     JSON Saved")
            print(f"     Database Saved")

        print()

        print("=" * 60)

        print(
            f"Database Records : {self.database.count()}"
        )

        print("=" * 60)

        self.database.close()


def main():

    parser = PDFParser()

    parser.run()


if __name__ == "__main__":

    main()