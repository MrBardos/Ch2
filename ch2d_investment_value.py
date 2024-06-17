def investment_growth(value, rate, years):
    """
    Calculates the value of an investment.
    :param value: initial value of the investment in dollars.
    :param rate: interest rate expressed as a percent
    :param years: number of years that the investment grows
    :return: new value rounded to the nearest cent.
    """
    return value * (1 + rate)**years


balance = float(input("What is your balance? "))
my_interest = float(input("What's your interest rate? "))
years = float(input("How many years of growth? "))
my_balance = my_balance * (1 + my_interest) ** years
print("Your investment will be worth $", my_balance)
print("hello world2")
