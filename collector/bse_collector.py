"""
OrderIQ Production BSE Collector

Responsibility
--------------
1. Open BSE Website
2. Apply Filters
3. Collect Announcement Metadata

It NEVER:
- Downloads PDFs
- Parses PDFs
- Writes Database
"""

from playwright.sync_api import sync_playwright

from scripts.filters import apply_filters
from scripts.parser import get_result_rows
from collector.scraper import open_bse


class BSECollector:

    URL = "https://www.bseindia.com/corporates/ann.html"

    def collect(
        self,
        from_date: str,
        to_date: str
    ):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False,
                args=[
                    "--disable-gpu",
                    "--disable-dev-shm-usage",
                    "--no-sandbox",
                ]
            )

            context = browser.new_context()

            page = context.new_page()

            page.goto(
                self.URL,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            page.wait_for_selector(
                "#ddlAnnType",
                timeout=60000
            )

            page.wait_for_timeout(2000)

            apply_filters(
                page,
                from_date,
                to_date
            )

            page.wait_for_timeout(3000)

            records = get_result_rows(page)

            context.close()

            browser.close()

            return records
if __name__ == "__main__":

   if __name__ == "__main__":

    collector = BSECollector()

    records = collector.collect(
        from_date="14-07-2026",
        to_date="14-07-2026"
    )

    print()

    print("=" * 70)
    print(f"Collected Records : {len(records)}")
    print("=" * 70)