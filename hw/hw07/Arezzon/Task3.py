# Task3. Write a function that calculates the number of characters included in
# given string

def calc(string: str):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1
    print(result)

calc("Hello")