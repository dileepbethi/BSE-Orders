"""
Search Engine Test

Sprint 5
Version: 2.0
"""

from database.search_engine import SearchEngine

search = SearchEngine()

print("=" * 80)
print("ORDERIQ SEARCH ENGINE")
print("=" * 80)

print()

print("DATABASE STATISTICS")
print("-" * 80)

print(f"Total Records   : {search.get_total_records()}")

print(f"Total Companies : {search.get_total_companies()}")

print(f"Total Customers : {search.get_total_customers()}")

print(f"Total Orders    : {search.get_total_orders()}")

print()

print("=" * 80)

print("COMPANY SEARCH")

print("=" * 80)

results = search.search_company("Innovision")

print(f"Results Found : {len(results)}")

print()

for row in results:

    print("-" * 80)

    print(f"Company  : {row[1]}")

    print(f"Customer : {row[2]}")

    print(f"Date     : {row[3]}")

    print(f"Value    : {row[5]}")

search.close()