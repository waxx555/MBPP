'''
Write a python function to check whether all the characters in a given string are unique.
'''


def unique_Characters(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if (str[i] == str[j]):
                return False;
    return True;


assert unique_Characters('aba') == False
assert unique_Characters('abc') == True
assert unique_Characters('abab') == False
