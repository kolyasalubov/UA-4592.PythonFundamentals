def number_calculates(word: str) -> str:
    lst = {}
    for i in word:
        if i in lst:
            lst[i] += 1
        else:
            lst[i] = 1
    return lst
test = number_calculates("hello")
print(test)