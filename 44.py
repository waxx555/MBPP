'''
Write a function that matches a word at the beginning of a string.
'''


import re
def text_match_string(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'


assert text_match_string(" python")==('Not matched!')
assert text_match_string("python")==('Found a match!')
assert text_match_string("  lang")==('Not matched!')
