'''
Write a function to find the maximum sum that can be formed which has no three consecutive elements present.
'''


def max_sum_of_three_consecutive(arr, n): 
	sum = [0 for k in range(n)] 
	if n >= 1: 
		sum[0] = arr[0] 
	if n >= 2: 
		sum[1] = arr[0] + arr[1] 
	if n > 2: 
		sum[2] = max(sum[1], max(arr[1] + arr[2], arr[0] + arr[2])) 
	for i in range(3, n): 
		sum[i] = max(max(sum[i-1], sum[i-2] + arr[i]), arr[i] + arr[i-1] + sum[i-3]) 
	return sum[n-1]


assert max_sum_of_three_consecutive([100, 1000, 100, 1000, 1], 5) == 2101
assert max_sum_of_three_consecutive([3000, 2000, 1000, 3, 10], 5) == 5013
assert max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8], 8) == 27
