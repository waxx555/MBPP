'''
Write a python function to replace multiple occurence of character by single.
'''


import re 
def replace(string, char): 
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string 


assert replace('peep','e') == 'pep'
assert replace('Greek','e') == 'Grek'
assert replace('Moon','o') == 'Mon'
