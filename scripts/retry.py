from playwright.sync_api import TimeoutError


def retry(action, retries=3):

    last_error = None

    for attempt in range(retries):

        try:

            return action()

        except TimeoutError as e:

            last_error = e

            print(
                f"[Retry {attempt+1}/{retries}]"
            )

    raise last_error