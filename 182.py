'''
Write a function to find uppercase, lowercase, special character and numeric values using regex.
'''


import re
def find_character(string):
  uppercase_characters = re.findall(r"[A-Z]", string) 
  lowercase_characters = re.findall(r"[a-z]", string) 
  numerical_characters = re.findall(r"[0-9]", string) 
  special_characters = re.findall(r"[, .!?]", string) 
  return uppercase_characters, lowercase_characters, numerical_characters, special_characters


assert find_character("ThisIsGeeksforGeeks") == (['T', 'I', 'G', 'G'], ['h', 'i', 's', 's', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'e', 'e', 'k', 's'], [], [])
assert find_character("Hithere2") == (['H'], ['i', 't', 'h', 'e', 'r', 'e'], ['2'], [])
assert find_character("HeyFolks32") == (['H', 'F'], ['e', 'y', 'o', 'l', 'k', 's'], ['3', '2'], [])
