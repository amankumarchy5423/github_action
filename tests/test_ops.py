from src.math_opr import add,sub


def test_add():
    assert add(1, 2) == 3
    assert add(5, 2) == 7
    assert add(1, 9) == 10


def test_sub():
    assert sub(1, 2) == -1
    assert sub(2, 2) == 0
    assert sub(10, 2) == 8

    