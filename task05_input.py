
# Task 05: Input and Type Conversion

print("KSHEERA MILK CO-OPERATIVE")
print("-------------------------")

farmer_id = input("Enter Farmer ID: ").strip()
shift = input("Enter Shift (Morning/Evening): ").strip()

try:
    litres = float(input("Enter milk quantity in litres: ").strip())
    fat = float(input("Enter fat percentage: ").strip())
    snf = float(input("Enter SNF percentage: ").strip())

    if not farmer_id:
        print("Error: Farmer ID cannot be empty.")

    elif shift.lower() not in ("morning", "evening"):
        print("Error: Invalid shift.")

    elif litres <= 0:
        print("Error: Quantity must be greater than zero.")

    elif not 2.0 <= fat <= 7.0:
        print("Error: Fat must be between 2.0 and 7.0.")

    elif snf < 0:
        print("Error: SNF cannot be negative.")

    else:
        print("\nENTRY DETAILS")
        print("-------------------------")
        print(f"Farmer ID: {farmer_id}")
        print(f"Shift: {shift}")
        print(f"Quantity: {litres:8.2f} L")
        print(f"Fat: {fat:8.2f}%")
        print(f"SNF: {snf:8.2f}%")

except ValueError:
    print("Error: Please enter valid numerical values.")
