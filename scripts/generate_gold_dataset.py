import json
from pathlib import Path


PROCESSED_FOLDER = Path("data/processed")
GOLD_DATASET = Path("data/gold_dataset.json")
class GoldDatasetGenerator:

    def __init__(self):

        self.records = {}

    def load_processed_records(self):

        for file in sorted(PROCESSED_FOLDER.glob("*.json")):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                self.records[file.stem] = json.load(f)
    def generate(self):

        gold_dataset = {}

        for record_id, record in self.records.items():

            gold_dataset[record_id] = {
                "company": record.get("company"),
                "announcement_date": record.get("announcement_date"),
                "awarding_entity": record.get("awarding_entity"),
                "order_value": record.get("order_value"),
                "execution_period": record.get("execution_period"),
                "domestic": record.get("domestic"),
                "order_type": record.get("order_type")
            }

        with open(
            GOLD_DATASET,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                gold_dataset,
                f,
                indent=4,
                ensure_ascii=False
            )
def main():

    generator = GoldDatasetGenerator()

    generator.load_processed_records()

    generator.generate()

    print("Gold dataset generated successfully.")


if __name__ == "__main__":

    main()