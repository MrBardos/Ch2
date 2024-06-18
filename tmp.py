# Sample program to illustrate Pythonic styling.
def effective_rate(continuous_rate):
    from math import e
    """
    Calculates the effective annual interest rate.
    :param continuous_rate: continuously compounding interest rate as a percent
    :return: effective annual interest rate as a percent
    """
    if continuous_rate < 0:
        raise ValueError("Interest rate cannot be negative.")
    else:
        return 100 * e**(continuous_rate / 100) - 100

print("Continuous  |   Effective")
print("-" * 25)
test_cases = [100, 0, -5, 0.1, 50, 10,]
for n in test_cases:
    print(f"{n:12.2f}|{effective_rate(n):12.2f}") # format numbers to 2 decimal places in 12 spaces