"""
Company Extractor V2 Benchmark
"""

from pathlib import Path
from time import perf_counter

from scripts.company_extractor_v2 import CompanyExtractor


extractor = CompanyExtractor()

RAW_FOLDER = Path("data/raw")

files = sorted(RAW_FOLDER.glob("*.txt"))

failed = []

start = perf_counter()

for file in files:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    company = extractor.extract(text)

    if not company.strip():
        failed.append(file.name)

end = perf_counter()

total = len(files)
success = total - len(failed)
accuracy = (success / total) * 100

print("=" * 60)
print("Company Extractor V2 Benchmark")
print("=" * 60)

print(f"Total Files : {total}")
print(f"Success     : {success}")
print(f"Failures    : {len(failed)}")
print(f"Accuracy    : {accuracy:.2f}%")
print(f"Runtime     : {end - start:.3f} sec")

print("-" * 60)

if failed:
    print("Failed Files:")
    for file in failed:
        print(" -", file)
else:
    print("All files passed.")

print("=" * 60)