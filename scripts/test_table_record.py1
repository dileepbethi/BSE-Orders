from pathlib import Path

from table_parser_v2 import TableParserV2

pdf = sorted(
    Path("data/downloads").glob("*.pdf")
)[0]

parser = TableParserV2()

tables = parser.extract_tables(pdf)

record = parser.build_record(
    tables[0]
)

print()

print("=" * 60)
print("NORMALIZED RECORD")
print("=" * 60)

for key, value in record.items():

    print(f"{key:20} : {value}")