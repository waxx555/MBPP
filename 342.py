'''
Write a function to find the smallest range that includes at-least one element from each of the given arrays.
'''


from heapq import heappop, heappush
class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
    def __lt__(self, other):
        return self.value < other.value
def find_minimum_range(list):
    high = float('-inf')
    p = (0, float('inf'))
    pq = []
    for i in range(len(list)):
        heappush(pq, Node(list[i][0], i, 0))
        high = max(high, list[i][0])
    while True:
        top = heappop(pq)
        low = top.value
        i = top.list_num
        j = top.index
        if high - low < p[1] - p[0]:
            p = (low, high)
        if j == len(list[i]) - 1:
            return p
        heappush(pq, Node(list[i][j + 1], i, j + 1))
        high = max(high, list[i][j + 1])


assert find_minimum_range([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]) == (4, 6)
assert find_minimum_range([[ 2, 3, 4, 8, 10, 15 ], [1, 5, 12], [7, 8, 15, 16], [3, 6]]) == (4, 7)
assert find_minimum_range([[4, 7, 9, 11, 16], [2, 6, 13], [5, 9, 16, 17], [3, 7]]) == (5, 7)
