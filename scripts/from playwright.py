from playwright.sync_api import sync_playwright

from filters import apply_filters
from parser import get_result_rows


def open_bse():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        print("[INFO] Opening BSE...")

        page.goto("https://www.bseindia.com/corporates/ann.html")

        page.wait_for_load_state("networkidle")

        print("[INFO] Applying Filters...")

        apply_filters(page)

        rows = get_result_rows(page)

        print(f"[SUCCESS] Parser returned {rows.count()} rows.")

        input("\nPress Enter to close browser...")

        browser.close()


if __name__ == "__main__":
    open_bse()