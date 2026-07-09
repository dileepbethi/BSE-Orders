from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    print("Opening...")

    page.goto(
        "https://www.bseindia.com/corporates/ann.html",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    print("TITLE :", page.title())
    print("URL   :", page.url)

    print("BODY LENGTH :", len(page.locator("body").inner_text()))

    print("ddlAnnType :", page.locator("#ddlAnnType").count())
    print("ddlAnnsubmType :", page.locator("#ddlAnnsubmType").count())
    print("ddlPeriod :", page.locator("#ddlPeriod").count())
    print("ddlsubcat :", page.locator("#ddlsubcat").count())

    input("Press Enter...")

    browser.close()