'''
Write a function to find the square root of a perfect number.
'''


import math
def sqrt_root(num):
 sqrt_root = math.pow(num, 0.5)
 return sqrt_root 


assert sqrt_root(4)==2
assert sqrt_root(16)==4
assert sqrt_root(400)==20
