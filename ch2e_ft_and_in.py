
import math
import random
# Choose which function to write. The first is easier.
# Advanced: try your converter with 3.1 feet. See if you get the correct answer
# or a floating point rounding error. For extra challenge, deal with this error.
#
def to_ft_and_in(decimal_feet):
    """
    Converts decimal feet to feet and inches
    :param decimal_feet: feet expressed as a decimal (assume positive numbers)
    :return: tuple with number of feet, inches rounded to two decimal places
    """
    feet = int(decimal_feet)
    inches = round((decimal_feet - feet) * 12, 2)
    return feet, inches

def to_ft_in_sixteenths(decimal_feet):
    """
    Converts decimal feet to feet, inches, and 16th of an inch in lowest terms
    :param decimal_feet:
    :return: tuple with 4 integers: feet, inches, and numerator and denominator of fraction of an inch
    : Note: there is a Fraction module, but for a programming challenge,
    : don't use it until you successfully write the program without it.
    """
    feet = int(decimal_feet)
    inches = round(decimal_feet * 12) % 12
    sixteenths = round(decimal_feet * 12 * 16) % 16
    divisor = math.gcd(sixteenths, 16)
    return feet, inches, sixteenths // divisor, 16 // divisor

if __name__ == "__main__":
    cases = [12, 14.75, 0, 100.1, 0.2, 15.3333333333, 16 + 5/12]
    cases += [random.random()*100 for _ in range(5)]
    print([(case, *to_ft_and_in(case)) for case in cases])
    print([(case, *to_ft_in_sixteenths(case)) for case in cases])

