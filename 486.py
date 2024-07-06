'''
Write a function to compute binomial probability for the given number.
'''


def nCr(n, r): 
	if (r > n / 2): 
		r = n - r 
	answer = 1 
	for i in range(1, r + 1): 
		answer *= (n - r + i) 
		answer /= i 
	return answer 
def binomial_probability(n, k, p): 
	return (nCr(n, k) * pow(p, k) *	pow(1 - p, n - k)) 


assert binomial_probability(10, 5, 1.0/3) == 0.13656454808718185
assert binomial_probability(11, 6, 2.0/4) == 0.2255859375
assert binomial_probability(12, 7, 3.0/5) == 0.227030335488
