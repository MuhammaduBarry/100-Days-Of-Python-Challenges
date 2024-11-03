from solutions.day_01_solutions import divisible_by_7_not_multiple_5

def test_divisible_by_7_not_multiple_5():
    solution = divisible_by_7_not_multiple_5()
    expected = [number for number in range(2000, 3201) if number % 7 == 0 and number % 5 != 0]
    assert solution == expected
