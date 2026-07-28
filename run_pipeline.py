"""
OrderIQ Pipeline

Official backend entry point.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from historical_import_service import HistoricalImportService


def main():

    print()
    print("=" * 70)
    print("ORDERIQ")
    print("=" * 70)
    print()

    service = HistoricalImportService()

    service.run(
        from_date="07-07-2026",
        to_date="26-07-2026"
    )


if __name__ == "__main__":
    main()