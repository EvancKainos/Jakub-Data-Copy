from math_functions import add

def test_add():
    assert add(1, 6) == 7
    assert add(-1, 1) == 0
    assert add(5, 5) == 10