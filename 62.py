'''
Write a python function to find smallest number in a list.
'''


def smallest_num(xs):
  return min(xs)



assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([1, 2, 3]) == 1
assert smallest_num([45, 46, 50, 60]) == 45
