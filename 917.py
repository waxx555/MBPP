'''
Write a function to find the sequences of one upper case letter followed by lower case letters.
'''


import re
def text_uppercase_lowercase(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return ('Not matched!')


assert text_uppercase_lowercase("AaBbGg")==('Found a match!')
assert text_uppercase_lowercase("aA")==('Not matched!')
assert text_uppercase_lowercase("PYTHON")==('Not matched!')
