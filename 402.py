'''
Write a function to compute the value of ncr%p.
'''


def ncr_modp(n, r, p): 
    C = [0 for i in range(r+1)]   
    C[0] = 1
    for i in range(1, n+1): 
        for j in range(min(i, r), 0, -1): 
            C[j] = (C[j] + C[j-1]) % p   
    return C[r] 


assert ncr_modp(10,2,13)==6
assert ncr_modp(15,12,43)==25
assert ncr_modp(17,9,18)==10
