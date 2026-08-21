from datetime import datetime, timedelta


class DateGenerator:

    def generate(
        self,
        from_date: str,
        to_date: str
    ):

        start = datetime.strptime(
            from_date,
            "%d-%m-%Y"
        )

        end = datetime.strptime(
            to_date,
            "%d-%m-%Y"
        )

        current = start

        while current <= end:

            yield current.strftime("%d-%m-%Y")

            current += timedelta(days=1)