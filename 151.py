'''
Write a python function to check whether the given number is co-prime or not.
'''


def gcd(p,q):
    while q != 0:
        p, q = q,p%q
    return p
def is_coprime(x,y):
    return gcd(x,y) == 1


assert is_coprime(17,13) == True
assert is_coprime(15,21) == False
assert is_coprime(25,45) == False
