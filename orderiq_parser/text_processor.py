"""
============================================================
ORDERIQ
Text Processor
Version : 1.0
============================================================

Purpose
-------
Shared text processing utilities used by all extractors.

This class DOES NOT know anything about:

- Company
- Customer
- Order Value
- Sector
- Project

It only processes text.

============================================================
"""

from __future__ import annotations

import re


class TextProcessor:

    """
    Shared text cleaning utilities.
    """

    def __init__(self):

        pass

    # ========================================================
    # PUBLIC METHODS
    # ========================================================

    def normalize(
        self,
        text: str
    ) -> str:

        """
        Main cleaning pipeline.
        """

        if not text:

            return ""

        text = self.remove_carriage_returns(text)

        text = self.normalize_spaces(text)

        text = self.remove_extra_blank_lines(text)

        text = self.strip_lines(text)

        return text

    def lines(
        self,
        text: str
    ) -> list[str]:

        text = self.normalize(text)

        return text.split("\n")

    def paragraphs(
        self,
        text: str
    ) -> list[str]:

        text = self.normalize(text)

        paragraphs = []

        for block in text.split("\n\n"):

            block = block.strip()

            if block:

                paragraphs.append(block)

        return paragraphs
    def sentences(
        self,
        text: str
    ) -> list[str]:

        """
        Split text into sentences.
        """

        text = self.normalize(text)

        text = text.replace("\n", " ")

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        parts = re.split(
            r'(?<=[.!?])\s+',
            text
        )

        sentences = []

        for sentence in parts:

            sentence = sentence.strip()

            if len(sentence) >= 3:

                sentences.append(sentence)

        return sentences

    # ========================================================
    # LOW LEVEL CLEANING
    # ========================================================

    def remove_carriage_returns(
        self,
        text: str
    ) -> str:

        return text.replace(
            "\r",
            ""
        )

    def normalize_spaces(
        self,
        text: str
    ) -> str:

        lines = []

        for line in text.split("\n"):

            line = re.sub(
                r"[ \t]+",
                " ",
                line
            )

            lines.append(line)

        return "\n".join(lines)

    def remove_extra_blank_lines(
        self,
        text: str
    ) -> str:

        return re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

    def strip_lines(
        self,
        text: str
    ) -> str:

        cleaned = []

        for line in text.split("\n"):

            cleaned.append(
                line.strip()
            )

        return "\n".join(cleaned)
    # ========================================================
    # FILTERING UTILITIES
    # ========================================================

    def remove_short_lines(
        self,
        text: str,
        minimum_length: int = 2
    ) -> str:

        kept = []

        for line in self.lines(text):

            if len(line.strip()) >= minimum_length:

                kept.append(line)

        return "\n".join(kept)


    def remove_duplicate_lines(
        self,
        text: str
    ) -> str:

        seen = set()

        cleaned = []

        for line in self.lines(text):

            key = line.strip()

            if not key:

                continue

            if key in seen:

                continue

            seen.add(key)

            cleaned.append(line)

        return "\n".join(cleaned)


    def remove_lines_containing(
        self,
        text: str,
        keywords: list[str]
    ) -> str:

        cleaned = []

        for line in self.lines(text):

            lower = line.lower()

            skip = False

            for keyword in keywords:

                if keyword.lower() in lower:

                    skip = True
                    break

            if not skip:

                cleaned.append(line)

        return "\n".join(cleaned)


    def keep_lines_containing(
        self,
        text: str,
        keywords: list[str]
    ) -> list[str]:

        matches = []

        for line in self.lines(text):

            lower = line.lower()

            for keyword in keywords:

                if keyword.lower() in lower:

                    matches.append(line)
                    break

        return matches
    # ========================================================
    # SEARCH UTILITIES
    # ========================================================

    def find_first_matching_line(
        self,
        text: str,
        keywords: list[str]
    ) -> str:

        for line in self.lines(text):

            lower = line.lower()

            for keyword in keywords:

                if keyword.lower() in lower:

                    return line

        return ""


    def find_all_matching_lines(
        self,
        text: str,
        keywords: list[str]
    ) -> list[str]:

        matches = []

        for line in self.lines(text):

            lower = line.lower()

            for keyword in keywords:

                if keyword.lower() in lower:

                    matches.append(line)
                    break

        return matches


    def contains_any(
        self,
        text: str,
        keywords: list[str]
    ) -> bool:

        lower = text.lower()

        for keyword in keywords:

            if keyword.lower() in lower:

                return True

        return False


    def contains_all(
        self,
        text: str,
        keywords: list[str]
    ) -> bool:

        lower = text.lower()

        for keyword in keywords:

            if keyword.lower() not in lower:

                return False

        return True


    # ========================================================
    # DEBUG
    # ========================================================

    def preview(
        self,
        text: str,
        lines: int = 15
    ) -> None:

        print("=" * 80)
        print("TEXT PREVIEW")
        print("=" * 80)

        for line in self.lines(text)[:lines]:

            print(line)

        print("=" * 80)
# ========================================================
# STANDALONE TEST
# ========================================================

if __name__ == "__main__":

    from pathlib import Path

    processor = TextProcessor()

    txt_files = sorted(
        Path("data/raw").glob("*.txt")
    )

    print("=" * 60)
    print("ORDERIQ TEXT PROCESSOR TEST")
    print("=" * 60)

    if not txt_files:

        print("No TXT files found in data/raw")

    else:

        sample = txt_files[0]

        print()
        print("Testing File:")
        print(sample.name)

        text = sample.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        clean = processor.normalize(text)

        print()
        print("=" * 60)
        print("NORMALIZED TEXT PREVIEW")
        print("=" * 60)

        processor.preview(clean)

        print()
        print("Statistics")
        print("-" * 60)
        print(f"Characters : {len(clean)}")
        print(f"Lines      : {len(processor.lines(clean))}")
        print(f"Paragraphs : {len(processor.paragraphs(clean))}")
        print(f"Sentences  : {len(processor.sentences(clean))}")

    print()
    print("=" * 60)
    print("TEXT PROCESSOR TEST COMPLETE")
    print("=" * 60)