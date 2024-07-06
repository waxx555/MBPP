'''
Write a function to calculate the area of a regular polygon.
'''


from math import tan, pi
def area_polygon(s,l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area


assert area_polygon(4,20)==400.00000000000006
assert area_polygon(10,15)==1731.1969896610804
assert area_polygon(9,7)==302.90938549487214
