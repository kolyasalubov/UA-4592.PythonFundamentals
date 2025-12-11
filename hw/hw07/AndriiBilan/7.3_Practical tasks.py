#1.Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"

#2.Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    import math
    x = x1 - x2
    y = y1 - y2
    res = math.sqrt(x**2 + y**2)
    return round(res, 2)

#3.No yelling!
def filter_words(st):
    st = st.lower()
    st = st.capitalize()
    st = st.split(" ")
    clean_st =[]
    for char in st:
        if char != "" and char != " ":
            clean_st.append(char)
    print(clean_st)
    st = " ".join(clean_st)
    return st

#4.Convert a Number to a String!
def number_to_string(num):
    return str(num)

#5.Reversing Words in a String
def reverse(st):
    st = st.split(" ")
    st.reverse()
    st = " ".join(st)
    return st

#6.Reverse List Order
def reverse_list(l):
    l.reverse()
    return l

#7.Multiples of 3 or 5
def solution(number):
    if number == -1:
        return 0
    multi_num = []
    for num in range(1,number):
        if num % 3 == 0 or num % 5 == 0:
            multi_num.append(num)
    return sum(multi_num)

#8.Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    miles = fuel_left * mpg
    if distance_to_pump <= miles:
        return True
    else:
        return False

#9.Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    return name + " does not play banjo"

#10.Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

#11.Counting sheep
def count_sheeps(sheep):
    count = 0
    for present in sheep:
        if present:
            count +=1
    return count

#12.Is this my tail?
def correct_tail(body, tail):
    if tail == body[-1]:
        return True
    return False