'''
Write a function to check if the letters of a given string can be rearranged so that two characters that are adjacent to each other are different.
'''


import heapq
from collections import Counter
def rearange_string(S):
    ctr = Counter(S)
    heap = [(-value, key) for key, value in ctr.items()]
    heapq.heapify(heap)
    if (-heap[0][0]) * 2 > len(S) + 1: 
        return ""
    ans = []
    while len(heap) >= 2:
        nct1, char1 = heapq.heappop(heap)
        nct2, char2 = heapq.heappop(heap)
        ans.extend([char1, char2])
        if nct1 + 1: heapq.heappush(heap, (nct1 + 1, char1))
        if nct2 + 1: heapq.heappush(heap, (nct2 + 1, char2))
    return "".join(ans) + (heap[0][1] if heap else "")


assert rearange_string("aab")==('aba')
assert rearange_string("aabb")==('abab')
assert rearange_string("abccdd")==('cdabcd')
