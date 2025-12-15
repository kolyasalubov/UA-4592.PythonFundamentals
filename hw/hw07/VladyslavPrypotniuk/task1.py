a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

def largest_number(a: int, b: int) -> None:
    if a > b:
        print(f"Number {a} more than number {b}")
    elif b > a:
        print(f"Number {b} more than number {a}")
    else:
        print(f"Both numbers are equal: {a}")

largest_number(a,b)