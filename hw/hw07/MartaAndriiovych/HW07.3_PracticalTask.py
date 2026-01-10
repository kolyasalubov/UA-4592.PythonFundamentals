#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#2
def distance(x1, y1, x2, y2):
    import math
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)  

#3
def filter_words(st):
    x = st.lower().capitalize().split()
    y = " ".join(x)
    return y

#4
def number_to_string(num):
    return str(num)

#5
def reverse(st):
    x = st.split()
    x.reverse()
    x_str = " ".join(x)
    return x_str

#6
def reverse_list(l):
    l.reverse()
    return l

#7
def solution(number):
    x = list(range(number))
    rez = 0
    for i in x:
        if i % 3 == 0 or i % 5 == 0:
            rez = rez + i
    return rez

#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        return True
    else:
        return False

#9
def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    
#10
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

#11
def count_sheeps(sheep):
    x = sheep.count(True)    
    return x

#12
def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    else:
        return False