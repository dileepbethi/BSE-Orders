from pathlib import Path
import requests

DOWNLOAD_FOLDER = Path("data/downloads")


def download_pdf(pdf_url: str):

    DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    filename = pdf_url.split("/")[-1]

    save_path = DOWNLOAD_FOLDER / filename

    print(f"\n[INFO] Downloading PDF")
    print(pdf_url)

    response = requests.get(
        pdf_url,
        timeout=60,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/138.0 Safari/537.36"
            )
        }
    )

    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)

    print(f"[SUCCESS] Saved : {save_path}")

    return str(save_path)