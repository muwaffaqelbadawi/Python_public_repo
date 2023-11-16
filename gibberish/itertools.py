import textwrap

def main():

  text = 'I\'m gonna take a shower because i\'m too stinky and it\'s so difficult to me to stay like this and doing nothing for that is too heavy to me I can\'t bear that'

  width = 20

  wrappedLine = textwrap.wrap(text, width)

  for line in wrappedLine:
    print(len(line), line)

  print('\n----------------\n')

  print(textwrap.fill(text, width))


if __name__ == '__main__':
  main()










# import functools

# def funcWrapper(outfunc):
#   print('i\'m a function wrapper')
#   @functools.wraps(outfunc)
#   def inside():
#     print('I am inside')
#     return outfunc()
#   return inside



# @funcWrapper
# def out():
#   return 'Iam out blah blah blah' 

# print(out.__name__)




















# import itertools

# _list = [True, True, False, True]

# x = lambda x: x is True

# # print(list(x))

# a = filter(x, _list)

# print(list(a))

# _list = [item for item in range(3)]


# counter = itertools.count(start=8, step=2)


# counter = itertools.combinations_with_replacement([i for i in range(4)], 4)

# print(len(list(counter)))


# _repeat = itertools.repeat(6, times=10)
# _repeat = itertools.repeat(2, times=3)

# squares = itertools.starmap(pow, [pair for pair in enumerate(_repeat)])

# print(list(squares))


# for item in enumerate([i for i in range(3)]):
#   print(item)

# for _iter in _repeat:
#   print(_iter, end=' ')

# print(pow)

# print(lambda)

# squares = map(pow, range(10), itertools.repeat(2))

# print(tuple(squares))

# print(next(_repeat))
# print(next(_repeat))
# print(next(_repeat))

# print(next(_repeat))
# print(next(_repeat))



# pair = list(itertools.zip_longest(range(15), _list))


# pair = itertools.zip_longest(range(1, 11), [i for i in range(5, 11)])

# print(next(pair))
# print(next(pair))
# print(next(pair))

# print(next(next(pair)))

# def _iter(t):
#   while next(t)[1]:
#     pair = next(t)
#     key, value = pair[0], pair[1]
#     print((key, value))

# _iter(pair)

# _iter(_list)

# def g(l):
#   for item in l:
#     yield item

# q = g([1,2])




# pair = zip(itertools.count(), _list)

# switch = [0, 1] 



# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# pair = list(zip(range(500), _list))

# couple = enumerate(_list, next(counter))


# print(pair)


# for i in range(len(_list)):
#   print(next(couple))

# print(next(pair)


# print(list(pair))
# for j, k in pair:
#   print(j, k)

# for i in counter:
#   print(i)

# for i in range(len(_list)):
#   print(_list[next(counter)])

# def c():
#   pair = []
#   for key, value in pair:
#     if value is None:
#       value = key % 14
#       pair.append((key, value))
#   return pair

# def _cycle(_iter, no):

#   counter = itertools.cycle(_iter)

#   for i in range(no):
#     for j in range(len(_iter)):
#       print(next(counter))

# _cycle(switch, 3)

# print(pow(5, 2, 5))