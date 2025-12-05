# Task1. Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).

def largest(*args):
    '''
    Takes two or more arguments
    return the largest number
    '''
    return max(args)

print(largest(4, 2, 3, 10))