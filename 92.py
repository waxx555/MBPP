'''
Write a function to check whether the given number is undulating or not.
'''


def is_undulating(n): 
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True


assert is_undulating("1212121") == True
assert is_undulating("1991") == False
assert is_undulating("121") == True
