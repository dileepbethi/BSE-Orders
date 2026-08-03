"""
OrderIQ PDF Parser

Compatibility wrapper.

The real implementation now lives in:

parser/
    io.py
    builder.py
    runner.py
    core.py
"""

from orderiq_parser.core import PDFParser

__all__ = [
    "PDFParser"
]


if __name__ == "__main__":

    from pathlib import Path

    from scripts.pdf_reader import process_pdfs

    pdfs = sorted(
        Path("data/downloads").glob("*.pdf")
    )

    txts = process_pdfs(pdfs)

    parser = PDFParser()

    parser.run(txts)