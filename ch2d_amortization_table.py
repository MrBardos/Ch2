def payment(amt, interest, yrs):
    """
    Calculates the monthly payment for a loan.
    :param amt: Loan amount
    :param interest: Annual interest rate as a percent.
    :param yrs: Term of loan in years.
    :return: monthly payment.
    """
    interest /= 100 * 12  # express interest as a monthly interest as a decimal
    n = yrs * 12
    return amt * interest * (1 + interest) ** n / ((1 + interest) ** n - 1)


def amortization(amt, interest, yrs, payment):
    """
    Prints amortization table of a loan
    :param amt: Amount of the loan
    :param payment: Monthly payment
    :param yrs: How long the loan is for
    :return: None. prints a table
    """
    interest /= 100 * 12
    n = yrs * 12
    for i in range(n + 1):
        print(f"{i}: ${amt:,.2f}")
        amt = amt * (1 + interest) - payment


if __name__ == '__main__':
    cases = [(100_000, 6, 30)]

    for a, i, y in cases:
        amortization(a, i, y, payment(a, i, y))