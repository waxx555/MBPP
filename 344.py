'''
Write a python function to find number of elements with odd factors in a given range.
'''


def count_Odd_Squares(n,m): 
    return int(m**0.5) - int((n-1)**0.5) 


assert count_Odd_Squares(5,100) == 8
assert count_Odd_Squares(8,65) == 6
assert count_Odd_Squares(2,5) == 1
