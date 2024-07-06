'''
Write a function to search some literals strings in a string.
'''


import re
def string_literals(patterns,text):
  for pattern in patterns:
     if re.search(pattern,  text):
       return ('Matched!')
     else:
       return ('Not Matched!')


assert string_literals(['language'],'python language')==('Matched!')
assert string_literals(['program'],'python language')==('Not Matched!')
assert string_literals(['python'],'programming language')==('Not Matched!')
