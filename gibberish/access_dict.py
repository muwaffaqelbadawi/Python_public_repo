import json

with open('D:/little projects/python/gibberish/apiExampleUsers.json') as access_json:
  data = json.load(access_json)
  
print(type(data))