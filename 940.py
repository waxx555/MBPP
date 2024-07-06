'''
Write a function to sort the given array by using heap sort.
'''


def heap_sort(arr):
    heapify(arr)  
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        shift_down(arr, 0, end - 1)
        end -= 1
    return arr

def heapify(arr):
    start = len(arr) // 2
    while start >= 0:
        shift_down(arr, start, len(arr) - 1)
        start -= 1
def shift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return



assert heap_sort([12, 2, 4, 5, 2, 3]) == [2, 2, 3, 4, 5, 12]
assert heap_sort([32, 14, 5, 6, 7, 19]) == [5, 6, 7, 14, 19, 32]
assert heap_sort([21, 15, 29, 78, 65]) == [15, 21, 29, 65, 78]
