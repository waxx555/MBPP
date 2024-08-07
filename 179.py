'''
Write a function to find if the given number is a keith number or not.
'''


def is_num_keith(x): 
	terms = [] 
	temp = x 
	n = 0 
	while (temp > 0): 
		terms.append(temp % 10) 
		temp = int(temp / 10) 
		n+=1 
	terms.reverse() 
	next_term = 0 
	i = n 
	while (next_term < x): 
		next_term = 0 
		for j in range(1,n+1): 
			next_term += terms[i - j] 
		terms.append(next_term) 
		i+=1 
	return (next_term == x) 


assert is_num_keith(14) == True
assert is_num_keith(12) == False
assert is_num_keith(197) == True
