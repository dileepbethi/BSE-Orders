from quality_classifier_v2 import QualityClassifierV2


sample_text = """
Disclosure under Regulation 30

Award of Order

The Company has received a Letter of Award from
Bharat Sanchar Nigam Limited (BSNL).

Order Value:
Rs. 47.06 Lakhs

Execution Period:
12 Months
"""


classifier = QualityClassifierV2()

result = classifier.classify(sample_text)

classifier.print_report(result)

assert result["is_procurement"] is True
assert result["score"] >= 4

print("\nTEST PASSED")