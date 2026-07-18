from playwright.sync_api import Page, expect

from page_waiter import wait_for_bse_filters
from date_picker import DatePicker


SUB_CATEGORY = "Award of Order / Receipt of Order"


def wait_until_option_exists(page: Page, selector: str, option_text: str, timeout=30000):

    page.wait_for_function(
        """
        ([selector, option]) => {
            const ddl = document.querySelector(selector);
            if (!ddl) return false;

            return [...ddl.options].some(
                o => o.text.trim() === option
            );
        }
        """,
        arg=[selector, option_text],
        timeout=timeout,
    )


def select_dropdown(page: Page, selector: str, label: str):

    print(f"[INFO] Selecting -> {label}")

    dropdown = page.locator(selector)

    expect(dropdown).to_be_visible()

    dropdown.select_option(label=label)


def apply_filters(
    page: Page,
    from_date: str,
    to_date: str
):

    picker = DatePicker()

    print("[1/8] Waiting for page...")

    wait_for_bse_filters(page)

    print("[2/8] Segment")

    select_dropdown(
        page,
        "#ddlAnnType",
        "Equity"
    )

    print("[3/8] Waiting for Announcement Type...")

    wait_until_option_exists(
        page,
        "#ddlAnnsubmType",
        "Announcement"
    )

    select_dropdown(
        page,
        "#ddlAnnsubmType",
        "Announcement"
    )

    print("[4/8] Waiting for Category...")

    wait_until_option_exists(
        page,
        "#ddlPeriod",
        "Company Update"
    )

    select_dropdown(
        page,
        "#ddlPeriod",
        "Company Update"
    )

    print("[5/8] Waiting for Sub Category...")

    wait_until_option_exists(
        page,
        "#ddlsubcat",
        SUB_CATEGORY,
        timeout=60000
    )

    select_dropdown(
        page,
        "#ddlsubcat",
        SUB_CATEGORY
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

    page.wait_for_load_state("networkidle")

    print("[SUCCESS] Filters Applied.")