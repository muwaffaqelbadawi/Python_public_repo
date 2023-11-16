lOfItems = ['A', 'B', 1, 2, 3]

isString = all(isinstance(item, str) for item in lOfItems)

print(isString)
