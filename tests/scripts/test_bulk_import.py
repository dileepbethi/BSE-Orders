"""
Bulk Import Service Test
"""

from scripts.bulk_import_service import BulkImportService
from database.database_manager import DatabaseManager

service = BulkImportService()

total = service.import_directory("data/raw")

db = DatabaseManager()

records = db.get_all_records()

print("=" * 80)
print("BULK IMPORT TEST")
print("=" * 80)

print(f"Files Processed : {total}")
print(f"Database Records: {len(records)}")
print(f"Missing Records : {total - len(records)}")

db.close()
service.close()