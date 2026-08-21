import json
from pathlib import Path


REPORT_FOLDER = Path("reports")
REPORT_FOLDER.mkdir(exist_ok=True)
class AccuracyReport:

    def __init__(self):

        self.report = {}

    def load(self, results):

        self.report = {
            "records_tested": len(results),
            "results": results
        }
    def save(self, filename="accuracy_report.json"):

        output_file = REPORT_FOLDER / filename

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.report,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Report saved: {output_file}")
def main():

    report = AccuracyReport()

    sample_results = []

    report.load(sample_results)

    report.save()


if __name__ == "__main__":

    main()