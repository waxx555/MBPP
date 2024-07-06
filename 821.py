'''
Write a function to merge two dictionaries into a single expression.
'''


import collections as ct
def merge_dictionaries(dict1,dict2):
    merged_dict = dict(ct.ChainMap({}, dict1, dict2))
    return merged_dict


assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White'}
assert merge_dictionaries({ "R": "Red", "B": "Black", "P": "Pink" },{ "O": "Orange", "W": "White", "B": "Black" })=={'O': 'Orange', 'P': 'Pink', 'B': 'Black', 'W': 'White', 'R': 'Red'}
assert merge_dictionaries({ "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'W': 'White', 'O': 'Orange', 'G': 'Green', 'B': 'Black'}
