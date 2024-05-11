import random


def quadratic_formula(a, b, c):
    """
    Uses the quadratic formula to find real zeros of a quadratic equation
    :param a, b, and c: coefficients of quadratic in standard form: ax**2 + bx + c.
    :return: tuple with two values of x or "None" if the result is complex or if a == 0.
    """
    determinant = b ** 2 - 4 * a * c
    if a == 0 or determinant < 0:
        return None

    return ((-b + determinant ** 0.5) / (2 * a),
            (-b - determinant ** 0.5) / (2 * a))



if __name__ == '__main__':
    test_cases = [(0, 1, 2), (1, -6, 9), (3, 1, 0), (5, 0, 1), (5, 0, -1), (4, 5, 6), (-4.9, 10, 12) ]
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