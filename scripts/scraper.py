from pathlib import Path

from playwright.sync_api import sync_playwright

from filters import apply_filters
from parser import get_result_rows
from downloader import download_pdf


def open_bse():

    download_folder = Path("data/downloads")
    download_folder.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context(
            accept_downloads=True
        )

        page = context.new_page()

        print("[INFO] Opening BSE...")

        page.goto(
            "https://www.bseindia.com/corporates/ann.html",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_load_state("networkidle")

        print("[INFO] Applying Filters...")

        apply_filters(page)

        records = get_result_rows(page)

        print(f"\n[SUCCESS] Records Found : {len(records)}\n")

        if len(records) == 0:

            print("[INFO] No records found.")

        else:

            print("=" * 80)
            print(f"Downloading {len(records)} PDFs...\n")

            success = 0
            failed = 0

            for i, record in enumerate(records, start=1):

                print("=" * 80)
                print(f"[{i}/{len(records)}]")

                print("HEADER:")
                print(record["header"])
                print()

                print("DESCRIPTION:")
                print(record["description"])
                print()

                print("TIME:")
                print(record["exchange_time"])
                print()

                print("PDF:")
                print(record["pdf"])
                print()

                if record["pdf"]:

                    try:

                        download_pdf(record["pdf"])

                    except Exception as e:

                        failed += 1

                        print(f"[ERROR] {e}")

                else:

                    failed += 1

                    print("[WARNING] No PDF link found.")

            print("\n" + "=" * 80)

            print("DOWNLOAD SUMMARY")

            print(f"Total Records : {len(records)}")
            print(f"Downloaded    : {success}")
            print(f"Failed        : {failed}")

            print("=" * 80)

        input("\nPress Enter to close browser...")

        context.close()

        browser.close()


if __name__ == "__main__":
    open_bse()