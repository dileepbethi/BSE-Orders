from pathlib import Path

from table_parser import TableParser

RAW_FOLDER = Path("data/raw")

parser = TableParser()

file = RAW_FOLDER / "02402050-f122-4912-a28b-dde573427a6a.txt"

text = file.read_text(
    encoding="utf-8",
    errors="ignore"
)

rows = parser.parse(text)

for i, row in enumerate(rows):

    print(f"{i:03}: {row}")