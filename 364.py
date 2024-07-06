'''
Write a function to find the number of flips required to make the given binary string a sequence of alternate characters.
'''


def make_flip(ch): 
	return '1' if (ch == '0') else '0'
def get_flip_with_starting_charcter(str, expected): 
	flip_count = 0
	for i in range(len( str)): 
		if (str[i] != expected): 
			flip_count += 1
		expected = make_flip(expected) 
	return flip_count 
def min_flip_to_make_string_alternate(str): 
	return min(get_flip_with_starting_charcter(str, '0'),get_flip_with_starting_charcter(str, '1')) 


assert min_flip_to_make_string_alternate("0001010111") == 2
assert min_flip_to_make_string_alternate("001") == 1
assert min_flip_to_make_string_alternate("010111011") == 2 
