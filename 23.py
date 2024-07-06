'''
Write a python function to find the maximum sum of elements of list in a list of lists.
'''


def maximum_Sum(list1): 
    maxi = -100000
    for x in list1: 
        sum = 0 
        for y in x: 
            sum+= y      
        maxi = max(sum,maxi)     
    return maxi 


assert maximum_Sum([[1,2,3],[4,5,6],[10,11,12],[7,8,9]]) == 33
assert maximum_Sum([[0,1,1],[1,1,2],[3,2,1]]) == 6
assert maximum_Sum([[0,1,3],[1,2,1],[9,8,2],[0,1,0],[6,4,8]]) == 19
