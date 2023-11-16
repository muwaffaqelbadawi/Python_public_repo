import requests

# r = requests.get('https://xkcd.com/353/')
# img = requests.get('https://imgs.xkcd.com/comics/python.png')
# payload = {'username':'Muwaffuq', 'password':'fofu'}
# http = requests.get('https://httpbin.org/get', params=payload)
# _http = requests.post('https://httpbin.org/post', data=payload)
# _http = requests.get('http://httpbin.org/basic-auth/Muwaffuq/fofu', auth=('Muwaffuq', 'fofu'))
_http = requests.get('http://httpbin.org/delay/6', timeout=3)

print(_http)


# status_code
# ok
# r.headers
# http.text
# http.url
# r_dict = _http.json()
# print(r_dict['form'])
# print(dir(r))
# help(r)
# print(img.content)
# with open('C:\\Users\\Muwaffuq\\Desktop\\img.png', 'wb') as f:
#   f.write(img.content)