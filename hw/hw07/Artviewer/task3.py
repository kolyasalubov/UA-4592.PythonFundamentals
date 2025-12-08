word = input("Enter a word: ")

def calc_chars(word: str) -> dict:
    """Calculate numbr of chars in the word."""
    char_dict = {}
    for char in word:
        if not char_dict.get(char):
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    print(char_dict)

calc_chars(word)

