'''
Write a function to count the longest repeating subsequences such that the two subsequences don’t have same string characters at same positions.
'''


def find_longest_repeating_subseq(str): 
	n = len(str) 
	dp = [[0 for k in range(n+1)] for l in range(n+1)] 
	for i in range(1, n+1): 
		for j in range(1, n+1): 
			if (str[i-1] == str[j-1] and i != j): 
				dp[i][j] = 1 + dp[i-1][j-1] 
			else: 
				dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
	return dp[n][n]


assert find_longest_repeating_subseq("AABEBCDD") == 3
assert find_longest_repeating_subseq("aabb") == 2
assert find_longest_repeating_subseq("aab") == 1
