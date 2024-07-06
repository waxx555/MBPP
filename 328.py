'''
Write a function to rotate a given list by specified number of items to the left direction.
'''


def rotate_left(list1,m,n):
  result =  list1[m:]+list1[:n]
  return result


assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
assert rotate_left([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2]
