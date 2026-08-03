"""
Record Validator
Version: 2.0

Validates extracted records before saving them
to the database.
"""

from datetime import datetime


class RecordValidator:

    def __init__(self):

        self.errors = []

    def validate_company(self, record):

        company = (record.get("company") or "").strip()

        if not company:

            self.errors.append("❌ Company is empty")

            return False

        return True

    def validate_date(self, record):

        date = (record.get("announcement_date") or "").strip()

        if not date:

            self.errors.append("❌ Announcement date is empty")

            return False

        try:

            datetime.strptime(date, "%Y-%m-%d")
            return True

        except ValueError:

            self.errors.append(
                f"❌ Invalid date : {date}"
            )

            return False

    def validate_source_file(self, record):

        source = (record.get("source_file") or "").strip()

        if not source:

            self.errors.append(
                "❌ Source file missing"
            )

            return False

        return True

    def validate_order_value(self, record):

        value = record.get("order_value")

        if value is None:

            self.errors.append(
                "❌ Order value missing"
            )

        return True

    def validate(self, record):

        self.errors = []

        self.validate_company(record)
        self.validate_date(record)
        self.validate_source_file(record)
        self.validate_order_value(record)

        if self.errors:

            print()
            print("=" * 60)
            print("VALIDATION ERRORS")
            print("=" * 60)

            for error in self.errors:
                print(error)

            print("=" * 60)
            print()

        return {

            "valid": len(self.errors) == 0,

            "errors": self.errors

        }