'''
Write a function to calculate the number of digits and letters in a string.
'''


def dig_let(s):
 d=l=0
 for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
 return (l,d)


assert dig_let("python")==(6,0)
assert dig_let("program")==(7,0)
assert dig_let("python3.0")==(6,2)
