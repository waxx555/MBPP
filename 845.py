'''
Write a python function to count the number of digits in factorial of a given number.
'''


import math 
def find_Digits(n): 
    if (n < 0): 
        return 0;
    if (n <= 1): 
        return 1; 
    x = ((n * math.log10(n / math.e) + math.log10(2 * math.pi * n) /2.0)); 
    return math.floor(x) + 1; 


assert find_Digits(7) == 4
assert find_Digits(5) == 3
assert find_Digits(4) == 2
