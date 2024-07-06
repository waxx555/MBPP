'''
Write a function to find all adverbs and their positions in a given sentence by using regex.
'''


import re
def find_adverbs(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))


assert find_adverbs("Clearly, he has no excuse for such behavior.") == '0-7: Clearly'
assert find_adverbs("Please handle the situation carefuly") == '28-36: carefuly'
assert find_adverbs("Complete the task quickly") == '18-25: quickly'
