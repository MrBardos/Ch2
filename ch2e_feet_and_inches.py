import random


def to_feet_and_inches(decimal_feet):
    """
    Converts decimal feet to feet and inches
    :param decimal_feet: feet expressed as a decimal (assume positive numbers)
    :return: tuple with number of feet, inches rounded to two decimal places
    """
    feet = int(decimal_feet)
    inches = round((decimal_feet - feet) * 12, 2)
    return feet, inches


if __name__ == "__main__":
    cases = [12, 14.75, 0, 0.2, 15.3333333333, 16 + 5/12]
    cases += [random.random()*100 for _ in range(5)]
    print([(case, *to_feet_and_inches(case)) for case in cases])

