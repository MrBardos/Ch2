def investment_value(value, rate, years):
    """
    Calculates the value of an investment over time.
    :param value: initial value of the investment.
    :param rate: annual growth rate expressed as a percent (can be negative)
    :param years: number of years that the investment grows
    :return: new value rounded to the nearest cent.
    """
    return round(value * (1 + rate / 100)**years, 2)

if __name__ == '__main__':
    value = float(input("What is the initial value of the investment? "))
    rate = float(input("What is the growth rate (as a percent)? "))
    years = int(input("How many years of growth (whole numbers only)? "))
    print("Year Value ($)")
    print("______________")
    for year in range(years + 1):
        print(year, investment_value(value, rate, year))

