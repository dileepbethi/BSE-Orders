from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.bseindia.com/corporates/ann",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(15000)

    selects = page.locator("select")

    print("Total SELECT elements:", selects.count())
    print()

    for i in range(selects.count()):

        s = selects.nth(i)

        print("=" * 60)

        print("Index :", i)
        print("id    :", s.get_attribute("id"))
        print("name  :", s.get_attribute("name"))
        print("class :", s.get_attribute("class"))

    input("\nPress Enter...")

    browser.close()