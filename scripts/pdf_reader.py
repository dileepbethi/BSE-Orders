from pathlib import Path
import pdfplumber


RAW_FOLDER = Path("data/raw")


def extract_text(pdf_file: Path) -> str:

    full_text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text + "\n"

    return full_text


def save_text(pdf_file: Path, text: str):

    RAW_FOLDER.mkdir(parents=True, exist_ok=True)

    txt_file = RAW_FOLDER / f"{pdf_file.stem}.txt"

    txt_file.write_text(
        text,
        encoding="utf-8"
    )

    return txt_file


def process_pdf(pdf_path):

    pdf_file = Path(pdf_path)

    print(f"[PDF] Reading : {pdf_file.name}")

    text = extract_text(pdf_file)

    txt_file = save_text(pdf_file, text)

    print(f"[PDF] Saved : {txt_file.name}")

    return txt_file


def process_pdfs(pdf_paths):

    txt_files = []

    success = 0
    failed = 0

    for pdf_path in pdf_paths:

        try:

            txt_file = process_pdf(pdf_path)

            txt_files.append(txt_file)

            success += 1

        except Exception as e:

            failed += 1

            print(e)

    print()
    print("=" * 60)
    print("PDF READER SUMMARY")
    print("=" * 60)
    print(f"SUCCESS : {success}")
    print(f"FAILED  : {failed}")
    print("=" * 60)

    return txt_files