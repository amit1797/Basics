print("Welcome to the Tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What Percentage tip would you like to give? 10, 12 or 15 percent? "))
people = int(input("How many people to split the bill? "))
amount = bill + (bill * tip)/100
amount_per_person = round((amount / people), 2)
print(f"Each Person should pay: ${amount_per_person}")