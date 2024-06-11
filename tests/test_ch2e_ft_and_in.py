import pytest
from ch2e_ft_and_in import *
cases = [(12, 12, 0), (14.75, 14, 9.0), (0, 0, 0),
         (0.2, 0, 2.4), (15.3333333333, 15, 4.0),
         (16.416666666666668, 16, 5.0), (53.41416696356196, 53, 4.97),
         (32.12541389862126, 32, 1.5), (91.58534352098503, 91, 7.02),
         (96.95699556918743, 96, 11.48), (73.84515023556213, 73, 10.14)]

@pytest.mark.parametrize("dec_ft, ex_ft, ex_in", cases)
def test_to_ft_and_in(dec_ft, ex_ft, ex_in):
    assert to_ft_and_in(dec_ft) == (ex_ft, ex_in)


cases = [(12, 12, 0, 0, 1), (14.75, 14, 9, 0, 1), (0, 0, 0, 0, 1),
    (100.1, 100, 1, 3, 16), (0.2, 0, 2, 3, 8), (15.3333333333, 15, 4, 0, 1),
    (16.416666666666668, 16, 5, 0, 1), (49.77240678471294, 49, 9, 1, 4),
    (77.77081056807654, 77, 9, 1, 4), (7.646272367266038, 7, 8, 3, 4),
    (8.380778290369694, 8, 5, 9, 16), (2.631337018332991, 2, 8, 9, 16)]

@pytest.mark.parametrize("dec_ft, ex_ft, ex_in, ex_16n, ex_16d", cases)
def test_to_ft_in_sixteenths(dec_ft, ex_ft, ex_in, ex_16n, ex_16d):
    str16 = f"and {ex_16n}/{ex_16d} in." if ex_16n else "in."
    print(f"Testing {dec_ft}. Should get {ex_ft} ft. {ex_in} {str16}")
    assert to_ft_in_sixteenths(dec_ft) == (ex_ft, ex_in, ex_16n, ex_16d)
