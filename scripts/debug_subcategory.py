from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    def log_request(request):
        if "api" in request.url.lower():
            print("\nREQUEST")
            print(request.method)
            print(request.url)

    def log_response(response):
        if "api" in response.url.lower():
            print("\nRESPONSE")
            print(response.status)
            print(response.url)

    page.on("request", log_request)
    page.on("response", log_response)

    page.goto(
        "https://www.bseindia.com/corporates/ann.html"
    )

    print()
    print("===================================")
    print("MANUAL MODE")
    print("===================================")
    print()

    print("1. Reload page if blank")
    print("2. Select Equity")
    print("3. Select Announcement")
    print("4. Select Company Update")
    print("5. Select Award of Order / Receipt of Order")
    print("6. DON'T press Submit")
    print()

    input("After all selections are completed, press Enter...")