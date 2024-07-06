'''
Write a function to re-arrange the given array in alternating positive and negative items.
'''


def right_rotate(arr, n, out_of_place, cur):
	temp = arr[cur]
	for i in range(cur, out_of_place, -1):
		arr[i] = arr[i - 1]
	arr[out_of_place] = temp
	return arr
def re_arrange(arr, n):
	out_of_place = -1
	for index in range(n):
		if (out_of_place >= 0):
			if ((arr[index] >= 0 and arr[out_of_place] < 0) or
			(arr[index] < 0 and arr[out_of_place] >= 0)):
				arr = right_rotate(arr, n, out_of_place, index)
				if (index-out_of_place > 2):
					out_of_place += 2
				else:
					out_of_place = - 1
		if (out_of_place == -1):
			if ((arr[index] >= 0 and index % 2 == 0) or
			 (arr[index] < 0 and index % 2 == 1)):
				out_of_place = index
	return arr


assert re_arrange([-5, -2, 5, 2, 4,	7, 1, 8, 0, -8], 10) == [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]
assert re_arrange([1, 2, 3, -4, -1, 4], 6) == [-4, 1, -1, 2, 3, 4]
assert re_arrange([4, 7, 9, 77, -4, 5, -3, -9], 8) == [-4, 4, -3, 7, -9, 9, 77, 5]
