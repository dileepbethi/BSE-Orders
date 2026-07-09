"""
Entity Extractor Test
"""

from pathlib import Path

from entity_extractor import EntityExtractor

RAW_FOLDER = Path("data/raw")

extractor = EntityExtractor()

files = sorted(RAW_FOLDER.glob("*.txt"))

for file in files:

    text = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    value = extractor.extract(text)

    print(f"{file.name}")
    print(f"Entity : {value}")
    print("-" * 60)