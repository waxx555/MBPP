'''
Write a function to remove multiple spaces in a string by using regex.
'''


import re
def remove_multiple_spaces(text1):
  return (re.sub(' +',' ',text1))


assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
assert remove_multiple_spaces('Quad      Core') == 'Quad Core'
assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'
