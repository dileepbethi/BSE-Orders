"""
OrderIQ Parser IO

Handles reading TXT files
and saving processed JSON.
"""

from pathlib import Path
import json


PROCESSED_FOLDER = Path("data/processed")


class ParserIO:

    def __init__(self):

        PROCESSED_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

    def read_text(
        self,
        txt_file: Path
    ) -> str:

        return txt_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    def save_json(
        self,
        txt_file: Path,
        record: dict
    ):

        output = PROCESSED_FOLDER / f"{txt_file.stem}.json"

        output.write_text(

            json.dumps(

                record,

                indent=4,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )

        return output