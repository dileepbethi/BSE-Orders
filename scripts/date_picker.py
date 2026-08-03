from datetime import datetime


class DatePicker:

    def split(self, date_string):

        dt = datetime.strptime(date_string, "%d-%m-%Y")

        return (
            dt.day,
            dt.month,
            dt.year
        )

    def select_from_date(
        self,
        page,
        date_string
    ):

        day, month, year = self.split(date_string)

        # Open calendar
        page.get_by_role(
            "textbox",
            name="From Date :"
        ).click()

        # Select Year
        page.get_by_label(
            "Select year"
        ).select_option(str(year))

        # Select Month
        page.get_by_label(
            "Select month"
        ).select_option(str(month))

        # Select Day
        page.locator(
            ".ngb-dp-day .btn-light:not(.outside)"
        ).filter(
            has_text=str(day)
        ).first.click()
    def select_to_date(
        self,
        page,
        date_string
    ):

        day, month, year = self.split(date_string)

        page.get_by_role(
            "textbox",
            name="To Date :"
        ).click()

        page.get_by_label(
            "Select year"
        ).select_option(str(year))

        page.get_by_label(
            "Select month"
        ).select_option(str(month))

        page.locator(
            ".ngb-dp-day .btn-light:not(.outside)"
        ).filter(
            has_text=str(day)
        ).first.click()