from pdf_reader import process_pdfs
from pdf_parser import PDFParser
from collector import BSECollector
from date_generator import DateGenerator


class HistoricalImportService:

    def __init__(self):

        self.collector = BSECollector()
        self.generator = DateGenerator()
        

    def run(
        self,
        from_date: str,
        to_date: str
    ):

        print()
        print("=" * 70)
        print("ORDERIQ HISTORICAL IMPORT")
        print("=" * 70)

        total_days = 0
        total_pdfs = 0
        total_records = 0

        for current_date in self.generator.generate(
            from_date,
            to_date
        ):

            total_days += 1

            print()
            print("-" * 70)
            print(f"Processing : {current_date}")
            print("-" * 70)

            try:

                pdf_files = self.collector.collect(
                    from_date=current_date,
                    to_date=current_date
                )

                pdf_count = len(pdf_files)

                total_pdfs += pdf_count

                print(f"Collected PDFs : {pdf_count}")

                if pdf_count == 0:

                    print("No PDFs found.")
                    continue

                print("Converting PDFs to TXT...")

                txt_files = process_pdfs(pdf_files)

                print("PDF to TXT Completed")

                print("Starting PDF Parser...")

                parser = PDFParser()

                processed = parser.run(txt_files)

                total_records += processed

                print("PDF Parsing Completed")

            except Exception as e:

                print()
                print("[ERROR]")
                print(current_date)
                print(e)

        print()
        print("=" * 70)
        print("IMPORT SUMMARY")
        print("=" * 70)
        print(f"Days Processed     : {total_days}")
        print(f"PDFs Downloaded    : {total_pdfs}")
        print(f"Records Imported   : {total_records}")
        print("=" * 70)