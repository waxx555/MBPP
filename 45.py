'''
Write a function to find the gcd of the given array elements.
'''


def find_gcd(x, y): 
	while(y): 
		x, y = y, x % y 
	return x 
def get_gcd(l):
  num1 = l[0]
  num2 = l[1]
  gcd = find_gcd(num1, num2)
  for i in range(2, len(l)):
    gcd = find_gcd(gcd, l[i])
  return gcd


assert get_gcd([2, 4, 6, 8, 16]) == 2
assert get_gcd([1, 2, 3]) == 1
assert get_gcd([2, 4, 6, 8]) == 2 
