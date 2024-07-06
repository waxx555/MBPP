'''
Write a python function to find the character made by adding all the characters of the given string.
'''


def get_Char(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)


assert get_Char("abc") == "f"
assert get_Char("gfg") == "t"
assert get_Char("ab") == "c"
