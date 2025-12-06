def getLargestNumber(num1: int, num2: int) -> int:
    """Returns the largest number"""
    if num1 > num2:
        return num1
    return num2

result = getLargestNumber(10, 20)
print(getLargestNumber.__doc__)
print(result)