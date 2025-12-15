def count_characters(text: str) -> dict:
  
    char_count = {}
    
    for char in text:
        char_count[char] = text.count(char)
    
    return char_count
# Test the function
input_text = input("Enter a string: ")
result = count_characters(input_text)
print(f"Character count: {result}")