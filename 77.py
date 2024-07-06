'''
Write a python function to find the difference between sum of even and odd digits.
'''


def is_Diff(n): 
    return (n % 11 == 0) 


assert is_Diff (12345) == False
assert is_Diff(1212112) == True
assert is_Diff(1212) == False
