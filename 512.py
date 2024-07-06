'''
Write a function to count the element frequency in the mixed nested tuple.
'''


def flatten(test_tuple): 
	for tup in test_tuple: 
		if isinstance(tup, tuple): 
			yield from flatten(tup) 
		else: 
			yield tup 
def count_element_freq(test_tuple):
  res = {}
  for ele in flatten(test_tuple):
    if ele not in res:
      res[ele] = 0
    res[ele] += 1
  return (res) 


assert count_element_freq((5, 6, (5, 6), 7, (8, 9), 9) ) == {5: 2, 6: 2, 7: 1, 8: 1, 9: 2}
assert count_element_freq((6, 7, (6, 7), 8, (9, 10), 10) ) == {6: 2, 7: 2, 8: 1, 9: 1, 10: 2}
assert count_element_freq((7, 8, (7, 8), 9, (10, 11), 11) ) == {7: 2, 8: 2, 9: 1, 10: 1, 11: 2}
