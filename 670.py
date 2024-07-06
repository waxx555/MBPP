'''
Write a python function to check whether a sequence of numbers has a decreasing trend or not.
'''


def decreasing_trend(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False


assert decreasing_trend([-4,-3,-2,-1]) == True
assert decreasing_trend([1,2,3]) == True
assert decreasing_trend([3,2,1]) == False
