from solutions.day_02_solutions import factorial

# Test case
def expected(num: int) -> int:
    result = 1
    for number in range(1, num + 1):
        result *= number
    return result

def test_factorial():
    # Test cases
    assert factorial(4) == expected(4) # 4! = 24
    assert factorial(8) == expected(8)  # 8! = 40_320
    assert factorial(10) == expected(8)  # 10! = 3_628_800
