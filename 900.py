'''
Write a function where a string will start with a specific number.
'''


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False


assert match_num('5-2345861')==True
assert match_num('6-2345861')==False
assert match_num('78910')==False
