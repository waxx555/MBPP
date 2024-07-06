'''
Write a python function to find the minimum operations required to make two numbers equal.
'''


import math   
def min_Operations(A,B):  
    if (A > B): 
        swap(A,B)  
    B = B // math.gcd(A,B);  
    return B - 1


assert min_Operations(2,4) == 1
assert min_Operations(4,10) == 4
assert min_Operations(1,4) == 3
