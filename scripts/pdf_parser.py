"""
BSE Orders
PDF Parser
Version: 1.0.0

Sprint-1
Part-1, 2, & 3 (Combined)
"""

from pathlib import Path
import json

RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")


class PDFParser:

    def __init__(self):
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

    def read_file(self, file_path: Path):
        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def build_record(self, file_path: Path):
        return {
            "company": "",
            "announcement_date": "",
            "awarding_entity": "",
            "order_value": "",
            "execution_period": "",
            "order_type": "",
            "domestic": "",
            "project_description": "",
            "source_file": file_path.name
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

    def run(self):
        files = self.load_files()

        print()
        print("=" * 60)
        print("BSE ORDERS PARSER")
        print("=" * 60)
        print()

        print(f"Found {len(files)} TXT files")
        print()

        for index, file in enumerate(files, start=1):
            text = self.read_file(file)
            record = self.build_record(file)
            self.save_json(file, record)

            print(f"[{index:02}] {file.name}")
            print(f"     Characters : {len(text)}")
            print(f"     JSON Saved : {file.stem}.json")

        print()
        print("=" * 60)
        print("Parser completed successfully.")
        print("=" * 60)


def main():
    parser = PDFParser()
    parser.run()


if __name__ == "__main__":
    main()