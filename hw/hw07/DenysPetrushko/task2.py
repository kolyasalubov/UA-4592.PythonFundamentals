# codewars.com

# task 1 
# Jenny's secret message
# ==================================================

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


# task 2
# Find The Distance Between Two Points
# ==================================================

def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return round(d, 2)


# task 3
# No yelling!
# ==================================================

def filter_words(st):
    clean = " ".join(st.split())
    return clean.capitalize()


# task 4
# Convert a Number to a String!
# ==================================================

def number_to_string(num):
    return str(num)


# task 5
# Reversing Words in a String
# ==================================================

def reverse(st):
     words = st.strip().split()
     return " ".join(words[::-1])


# task 6
# Reverse List Order
# ==================================================

def reverse_list(l):
    'return a list with the reverse order of l'
    return l[:: -1]


# task 7
# Multiples of 3 or 5
# ==================================================

def solution(number):
    
    if number < 0:
        return 0
    total = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            
    return total


# task 8
# Will you make it?
# ==================================================

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    return bool((mpg * fuel_left) >= distance_to_pump)


# task 9
# Are You Playing Banjo?
# ==================================================

def are_you_playing_banjo(name):
    # Implement me!
    
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


# task 10
# Convert boolean values to strings 'Yes' or 'No'.
# ==================================================

def bool_to_word(boolean):
    # TODO
    if boolean:
        return "Yes"
    else:
        return "No"


# task 11
# Counting sheep...
# ==================================================

def count_sheeps(sheep):
    # TODO May the force be with you
    array1 = []
    for i in sheep:
        if i:
            array1.append(i)
    return len(array1)


# task 12
# Is this my tail?
# ==================================================

def correct_tail(body, tail):
     return body[-1] == tail

