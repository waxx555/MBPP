'''
Write a function to find the ascii value of total characters in a string.
'''


def ascii_value_string(str1):
  for i in range(len(str1)):
   return ord(str1[i])


assert ascii_value_string("python")==112
assert ascii_value_string("Program")==80
assert ascii_value_string("Language")==76
