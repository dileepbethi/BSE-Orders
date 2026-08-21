import json
from pathlib import Path


PROCESSED_FOLDER = Path("data/processed")
GOLD_DATASET = Path("data/gold_dataset.json")
class GoldDatasetBuilder:

    def __init__(self):

        self.processed_records = {}
        self.gold_dataset = {}

    def load_processed_records(self):

        for file in sorted(PROCESSED_FOLDER.glob("*.json")):

            with open(
                file,
                "r",
                encoding="utf-8"
            ) as f:

                self.processed_records[file.stem] = json.load(f)

    def load_gold_dataset(self):

        if GOLD_DATASET.exists():

            with open(
                GOLD_DATASET,
                "r",
                encoding="utf-8"
            ) as f:

                self.gold_dataset = json.load(f)
    def merge(self):

        for record_id, record in self.processed_records.items():

            if record_id not in self.gold_dataset:

                self.gold_dataset[record_id] = {
                    "company": record.get("company", ""),
                    "announcement_date": record.get("announcement_date", ""),
                    "awarding_entity": record.get("awarding_entity", ""),
                    "order_value": record.get("order_value", ""),
                    "execution_period": record.get("execution_period", ""),
                    "domestic": record.get("domestic", ""),
                    "order_type": record.get("order_type", "")
                }

    def save(self):

        with open(
            GOLD_DATASET,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.gold_dataset,
                f,
                indent=4,
                ensure_ascii=False
            )
def main():

    builder = GoldDatasetBuilder()

    builder.load_processed_records()

    builder.load_gold_dataset()

    builder.merge()

    builder.save()

    print("Gold dataset builder completed successfully.")


if __name__ == "__main__":

    main()