import json
from pathlib import Path

PROCESSED_DIR = Path("data/processed")
REVIEW_DIR = Path("data/gold_review")


def main():

    REVIEW_DIR.mkdir(exist_ok=True)

    files = sorted(PROCESSED_DIR.glob("*.json"))

    print(f"Found {len(files)} processed files")
    for file in files:

        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        review = {
            "id": data.get("id", ""),
            "company": data.get("company", ""),
            "announcement_date": data.get("announcement_date", ""),
            "awarding_entity": data.get("awarding_entity", ""),
            "order_value": data.get("order_value", ""),
            "execution_period": data.get("execution_period", ""),
            "domestic": data.get("domestic", ""),
            "order_type": data.get("order_type", "")
        }
        output_file = REVIEW_DIR / file.name

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                review,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(f"Exported: {file.name}")
if __name__ == "__main__":
    main()