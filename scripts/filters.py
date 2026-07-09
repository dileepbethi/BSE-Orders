from playwright.sync_api import Page


def apply_filters(page: Page):

    print("[1/8] Waiting for page...")

    page.wait_for_load_state("domcontentloaded")

    page.locator("#ddlAnnType").wait_for(state="visible", timeout=60000)
    page.locator("#ddlAnnsubmType").wait_for(state="visible", timeout=60000)
    page.locator("#ddlPeriod").wait_for(state="visible", timeout=60000)
    page.locator("#ddlsubcat").wait_for(state="visible", timeout=60000)

    print("[2/8] Segment")

    page.locator("#ddlAnnType").select_option(label="Equity")

    print("[3/8] Announcement Submission Type")

    page.locator("#ddlAnnsubmType").select_option(label="Announcement")

    print("[4/8] Category")

    page.locator("#ddlPeriod").select_option(label="Company Update")

    print("[INFO] Waiting for Sub Category options...")

    page.locator("#ddlsubcat").locator("option").nth(1).wait_for(
        state="attached",
        timeout=60000
    )

    print("[5/8] Sub Category")

    page.locator("#ddlsubcat").select_option(
        label="Award of Order / Receipt of Order"
    )

    print("[6/8] From Date")

    page.get_by_role("dialog", name="dd/mm/yyyy").first.click()
    page.get_by_label("Tuesday, 7 July,").get_by_text("7", exact=True).click()

    print("[7/8] To Date")

    page.get_by_role("dialog", name="dd/mm/yyyy").nth(1).click()
    page.get_by_label("Tuesday, 7 July,").get_by_text("7", exact=True).click()

    print("[8/8] Submit")

    page.get_by_role("button", name="Submit").click()

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(2000)

    print("[SUCCESS] Filters Applied.")