'''
Write a function to find the occurrences of n most common words in a given text.
'''


from collections import Counter
import re
def n_common_words(text,n):
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)


assert n_common_words("python is a programming language",1)==[('python', 1)]
assert n_common_words("python is a programming language",1)==[('python', 1)]
assert n_common_words("python is a programming language",5)==[('python', 1),('is', 1), ('a', 1), ('programming', 1), ('language', 1)]
