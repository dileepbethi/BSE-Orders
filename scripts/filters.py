from playwright.sync_api import Page

from date_picker import DatePicker


def apply_filters(
    page: Page,
    from_date: str,
    to_date: str
):

    picker = DatePicker()

    print("[1/8] Waiting for page...")

    page.wait_for_load_state("domcontentloaded")

    page.locator("#ddlAnnType").wait_for(
        state="visible",
        timeout=60000
    )

    page.locator("#ddlAnnsubmType").wait_for(
        state="visible",
        timeout=60000
    )

    page.locator("#ddlPeriod").wait_for(
        state="visible",
        timeout=60000
    )

    page.locator("#ddlsubcat").wait_for(
        state="visible",
        timeout=60000
    )

    print("[2/8] Segment")

    page.locator("#ddlAnnType").select_option(
        label="Equity"
    )

    print("[3/8] Announcement Submission Type")

    page.locator("#ddlAnnsubmType").select_option(
        label="Announcement"
    )

    print("[4/8] Category")

    page.locator("#ddlPeriod").select_option(
        label="Company Update"
    )

    print("[INFO] Waiting for Sub Category options...")

    page.wait_for_function("""
    () => {
        const ddl = document.querySelector("#ddlsubcat");
        return ddl && ddl.options.length > 1;
    }
    """, timeout=60000)

    print("[5/8] Sub Category")

    page.locator("#ddlsubcat").select_option(
        label="Award of Order / Receipt of Order"
    )

    print("[6/8] From Date")

    picker.select_from_date(
        page,
        from_date
    )

    print("[7/8] To Date")

    picker.select_to_date(
        page,
        to_date
    )

    print("[8/8] Submit")

    page.get_by_role(
        "button",
        name="Submit"
    ).click()

    page.wait_for_timeout(3000)

    print("[SUCCESS] Filters Applied.")