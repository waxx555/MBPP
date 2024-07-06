'''
Write a function to count the most common character in a given string.
'''


from collections import Counter 
def max_char(str1):
    temp = Counter(str1) 
    max_char = max(temp, key = temp.get)
    return max_char


assert max_char("hello world")==('l')
assert max_char("hello ")==('l')
assert max_char("python pr")==('p')
