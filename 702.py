'''
Write a function to find the minimum number of elements that should be removed such that amax-amin<=k.
'''


def find_ind(key, i, n, 
			k, arr):
	ind = -1
	start = i + 1
	end = n - 1;
	while (start < end):
		mid = int(start +
				(end - start) / 2)
		if (arr[mid] - key <= k):
			ind = mid
			start = mid + 1
		else:
			end = mid
	return ind
def removals(arr, n, k):
	ans = n - 1
	arr.sort()
	for i in range(0, n):
		j = find_ind(arr[i], i, 
					n, k, arr)
		if (j != -1):
			ans = min(ans, n -
						(j - i + 1))
	return ans


assert removals([1, 3, 4, 9, 10,11, 12, 17, 20], 9, 4) == 5
assert removals([1, 5, 6, 2, 8], 5, 2) == 3
assert removals([1, 2, 3 ,4, 5, 6], 6, 3) == 2
