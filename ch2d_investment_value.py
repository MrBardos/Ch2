# Interest calculator
my_balance = float(input("What is your balance? "))
my_interest = float(input("What's your interest rate? "))
years = float(input("How many years of growth? "))
my_balance = my_balance * (1 + my_interest) ** years
print("Your investment will be worth $", my_balance)
print("hello world")
