from database_manager import DatabaseManager

db = DatabaseManager()

print("\n" + "=" * 60)
print("DATABASE TEST")
print("=" * 60)

print("\nTotal Records:")
print(db.count())

print("\nLatest 5 Records:")

rows = db.latest(5)

for row in rows:
    print("-" * 60)
    print(f"Company : {row[1]}")
    print(f"Date    : {row[2]}")
    print(f"Value   : {row[4]}")
    print(f"Source  : {row[9]}")

db.close()