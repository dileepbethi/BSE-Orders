from pathlib import Path

from field_parser import FieldParser

RAW_FOLDER = Path("data/raw")

parser = FieldParser()

text = (
    RAW_FOLDER /
    "02402050-f122-4912-a28b-dde573427a6a.txt"
).read_text(
    encoding="utf-8",
    errors="ignore"
)

fields = parser.parse(text)

for key, value in fields.items():

    print(f"{key:20} : {value}")