'''
Write a python function to find the digit distance between two integers.
'''


def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))


assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(23,56) == 6
assert digit_distance_nums(123,256) == 7
