"""
OrderIQ Record Builder

Creates a structured record from
one TXT file.
"""

from pathlib import Path

from scripts.company_extractor import CompanyExtractor
from scripts.customer_extractor import CustomerExtractor
from scripts.date_extractor import DateExtractor
from scripts.order_value_extractor import OrderValueExtractor
from scripts.announcement_classifier import AnnouncementClassifier
from scripts.field_parser import FieldParser
from scripts.field_cleaner import FieldCleaner


class RecordBuilder:

    def __init__(self):

        self.company = CompanyExtractor()

        self.customer = CustomerExtractor()

        self.date = DateExtractor()

        self.value = OrderValueExtractor()

        self.classifier = AnnouncementClassifier()

        self.field_parser = FieldParser()

        self.cleaner = FieldCleaner()

    def build(
        self,
        txt_file: Path,
        text: str
    ):

        raw_fields = self.field_parser.parse(text)

        fields = self.cleaner.clean(raw_fields)

        company = self.company.extract(text)

        print("=" * 80)
        print("EXTRACTED COMPANY")
        print(company)
        print("=" * 80)

        customer = self.customer.extract(text)

        announcement_date = self.date.extract(text)

        print("=" * 80)
        print("EXTRACTED DATE")
        print(announcement_date)
        print("=" * 80)

        if fields.get("order_value"):

            order_value = fields["order_value"]

        else:

            order_value = self.value.extract(text)

        return {

            "company":
                company,

            "customer":
                customer,

            "announcement_date":
                announcement_date,

            "announcement_type":
                self.classifier.classify(text),

            "awarding_entity":
                fields.get(
                    "entity_awarding",
                    ""
                ),

            "order_value":
                order_value,

            "order_value_crore":
                self.value.convert_to_crore(
                    order_value
                ),

            "execution_period":
                fields.get(
                    "execution_period",
                    ""
                ),

            "order_type":
                fields.get(
                    "order_type",
                    ""
                ),

            "domestic":
                fields.get(
                    "domestic",
                    ""
                ),

            "project_description":
                fields.get(
                    "terms",
                    ""
                ),

            "source_file":
                txt_file.name,

            "exchange":
                "BSE",

            "confidence_score":
                1.0,

            "processing_status":
                "SUCCESS"

        }