'''
Write a function to check whether a given string has a capital letter, a lower case letter, a number and specified length using lambda function.
'''


def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result  


assert check_string('python')==['String must have 1 upper case character.', 'String must have 1 number.', 'String length should be atleast 8.']
assert check_string('123python')==['String must have 1 upper case character.']
assert check_string('123Python')==['Valid string.']
