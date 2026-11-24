
from decimal import Decimal, ROUND_HALF_UP

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")

FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")


def money(value):
    """Round a monetary value to two decimal places."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def validate_entry(farmer_id, litres, fat, snf):
    """Validate one farmer's milk entry."""

    if not farmer_id.strip():
        return False, "Farmer ID cannot be empty"

    try:
        litres = Decimal(str(litres).strip())
        fat = Decimal(str(fat).strip())
        snf = Decimal(str(snf).strip())

    except Exception:
        return False, "Invalid numerical input"

    if not all(x.is_finite() for x in (litres, fat, snf)):
        return False, "Values must be finite numbers"

    if litres <= 0:
        return False, "Quantity must be greater than zero"

    if not MIN_FAT <= fat <= MAX_FAT:
        return False, "Fat must be between 2.0 and 7.0"

    if snf < 0:
        return False, "SNF cannot be negative"

    return True, "Valid entry"


def rate_per_litre(fat, snf):
    """Calculate the adjusted milk rate."""

    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    fat_steps = int(
        ((fat - STANDARD_FAT) / Decimal("0.1"))
        .quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    )

    snf_steps = int(
        ((snf - STANDARD_SNF) / Decimal("0.1"))
        .quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    )

    rate = (
        BASE_RATE
        + Decimal(fat_steps) * FAT_STEP_VALUE
        + Decimal(snf_steps) * SNF_STEP_VALUE
    )

    return money(rate)


def payout(litres, fat, snf):
    """Calculate the payment for one valid milk entry."""

    litres = Decimal(str(litres))
    rate = rate_per_litre(fat, snf)

    return money(litres * rate)


# Five sample farmer entries
entries = [
    ("F001", "10.0", "3.5", "8.5"),
    ("F002", "8.5", "4.2", "8.7"),
    ("F003", "12.0", "3.1", "8.3"),
    ("F004", "5.0", "4.0", "8.5"),
    ("F005", "6.0", "3.0", "8.6")
]

total = Decimal("0.00")

print("KSHEERA MILK CO-OPERATIVE")
print("=" * 75)

print(
    f"{'ID':<8}{'Litres':>9}{'Fat':>9}"
    f"{'SNF':>9}{'Rate':>13}{'Payment':>14}"
)

print("-" * 75)

for farmer_id, litres, fat, snf in entries:

    valid, message = validate_entry(
        farmer_id, litres, fat, snf
    )

    if valid:

        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)

        total += amount

        print(
            f"{farmer_id:<8}{float(litres):>9.2f}"
            f"{float(fat):>9.2f}{float(snf):>9.2f}"
            f"{rate:>13.2f}{amount:>14.2f}"
        )

    else:
        print(f"{farmer_id}: {message}")

print("-" * 75)
print(f"TOTAL PAYMENT: Rs. {money(total):.2f}")


# Automated testing
print("\nAUTOMATED TESTING")

assert payout("10", "3.5", "8.5") == Decimal("300.00")
assert payout("8.5", "4.2", "8.7") == Decimal("283.90")
assert payout("12", "3.1", "8.3") == Decimal("333.60")

assert validate_entry("F001", "10", "2.0", "8.5")[0]
assert validate_entry("F001", "10", "7.0", "8.5")[0]

assert not validate_entry("F001", "-5", "3.5", "8.5")[0]
assert not validate_entry("F001", "10", "8.0", "8.5")[0]
assert not validate_entry("F001", "ten", "3.5", "8.5")[0]
assert not validate_entry("", "10", "3.5", "8.5")[0]

print("All automated tests passed!")
