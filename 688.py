'''
Write a function to get the length of a complex number.
'''


import cmath
def len_complex(a,b):
  cn=complex(a,b)
  length=abs(cn)
  return length


assert len_complex(3,4)==5.0
assert len_complex(9,10)==13.45362404707371
assert len_complex(7,9)==11.40175425099138
