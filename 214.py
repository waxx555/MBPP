'''
Write a function to convert radians to degrees.
'''


import math
def degree_radian(radian):
 degree = radian*(180/math.pi)
 return degree


assert degree_radian(90)==5156.620156177409
assert degree_radian(60)==3437.746770784939
assert degree_radian(120)==6875.493541569878
