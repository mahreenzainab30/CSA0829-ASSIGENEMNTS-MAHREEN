
from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
STEP_SIZE = Decimal("0.10")

BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

RATE_CARDS = {
    "original": {
        "base_rate": Decimal("30.00"),
        "fat_step": Decimal("0.40"),
        "snf_step": Decimal("0.30")
    },
    "april_june": {
        "base_rate": Decimal("32.00"),
        "fat_step": Decimal("0.45"),
        "snf_step": Decimal("0.30")
    }
}


def round_money(value):
    return value.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )


def count_steps(reading, standard):
    difference = (reading - standard) / STEP_SIZE

    return difference.quantize(
        Decimal("1"),
        rounding=ROUND_HALF_UP
    )


def select_rate_card(month):
    if month in (4, 5, 6):
        return RATE_CARDS["april_june"]

    return RATE_CARDS["original"]


def rate_per_litre(fat, snf, month):
    rates = select_rate_card(month)

    fat_steps = count_steps(fat, STANDARD_FAT)
    snf_steps = count_steps(snf, STANDARD_SNF)

    rate = rates["base_rate"]
    rate += fat_steps * rates["fat_step"]
    rate += snf_steps * rates["snf_step"]

    return round_money(rate)


def payout(litres, fat, snf, month):
    rate = rate_per_litre(fat, snf, month)

    return round_money(litres * rate)


def calculate_bonus(total_litres):
    if total_litres > BONUS_THRESHOLD:
        return round_money(total_litres * BONUS_PER_LITRE)

    return Decimal("0.00")


def ten_day_total(entries, month):
    total_litres = Decimal("0.00")
    payment_total = Decimal("0.00")

    print("\nTEN-DAY PAYMENT DETAILS")

    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf, month)
        payment = payout(litres, fat, snf, month)

        total_litres += litres
        payment_total += payment

        print(
            f"Quantity: {litres} L | "
            f"Fat: {fat}% | SNF: {snf}% | "
            f"Rate: Rs. {rate} | "
            f"Payment: Rs. {payment}"
        )

    bonus = calculate_bonus(total_litres)
    final_total = round_money(payment_total + bonus)

    print("\nTOTAL QUANTITY:", total_litres, "litres")
    print("MILK PAYMENT: Rs.", payment_total)
    print("BONUS: Rs.", bonus)
    print("FINAL TEN-DAY PAYMENT: Rs.", final_total)

    return final_total


# Test data for one farmer across ten days
entries = [
    (
        Decimal("200.00"),
        Decimal("3.56"),
        Decimal("8.54")
    ),
    (
        Decimal("180.00"),
        Decimal("3.45"),
        Decimal("8.50")
    ),
    (
        Decimal("130.00"),
        Decimal("3.50"),
        Decimal("8.60")
    )
]


# Test both original and revised seasons
print("========== APRIL RATE SYSTEM ==========")
april_total = ten_day_total(entries, 4)

print("\n========== ORIGINAL RATE SYSTEM ==========")
original_total = ten_day_total(entries, 1)


# Automated tests
assert rate_per_litre(
    Decimal("3.56"), Decimal("8.54"), 4
) == Decimal("32.45")

assert rate_per_litre(
    Decimal("3.56"), Decimal("8.54"), 1
) == Decimal("30.40")

assert calculate_bonus(
    Decimal("500.00")
) == Decimal("0.00")

assert calculate_bonus(
    Decimal("501.00")
) == Decimal("250.50")

assert april_total == Decimal("16623.00")
assert original_total == Decimal("15602.00")

print("\nALL TASK 12 TESTS PASSED!")
