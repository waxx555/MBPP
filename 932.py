'''
Write a function to remove duplicate words from a given list of strings.
'''


def remove_duplic_list(l):
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return temp


assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises"])==['Python', 'Exercises', 'Practice', 'Solution']
assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","Java"])==['Python', 'Exercises', 'Practice', 'Solution', 'Java']
assert remove_duplic_list(["Python", "Exercises", "Practice", "Solution", "Exercises","C++","C","C++"])==['Python', 'Exercises', 'Practice', 'Solution','C++','C']
