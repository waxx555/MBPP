'''
Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
'''


import re
def replace_max_specialchar(text,n):
 return (re.sub("[ ,.]", ":", text, n))


assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')
assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')
assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')
