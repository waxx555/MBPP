'''
Write a function to rearrange positive and negative numbers in a given array using lambda function.
'''


def rearrange_numbs(array_nums):
  result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
  return result 


assert rearrange_numbs([-1, 2, -3, 5, 7, 8, 9, -10])==[2, 5, 7, 8, 9, -10, -3, -1]
assert rearrange_numbs([10,15,14,13,-18,12,-20])==[10, 12, 13, 14, 15, -20, -18]
assert rearrange_numbs([-20,20,-10,10,-30,30])==[10, 20, 30, -30, -20, -10]
