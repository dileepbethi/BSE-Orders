"""
OrderIQ Company Extractor
Version: 3.0
"""

import re
from typing import Optional


class CompanyExtractor:

    COMPANY_PATTERN = (
        r"[A-Z][A-Za-z0-9&.,()'/\- ]+"
        r"(?:Limited|LIMITED|Ltd|LTD)"
    )

    INVALID_COMPANIES = {

        "BSE Limited",

        "National Stock Exchange of India Limited",

        "Exchange Plaza",

        "Listing Department",

        "Dear Sir",

        "Dear Sir/Madam",

        "Security Code",

        "Scrip Code"

    }

    def __init__(self):
        pass

    # =====================================================
    # NORMALIZATION
    # =====================================================

    def normalize_text(self, text: str) -> str:

        if not text:
            return ""

        text = text.replace("\r", "\n")

        text = re.sub(r"\n+", "\n", text)

        text = re.sub(r"[ \t]+", " ", text)

        text = text.replace("’", "'")
        text = text.replace("‘", "'")
        text = text.replace("“", '"')
        text = text.replace("”", '"')
        text = text.replace("–", "-")
        text = text.replace("—", "-")

        return text.strip()

    # =====================================================
    # CLEANER
    # =====================================================

    def clean_company(self, company: str) -> str:

        if not company:
            return ""

        company = re.sub(
            r"\s+",
            " ",
            company
        )

        return company.strip(" :-,.;")

    # =====================================================
    # VALIDATION
    # =====================================================

    def is_valid_company(self, company: str) -> bool:

        if not company:

            return False

        company = self.clean_company(company)

        if len(company) < 4:

            return False

        for invalid in self.INVALID_COMPANIES:

            if company == invalid:

                return False

        return True
    # =====================================================
    # HEADER STRATEGY
    # =====================================================

    def _header_strategy(self, text: str) -> Optional[str]:

        lines = text.split("\n")

        for line in lines[:12]:

            line = line.strip()

            if not line:
                continue

            match = re.fullmatch(
                rf"({self.COMPANY_PATTERN})",
                line
            )

            if not match:
                continue

            company = self.clean_company(
                match.group(1)
            )

            if self.is_valid_company(company):

                return company

        return None

    # =====================================================
    # COMPANY FIELD STRATEGY
    # =====================================================

    def _company_field_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"Company\s+Name\s*:\s*({self.COMPANY_PATTERN})",

            rf"Name\s+of\s+Company\s*:\s*({self.COMPANY_PATTERN})",

            rf"Issuer\s+Name\s*:\s*({self.COMPANY_PATTERN})"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            company = self.clean_company(
                match.group(1)
            )

            if self.is_valid_company(company):

                return company

        return None

    # =====================================================
    # BODY STRATEGY
    # =====================================================

    def _body_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+received",

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+secured",

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+been\s+awarded",

            rf"({self.COMPANY_PATTERN})\s+has\s+received",

            rf"({self.COMPANY_PATTERN})\s+has\s+secured",

            rf"({self.COMPANY_PATTERN})\s+has\s+been\s+awarded",

            rf"The\s+({self.COMPANY_PATTERN})\s+is\s+pleased",

            rf"({self.COMPANY_PATTERN})\s+announced",

            rf"({self.COMPANY_PATTERN})\s+informed"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            company = self.clean_company(
                match.group(1)
            )

            if self.is_valid_company(company):

                return company

        return None
    # =====================================================
    # HEADER STRATEGY
    # =====================================================

    def _header_strategy(self, text: str) -> Optional[str]:

        lines = text.split("\n")

        for line in lines[:12]:

            line = line.strip()

            if not line:
                continue

            match = re.fullmatch(
                rf"({self.COMPANY_PATTERN})",
                line
            )

            if not match:
                continue

            company = self.clean_company(match.group(1))

            if not self.is_valid_company(company):
                continue

            return company

        return None

    # =====================================================
    # COMPANY FIELD STRATEGY
    # =====================================================

    def _company_field_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"Company\s+Name\s*:\s*({self.COMPANY_PATTERN})",

            rf"Name\s+of\s+Company\s*:\s*({self.COMPANY_PATTERN})",

            rf"Issuer\s+Name\s*:\s*({self.COMPANY_PATTERN})"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            company = self.clean_company(match.group(1))

            if self.is_valid_company(company):
                return company

        return None

    # =====================================================
    # BODY STRATEGY
    # =====================================================

    def _body_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+received",

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+secured",

            rf"we\s+wish\s+to\s+inform\s+you\s+that\s+({self.COMPANY_PATTERN})\s+has\s+been\s+awarded",

            rf"({self.COMPANY_PATTERN})\s+has\s+received",

            rf"({self.COMPANY_PATTERN})\s+has\s+secured",

            rf"({self.COMPANY_PATTERN})\s+has\s+been\s+awarded",

            rf"The\s+({self.COMPANY_PATTERN})\s+is\s+pleased",

            rf"({self.COMPANY_PATTERN})\s+announced",

            rf"({self.COMPANY_PATTERN})\s+informed"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            company = self.clean_company(match.group(1))

            if self.is_valid_company(company):
                return company

        return None
    # =====================================================
    # REFERENCE STRATEGY
    # =====================================================

    def _reference_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"Ref:\s*.*?(?:M/s\.?\s*)?({self.COMPANY_PATTERN})",

            rf"Reference\s*:.*?(?:M/s\.?\s*)?({self.COMPANY_PATTERN})"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.DOTALL
            )

            if not match:
                continue

            company = self.clean_company(match.group(1))

            if self.is_valid_company(company):
                return company

        return None

    # =====================================================
    # SIGNATURE STRATEGY
    # =====================================================

    def _signature_strategy(self, text: str) -> Optional[str]:

        patterns = [

            rf"({self.COMPANY_PATTERN})\s+Yours\s+faithfully",

            rf"For\s*&\s*on\s*behalf\s*of\s+({self.COMPANY_PATTERN})",

            rf"For,?\s+({self.COMPANY_PATTERN})",

            rf"FOR\s+({self.COMPANY_PATTERN})"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE | re.MULTILINE
            )

            if not match:
                continue

            company = self.clean_company(match.group(1))

            if self.is_valid_company(company):
                return company

        return None

    # =====================================================
    # MAIN EXTRACTION PIPELINE
    # =====================================================

    def extract(self, text: str) -> str:

        text = self.normalize_text(text)

        strategies = [

            self._header_strategy,

            self._company_field_strategy,

            self._body_strategy,

            self._reference_strategy,

            self._signature_strategy

        ]

        for strategy in strategies:

            company = strategy(text)

            if not company:
                continue

            company = self.clean_company(company)

            if self.is_valid_company(company):
                return company

        return ""