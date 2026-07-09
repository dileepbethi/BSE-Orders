from playwright.sync_api import Page

BASE_URL = "https://www.bseindia.com"


def get_result_rows(page: Page):

    records = []

    rows = page.locator("tr")
    total = rows.count()

    print(f"\n[INFO] Total TR Rows : {total}\n")

    current = None

    for i in range(total):

        try:
            text = rows.nth(i).inner_text(timeout=1000).strip()

        except:
            continue

        if not text:
            continue

        # Ignore date row
        if text.startswith("07 Jul") or text.startswith("08 Jul"):
            continue

        # Company Header
        if (
            "Announcement under Regulation 30" in text
            and "Award_of_Order_Receipt_of_Order" in text
        ):

            if current:
                records.append(current)

            current = {
                "header": text,
                "description": "",
                "exchange_time": "",
                "pdf": ""
            }

            try:
                href = rows.nth(i).locator("a.tablebluelink").get_attribute("href")

                if href:

                    current["pdf"] = BASE_URL + href

                    print("\n-----------------------")
                    print(current["header"])
                    print(current["pdf"])
                    print("-----------------------")

            except:
                pass

            continue

        if current is None:
            continue

        # Exchange Time

        if "Exchange Received Time" in text:

            current["exchange_time"] = text

            continue

        # Description

        if current["description"] == "":

            current["description"] = text

    if current:

        records.append(current)

    return records