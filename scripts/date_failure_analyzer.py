"""
OrderIQ Date Failure Analyzer

Sprint 4
Version: 1.0
"""

from pathlib import Path

from pipeline.orderiq_pipeline import OrderIQPipeline


class DateFailureAnalyzer:

    def analyze(self, folder_path: str):

        pipeline = OrderIQPipeline()

        failures = []

        folder = Path(folder_path)

        for file in sorted(folder.glob("*.txt")):

            record = pipeline.process_file(file)

            if "Announcement date is empty" in record["errors"]:

                failures.append(file)

        print("=" * 80)
        print("DATE FAILURE ANALYSIS")
        print("=" * 80)

        print(f"Total Date Failures : {len(failures)}")
        print()

        for file in failures:

            print("=" * 80)
            print(file.name)
            print("=" * 80)

            text = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            print(text[:1500])

            print()