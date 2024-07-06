'''
Write a function to split a string at lowercase letters.
'''


import re
def split_lowerstring(text):
 return (re.findall('[a-z][^a-z]*', text))


assert split_lowerstring("AbCd")==['bC','d']
assert split_lowerstring("Python")==['y', 't', 'h', 'o', 'n']
assert split_lowerstring("Programming")==['r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
