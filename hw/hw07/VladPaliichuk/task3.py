def count_chars(text):
    result = {}
    for char in text:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result
