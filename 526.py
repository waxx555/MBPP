'''
Write a python function to capitalize first and last letters of each word of a given string.
'''


def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  


assert capitalize_first_last_letters("python") == "PythoN"
assert capitalize_first_last_letters("bigdata") == "BigdatA"
assert capitalize_first_last_letters("Hadoop") == "HadooP"
