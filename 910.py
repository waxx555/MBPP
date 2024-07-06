'''
Write a function to validate a gregorian date.
'''


import datetime
def check_date(m, d, y):
    try:
        m, d, y = map(int, (m, d, y))
        datetime.date(y, m, d)
        return True
    except ValueError:
        return False


assert check_date(11,11,2002)==True
assert check_date(13,11,2002)==False
assert check_date('11','11','2002')==True
