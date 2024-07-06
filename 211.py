'''
Write a python function to count numbers whose oth and nth bits are set.
'''


def count_Num(n): 
    if (n == 1): 
        return 1
    count = pow(2,n - 2) 
    return count 


assert count_Num(2) == 1
assert count_Num(3) == 2
assert count_Num(1) == 1
