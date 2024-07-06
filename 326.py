'''
Write a function to get the word with most number of occurrences in the given strings list.
'''


from collections import defaultdict 

def most_occurrences(test_list):
  temp = defaultdict(int)
  for sub in test_list:
    for wrd in sub.split():
      temp[wrd] += 1
  res = max(temp, key=temp.get)
  return (str(res)) 


assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
