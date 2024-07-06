'''
Write a function to abbreviate 'road' as 'rd.' in a given string.
'''


import re
def road_rd(street):
  return (re.sub('Road$', 'Rd.', street))


assert road_rd("ravipadu Road")==('ravipadu Rd.')
assert road_rd("palnadu Road")==('palnadu Rd.')
assert road_rd("eshwar enclave Road")==('eshwar enclave Rd.')
