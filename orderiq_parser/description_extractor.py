"""
============================================================
ORDERIQ DESCRIPTION EXTRACTOR
============================================================
Extracts the work / project description from BSE order PDFs.
============================================================
"""

import re

from orderiq_parser.text_processor import TextProcessor


class DescriptionExtractor:

    def __init__(self):

        self.processor = TextProcessor()

        self.patterns = [
            r"(?:for|towards|regarding|to provide|for supply of)\s+(.+?)(?:\.|\n)",
            r"scope of work\s*[:\-]?\s*(.+?)(?:\.|\n)",
            r"description\s*[:\-]?\s*(.+?)(?:\.|\n)",
            r"work order\s*for\s+(.+?)(?:\.|\n)"
        ]
    # ========================================================
    # EXTRACT DESCRIPTION
    # ========================================================

    def extract(
        self,
        text: str
    ) -> str:

        text = self.processor.normalize(text)

        for pattern in self.patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if match:

                description = match.group(1).strip()

                description = re.sub(
                    r"\s+",
                    " ",
                    description
                )

                if len(description) > 500:
                    description = description[:500]

                return description

        return ""
# ========================================================
# STANDALONE TEST
# ========================================================

if __name__ == "__main__":

    from pathlib import Path

    extractor = DescriptionExtractor()

    txt_files = sorted(
        Path("data/raw").glob("*.txt")
    )

    print("=" * 60)
    print("DESCRIPTION EXTRACTOR TEST")
    print("=" * 60)

    success = 0
    failed = 0

    for txt_file in txt_files[:10]:

        print()
        print("-" * 60)
        print(txt_file.name)

        try:

            text = txt_file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            description = extractor.extract(text)

            if description:

                print("SUCCESS")
                print(description)
                success += 1

            else:

                print("NOT FOUND")
                failed += 1

        except Exception as e:

            print("ERROR")
            print(e)
            failed += 1

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"SUCCESS : {success}")
    print(f"FAILED  : {failed}")

    print()
    print("=" * 60)
    print("DESCRIPTION EXTRACTOR TEST COMPLETE")
    print("=" * 60)