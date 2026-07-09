from pathlib import Path

RAW_FOLDER = Path("data/raw")

KEYWORDS = [
    "entity awarding",
    "name of the entity",
    "awarding the"
]

for file in sorted(RAW_FOLDER.glob("*.txt")):

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    lines = text.splitlines()

    for i, line in enumerate(lines):

        lower = line.lower()

        if any(keyword in lower for keyword in KEYWORDS):

            print("=" * 80)
            print(file.name)
            print("=" * 80)

            start = max(0, i - 3)
            end = min(len(lines), i + 10)

            for j in range(start, end):
                print(f"{j:03}: {lines[j]}")

            print()