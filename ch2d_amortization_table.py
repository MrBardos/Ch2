def payment(amt, rate, yrs):
    """
    Calculates the monthly payment for a loan.
    :param amt: Loan amount in dollars
    :param rate: Annual interest rate as a percent.
    :param yrs: Term of loan in years.
    :return: monthly payment.
    """
    rate /= 100 * 12  # express interest as a monthly interest as a decimal
    n = yrs * 12
    return amt * rate * (1 + rate) ** n / ((1 + rate) ** n - 1)


def amortization(amt, interest, yrs, payment):
    """
    Prints amortization table of a loan
    :param amt: Amount of the loan.
    :param payment: Monthly payment
    :param yrs: How long the loan is for in years
    :return: None. prints a table
    """
    interest /= 100 * 12
    n = yrs * 12
    print("Month Loan Amount")
    for i in range(n + 1):
        # print(f"{i}: ${amt:,.2f}")
        print(i, round(amt,2))
        amt = amt * (1 + interest) - payment


if __name__ == '__main__':
    cases = [(40_000, 6, 5)]

    for a, i, y in cases:
        print(payment(a, i, y))
        amortization(a, i, y, payment(a, i, y))