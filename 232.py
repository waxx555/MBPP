'''
Write a function to get the n largest items from a dataset.
'''


import heapq
def larg_nnum(list1,n):
 largest=heapq.nlargest(n,list1)
 return largest


assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[100,90]
assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],5)==[100,90,80,70,60]
assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],3)==[100,90,80]
