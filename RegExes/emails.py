import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[A-Za-z]+@[A-Za-z]+\.com')
# pattern = re.compile(r'[A-Za-z0-9.]+@[A-Za-z]+\.(com|edu)')
# pattern = re.compile(r'[A-Za-z0-9.-]+@[A-Za-z-]+\.(com|edu|net)')
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

pattern = r'@([\w\-]+)\.([\w\-]+)'

domains = re.findall(pattern, emails)

for domain in domains:
    print(domain[0] + '.' + domain[1])








# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)
