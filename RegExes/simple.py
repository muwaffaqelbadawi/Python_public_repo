import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321--555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'


# print('\tTab')     #Tab
# print(r'\tTab')    #raw string

# pattern = re.compile(r'abc')
# pattern = re.compile(r'bca')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'[1-5]')
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[A-Z]')
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]') #nigate
# pattern = re.compile(r'[^b]at') #nigate
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') #common factor
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'Start')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'dne')
pattern = re.compile(r'start', re.I)


# matches = pattern.finditer(text_to_search)
# matches = pattern.finditer(sentence)
# matches = pattern.findall(text_to_search)
# matches = pattern.match(sentence)
matches = pattern.search(sentence)

print(matches)

# for match in matches:
#     print(match)


# with open("data.txt") as data_file:
#     content = data_file.read()

#     matches = pattern.finditer(content)

#     for match in matches:
#         print(match)


# print(text_to_search[1:4])

# pattern = re.compile(r'start', re.I)

# matches = pattern.search(sentence)

# print(matches)
