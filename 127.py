'''
Write a function to multiply two integers without using the * operator in python.
'''


def multiply_int(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)


assert multiply_int(10,20)==200
assert multiply_int(5,10)==50
assert multiply_int(4,8)==32
