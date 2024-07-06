'''
Write a python function to check whether the count of inversion of two types are same or not.
'''


import sys 
def solve(a,n):   
    mx = -sys.maxsize - 1
    for j in range(1,n):  
        if (mx > a[j]):  
            return False  
        mx = max(mx,a[j - 1])    
    return True


assert solve([1,0,2],3) == True
assert solve([1,2,0],3) == False
assert solve([1,2,1],3) == True
