'''
Write a python function to find the average of odd numbers till a given odd number.
'''


def average_Odd(n) : 
    if (n%2==0) : 
        return ("Invalid Input") 
        return -1 
    sm =0
    count =0
    while (n>=1) : 
        count=count+1
        sm = sm + n 
        n = n-2
    return sm//count 


assert average_Odd(9) == 5
assert average_Odd(5) == 3
assert average_Odd(11) == 6
