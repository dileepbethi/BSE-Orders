"""
OrderIQ Parser Runner

Runs the parser over a list of TXT files.
"""

from pathlib import Path
import traceback

from orderiq_parser.io import ParserIO
from orderiq_parser.builder import RecordBuilder

from scripts.record_validator import RecordValidator

from database.database_manager import DatabaseManager


class ParserRunner:

    def __init__(self):

        self.io = ParserIO()

        self.builder = RecordBuilder()

        self.validator = RecordValidator()

        self.database = DatabaseManager()

    def run(
        self,
        txt_files
    ):

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER")
        print("=" * 60)

        processed = 0
        skipped = 0

        print()
        print(f"Found {len(txt_files)} TXT files")

        for item in txt_files:

            try:

                if isinstance(item, dict):

                    txt_file = item["txt"]

                else:

                    txt_file = Path(item)

                print()
                print("-" * 60)
                print(txt_file.name)

                text = self.io.read_text(txt_file)

                record = self.builder.build(
                    txt_file,
                    text
                )

                validation = self.validator.validate(
                    record
                )

                record["valid"] = validation["valid"]

                record["errors"] = validation["errors"]

                self.io.save_json(
                    txt_file,
                    record
                )

                if record["valid"]:

                    self.database.insert_record(
                        record
                    )

                    print("Database Saved")

                else:

                    print("Validation Failed")

                processed += 1

            except Exception as e:

                import traceback

                skipped += 1

                print()

                print("=" * 80)
                print("FULL TRACEBACK")
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