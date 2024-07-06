'''
Write a function to extract the ranges that are missing from the given list with the given start range and end range values.
'''


def extract_missing(test_list, strt_val, stop_val):
  res = []
  for sub in test_list:
    if sub[0] > strt_val:
      res.append((strt_val, sub[0]))
      strt_val = sub[1]
    if strt_val < stop_val:
      res.append((strt_val, stop_val))
  return (res) 


assert extract_missing([(6, 9), (15, 34), (48, 70)], 2, 100) == [(2, 6), (9, 100), (9, 15), (34, 100), (34, 48), (70, 100)]
assert extract_missing([(7, 2), (15, 19), (38, 50)], 5, 60) == [(5, 7), (2, 60), (2, 15), (19, 60), (19, 38), (50, 60)]
assert extract_missing([(7, 2), (15, 19), (38, 50)], 1, 52) == [(1, 7), (2, 52), (2, 15), (19, 52), (19, 38), (50, 52)]
