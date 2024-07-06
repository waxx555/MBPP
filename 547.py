'''
Write a python function to find the sum of hamming distances of all consecutive numbers from o to n.
'''


def Total_Hamming_Distance(n):   
    i = 1
    sum = 0
    while (n // i > 0):  
        sum = sum + n // i  
        i = i * 2     
    return sum


assert Total_Hamming_Distance(4) == 7
assert Total_Hamming_Distance(2) == 3
assert Total_Hamming_Distance(5) == 8
