def payment(amt, annual_rate, yrs):
    """
    Calculates the monthly payment for a loan.
    :param amt: Loan amount in dollars
    :param annual_rate: Annual interest rate as a percent.
    :param yrs: Term of loan in years.
    :return: monthly payment.
    """
    rate = annual_rate / 100 / 12  # monthly interest rate as a decimal
    n = yrs * 12
    return amt * rate * (1 + rate) ** n / ((1 + rate) ** n - 1)

amt = float(input("Enter the principal: "))
annual_rate = float(input("Enter the annual interest rate: "))
years = int(input("Enter the term in years: "))
rate = annual_rate / 100 / 12
n = years * 12
monthly_payment = payment(amt, annual_rate, years)
print("Monthly Payment = ", round(monthly_payment,2))
print("Month Loan Amount")
for i in range(n + 1):
    # print(f"{i}: ${amt:,.2f}")
    print(i, round(amt,2))
    amt = amt * (1 + rate) - monthly_payment