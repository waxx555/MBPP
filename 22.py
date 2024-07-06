'''
Write a function to find the first duplicate element in a given array of integers.
'''


def find_first_duplicate(nums):
    num_set = set()
    no_duplicate = -1

    for i in range(len(nums)):

        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add(nums[i])

    return no_duplicate


assert find_first_duplicate(([1, 2, 3, 4, 4, 5]))==4
assert find_first_duplicate([1, 2, 3, 4])==-1
assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2])==1
