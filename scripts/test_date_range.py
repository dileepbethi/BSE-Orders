from date_range import DateRange


generator = DateRange(

    "2026-07-08",

    "2026-07-10"

)

print()

print("=" * 60)

print("ISO FORMAT")

print()

for d in generator.iso_dates():

    print(d)

print()

print("=" * 60)

print("DISPLAY FORMAT")

print()

for d in generator.formatted_dates():

    print(d)

print("=" * 60)