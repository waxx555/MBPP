'''
Write a function to delete the smallest element from the given heap and then insert a new item.
'''


import heapq as hq
def heap_replace(heap,a):
  hq.heapify(heap)
  hq.heapreplace(heap, a)
  return heap


assert heap_replace( [25, 44, 68, 21, 39, 23, 89],21)==[21, 25, 23, 44, 39, 68, 89]
assert heap_replace([25, 44, 68, 21, 39, 23, 89],110)== [23, 25, 68, 44, 39, 110, 89]
assert heap_replace([25, 44, 68, 21, 39, 23, 89],500)==[23, 25, 68, 44, 39, 500, 89]
