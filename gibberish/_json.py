import json

people_string = '''
{
  "people": [
  {
    "name": "Muwaffuq Faiz Albadawi",
    "phone": "0928071191",
    "emails": ["moaffage@gmail.com", "mr.moaffag10@hotmail.com"],
    "has liscense": false
  },
  {
    "name": "Jhon Doe",
    "phone": "666-696969",
    "emails": null,
    "has liscense": true
  }
  ]
}
'''

data = json.loads(people_string)
for person in data['people']:
  del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

# print(type(data['people']))
# # print(data)