### ---------------------- task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return (f"Hello, {name}!")
    
### ---------------------- task 2

def distance(x1, y1, x2, y2):
    return round((((x2 - x1)**2 + (y2 - y1)**2)**0.5),2)

### ---------------------- task 3

def filter_words(st):
    cleaned = " ".join(st.split()).lower()
    return cleaned.capitalize()

### ---------------------- task 4

def number_to_string(num):
    num_str = str(num)
    return(num_str)

### ---------------------- task 5

def reverse(st):
     words = st.strip().split()
     return " ".join(words[::-1])

### ---------------------- task 6

def reverse_list(l):
    return l[:: -1]

### ---------------------- task 7

def solution(number):
    if number < 0:
        return 0
    total = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            
    return total

### ---------------------- task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return bool((mpg * fuel_left) >= distance_to_pump)


### ---------------------- task 9

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
### ---------------------- task 10

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

### ---------------------- task 11

def count_sheeps(sheep):
    array1 = []
    for i in sheep:
        if i:
            array1.append(i)
    return len(array1)

### ---------------------- task 12

def correct_tail(body, tail):
    sub = body[len(body) - len(tail):]
    if sub == tail:
        return True
    else:
        return False
