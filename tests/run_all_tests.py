"""
OrderIQ Test Runner
"""

import subprocess
import sys

TESTS = [

    "tests.scripts.test_company_extractor_v2",

    "tests.scripts.test_order_value_extractor",

    "tests.scripts.test_announcement_classifier",

    "tests.scripts.test_record_validator",

]

print("=" * 70)
print("ORDERIQ TEST SUITE")
print("=" * 70)

failed = 0

for test in TESTS:

    print(f"\nRunning: {test}\n")

    result = subprocess.run(
        [sys.executable, "-m", test],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if (
        result.returncode != 0
        or "Result   : FAIL" in result.stdout
    ):
        failed += 1

print("=" * 70)

if failed == 0:
    print("ALL TESTS PASSED")
else:
    print(f"{failed} TEST SUITE(S) FAILED")

print("=" * 70)