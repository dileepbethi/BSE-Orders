"""
OrderIQ Bulk Import Service

Sprint 3
Version: 1.0
"""

from pathlib import Path

from pipeline.orderiq_pipeline import OrderIQPipeline


class BulkImportService:

    def __init__(self):

        self.pipeline = OrderIQPipeline(
            auto_save=True
        )

    def import_directory(self, folder_path: str) -> int:

        folder = Path(folder_path)

        total = 0

        for file in sorted(folder.glob("*.txt")):

            try:

                self.pipeline.process_file(file)

                total += 1

            except Exception as e:

                print(f"ERROR : {file.name}")

                print(e)

        return total

    def close(self):

        self.pipeline.close()