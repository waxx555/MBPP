'''
Write a function to find all words starting with 'a' or 'e' in a given string.
'''


import re
def words_ae(text):
 list = re.findall("[ae]\w+", text)
 return list


assert words_ae("python programe")==['ame']
assert words_ae("python programe language")==['ame','anguage']
assert words_ae("assert statement")==['assert', 'atement']
