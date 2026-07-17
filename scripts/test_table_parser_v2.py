from pathlib import Path

from table_parser_v2 import TableParserV2


PDF_FOLDER = Path("data/downloads")

pdf = sorted(PDF_FOLDER.glob("*.pdf"))[0]

parser = TableParserV2()

tables = parser.extract_tables(pdf)
table = parser.table_to_dict(
    tables[0]
)

print()

print("=" * 60)

print("TABLE AS DICTIONARY")

print("=" * 60)

for number, item in table.items():

    print()

    print(number)

    print(item["title"])

    print(item["value"])

print("\n" + "=" * 60)
print(pdf.name)
print("=" * 60)

print(f"\nTables Found : {len(tables)}\n")

for table_index, table in enumerate(tables, start=1):

    print("=" * 60)
    print(f"TABLE {table_index}")
    print(f"Page : {table['page']}")
    print("=" * 60)

    rows = table["rows"][:10]

    for row in rows:
        print(row)

    print()