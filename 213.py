'''
Write a function to perform the concatenation of two string tuples.
'''


def concatenate_strings(test_tup1, test_tup2):
  res = tuple(ele1 + ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 


assert concatenate_strings(("Manjeet", "Nikhil", "Akshat"), (" Singh", " Meherwal", " Garg")) == ('Manjeet Singh', 'Nikhil Meherwal', 'Akshat Garg')
assert concatenate_strings(("Shaik", "Ayesha", "Sanya"), (" Dawood", " Begum", " Singh")) == ('Shaik Dawood', 'Ayesha Begum', 'Sanya Singh')
assert concatenate_strings(("Harpreet", "Priyanka", "Muskan"), ("Kour", " Agarwal", "Sethi")) == ('HarpreetKour', 'Priyanka Agarwal', 'MuskanSethi')
