'''
Write a python function to sort a list according to the second element in sublist.
'''


def Sort(sub_li): 
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 


assert Sort([['a', 10], ['b', 5], ['c', 20], ['d', 15]]) == [['b', 5], ['a', 10], ['d', 15], ['c', 20]]
assert Sort([['452', 10], ['256', 5], ['100', 20], ['135', 15]]) == [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
assert Sort([['rishi', 10], ['akhil', 5], ['ramya', 20], ['gaur', 15]]) == [['akhil', 5], ['rishi', 10], ['gaur', 15], ['ramya', 20]]
