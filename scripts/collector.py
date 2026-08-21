from pathlib import Path
from typing import List, Dict

from scraper import open_bse


class BSECollector:
    """
    Production Collector

    Responsibility:
    ----------------
    1. Open BSE
    2. Apply filters
    3. Download PDFs
    4. Return downloaded PDF paths

    It NEVER:
    - Parses PDFs
    - Writes database
    - Extracts entities
    """

    def __init__(self):

        self.download_folder = Path("data/downloads")

    def collect(
        self,
        from_date: str,
        to_date: str
    ) -> List[Path]:

        print("\n" + "=" * 70)
        print("BSE COLLECTOR")
        print("=" * 70)

        pdf_files = open_bse(
            from_date=from_date,
            to_date=to_date
        )

        if pdf_files is None:
            pdf_files = []

        print(f"\nCollected PDFs : {len(pdf_files)}")

        return pdf_files

    def summary(
        self,
        pdf_files: List[Path]
    ) -> Dict:

        return {
            "total": len(pdf_files),
            "files": [str(f) for f in pdf_files]
        }