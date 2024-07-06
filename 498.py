'''
Write a python function to find gcd of two positive integers.
'''


def gcd(x, y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd


assert gcd(12, 17) == 1
assert gcd(4,6) == 2
assert gcd(2,9) == 1
