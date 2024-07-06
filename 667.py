'''
Write a python function to count number of vowels in the string.
'''


def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return(len(final)) 



assert Check_Vow('corner','AaEeIiOoUu') == 2
assert Check_Vow('valid','AaEeIiOoUu') == 2
assert Check_Vow('true','AaEeIiOoUu') ==2
