from playwright.sync_api import TimeoutError


def wait_for_bse_filters(page):

    page.wait_for_load_state("domcontentloaded")

    page.wait_for_timeout(3000)

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