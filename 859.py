'''
Write a function to generate all sublists of a given list.
'''


from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs


assert sub_lists([10, 20, 30, 40])==[[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]
assert sub_lists(['X', 'Y', 'Z'])==[[], ['X'], ['Y'], ['Z'], ['X', 'Y'], ['X', 'Z'], ['Y', 'Z'], ['X', 'Y', 'Z']]
assert sub_lists([1,2,3])==[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
