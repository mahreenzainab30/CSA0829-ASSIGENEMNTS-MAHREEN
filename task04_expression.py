
import math

# Standard values
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Farmer details
litres = 8.5
fat = 4.2
snf = 8.7

# Calculate steps
fat_steps = round((fat - STANDARD_FAT) / 0.1)
snf_steps = round((snf - STANDARD_SNF) / 0.1)

# Calculate rate
rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)

# Calculate payment
amount = round(litres * rate, 2)

print("FAT STEPS:", fat_steps)
print("SNF STEPS:", snf_steps)
print("RATE PER LITRE: Rs.", round(rate, 2))
print("TOTAL PAYMENT: Rs.", amount)

print("\nUNEXPECTED RESULTS")
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("-7 // 2:", -7 // 2)
print("-2 ** 2:", -2 ** 2)
print("round(2.5):", round(2.5))

print("\nCOMPARISON OF STEP METHODS")
value = (3.1 - 3.5) / 0.1

print("Original value:", value)
print("round():", round(value))
print("int():", int(value))
print("floor():", math.floor(value))
