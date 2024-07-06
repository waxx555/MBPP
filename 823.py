'''
Write a function to check if the given string starts with a substring using regex.
'''


import re 
def check_substring(string, sample) : 
  if (sample in string): 
      y = "\A" + sample 
      x = re.search(y, string) 
      if x : 
          return ("string starts with the given substring") 
      else : 
          return ("string doesnt start with the given substring") 
  else : 
      return ("entered string isnt a substring")


assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'
assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'
