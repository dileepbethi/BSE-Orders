"""
OrderIQ Pipeline

Official backend entry point.
"""

import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from historical_import_service import HistoricalImportService  # type: ignore[reportMissingImports]


def run_historical():

    service = HistoricalImportService()

    service.run(
        from_date="07-07-2026",
        to_date="03-08-2026"
    )


def run_today():

    today = datetime.today().strftime("%d-%m-%Y")

    service = HistoricalImportService()

    service.run(
        from_date=today,
        to_date=today
    )


def main():

    print()
    print("=" * 70)
    print("ORDERIQ")
    print("=" * 70)
    
    # MODE = "daily"
    MODE = "historical"

    if MODE == "historical":
        run_historical()
    else:
        run_today()


if __name__ == "__main__":
    main()