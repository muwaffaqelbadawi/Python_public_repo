# l1 = [1,2,3,4]
l2 = [5,6,7,8]

# print(l1+l2)

dict1 = {
  'name':'dgdg',
  'age':256,
  'c':5,
  'f':4,
  'r':7,
  (1,2,5):'jhg'
}

# keys, values = zip(*dict1.items())
# print(keys)
# print(values)

# l = list(zip(*dict1.items()))
# l = list(zip(*enumerate(l2)))

li = list(zip(*map(dict1.items, l2)))

print(li)



# print(type(dict1.items()))

# print(type(dictItems))

# print('{} value is being deleted'.format(dict1.pop('c')))

# print(dict1.setdefault('age'))
# print(dict1.setdefault('dd'))
# print(dict1.setdefault('e', 50))


# dict1.clear()
print(dict1)

# print(l2.pop(1))

# l1 = ['k',4]

# l2 = [i for i in range(10)]

# _iter = 0

# print(len(l2)/2)

# s = dict(
#   a = 0
# ) 

# print(eval('5'))

# for i in range(int(len(l2)/2)):
#   dict1.update([l2[_iter:_iter+2]])
#   _iter+=2

# dict1.update(
#   x = 1,
#   y = 5,
#   z = 3
# )


# dict1['name'] +=   ' {0}'.format(len(dict1['name']))

# print(type(' {0}'.format(4)))

# print(dict1)

# tuple_ = ()

# tuple_[0] = 'fff'

# print(tuple_)
