'''
Write a function to calculate the harmonic sum of n-1.
'''


def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))


assert harmonic_sum(10)==2.9289682539682538
assert harmonic_sum(4)==2.083333333333333
assert harmonic_sum(7)==2.5928571428571425 
