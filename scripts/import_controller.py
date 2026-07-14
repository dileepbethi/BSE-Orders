"""
Import Controller
Version: 1.0

Coordinates historical and daily imports.
"""

from date_range import DateRange


class ImportController:

    def __init__(self):

        self.total_dates = 0
        self.success = 0
        self.failed = 0

    def process_date(self, date):

        """
        Placeholder.

        Later this method will:

        - Open BSE
        - Apply filters
        - Download PDFs
        - Parse PDFs
        - Save to database
        """

        print(f"Processing : {date}")

        self.success += 1

    def import_range(self, start_date, end_date):

        generator = DateRange(
            start_date,
            end_date
        )

        dates = generator.iso_dates()

        self.total_dates = len(dates)

        print()
        print("=" * 60)
        print("IMPORT STARTED")
        print("=" * 60)
        print()

        for date in dates:

            try:

                self.process_date(date)

            except Exception as e:

                self.failed += 1

                print(f"Failed : {date}")

                print(e)

        print()

        print("=" * 60)
        print("IMPORT SUMMARY")
        print("=" * 60)

        print(f"Dates Processed : {self.total_dates}")
        print(f"Successful     : {self.success}")
        print(f"Failed         : {self.failed}")

        print("=" * 60)