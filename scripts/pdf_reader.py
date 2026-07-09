from pathlib import Path
import pdfplumber


PDF_FOLDER = Path("data/downloads")
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

    txt_file = RAW_FOLDER / f"{pdf_file.stem}.txt"

    txt_file.write_text(
        text,
        encoding="utf-8"
    )

    return txt_file


def extract_all_pdfs():

    RAW_FOLDER.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(PDF_FOLDER.glob("*.pdf"))

    print(f"\nFound {len(pdf_files)} PDF files\n")

    success = 0
    failed = 0

    for pdf_file in pdf_files:

        try:

            print(f"Reading : {pdf_file.name}")

            text = extract_text(pdf_file)

            txt_file = save_text(pdf_file, text)

            print(f"Saved : {txt_file.name}")

            success += 1

        except Exception as e:

            failed += 1

            print(f"ERROR : {pdf_file.name}")
            print(e)

    print("\n" + "=" * 60)
    print(f"SUCCESS : {success}")
    print(f"FAILED  : {failed}")
    print("=" * 60)


if __name__ == "__main__":

    extract_all_pdfs()