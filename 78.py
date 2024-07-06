'''
Write a python function to find number of integers with odd number of set bits.
'''


def count_With_Odd_SetBits(n): 
    if (n % 2 != 0): 
        return (n + 1) / 2
    count = bin(n).count('1') 
    ans = n / 2
    if (count % 2 != 0): 
        ans += 1
    return ans 


assert count_With_Odd_SetBits(5) == 3
assert count_With_Odd_SetBits(10) == 5
assert count_With_Odd_SetBits(15) == 8
