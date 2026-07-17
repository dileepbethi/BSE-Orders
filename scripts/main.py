"""
BSE Orders Engine
Production Pipeline V1
"""

from collector import BSECollector
from pdf_reader import process_pdfs
from pdf_parser import PDFParser


def main():

    print()
    print("=" * 70)
    print("BSE ORDERS ENGINE V1")
    print("=" * 70)

    collector = BSECollector()

    pdf_files = collector.collect(
        from_date="14-07-2026",
        to_date="14-07-2026"
    )

    if not pdf_files:

        print("\nNo PDFs collected.")
        return

    txt_files = process_pdfs(pdf_files)

    parser = PDFParser()

    parser.process_files(txt_files)

    summary = collector.summary(pdf_files)

    print()
    print("=" * 70)
    print("PIPELINE SUMMARY")
    print("=" * 70)
    print(f"PDFs Collected : {summary['total']}")
    print("=" * 70)

    print()
    print("=" * 70)
    print("PIPELINE COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()