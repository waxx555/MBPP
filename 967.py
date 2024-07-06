'''
Write a python function to accept the strings which contains all vowels.
'''


def check(string): 
  if len(set(string).intersection("AEIOUaeiou"))>=5: 
    return ('accepted') 
  else: 
    return ("not accepted") 


assert check("SEEquoiaL") == 'accepted'
assert check('program') == "not accepted"
assert check('fine') == "not accepted"
