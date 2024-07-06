'''
Write a function to round up a number to specific digits.
'''


import math
def round_up(a, digits):
    n = 10**-digits
    return round(math.ceil(a / n) * n, digits)


assert round_up(123.01247,0)==124
assert round_up(123.01247,1)==123.1
assert round_up(123.01247,2)==123.02
