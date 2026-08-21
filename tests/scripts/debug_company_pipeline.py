from pathlib import Path

from scripts.company_extractor import CompanyExtractor

e = CompanyExtractor()

text = Path(
    "data/raw",
    "183582ac-c542-404a-8659-ebfe72e55830.txt"
).read_text(
    encoding="utf-8",
    errors="ignore"
)

text = e.normalize_text(text)

print("=" * 70)
print("HEADER")
print("=" * 70)
print(e._header_strategy(text))

print()

print("=" * 70)
print("COMPANY FIELD")
print("=" * 70)
print(e._company_field_strategy(text))

print()

print("=" * 70)
print("BODY")
print("=" * 70)
print(e._body_strategy(text))

print()

print("=" * 70)
print("REFERENCE")
print("=" * 70)
print(e._reference_strategy(text))

print()

print("=" * 70)
print("SIGNATURE")
print("=" * 70)
print(e._signature_strategy(text))