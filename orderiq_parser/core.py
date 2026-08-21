"""
OrderIQ Parser Core

Public API for the parser package.
"""

from orderiq_parser.runner import ParserRunner


class PDFParser:

    def __init__(self):

        self.runner = ParserRunner()

    def run(
        self,
        txt_files
    ):

        return self.runner.run(
            txt_files
        )