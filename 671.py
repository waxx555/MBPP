'''
Write a python function to set the right most unset bit.
'''


import math 
def get_Pos_Of_Right_most_Set_Bit(n): 
    return int(math.log2(n&-n)+1)   
def set_Right_most_Unset_Bit(n): 
    if (n == 0): 
        return 1
    if ((n & (n + 1)) == 0):     
        return n 
    pos = get_Pos_Of_Right_most_Set_Bit(~n)      
    return ((1 << (pos - 1)) | n) 


assert set_Right_most_Unset_Bit(21) == 23
assert set_Right_most_Unset_Bit(11) == 15
assert set_Right_most_Unset_Bit(15) == 15
