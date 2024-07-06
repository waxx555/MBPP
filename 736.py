'''
Write a function to locate the left insertion point for a specified value in sorted order.
'''


import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i


assert left_insertion([1,2,4,5],6)==4
assert left_insertion([1,2,4,5],3)==2
assert left_insertion([1,2,4,5],7)==4
