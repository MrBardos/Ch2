import random


def quadratic_formula(a, b, c):
    """
    Finds the zeros of a quadratic function using the quadratic formula
    :param a, b, and c: coefficients in standard form: ax**2 + bx + c. Assume that a is not zero.
    :return: tuple with two solution, with the first value being the one computed by adding the square root of the determinant
    """
    determinant = b ** 2 - 4 * a * c
    x1 = (-b + determinant ** 0.5) / (2 * a)
    x2 = (-b - determinant ** 0.5) / (2 * a)
    return x1, x2



if __name__ == '__main__':
    test_cases = [(-4, 1, 2), (1, -6, 9), (3, 1, 0), (5, 0, 1), (5, 0, -1), (4, 5, 6), (-4.9, 10, 12) ]
    random_cases = [(random.random() * 100 - 50, random.random() * 100 - 50, random.random() * 100 - 50) for _ in range(5)]
    for a, b, c in test_cases + random_cases:
        if quadratic_formula(a, b, c) is not None:
            expected_x1, expected_x2 = quadratic_formula(a, b, c)
        else:
            expected_x1, expected_x2 = None, None
        print(f"({a}, {b}, {c}, {expected_x1}, {expected_x2}), ")
    """
    a = float(input("Enter a value for a: "))
    b = float(input("Enter a value for b: "))
    c = float(input("Enter a value for c: "))
    """
    print(quadratic_formula(a, b, c))