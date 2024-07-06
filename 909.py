'''
Write a function to find the previous palindrome of a specified number.
'''


def previous_palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x


assert previous_palindrome(99)==88
assert previous_palindrome(1221)==1111
assert previous_palindrome(120)==111
