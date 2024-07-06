'''
Write a python function to get the position of rightmost set bit.
'''


import math
def get_First_Set_Bit_Pos(n):
     return math.log2(n&-n)+1


assert get_First_Set_Bit_Pos(12) == 3
assert get_First_Set_Bit_Pos(18) == 2
assert get_First_Set_Bit_Pos(16) == 5
