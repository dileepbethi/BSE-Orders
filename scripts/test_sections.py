from pathlib import Path

from field_parser import FieldParser


RAW = Path("data/raw")

parser = FieldParser()

file = sorted(RAW.glob("*.txt"))[0]

text = file.read_text(
    encoding="utf-8",
    errors="ignore"
)

sections = parser.extract_sections(text)

print("\n" + "=" * 60)
print(file.name)
print("=" * 60)

for number, content in sections.items():

    print()
    print(f"SECTION {number}")
    print("-" * 40)
    print(content[:250])