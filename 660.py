'''
Write a python function to choose points from two ranges such that no point lies in both the ranges.
'''


def find_Points(l1,r1,l2,r2): 
    x = min(l1,l2) if (l1 != l2) else -1
    y = max(r1,r2) if (r1 != r2) else -1
    return (x,y)


assert find_Points(5,10,1,5) == (1,10)
assert find_Points(3,5,7,9) == (3,9)
assert find_Points(1,5,2,8) == (1,8)
