"""
Analyze Bulk Import Results
"""

from pathlib import Path

from pipeline.orderiq_pipeline import OrderIQPipeline


pipeline = OrderIQPipeline()

total = 0
valid = 0
invalid = 0

invalid_files = []

for file in sorted(Path("data/raw").glob("*.txt")):

    total += 1

    record = pipeline.process_file(file)

    if record["valid"]:

        valid += 1

    else:

        invalid += 1

        invalid_files.append(
            (
                file.name,
                record["errors"]
            )
        )

print("=" * 80)
print("BULK IMPORT ANALYSIS")
print("=" * 80)

print(f"Total Files : {total}")
print(f"Valid Files : {valid}")
print(f"Invalid Files : {invalid}")

print()

print("INVALID FILES")

print("-" * 80)

for filename, errors in invalid_files:

    print(filename)

    print(errors)

    print()