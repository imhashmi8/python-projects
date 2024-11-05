print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_bill = bill * tip_as_percent + bill
total_bill_per_person = round(total_bill / people)
print(f"Each person needs to pay :  +${total_bill_per_person}")


