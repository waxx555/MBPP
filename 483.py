'''
Write a python function to find the first natural number whose factorial is divisible by x.
'''


def first_Factorial_Divisible_Number(x): 
    i = 1;
    fact = 1; 
    for i in range(1,x): 
        fact = fact * i 
        if (fact % x == 0): 
            break
    return i 


assert first_Factorial_Divisible_Number(10) == 5
assert first_Factorial_Divisible_Number(15) == 5
assert first_Factorial_Divisible_Number(5) == 4
