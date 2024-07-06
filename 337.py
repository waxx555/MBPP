'''
Write a function that matches a word at the end of a string, with optional punctuation.
'''


import re
def text_match_word(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'


assert text_match_word("python.")==('Found a match!')
assert text_match_word("python.")==('Found a match!')
assert text_match_word("  lang  .")==('Not matched!')
