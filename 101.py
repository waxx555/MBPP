'''
Write a function to find the kth element in the given array.
'''


def kth_element(arr, n, k):
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]


assert kth_element([12,3,5,7,19], 5, 2) == 3
assert kth_element([17,24,8,23], 4, 3) == 8
assert kth_element([16,21,25,36,4], 5, 4) == 36
