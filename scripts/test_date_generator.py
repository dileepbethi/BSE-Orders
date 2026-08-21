from date_generator import DateGenerator

generator = DateGenerator()

for date in generator.generate(
    "01-01-2026",
    "05-01-2026"
):
    print(date)