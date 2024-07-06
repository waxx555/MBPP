'''
Write a function to find the maximum total path sum in the given triangle.
'''


def max_path_sum(tri, m, n): 
	for i in range(m-1, -1, -1): 
		for j in range(i+1): 
			if (tri[i+1][j] > tri[i+1][j+1]): 
				tri[i][j] += tri[i+1][j] 
			else: 
				tri[i][j] += tri[i+1][j+1] 
	return tri[0][0]


assert max_path_sum([[1, 0, 0], [4, 8, 0], [1, 5, 3]], 2, 2) == 14
assert max_path_sum([[13, 0, 0], [7, 4, 0], [2, 4, 6]], 2, 2) == 24 
assert max_path_sum([[2, 0, 0], [11, 18, 0], [21, 25, 33]], 2, 2) == 53
