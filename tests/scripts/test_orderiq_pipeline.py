"""
OrderIQ Pipeline Test
"""

from pathlib import Path

from pipeline.orderiq_pipeline import OrderIQPipeline


pipeline = OrderIQPipeline()

filename = "183582ac-c542-404a-8659-ebfe72e55830.txt"

record = pipeline.process_file(
    Path(
        "data/raw",
        filename
    )
)

print("=" * 80)
print("ORDERIQ PIPELINE TEST")
print("=" * 80)

for key, value in record.items():

    print(f"{key:20}: {value}")