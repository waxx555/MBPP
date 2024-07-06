'''
Write a function to zip the two given tuples.
'''


def zip_tuples(test_tup1, test_tup2):
  res = []
  for i, j in enumerate(test_tup1):
    res.append((j, test_tup2[i % len(test_tup2)])) 
  return (res) 


assert zip_tuples((7, 8, 4, 5, 9, 10),(1, 5, 6) ) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
assert zip_tuples((8, 9, 5, 6, 10, 11),(2, 6, 7) ) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
assert zip_tuples((9, 10, 6, 7, 11, 12),(3, 7, 8) ) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]
