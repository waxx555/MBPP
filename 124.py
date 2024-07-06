'''
Write a function to get the angle of a complex number.
'''


import cmath
def angle_complex(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle


assert angle_complex(0,1j)==1.5707963267948966 
assert angle_complex(2,1j)==0.4636476090008061
assert angle_complex(0,2j)==1.5707963267948966
