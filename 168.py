'''
Write a python function to find the frequency of a number in a given array.
'''


def frequency(a,x): 
    count = 0  
    for i in a: 
        if i == x: count += 1
    return count 


assert frequency([1,2,3],4) == 0
assert frequency([1,2,2,3,3,3,4],3) == 3
assert frequency([0,1,2,3,1,2],1) == 2
