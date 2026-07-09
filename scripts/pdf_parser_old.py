from pathlib import Path
import re
import json


RAW_FOLDER = Path("data/raw")


class PDFParser:

    def __init__(self):
        self.reset()

    def reset(self):
        self.fields = {
            "company": "",
            "announcement_date": "",
            "awarding_entity": "",
            "order_value": "",
            "order_type": "",
            "execution_period": "",
            "domestic": "",
            "project_description": "",
            "source_file": ""
        }

    def normalize_text(self, text: str) -> str:

        text = text.replace("\r", "")

        lines = []

        for line in text.split("\n"):

            line = line.strip()

            if line:
                lines.append(line)

        return "\n".join(lines)

    def load_file(self, txt_file: Path):

        self.reset()

        self.fields["source_file"] = txt_file.name

        text = txt_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return self.normalize_text(text)

    def extract_company(self, text):

        patterns = [

            r"For\s*&\s*on\s*behalf\s*of\s+([A-Za-z0-9&.,()'\/\- ]+?(?:Limited|Ltd\.?))",

            r"For\s+([A-Za-z0-9&.,()'\/\- ]+?(?:Limited|Ltd\.?))",

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:

                company = match.group(1).strip()

                company = re.sub(
                    r"^&?\s*on\s*behalf\s*of\s*",
                    "",
                    company,
                    flags=re.IGNORECASE
                )

                self.fields["company"] = company

                return

    def extract_date(self, text):
        
        

        patterns = [

            r"Date\s*[:\-]?\s*(\d{2}\.\d{2}\.\d{4})",

            r"Date\s*[:\-]?\s*(\d{2}-\d{2}-\d{4})",

            r"Date\s*[:\-]?\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})",

            r"Date\s*[:\-]?\s*(\d{1,2}\s+[A-Za-z]+\s+\d{4})",

        ]
        
    def clean_value(self, value: str) -> str:

        value = value.replace("\n", " ")

        value = re.sub(r"\s+", " ", value)

        return value.strip(" :;,-")


    def find_after_label(self, text: str, labels):

        lines = text.split("\n")

        for i, line in enumerate(lines):

            lower = line.lower()

            for label in labels:

                if label.lower() in lower:

                    # Value in same line
                    pos = lower.find(label.lower())

                    value = line[pos + len(label):].strip(" :-")

                    if value:
                        return self.clean_value(value)

                    # Otherwise next non-empty line
                    for j in range(i + 1, min(i + 6, len(lines))):

                        candidate = lines[j].strip()

                        if candidate:

                            if len(candidate) > 3:

                                return self.clean_value(candidate)

        return ""

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:

                self.fields["announcement_date"] = match.group(1).strip()

                return

    def parse(self, txt_file: Path):

        text = self.load_file(txt_file)

        self.extract_company(text)

        self.extract_date(text)

        return self.fields


def main():

    parser = PDFParser()

    txt_files = sorted(RAW_FOLDER.glob("*.txt"))

    print(f"\nFound {len(txt_files)} TXT files\n")

    for txt_file in txt_files:

        result = parser.parse(txt_file)

        print("=" * 80)

        print(
            json.dumps(
                result,
                indent=4,
                ensure_ascii=False
            )
        )


if __name__ == "__main__":
    main()