'''
Write a function to find the occurrence and position of the substrings within a string.
'''


import re
def occurance_substring(text,pattern):
 for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    return (text[s:e], s, e)


assert occurance_substring('python programming, python language','python')==('python', 0, 6)
assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)
assert occurance_substring('python programming,programming language','language')==('language', 31, 39)
