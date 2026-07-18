from playwright.sync_api import Page

BASE_URL = "https://www.bseindia.com"


def get_result_rows(page: Page):

    records = []

    rows = page.locator("tbody tr")
    total = rows.count()

    print(f"\n[INFO] Total tbody TR Rows : {total}\n")

    i = 0

    while i < total:

        try:
            row = rows.nth(i)

            pdf_locator = row.locator("a.tablebluelink")

            if pdf_locator.count() == 0:
                i += 1
                continue

            header = row.inner_text().strip()

            href = pdf_locator.first.get_attribute("href")

            pdf = ""

            if href:

                if href.startswith("http"):
                    pdf = href
                else:
                    pdf = BASE_URL + href

            description = ""
            exchange_time = ""

            if i + 1 < total:
                description = rows.nth(i + 1).inner_text().strip()

            if i + 2 < total:
                exchange_time = rows.nth(i + 2).inner_text().strip()

            records.append(
                {
                    "header": header,
                    "description": description,
                    "exchange_time": exchange_time,
                    "pdf": pdf,
                }
            )

            print(f"[FOUND] {header[:80]}")

        except Exception as e:

            print(f"[WARNING] Row {i}: {e}")

        i += 1

    return records