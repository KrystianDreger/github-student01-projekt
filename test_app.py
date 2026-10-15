from app import add, multiply, substract


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6

def test_substract():
    assert substract(5, 3) == 2
