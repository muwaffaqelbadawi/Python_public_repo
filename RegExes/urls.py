import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'[a-z]+s?://(w.|[a-z])+\.com')
# pattern = re.compile(r'https?://(www\.)?\w+\.(com|gov)')
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


matches = pattern.finditer(urls)

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# for match in matches:
#   # print(match)
    # print(match.group(1))  #entire url
    # print(match.group(2))  #domain name
#   # print(match.group(3))  #top level domain
