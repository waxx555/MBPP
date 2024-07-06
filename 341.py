'''
Write a function to convert the given set into ordered tuples.
'''


def set_to_tuple(s):
  t = tuple(sorted(s))
  return (t)


assert set_to_tuple({1, 2, 3, 4, 5}) == (1, 2, 3, 4, 5)
assert set_to_tuple({6, 7, 8, 9, 10, 11}) == (6, 7, 8, 9, 10, 11)
assert set_to_tuple({12, 13, 14, 15, 16}) == (12, 13, 14, 15, 16)
