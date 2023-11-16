import urllib.request
import urllib.parse
import re

url = 'https://www.pythonprogramming.net'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall('<p>(.*?)</p>', str(respData))
for eachp in paragraphs:
  print(eachp)










# '''url = 'https://pythonprogramming.net'
# values = {'s':'basic',
#           'submit':'search'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# print(respData)

# # request = urllib.request.urlopen('https://google.com')

# # print(request.read())'''

# try:
#   request = urllib.request.urlopen('https://google.com/search?q=test')
#   print(request.read())
# except Exception as e:
#   print(e)
  
  
# try:
#   url = urllib.request.urlopen('https://google.com/search?q=test')
#   headers = {}
#   headers['User-Agent'] = 'Mozilla/5.0 (X11, Linux i686) AppleWebKit/537.17 (HTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
#   req = url.request.Request(url, headers=headers)
#   resp = url.request.urlopen(req)
#   reqData = resp.read()

#   saveFile = open('c:\\Users\\Muwaffuq\\Desktop\\WithHeaders.txt', 'w')
#   saveFile.write(str(reqData))
#   saveFile.close()

# except Exception as e:
#   print(e)