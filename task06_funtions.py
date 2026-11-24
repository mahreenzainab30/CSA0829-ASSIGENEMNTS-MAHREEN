
# Task 06: Organising the Calculator Using Functions

# Named constants
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the adjusted milk rate per litre."""

    fat_steps = round((fat - STANDARD_FAT) / 0.1)
    snf_steps = round((snf - STANDARD_SNF) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )

    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the payment for one milk entry."""

    rate = rate_per_litre(fat, snf)
    amount = litres * rate

    return round(amount, 2)


def ten_day_total(payments):
    """Calculate the total payment for ten days."""

    return round(sum(payments), 2)


# Farmer milk entries
entries = [
    (10.0, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12.0, 3.1, 8.3)
]

payments = []

print("KSHEERA MILK CO-OPERATIVE")
print("--------------------------------")

for litres, fat, snf in entries:

    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)

    payments.append(amount)

    print(
        f"Quantity: {litres:5.2f} L | "
        f"Fat: {fat:4.1f}% | "
        f"SNF: {snf:4.1f}% | "
        f"Rate: Rs. {rate:5.2f} | "
        f"Payment: Rs. {amount:7.2f}"
    )

total = ten_day_total(payments)

print("--------------------------------")
print(f"Total Payment: Rs. {total:.2f}")
