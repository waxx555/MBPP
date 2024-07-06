'''
Write a function to sort a given list of elements in ascending order using heap queue algorithm.
'''


import heapq as hq
def heap_assending(nums):
  hq.heapify(nums)
  s_result = [hq.heappop(nums) for i in range(len(nums))]
  return s_result


assert heap_assending([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==[1, 2, 3, 4, 7, 8, 9, 9, 10, 14, 18]
assert heap_assending([25, 35, 22, 85, 14, 65, 75, 25, 58])==[14, 22, 25, 25, 35, 58, 65, 75, 85]
assert heap_assending([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
