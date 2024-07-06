'''
Write a python function to check whether the given number can be represented by sum of two squares or not.
'''


def sum_Square(n) : 
    i = 1 
    while i*i <= n : 
        j = 1
        while (j*j <= n) : 
            if (i*i+j*j == n) : 
                return True
            j = j+1
        i = i+1     
    return False


assert sum_Square(25) == True
assert sum_Square(24) == False
assert sum_Square(17) == True
