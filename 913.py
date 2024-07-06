'''
Write a function to check for a number at the end of a string.
'''


import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False


assert end_num('abcdef')==False
assert end_num('abcdef7')==True
assert end_num('abc')==False
