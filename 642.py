'''
Write a function to remove similar rows from the given tuple matrix.
'''


def remove_similar_row(test_list):
  res = set(sorted([tuple(sorted(set(sub))) for sub in test_list]))
  return (res) 


assert remove_similar_row([[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]] ) == {((2, 2), (4, 6)), ((3, 2), (4, 5))}
assert remove_similar_row([[(5, 6), (4, 3)], [(3, 3), (5, 7)], [(4, 3), (5, 6)]] ) == {((4, 3), (5, 6)), ((3, 3), (5, 7))}
assert remove_similar_row([[(6, 7), (5, 4)], [(4, 4), (6, 8)], [(5, 4), (6, 7)]] ) =={((4, 4), (6, 8)), ((5, 4), (6, 7))}
