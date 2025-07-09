from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 2) == 3
    assert sub(9, 4) == 5
    assert sub(7, 2) == 5 