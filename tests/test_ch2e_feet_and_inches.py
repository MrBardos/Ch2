import pytest
from ch2e_feet_and_inches import to_feet_and_inches
cases = [(12, 12, 0), (14.75, 14, 9.0), (0, 0, 0),
         (0.2, 0, 2.4), (15.3333333333, 15, 4.0),
         (16.416666666666668, 16, 5.0), (53.41416696356196, 53, 4.97),
         (32.12541389862126, 32, 1.5), (91.58534352098503, 91, 7.02),
         (96.95699556918743, 96, 11.48), (73.84515023556213, 73, 10.14)]

@pytest.mark.parametrize("dec_ft, ex_ft, ex_in", cases)
def test_to_feet_and_inches(dec_ft, ex_ft, ex_in):
    assert to_feet_and_inches(dec_ft) == (ex_ft, ex_in)
