'''
Write a python function to find the sum of squares of first n odd natural numbers.
'''


def square_Sum(n):  
    return int(n*(4*n*n-1)/3) 


assert square_Sum(2) == 10
assert square_Sum(3) == 35
assert square_Sum(4) == 84
