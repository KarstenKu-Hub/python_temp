from temp_pyuq import example
from math import isclose 

def test_calc_area():
    assert isclose(example.calc_area(2), 12.5, abs_tol=0.1)

