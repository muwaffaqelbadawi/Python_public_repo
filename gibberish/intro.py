categories = [
{'id': 'animals', 'parent': None},
{'id': 'mammals', 'parent': 'animals'},
{'id': 'cats', 'parent': 'mammals'},
{'id': 'dogs', 'parent': 'mammals'},
{'id': 'chihuahua', 'parent': 'dogs'},
{'id': 'labrador', 'parent': 'dogs'},
{'id': 'prsian', 'parent': 'cat'},
{'id': 'siamese', 'parent': 'cat'}
]


# def out(categories, parent):
#   node = {}
  
a = lambda x: x == categories['parent']

for i in range(len(categories)):
  f = filter(a, categories)
  print(list(f))
    



# for i in range(len(categories)):
#   print(categories[i]['id'])



# print(categories[0]['id'])

# def makeTree(categories, parent):
#   node = {}
#   categories.filter(c, c.parent == parent)
#   return node

# print(makeTree())