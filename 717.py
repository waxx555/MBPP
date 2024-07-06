'''
Write a function to calculate the standard deviation.
'''


import math
import sys
def sd_calc(data):
    n = len(data)
    if n <= 1:
        return 0.0
    mean, sd = avg_calc(data), 0.0
    for el in data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))
    return sd
def avg_calc(ls):
    n, mean = len(ls), 0.0
    if n <= 1:
        return ls[0]
    for el in ls:
        mean = mean + float(el)
    mean = mean / float(n)
    return mean


assert sd_calc([4, 2, 5, 8, 6])== 2.23606797749979
assert sd_calc([1,2,3,4,5,6,7])==2.160246899469287
assert sd_calc([5,9,10,15,6,4])==4.070217029430577
