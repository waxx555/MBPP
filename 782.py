'''
Write a python function to find the sum of all odd length subarrays.
'''


def Odd_Length_Sum(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum


assert Odd_Length_Sum([1,2,4]) == 14
assert Odd_Length_Sum([1,2,1,2]) == 15
assert Odd_Length_Sum([1,7]) == 8
