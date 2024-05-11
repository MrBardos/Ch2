import pytest
from ch2b_quadratic_formula import quadratic_formula


test_cases = [
    (0, 1, 2, None, None),
    (1, -6, 9, 3.0, 3.0),
    (3, 1, 0, 0.0, -0.3333333333333333),
    (5, 0, 1, None, None),
    (5, 0, -1, 0.447213595499958, -0.447213595499958),
    (4, 5, 6, None, None),
    (-4.9, 10, 12, -0.8478028557299278, 2.88861918226054),
    (-16.64516174450685, -45.26296503938427, -42.472889230289844, None, None),
    (-8.66697554521901, 32.888877005943314, -24.554975401757318, 1.021674520112083, 2.773060659922653),
    (7.769336183131337, 20.80136773320767, -17.56903169719324, 0.6746229966077572, -3.351990437390057),
    (35.72193273761283, 24.904428350216122, 34.153793652915724, None, None),
    (-40.636717647461225, 31.46501662699295, 45.456581664595205, -0.739124214554413, 1.5134243659584652),
]
@pytest.mark.parametrize("a, b, c, ex1, ex2", test_cases)
def test_quadratic_formula(a, b, c, ex1, ex2):
    if ex1 is None:
        assert quadratic_formula(a, b, c) is None
    else:
        x1, x2 = quadratic_formula(a, b, c)
        assert (x1 == pytest.approx(ex1) and x2 == pytest.approx(ex2) or
                x2 == pytest.approx(ex1) and x2 == pytest.approx(ex1))