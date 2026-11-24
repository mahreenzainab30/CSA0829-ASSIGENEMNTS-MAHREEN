
from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

D_BASE_RATE = Decimal("30.00")
D_FAT_STEP = Decimal("0.40")
D_SNF_STEP = Decimal("0.30")
D_STANDARD_FAT = Decimal("3.5")
D_STANDARD_SNF = Decimal("8.5")
D_STEP = Decimal("0.1")
D_ZERO = Decimal("0.00")


def float_payment(litres, fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE

    return round(litres * rate, 2)


def decimal_payment(litres, fat, snf):
    fat_steps = (
        (fat - D_STANDARD_FAT) / D_STEP
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    snf_steps = (
        (snf - D_STANDARD_SNF) / D_STEP
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = D_BASE_RATE
    rate += fat_steps * D_FAT_STEP
    rate += snf_steps * D_SNF_STEP

    rate = rate.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    amount = litres * rate

    return amount.quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def create_entries(number):
    readings = [
        ("10.00", "3.5", "8.5"),
        ("8.50", "4.2", "8.7"),
        ("12.00", "3.1", "8.3"),
        ("5.00", "4.0", "8.5"),
        ("6.00", "3.0", "8.6")
    ]

    entries = []

    for i in range(number):
        litres, fat, snf = readings[i % len(readings)]
        entries.append((litres, fat, snf))

    return entries


def run_float(entries):
    total = 0.0

    for litres, fat, snf in entries:
        total += float_payment(
            float(litres), float(fat), float(snf)
        )

    return round(total, 2)


def run_decimal(entries):
    total = D_ZERO

    for litres, fat, snf in entries:
        total += decimal_payment(
            Decimal(litres),
            Decimal(fat),
            Decimal(snf)
        )

    return total


def measure(function, entries):
    start = perf_counter()
    result = function(entries)
    end = perf_counter()

    return result, end - start


for size in (300, 6000, 150000):
    entries = create_entries(size)

    float_total, float_time = measure(run_float, entries)
    decimal_total, decimal_time = measure(run_decimal, entries)

    difference = abs(
        Decimal(str(float_total)) - decimal_total
    )

    print("\nNumber of payments:", size)
    print("Float total: Rs.", f"{float_total:.2f}")
    print("Decimal total: Rs.", f"{decimal_total:.2f}")
    print("Difference: Rs.", f"{difference:.2f}")
    print("Float time:", f"{float_time:.6f}", "seconds")
    print("Decimal time:", f"{decimal_time:.6f}", "seconds")


# Compare rounding each payment with rounding only the total
sample = create_entries(300)

rounded_individually = run_decimal(sample)

unrounded_total = sum(
    Decimal(litres) *
    (
        D_BASE_RATE
        + (
            (Decimal(fat) - D_STANDARD_FAT) / D_STEP
        ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        * D_FAT_STEP
        + (
            (Decimal(snf) - D_STANDARD_SNF) / D_STEP
        ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        * D_SNF_STEP
    )
    for litres, fat, snf in sample
)

rounded_at_end = unrounded_total.quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)

print("\nROUNDING COMPARISON")
print("Round each payment:", rounded_individually)
print("Round only final total:", rounded_at_end)
rate_table = {}

key = (3.5, 8.5)

if key not in rate_table:
    rate_table[key] = 30.00

rate = rate_table[key]