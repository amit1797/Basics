age = int(input("Enter your current age: "))
years_left = 90 - age
months_left = years_left * 12
days_left = years_left * 365
weeks_left = days_left // 7
print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months")
