"""
Quality Classifier V2

Determines whether a PDF is likely to be a procurement /
order announcement before sending it to the parser.
"""

import re


class QualityClassifierV2:

    def __init__(self):

        self.positive_patterns = [
            r"award of order",
            r"receipt of order",
            r"purchase order",
            r"work order",
            r"letter of award",
            r"\bloa\b",
            r"\bloi\b",
            r"contract",
            r"customer",
            r"project",
            r"execution",
            r"order value",
            r"annexure",
            r"disclosure under regulation 30",
        ]

        self.negative_patterns = [
            r"board meeting",
            r"newspaper",
            r"postal ballot",
            r"voting results",
            r"shareholding",
            r"agm",
            r"egm",
            r"financial results",
            r"quarterly results",
            r"investor presentation",
            r"credit rating",
            r"analyst",
            r"transcript",
            r"newspaper publication",
        ]
        
    def classify(self, text: str):
        """
        Returns a classification result.

        Output:
        {
            "is_procurement": True,
            "score": 13,
            "confidence": 86,
            "positive_hits": [...],
            "negative_hits": [...]
        }
        """

        text = text.lower()

        score = 0

        positive_hits = []
        negative_hits = []

        for pattern in self.positive_patterns:

            if re.search(pattern, text, re.IGNORECASE):
                score += 2
                positive_hits.append(pattern)

        for pattern in self.negative_patterns:

            if re.search(pattern, text, re.IGNORECASE):
                score -= 2
                negative_hits.append(pattern)

        confidence = min(100, max(0, score * 10))

        return {
            "is_procurement": score >= 4,
            "score": score,
            "confidence": confidence,
            "positive_hits": positive_hits,
            "negative_hits": negative_hits,
        }
    
    def classify_file(self, text: str):
        """
        Convenience wrapper used by the pipeline.
        """

        return self.classify(text)

    def is_high_quality(self, text: str) -> bool:
        """
        Returns True if the document is considered
        suitable for parsing.
        """

        result = self.classify(text)
        return result["is_procurement"]

    def print_report(self, result):

        print("=" * 60)
        print("QUALITY CLASSIFICATION")
        print("=" * 60)

        print(f"Procurement : {result['is_procurement']}")
        print(f"Score       : {result['score']}")
        print(f"Confidence  : {result['confidence']}%")

        print("\nPositive Matches")
        for item in result["positive_hits"]:
            print("  +", item)

        print("\nNegative Matches")
        for item in result["negative_hits"]:
            print("  -", item)