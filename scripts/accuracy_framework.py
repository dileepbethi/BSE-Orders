"""
Accuracy Framework V1

Measures parser accuracy against
a manually verified Gold Dataset.
"""

import json
from pathlib import Path

GOLD_DATASET = Path("data/gold_dataset.json")
PROCESSED_FOLDER = Path("data/processed")

REPORT_FOLDER = Path("reports")
REPORT_FOLDER.mkdir(exist_ok=True)


class AccuracyFramework:

    def __init__(self):

        self.gold_data = self.load_gold_dataset()

    def load_gold_dataset(self):

        if not GOLD_DATASET.exists():

            print("Gold dataset not found.")

            print("Create: data/gold_dataset.json")

            return {}

        with open(
            GOLD_DATASET,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)
    def load_processed_records(self):

        records = {}

        for file in sorted(PROCESSED_FOLDER.glob("*.json")):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                records[file.stem] = json.load(f)

        return records

    def compare_field(
        self,
        expected,
        actual
    ):

        if expected is None:

            return True

        expected = str(expected).strip().lower()
        actual = str(actual).strip().lower()

        return expected == actual

    def evaluate(self):

        processed = self.load_processed_records()

        results = []

        for key, expected in self.gold_data.items():

            actual = processed.get(key)

            if actual is None:

                continue

            result = {
                "id": key,
                "company": self.compare_field(
                    expected.get("company"),
                    actual.get("company")
                ),
                "announcement_date": self.compare_field(
                    expected.get("announcement_date"),
                    actual.get("announcement_date")
                ),
                "awarding_entity": self.compare_field(
                    expected.get("awarding_entity"),
                    actual.get("awarding_entity")
                ),
                "order_value": self.compare_field(
                    expected.get("order_value"),
                    actual.get("order_value")
                ),
                "execution_period": self.compare_field(
                    expected.get("execution_period"),
                    actual.get("execution_period")
                ),
                "domestic": self.compare_field(
                    expected.get("domestic"),
                    actual.get("domestic")
                ),
                "order_type": self.compare_field(
                    expected.get("order_type"),
                    actual.get("order_type")
                ),
            }

            results.append(result)

        return results
    def print_report(self, results):

        if not results:

            print("No matching records found.")
            return

        fields = [
            "company",
            "announcement_date",
            "awarding_entity",
            "order_value",
            "execution_period",
            "domestic",
            "order_type",
        ]

        print("=" * 60)
        print("BSE ACCURACY REPORT")
        print("=" * 60)
        print(f"Records Tested : {len(results)}")
        print()

        for field in fields:

            passed = sum(
                1 for result in results
                if result[field]
            )

            total = len(results)

            accuracy = (
                passed / total * 100
            ) if total else 0

            print(
                f"{field:<20}"
                f"{passed:>4}/{total:<4}"
                f"{accuracy:>8.2f}%"
            )

        print()
        print("=" * 60)
    def save_report(self, results):

        output_file = REPORT_FOLDER / "accuracy_report.json"

        report = {
            "records_tested": len(results),
            "results": results
        }

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                report,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Report saved: {output_file}")
    def run(self):

       results = self.evaluate()

       self.print_report(results)

       self.save_report(results)

def main():

    framework = AccuracyFramework()

    framework.run()


if __name__ == "__main__":

    main()

