'''
Write a python function to check whether the given two arrays are equal or not.
'''


def are_Equal(arr1,arr2,n,m):
    if (n != m):
        return False
    arr1.sort()
    arr2.sort()
    for i in range(0,n - 1):
        if (arr1[i] != arr2[i]):
            return False
    return True


assert are_Equal([1,2,3],[3,2,1],3,3) == True
assert are_Equal([1,1,1],[2,2,2],3,3) == False
assert are_Equal([8,9],[4,5,6],2,3) == False
