'''
Write a function to calculate electricity bill.
'''


def cal_electbill(units):
 if(units < 50):
    amount = units * 2.60
    surcharge = 25
 elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
 elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
 else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
 total = amount + surcharge
 return total


assert cal_electbill(75)==246.25
assert cal_electbill(265)==1442.75
assert cal_electbill(100)==327.5
