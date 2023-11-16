import pygame
import index
from pygame import mixer

gray = (100,100,100)


pygame.init()
mixer.init()
forward = index._next()
backward = index.previous()
main_S = pygame.display.set_mode((800,600))
pygame.display.set_caption('test')


def play(link):
  mixer.music.load(link)
  mixer.music.play()


break_loop = False

while not break_loop:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      break_loop = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        play(next(forward))
      if event.key == pygame.K_LEFT:
        play(next(backward))
  main_S.fill(gray)
  pygame.display.update()

pygame.quit()
quit()



# gen = (word for word in ['serious','tedious','tough','miscellaneous'])
# print(next(gen))


# def next_song():
#   mixer.music.set_endevent(next(Q))
#   mixer.music.get_endevent()



# while True:
#   try:
#     print(next(g))
#   except StopIteration:
#     break


# print(_list[-4:])

# class animalActions:
#   def quack(self): return self.strings['quack']
#   def feathers(self): return self.strings['feathers']
#   def bark(self): return self.strings['bark']
#   def fur(self): return self.strings['fur']


# class Duck(animalActions):
#     strings = dict(
#     quack = 'Quaaaack!!',
#     feathers = 'the duck has gray and white feathers',
#     bark = 'the duck can not bark',
#     fur = 'the duck has no fur'
#   )

# class Person(animalActions):
#     strings = dict(
#     quack = 'the person imitate a duck',
#     feathers = 'the peerson takes a feathers from the ground and shows it',
#     bark = 'the person says woof!!',
#     fur = 'the person puts on a fur coat'
#   )

# class Dog(animalActions):
#     strings = dict(
#     quack = 'the dog cannot quack',
#     feathers = 'the dog has no feathers',
#     bark = 'Arf!',
#     fur = 'the dog has a wight fur with black spot'
#   )

# def in_the_dog_house(dog):
#   print(dog.bark())
#   print(dog.fur())

# def in_the_forest(duck):
#   print(duck.quack())
#   print(duck.feathers())

# def main():
#   donald = Duck()
#   john = Person()
#   spike = Dog()

#   print('in the forest:')
#   for o in (donald, john, spike):
#     in_the_forest(o)

#   print('in the dog house:')
#   for o in (donald, john, spike):
#     in_the_dog_house(o)

# main()

# print(type(dict))
# dict
# list
# int
# float
# set

# _dict = dict(
#   name = "Muwaffuq",
#   address = "block 84",
#   profession = "SE",
#   age = 22
# )

# print(_dict)

# _dict = {
#   'name': 'Muwaffuq',
#   'address': 'block 84',
#   'profession': 'SE',
#   'age': 22
# }

# a = ('asdf:dbbsfhb:ffFN:bsffb')

# print(a.split(':'), a.split())

# print(''.__subclasshook__())

# help(__module__)

# print(type(1), int.__class__)
# print(type(list), list.__class__)
# print(type([]), [].__class__)

# List = []

# print(False is bool([]))

# print(id(False), id(bool([])))


# while bool(List) is False:
#   print(List)


# if List:
#   print(List)
# List.append(1)
# print(List)




# help(zip)


# def gen():
#   for i in range(5):
#     yield i

# g = gen()
# g.hasnext()

# help(__all__())


# Dic = {1:'f'}
# print(Dic[1])




# _dict = {}

# _dict['a'] = 'b'

# print(_dict)




# a = []
# b = [None]


# class Gate:
#   def __init__(self):
#     self.entrance = []
#   def _pass(self):
#     self.entrance.append(1)

# g = Gate()
# g._pass()

# if g.entrance:
#   print('Access granted')
# else:
#   print('Access denied')

# print(a)


# print(any(i for i in a))
# print(any(i for i in b))

# if a:
#   print(a)

# if b:
#   print(b)


# print(type(None))

# print(bool([1]))
# print(bool([0]))
# print(bool({1}))
# print(bool((1)))
# print(bool({'f':'r'}))
# print(bool('e'))
# print(bool('UNKNOWN'))

# print(bool(None))
# print(bool([None]))


# init = []

# if init:
#   init.append('')
# print(init)


# class design:
#   def __init__(self):
#     self.act = 'UNKNOWN'

#   def Act(self):
#     if self.act:
#       self.act = []
#     self.act = 0
#     # return self.act



# if '':
#   print('str')
# print('vacation')

# print(bool(''))
# print(bool(None))
# print(bool(0))
# print(bool(False))
# print(bool(not False))
# print(bool(not None))
# print(bool(not True))
# print(bool(not 0))
# print(bool([]))
# print(bool({}))
# print(bool(()))
# print(bool(i for i in []))
# print(bool(any(i for i in [])))

# print(type(0))
# print(type(any(i for i in [])))
# print(type((1,2,3)))
# print(type({1,2,3}))
# print(type({'name':'Muwaffuq'}))
# print(type(i for i in []))

# D = design()

# print(D.act)
# D.Act()
# print(D.act)