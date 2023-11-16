from pprint import pprint


users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

for user in users:
  # print(type(user))
  user["friends"] = []
  
pprint(users)
  
  
  
for i, j in friendships:
  # this works because users[i] is the user whose id is i
users[i]["friends"].append(users[j]) # add i as a friend of j
users[j]["friends"].append(users[i]) # add j as a friend of i


