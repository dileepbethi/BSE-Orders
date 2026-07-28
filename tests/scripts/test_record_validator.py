"""
Record Validator Tests
"""

from scripts.record_validator import RecordValidator


validator = RecordValidator()

record = {

    "company": "HFCL Limited",

    "announcement_date": "2026-07-17",

    "source_file": "abc.pdf",

    "order_value": "18,53,66,820"

}

result = validator.validate(record)

print(result)