"""
Pipeline Auto Save Test
"""

from pathlib import Path

from pipeline.orderiq_pipeline import OrderIQPipeline
from database.database_manager import DatabaseManager


pipeline = OrderIQPipeline(auto_save=True)

db = DatabaseManager()

record = pipeline.process_file(
    Path(
        "data/raw",
        "183582ac-c542-404a-8659-ebfe72e55830.txt"
    )
)

records = db.get_all_records()

print("=" * 80)
print("PIPELINE AUTO SAVE TEST")
print("=" * 80)

print(f"Database Records : {len(records)}")
print()

print("Latest Record")

print("-" * 80)

print(records[-1])

pipeline.close()

db.close()