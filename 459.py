'''
Write a function to remove uppercase substrings from a given string by using regex.
'''


import re
def remove_uppercase(str1):
  remove_upper = lambda text: re.sub('[A-Z]', '', text)
  result =  remove_upper(str1)
  return (result)


assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
