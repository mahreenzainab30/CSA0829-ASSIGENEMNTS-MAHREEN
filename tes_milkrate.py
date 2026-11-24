
# Importing the module
import milkrate

# Calling functions from the module
print("MODULE IMPORT DEMONSTRATION")

rate = milkrate.rate_per_litre(4.2, 8.7)
amount = milkrate.payout(8.5, 4.2, 8.7)

print("Rate per litre:", rate)
print("Payment amount:", amount)

# Importing an individual function
from milkrate import payout

print("Payment using direct import:", payout(10, 3.5, 8.5))

# Importing with an alias
import milkrate as mr

print("Payment using alias:", mr.payout(12, 3.1, 8.3))
