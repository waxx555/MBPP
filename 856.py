'''
Write a python function to find minimum adjacent swaps required to sort binary array.
'''


def find_Min_Swaps(arr,n) : 
    noOfZeroes = [0] * n 
    count = 0 
    noOfZeroes[n - 1] = 1 - arr[n - 1] 
    for i in range(n-2,-1,-1) : 
        noOfZeroes[i] = noOfZeroes[i + 1] 
        if (arr[i] == 0) : 
            noOfZeroes[i] = noOfZeroes[i] + 1
    for i in range(0,n) : 
        if (arr[i] == 1) : 
            count = count + noOfZeroes[i] 
    return count 


assert find_Min_Swaps([1,0,1,0],4) == 3
assert find_Min_Swaps([0,1,0],3) == 1
assert find_Min_Swaps([0,0,1,1,0],5) == 2
