from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://www.bseindia.com/corporates/ann",
        wait_until="domcontentloaded"
    )

    print("Waiting 15 seconds for Angular...")

    page.wait_for_timeout(15000)

    print("\nCurrent URL:")
    print(page.url)

    print("\nTitle:")
    print(page.title())

    selectors = [
        "#ddlAnnType",
        "#ddlAnnsubmType",
        "#ddlPeriod",
        "#ddlsubcat"
    ]

    print("\nSelector Counts")

    for selector in selectors:

        count = page.locator(selector).count()

        print(selector, "=", count)

    page.screenshot(
        path="page_debug.png",
        full_page=True
    )

    print("\nScreenshot saved.")

    input("\nPress Enter...")

    browser.close()