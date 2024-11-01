from solutions.day_03_solutions import double_dict

def expected(num: int) -> dict:
    new_dict = dict()
    for i in range(1, num + 1):
        new_dict[i] = i ** 2
    return new_dict

def test_double_dict():
    assert double_dict(2) == expected(2)
    assert double_dict(8) == expected(8)
    assert double_dict(1) == expected(1)
    assert double_dict(4) == expected(4)