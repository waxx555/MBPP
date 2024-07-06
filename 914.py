'''
Write a python function to check whether the given string is made up of two alternating characters or not.
'''


def is_Two_Alter(s):  
    for i in range (len( s) - 2) : 
        if (s[i] != s[i + 2]) : 
            return False
    if (s[0] == s[1]): 
        return False
    return True


assert is_Two_Alter("abab") == True
assert is_Two_Alter("aaaa") == False
assert is_Two_Alter("xyz") == False
