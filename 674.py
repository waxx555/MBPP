'''
Write a function to remove duplicate words from a given string using collections module.
'''


from collections import OrderedDict
def remove_duplicate(string):
  result = ' '.join(OrderedDict((w,w) for w in string.split()).keys())
  return result


assert remove_duplicate("Python Exercises Practice Solution Exercises")==("Python Exercises Practice Solution")
assert remove_duplicate("Python Exercises Practice Solution Python")==("Python Exercises Practice Solution")
assert remove_duplicate("Python Exercises Practice Solution Practice")==("Python Exercises Practice Solution")
