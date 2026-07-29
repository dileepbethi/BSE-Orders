"""
OrderIQ Directory Processing Test
"""

from pipeline.orderiq_pipeline import OrderIQPipeline

pipeline = OrderIQPipeline()

records = pipeline.process_directory("data/raw")

print("=" * 80)
print("ORDERIQ DIRECTORY TEST")
print("=" * 80)

print(f"Total Records : {len(records)}")
print()

for record in records[:5]:

    print(record["company"])
    print(record["customer"])
    print(record["order_value"])
    print("-" * 60)