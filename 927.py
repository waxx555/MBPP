'''
Write a function to calculate the height of the given binary tree.
'''


class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1


assert (max_height(root)) == 3
assert (max_height(root1)) == 5 
assert (max_height(root2)) == 4
