#1 
def largestNum(num1, num2):
    """This function returns the largest number"""
    if num1 < num2:
        return num2 
    else:
        return num1

#2   
def rectangleArea(a, b):
    return a * b
def triangularArea(a, h):
    return a * h / 2
def circleArea(R):
    PI = 3.14
    return PI * R ** 2
def area():
    f = input("Write which figure area we are going to calculate: ")
    if f == "rectangle":
        a = int(input("a = "))
        b = int(input("b = "))
        return rectangleArea(a, b)
    elif f == "triangle":
        a = int(input("a = "))
        h = int(input("h = "))
        return triangularArea(a, h)
    elif f == "circle":
        R = int(input("R = "))
        return circleArea(R)
    else:
        print("Choose another figure")
        
#print(area())

#3

def calLetters(word):
    res = {}
    for i in word:
        res.update({i: word.count(i)})
    return res

#word1 = input()
#print(calLetters(word1))