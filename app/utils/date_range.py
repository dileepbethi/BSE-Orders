"""
Date Range Generator
Version: 1.0

Generates dates between a start date and end date.
"""

from datetime import datetime, timedelta


class DateRange:

    def __init__(self, start_date, end_date):

        self.start_date = datetime.strptime(
            start_date,
            "%Y-%m-%d"
        )

        self.end_date = datetime.strptime(
            end_date,
            "%Y-%m-%d"
        )

    def dates(self):

        current = self.start_date

        while current <= self.end_date:

            yield current

            current += timedelta(days=1)

    def formatted_dates(self):

        return [

            d.strftime("%d-%m-%Y")

            for d in self.dates()

        ]

    def iso_dates(self):

        return [

            d.strftime("%Y-%m-%d")

            for d in self.dates()

        ]