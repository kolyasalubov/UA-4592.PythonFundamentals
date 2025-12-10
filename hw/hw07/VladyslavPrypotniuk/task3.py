def count(word: str) -> dict:
    result = {}
    for i in word:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

word = input("Enter the word:")
print(count(word))