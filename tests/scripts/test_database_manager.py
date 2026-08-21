"""
Database Manager Read Test
"""

from pathlib import Path

from database.database_manager import DatabaseManager
from pipeline.orderiq_pipeline import OrderIQPipeline


db = DatabaseManager()
db.create_tables()

pipeline = OrderIQPipeline()

filename = "183582ac-c542-404a-8659-ebfe72e55830.txt"

record = pipeline.process_file(
    Path(
        "data/raw",
        filename
    )
)

db.insert_record(record)

records = db.get_all_records()

print("=" * 80)
print("DATABASE READ TEST")
print("=" * 80)

print(f"Total Records : {len(records)}")
print()

last = records[-1]

print("Last Record")

print("-" * 80)

print(last)

db.close()