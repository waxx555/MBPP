'''
Write a function to find the third side of a right angled triangle.
'''


import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s


assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685
