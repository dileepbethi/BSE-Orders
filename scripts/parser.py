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

            header = rows.nth(i).inner_text().strip()

        except:

            i += 1
            continue

        if (
            "Announcement under Regulation 30" not in header
            or
            "Award_of_Order_Receipt_of_Order" not in header
        ):
            i += 1
            continue

        description = ""
        exchange_time = ""
        pdf = ""

        # Description
        if i + 1 < total:

            description = rows.nth(i + 1).inner_text().strip()

        # Exchange Time
        if i + 2 < total:

            exchange_time = rows.nth(i + 2).inner_text().strip()

        # PDF Link
        try:

            href = rows.nth(i).locator(
                "a.tablebluelink"
            ).get_attribute("href")

            if href:

                pdf = BASE_URL + href

        except:

            pass

        records.append({

            "header": header,

            "description": description,

            "exchange_time": exchange_time,

            "pdf": pdf

        })

        i += 4

    return records