def char_count(text):
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

#output = char_count("hello")
#print(output)

