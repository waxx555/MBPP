'''
Write a function to flatten the given tuple matrix into the tuple list with each tuple representing each column.
'''


def matrix_to_list(test_list):
  temp = [ele for sub in test_list for ele in sub]
  res = list(zip(*temp))
  return (str(res))


assert matrix_to_list([[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]) == '[(4, 7, 10, 18, 0, 10), (5, 8, 13, 17, 4, 1)]'
assert matrix_to_list([[(5, 6), (8, 9)], [(11, 14), (19, 18)], [(1, 5), (11, 2)]]) == '[(5, 8, 11, 19, 1, 11), (6, 9, 14, 18, 5, 2)]'
assert matrix_to_list([[(6, 7), (9, 10)], [(12, 15), (20, 21)], [(23, 7), (15, 8)]]) == '[(6, 9, 12, 20, 23, 15), (7, 10, 15, 21, 7, 8)]'
