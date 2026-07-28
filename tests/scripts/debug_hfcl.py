from pathlib import Path

from scripts.company_extractor import CompanyExtractor

e = CompanyExtractor()

text = Path(
    "data/raw/8d217589-04c2-4237-ab71-f435b687f54b.txt"
).read_text(
    encoding="utf-8",
    errors="ignore"
)

text = e.normalize_text(text)

print("=" * 60)
print("HEADER")
print("=" * 60)
print(e._header_strategy(text))

print("=" * 60)
print("COMPANY FIELD")
print("=" * 60)
print(e._company_field_strategy(text))

print("=" * 60)
print("BODY")
print("=" * 60)
print(e._body_strategy(text))

print("=" * 60)
print("REFERENCE")
print("=" * 60)
print(e._reference_strategy(text))

print("=" * 60)
print("SIGNATURE")
print("=" * 60)
print(e._signature_strategy(text))

print("=" * 60)
print("FINAL")
print("=" * 60)
print(e.extract(text))