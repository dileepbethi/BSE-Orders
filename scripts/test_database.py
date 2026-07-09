from database_manager import DatabaseManager

db = DatabaseManager()

print()

print("=" * 50)

print("Database Created Successfully")

print()

print("Current Records :", db.count())

print("=" * 50)

db.close()