# Tip Calculator

print("Welcome to the tip Calculator!\n")

bill = float(input("What was the total bill ? $"))
tip_percentage = int(input("How much tip would you like to give ? 10, 12, 15 ? "))
people_to_split_bill = int(input("How many people to split the bill ? "))
tip = (tip_percentage / 100) * bill
totalBill = bill + tip

#payment_per_person = round(totalBill / people_to_split_bill, 2)

#We wanzt to force the formating of 2 decimal places even if the value is something like 33.60. We do this using the format function as done below.

payment_per_person = "{:.2f}".format(totalBill / people_to_split_bill)
print(f"Each person should pay:  ${payment_per_person}")
