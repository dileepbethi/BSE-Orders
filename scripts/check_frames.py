from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.bseindia.com/corporates/ann",
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(15000)

    print("=" * 60)
    print("TOTAL FRAMES:", len(page.frames))
    print("=" * 60)

    for i, frame in enumerate(page.frames):

        print()
        print("FRAME", i)
        print("URL :", frame.url)
        print("TITLE :", frame.title())

    input("\nPress Enter...")

    browser.close()