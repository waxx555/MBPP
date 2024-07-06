'''
Write a python function to find two distinct numbers such that their lcm lies within the given range.
'''


def answer(L,R): 
    if (2 * L <= R): 
        return (L ,2*L)
    else: 
        return (-1) 


assert answer(3,8) == (3,6)
assert answer(2,6) == (2,4)
assert answer(1,3) == (1,2)
