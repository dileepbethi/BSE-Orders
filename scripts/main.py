"""
BSE Orders Engine
Main Pipeline
"""

from scraper import open_bse
from pdf_reader import process_pdfs
from pdf_parser import PDFParser


def main():

    print()
    print("=" * 60)
    print("BSE ORDERS ENGINE")
    print("=" * 60)

    pdf_files = open_bse(
    from_date="14-07-2026",
    to_date="14-07-2026"
)

    txt_files = process_pdfs(pdf_files)

    parser = PDFParser()

    parser.process_files(txt_files)

    print()
    print("=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()