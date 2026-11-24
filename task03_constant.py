
# Task 03: Variables and Constants

# Defining named constants
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Farmer details
farmer_id = "F001"
litres = 10.0
fat = 4.2
snf = 8.7

# Multiple assignment
a, b, c = 10, 20, 30

print("MILK CO-OPERATIVE RATE CARD")
print("---------------------------")

print("Base Rate:", BASE_RATE)
print("Standard Fat:", STANDARD_FAT)
print("Standard SNF:", STANDARD_SNF)
print("Fat Adjustment:", FAT_STEP_VALUE)
print("SNF Adjustment:", SNF_STEP_VALUE)

print("\nFARMER DETAILS")
print("Farmer ID:", farmer_id)
print("Milk Quantity:", litres)
print("Fat:", fat)
print("SNF:", snf)

# Demonstrating dynamic typing
value = 100
print("\nInitial Value:", value)
print("Initial Type:", type(value))

value = "Milk Payment"
print("Changed Value:", value)
print("Changed Type:", type(value))

# Demonstrating swapping
x = 10
y = 20

x, y = y, x

print("\nAfter Swapping:")
print("x =", x)
print("y =", y)
