import string
import re

l_alphabet  = string.ascii_lowercase
u_alphabet  = string.ascii_uppercase
b_numbers = 123456789

sentence = 'This sentence start with blah blah blah'

pattern = re.compile(r'blah$')

matches = pattern.finditer(sentence)

indices = None

for match in matches:
  print(match)