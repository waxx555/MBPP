'''
Write a function to assign with each element, its pair elements from other similar pairs in the given tuple.
'''


def assign_elements(test_list):
  res = dict()
  for key, val in test_list:
    res.setdefault(val, [])
    res.setdefault(key, []).append(val)
  return (res) 


assert assign_elements([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)] ) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
assert assign_elements([(6, 4), (9, 4), (3, 8), (4, 9), (9, 5)] ) == {4: [9], 6: [4], 9: [4, 5], 8: [], 3: [8], 5: []}
assert assign_elements([(6, 2), (6, 8), (4, 9), (4, 9), (3, 7)] ) == {2: [], 6: [2, 8], 8: [], 9: [], 4: [9, 9], 7: [], 3: [7]}
