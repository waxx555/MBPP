'''
Write a function to find n-th rencontres number.
'''


def binomial_coeffi(n, k): 
	if (k == 0 or k == n): 
		return 1
	return (binomial_coeffi(n - 1, k - 1) 
		+ binomial_coeffi(n - 1, k)) 
def rencontres_number(n, m): 
	if (n == 0 and m == 0): 
		return 1
	if (n == 1 and m == 0): 
		return 0
	if (m == 0): 
		return ((n - 1) * (rencontres_number(n - 1, 0)+ rencontres_number(n - 2, 0))) 
	return (binomial_coeffi(n, m) * rencontres_number(n - m, 0))


assert rencontres_number(7, 2) == 924
assert rencontres_number(3, 0) == 2
assert rencontres_number(3, 1) == 3
