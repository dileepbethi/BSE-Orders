"""
OrderIQ Company Extractor
Version: 2.0

Purpose
-------
Extract the listed company's name from BSE / NSE corporate
announcement PDFs using multiple extraction strategies.

Pipeline

Normalize Text
      ↓
Signature Strategy
      ↓
On-Behalf Strategy
      ↓
FOR Strategy
      ↓
Heading Strategy
      ↓
Company Field Strategy
      ↓
Validation
      ↓
Return Company
"""

import re


class CompanyExtractor:

    COMPANY_SUFFIXES = (
        "Limited",
        "LIMITED",
        "Ltd",
        "LTD",
        "Technologies",
        "TECHNOLOGIES"
    )

    INVALID_WORDS = {

        "BSE Limited",
        "National Stock Exchange of India Limited",
        "Exchange Plaza",
        "Security Code",
        "Scrip Code",
        "Dear Sir",
        "Dear Sir/Madam"

    }

    def __init__(self):
        pass

    # =====================================================
    # TEXT NORMALIZATION
    # =====================================================

    def normalize_text(self, text: str) -> str:

        if not text:
            return ""

        text = text.replace("\r", "\n")

        text = re.sub(r"\n+", "\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()

    # =====================================================
    # COMPANY CLEANER
    # =====================================================

    def clean_company(self, company: str) -> str:

        if not company:
            return ""

        company = company.strip()

        company = re.sub(r"\s+", " ", company)

        company = company.strip(" :-,.;")

        return company

    # =====================================================
    # VALIDATOR
    # =====================================================

    def is_valid_company(self, company: str) -> bool:

        if not company:
            return False

        company = self.clean_company(company)

        if len(company) < 4:
            return False

        if company in self.INVALID_WORDS:
            return False

        return True
    def is_valid_company(self, company: str) -> bool:

        if not company:
            return False

        company = self.clean_company(company)

        if len(company) < 4:
            return False

        if company in self.INVALID_WORDS:
            return False

        return True