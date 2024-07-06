'''
Write a function to find the surface area of a sphere.
'''


import math
def surfacearea_sphere(r):
  surfacearea=4*math.pi*r*r
  return surfacearea


assert surfacearea_sphere(10)==1256.6370614359173
assert surfacearea_sphere(15)==2827.4333882308138
assert surfacearea_sphere(20)==5026.548245743669
