'''
Write a function to sort dictionary items by tuple product of keys for the given dictionary with tuple keys.
'''


def sort_dict_item(test_dict):
  res = {key: test_dict[key] for key in sorted(test_dict.keys(), key = lambda ele: ele[1] * ele[0])}
  return  (res) 



assert sort_dict_item({(5, 6) : 3, (2, 3) : 9, (8, 4): 10, (6, 4): 12} ) == {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
assert sort_dict_item({(6, 7) : 4, (3, 4) : 10, (9, 5): 11, (7, 5): 13} ) == {(3, 4): 10, (7, 5): 13, (6, 7): 4, (9, 5): 11}
assert sort_dict_item({(7, 8) : 5, (4, 5) : 11, (10, 6): 12, (8, 6): 14} ) == {(4, 5): 11, (8, 6): 14, (7, 8): 5, (10, 6): 12}
