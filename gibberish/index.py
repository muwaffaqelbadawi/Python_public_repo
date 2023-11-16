# import pygame

# pygame.init()

songs = dict(
  song1 = 'C:\\Users\\Muwaffuq\\Music\\Burak Yeter - Happy.mp3',
  song2 = 'C:\\Users\\Muwaffuq\\Music\\Calvin Harris - My Way (Official Video).mp3',
  song3 = 'C:\\Users\\Muwaffuq\\Music\\Charli XCX - 3am (Pull Up) feat. MØ [Official Audio].mp3',
  song4 = 'C:\\Users\\Muwaffuq\\Music\\Dami Im - Gladiator.mp3',
  song5 = 'C:\\Users\\Muwaffuq\\Music\\Daya - Words (Night Version).mp3'
)


class move(object):
  def __init__(self):
    self._pos = None

  @property
  def pos(self):
    if self._pos is not None:
      return self._pos
  
  @pos.setter
  def pos(self, pos):
      self._pos = pos

  def _next(self):
    for song in songs:
      yield songs[song]

  def previous(self):
    for i in range(len(songs)-1,-1,-1):
      yield songs[list(songs)[i]]

  @pos.getter
  def pos(self):
    return self._pos


m = move()
n = m._next()
p = m.previous()
print(m.pos)
m.pos = next(n)
m.pos = next(n)
m.pos = next(p)

print(m.pos)


# import logging
# import sample


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# fileHandler = logging.FileHandler('sample.log')
# fileHandler.setLevel(logging.ERROR)
# fileHandler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)

# logger.addHandler(fileHandler)
# logger.addHandler(stream_handler)


# def add(x, y):
#   '''add Function'''
#   return x + y

# def subtract(x, y):
#   '''subtract Function'''
#   return x - y

# def multiply(x, y):
#   '''multiply Function'''
#   return x * y

# def divide(x, y):
#   '''divide Function'''
#   try:
#     result = x / y
#   except ZeroDivisionError:
#     logger.exception('try divide by zero')
#   else:
#     return result

# num_1 = 10
# num_2 = 0

# add_result = add(num_1, num_2)
# logger.debug('Add: {0} + {1} = {2}'.format(num_1, num_2, add_result))

# subtract_result = subtract(num_1, num_2)
# logger.debug('Add: {0} - {1} = {2}'.format(num_1, num_2, subtract_result))

# multiply_result = multiply(num_1, num_2)
# logger.debug('Add: {0} * {1} = {2}'.format(num_1, num_2, multiply_result))

# divide_result = divide(num_1, num_2)
# logger.debug('Add: {0} / {1} = {2}'.format(num_1, num_2, divide_result))




# import logging

# logging.basicConfig(filename='people.log', level=logging.DEBUG,
#       format='%(levelname)s:%(message)s')

# class person(object):
#   def __init__(self, firstname, lastname):
#     self.firstName = firstname
#     self.lastName = lastname

#     logging.debug('my name is {0}\nmy email is {1}'.format(self.fullName, self.email))
  
#   @property
#   def email(self):
#     return '{0}.{1}@email.com'.format(self.firstName, self.lastName)
#   @property
#   def fullName(self):
#     return '{0} {1}'.format(self.firstName, self.lastName)

# p1 = person('Carl', 'anderson')
# p2 = person('Suzanne', 'Clark')
# p3 = person('John', 'Doe')

# def example(**kwargs):
#   return kwargs.values()
# print(example(a=5, b=6, c=1))
# def main_function(outdoor_function):
#   def local_function(*args, **kwargs):
#     print('this is will be printed out before {0} executed'.format(outdoor_function.__name__))
#     return outdoor_function(*args, **kwargs)
#   return local_function

# class decorator_class(object):
#   def __init__(self, outdoor_function):
#     self.outdoor_function = outdoor_function

#   def __call__(self, *args, **kwargs):
#     print('this is will be printed out before {0} executed'.format(self.outdoor_function.__name__))
#     return self.outdoor_function(*args, **kwargs)

# @decorator_class
# def outdoor_function():
#   print('I am the outdoor function')

# @decorator_class
# def display_info(*args):
#   print('my name {0[0]} and i\'m in {0[1]}'.format(args))

# display_info('Muwaffuq', 22)
# outdoor_function()

# outdoor_function = main_function(outdoor_function)
# outdoor_function()

# outdoor_function_display = main_function(outdoor_function)
# outdoor_function_display()

# from functools import reduce

# str
# bool
# filter
# reduce

# a = filter(lambda x: x % 2 == 0, [i for i in range(5)])
# print(type(a))

# for i in a:
#   print(i)

# def A(*args):
#   for i in args:
#     print(i)
  
# A(1,2,3,4,5).__ 

# a = lambda x: x<10

# help(map)

# _list = list((i for i in range(5)))
# print(_list)

# L = [num for num in range(1, 11)]
# def calc(_list):
#   _sum = 0
#   for i in _list:
#     _sum+=i
#     yield _sum

# gen = calc(num for num in range(1, 11))

# print(gen[0])

# for i in range(len(L)):
#   _sum = L[i]
#   _sum+=L[i+1]
#   print('{0} + {1} = {2}'.format(next(gen), L[i+1], _sum))

# def even():
#   evenList = []
#   for num in L:
#     if num % 2 == 0:
#        evenList.append(num)
#   return evenList

# print(2 % 2 == 0)

# print(even())

# even = lambda num: num % 2 == 0
# g = map(lambda num: num % 2 == 0, L)
# q = filter(lambda num: num % 2 == 0, L)

# r = reduce(lambda x,y: x+y, L)
# print(r)

# print(list(q))

# print(list(g)
# print(g.__iter__)

# print(type(test))

# a = map

# print(list(g))

# print(even(6))

# print(4 % 2)

# print(a.__bases__)

# a = lambda x: x in L
# c = lambda y: y<10 or y>11
# d = lambda z: z>2 & z<3
# e = lambda j: j<10 | j>8

# b = any(x for x in L)

# # print(d(7))
# print(type(d(7)))

# print(a())
# print(type(a))

# print(type(a))
# print(type(b))

# def check():
#   if M:
#     return True
#   else:
#     return False

# print(check())
# print(type(check))

# if any(y for y in M):
#   print(M)
# else:
#   print('it\'s empty')

# if M:
#   print(M)
# else:
#   print('it\'s empty')

# print(b)

# def Gen(*L):
#   for i in L:
#     yield i

# g = Gen(1,2,3,4,5,6)

# for i in range(6):
#   print(next(g))

# class A:
#   pass

# class B(A):
#   pass

# class C(B):
#   pass

# print('mor: {0}, {1}, {2}'.format(C.__bases__, B.__bases__, A.__bases__))
# print(C.__mro__)

# __file__
# __all__
# __module__
# __bases__
# __mro__
# __eq__
# __ge__
# print(__name__)  current module == __main__
# print(__file__)  current module  == fileName.py
# print(imported_module.__name__)  imported module == fileName
# print(imported_module.__file__)  imported module == file directory


# class Car(object):
#   def __init__(self, logo, color):
#     self.logo = logo
#     self.color = color
#   def Mobility(self):
#     return '{0} car with {1} color going ahead to New York'.format(self.logo, self.color)
#   def typo(self):
#     return type(self)

# class Hyundai(Car):
#   def __init__(self, logo, color):
#     super(Hyundai, self).__init__(logo, color)

# Accent = Hyundai('Hyundai', 'white')
# print(Accent.Mobility())
# print(Accent.typo())

# help(Hyundai)

# print(object.__mro__)
# print(Car.__mro__)
# print(Hyundai.__mro__)

# _tuple = (1,2,3,4,5,6)

# def arbitrary(*args, **kwargs):
#   # result = args[2] + args[1]
#   for i in args:
#     print(i)
#   for j in kwargs:
#     print('{0} : {1}'.format(j,kwargs[j]))
#   # name = kwargs[args[0]]
#   # return result, name

# arbitrary('name',2,3,4,5,
# name = 'Muwaffuq',
# age = 22,
# profession = "SE"
# )

# import threading, time

# def sleeper(n,name):
#   print('Hi I am a {} i\'m going to sleep for {}'.format(name, n))
#   time.sleep(n)
#   print('{} has woken up from sleep \n'.format(name))

# thread_list = []
# start = time.time()
# for i in range(5):
#   t = threading.Thread(target=sleeper, name='thread{}'.format(i), args=(5, 'thread{}'.format(i)
#   ))
#   thread_list.append(t)
#   t.start()
#   print('{} has started'.format(t.name))

# for t in thread_list:
#   t.join()

# end = time.time()

# print('time taking: {0}'.format(end-start))
# print('all five threads have finished')


# def sleeper(n,name):
#   print('Hi I am a {} i\'m going to sleep for {}'.format(name, n))
#   time.sleep(n)
#   print('{} has woken up from sleep \n'.format(name))

# start = time.time()

# for i in range(5):
#   print('iteration {} has started'.format(i))
#   sleeper(5, i)

# end = time.time()

# print('time taken: {}'.format(end-start))

# def threadingFunc(n, name):
#   print('I am a {0} function and i\'m going to sleep for {1} seconds'.format(name,n))
#   time.sleep(5)
#   print('I am waking now')

# t = threading.Thread(target=threadingFunc, name='thread1', args=(5, 'thread1'))

# t.start()
# t.join()


# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')
# print('Hello World')

# _tuple = ()
# print(bool(_tuple))

# def func(**kwargs):
#   return type(kwargs)
  
# print(func(
#   name = 'Muwaffuq'
# ))

# class identity:
#   def __init__(self, name, age, profession):
#     self.name = name
#     self.age = age
#     self.profession = profession

#   def attr(self):
#     return self

# carl = identity('carl', 30, 'Lawyer')
# print(carl.attr.-

# _dict = dict(
#   name = 'Muwaffuq',
#   age = 22,
#   profession = 'SE'
# )

# for i in _dict:
#   print(i)

# def Array(L):
#   _list = [L]
#   return _list
# print(Array(range(5)))

# print(array)

# import pygame

# class decorator_class:
#   def __init__(self, myFunc):
#     self.myFunc = myFunc
#   def __call__(self, *args, **kwargs):
#      print('call method executed this before {}'.format(self.myFunc.__name__))
#      return self.myFunc() 


# def decorator_function(myFunc):
#   def wrapper_function():
#     print('this will be executed before {}'.format(myFunc.__name__))
#     return myFunc()
#   return wrapper_function




# @decorator_class
# def myFunc():
#   print('this is my function')

# myFunc()



# _dict = {
#   'name':'Muwaffuq',
#   'age':22,
#   'profession': 'SE'
#   }

# for keys in _dict:
#   print('{0}:{1}'.format(keys, _dict[keys]))

# array = [[x for x in range(5)] for y in range(5)]

# for x in range(len(array)):
#   for y in range(len(array[x])):
#     print('({0},{1}) = {2}'.format(x,y,array[x][y]))

# width = 800
# heighth = 600
# default_Color_bg = (100,100,100)
# wight = (255,255,255)
# black = (0,0,0)
# blue = (0,0,255)

# x_coordinates = [0,10,20,30,40]
# y_coordinates = [0,10,20,30,40]

# pygame.init()
# MAIN_SURFACE = pygame.display.set_mode((width,heighth))
# pygame.display.set_caption('Resolution')

# close = False

# while not close:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       close = True

#   MAIN_SURFACE.fill(default_Color_bg)
#   pygame.draw.rect(MAIN_SURFACE, blue, [200, 200, 40, 40])
#   pygame.display.update()

# pygame.quit()
# quit()

# from pprint import pprint

#                          0 0 0
#                          0 0 0 
#                          0 0 0
# 


# nested_list = [ [ [1] ] ]



# print(nested_list[0][0][0])



# print(nested.count([]))


# print(nested[0][0][0][0])


# nested_list = [[x for x in range(1,5)] for y in range(5)]
# print(nested_list)

# print(nested_list[0])

# for i in nested_list:
#  print(i)