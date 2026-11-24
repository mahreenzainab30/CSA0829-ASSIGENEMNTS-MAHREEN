
from decimal import Decimal

# 1,000 payments of Rs 33.40 and three small adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total


print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))
print(0.1 + 0.2 == 0.3,
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

import sys
from decimal import Decimal

float_value = 33.40
decimal_value = Decimal("33.40")
paise_value = 3340

print("Float memory:", sys.getsizeof(float_value), "bytes")
print("Decimal memory:", sys.getsizeof(decimal_value), "bytes")
print("Integer paise memory:", sys.getsizeof(paise_value), "bytes")

print("\nDecimal from string:", Decimal("0.1") + Decimal("0.2"))
print("Decimal from float:", Decimal(float(0.1)) + Decimal(float(0.2)))
