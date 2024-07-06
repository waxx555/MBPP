'''
Write a python function to find the maximum element in a sorted and rotated array.
'''


def find_Max(arr,low,high): 
    if (high < low): 
        return arr[0] 
    if (high == low): 
        return arr[low] 
    mid = low + (high - low) // 2 
    if (mid < high and arr[mid + 1] < arr[mid]): 
        return arr[mid] 
    if (mid > low and arr[mid] < arr[mid - 1]): 
        return arr[mid - 1]  
    if (arr[low] > arr[mid]): 
        return find_Max(arr,low,mid - 1) 
    else: 
        return find_Max(arr,mid + 1,high) 


assert find_Max([2,3,5,6,9],0,4) == 9
assert find_Max([3,4,5,2,1],0,4) == 5
assert find_Max([1,2,3],0,2) == 3
