#====================Task1========================
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"
#=================================================
#====================Task2========================
import math
def distance(x1, y1, x2, y2):
    x = (x2 - x1)**2 
    y = (y2 - y1)**2

    distance_val = math.sqrt(x + y)
    
    return round(distance_val, 2)
#=================================================
#====================Task3========================
def filter_words(st):
    strn = st.lower()
    strn = st.capitalize()
    strn = strn.split(" ")
    st = ""
    for item in strn:
        if len(item) > 0:
            st = st + item + " " 
        else:
            continue
    else:
        st = st[:-1]
    return st
#=================================================
#====================Task4========================
def number_to_string(num):
    return str(num)
#=================================================
#====================Task5========================
def reverse(st):
    st = st.split(" ")
    st = st[::-1]
    return st[0] + " " + st[1]
#=================================================
#====================Task6========================
def reverse_list(l):
    l.reverse()
    return l
#=================================================
#====================Task7========================
def solution(number):
    i = 0
    result = 0
    while i < number:
        if i % 3 == 0 and i % 5 == 0:
            result += i
            i += 1
            continue
        elif i % 3 == 0 or i % 5 == 0:
            result += i
            i += 1
            continue
        else:
            i += 1
            continue
    return result
#==================================================
#====================Task8=========================
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left
#==================================================
#====================Task9=========================
def are_you_playing_banjo(name):
    return name + " plays banjo" if name.startswith("R") or  name.startswith("r") else name + " does not play banjo"
#==================================================
#====================Task10========================
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
#==================================================
#====================Task11========================
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count
#==================================================
#====================Task12========================
def correct_tail(body, tail):
    if body[-1:] == tail:
        return True
    else: 
        return False
#==================================================