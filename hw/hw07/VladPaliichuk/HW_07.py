#    1.     Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)


# 2.  Simple: Find The Distance Between Two Points

# import math
# def distance(x1, y1, x2, y2):
#     result = math.sqrt((x2-x1)**2+(y2-y1)**2)
#     return round(result, 2)

#       3. No yelling!
# def filter_words(st):
#     return ' '.join(st.capitalize().split())

#     .4 Convert a Number to a String

# def number_to_string(num):
#     return str(num)


#    5.    Reversing Words in a String

# def reverse(st):
#     text_split = st.split()
#     text_split.reverse()
#     result = ' '.join(text_split).strip()
#     return result


#    6.    Reverse List Order

# def reverse_list(l):
#     return l[::-1]

#       7. Multiples of 3 or 5

# def solution(number):
#     if number < 0:
#         return 0
    
#     result = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result


#    8.    Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     car_range = mpg * fuel_left
#     return car_range >= distance_to_pump

#       .9 Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     check = name.startswith(("R", "r"))
#     if check == True :
#         name = name + " plays banjo"
#     else:    
#         name = name + " does not play banjo"
#     return name 

#    10.   Convert boolean values to strings 'Yes' or 'No'

# def bool_to_word(boolean):
#     if boolean :
#         return "Yes"
#     else:
#         return "No" 


#    11.   Counting sheep

# def count_sheeps(sheep):
#     return sheep.count(True)

#   12.  Is this my tail?

# def correct_tail(body, tail):
#     return body[-1] == tail

