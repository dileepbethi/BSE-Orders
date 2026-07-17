from pathlib import Path

from pdf_reader import process_pdfs

pdfs = sorted(
    Path("data/downloads").glob("*.pdf")
)[:2]

items = process_pdfs(pdfs)

print()

print("=" * 60)
print("PDF READER V2")
print("=" * 60)

for item in items:

    print()

    print(item["pdf"])

    print(item["txt"])