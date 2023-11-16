import os
import tkinter as tk
# from pprint import pprint
from mutagen.id3 import ID3
# from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from tkinter.filedialog import askdirectory
# import time

# path = "C://Users//Muwaffuq//Music//SENSE _u0026 SENSIBILITY by Jane Austen - FULL AudioBook ¦ Greatest AudioBooks.mp3"

_dir = askdirectory()

root = tk.Tk()
root.withdraw()
pathList = os.listdir(_dir)
class Tags:
  def __init__(self, path):
    self.tagDict = {}
    self.audioID3 = ID3(path)

  def get(self):
    for p in self.audioID3:
      print(p)


# t = Tags()

print(pathList)




# def musicRow():
#   os.chdir(_dir)
#   # print(os.curdir)

#   for path in pathList:
#     song = Tags(path)
#     yield song.printInfo()

# def _print(_property):
#   song = musicRow()
#   return next(song)[_property]

# print(_print('title'))


# print(song['title'])
# pprint(next(song))
# pprint(next(song))
# pprint(next(song))
# print(song.printInfo())
# musicRow()

# song = Tags()
# print(song.setTagPairs())

# print(dir(T.audioID3))

# if 'TIT2' in audioID3.keys():
#   title = audioID3['TIT2']
# else:
#   title = os.path.splitext(os.path.basename(audioID3.filename))[0]

# print(title)

# _map = {
#       'name': 'Muwaffuq',
#       'age': 22,
#       'level': 'intermediate'
#       }

# for key in _map.keys():
  # print(type(key))

# b = [1,2,3,4,5]

# print(b.__contains__(1))


# try:
#   Input = input('Enter your name\n')
#   if any(char.isdigit() for char in Input):
#     pass

# except KeyError:
#   print('you entered a digit')

# else:
#   print('there is no error at all')

# finally:
#   print('this will be printed fuck ya!!')


# gibberish = '1'

# print(gibberish.isdigit())


# //////print(dir(''))

# a = []


# test = '{0} {1} {2}'.format(1,2,3)
# _test = '{0} {0} {0}'.format(1)
# __test = '{0} {0} {0}'.format(1,2,3)
# ___test = '{2} {0} {1}'.format(1,2,3)
# ll = '{0} {1} {2}'.format('Muw','aff','uq')
# print(test)  
# print(_test)
# print(__test)
# print(___test)
# print(ll)

# a = f"{0}"

# print(a)

# help(''.format)


# class A:
#   def __init__(self):
#     self.list = [1,2,3]
#     self.a = 0
#     self.blah = self.list[self.a]
#   def Change(self):
#     self.a = 5

# a = A()
# print(a.a)
# a.Change()
# print(a.blah)
# print(a.a)
# print(a.blah)


# time.sleep()

# pprint - pretty print

# a = (i for i in range(5))
# Pass = True
# while(Pass):
#   try:
#     print(next(a))
#     time.sleep(3)
#   except StopIteration:
    # Pass = False


# a = 0

# def g():
#   global a
#   a = 5

# print(a)



# for i in askdirectory():
#   print(i, end='')

# print(tk.filedialog.askopenfilenames())

# print(os.link(askdirectory()))

# help()

# pprint(a)

# def gen_Func(nums):
#   for i in nums:
#       yield i

# generator = gen_Func(a)

# for i in range(len(a)):
#     print(next(generator))

# print(a)

# a = []

# a.append(
#   i for i in range(3)
# )

# print(a)

# print(a.count(a))

# print(os.path.splitext(os.path.basename(path))[0])

# a = 1.045227

# print("{:0.0f}{:0.0d}".format(a))

# easyID3 = EasyID3(path)

# print(easyID3.get('l'))



# help(os.stat)

# a = [i for i in range(10)]

# a = [1,2,3]

# for i in range(5):
#   a.append(i)

# b = [1,2,3,4]

# a.extend(a)

# print(a)


# help(a.extend)

# size = os.stat(path).st_size/1048576

# print(size)

# Sum = 0

# for i in range(3):
#   Sum+=1

# # print(Sum)


# s = ""

# for i in string.ascii_lowercase:
#   s+=i

# # print(s)




# a = "".join("Muwaffuq")

# # print(a)


# f = ""+"dfr"

# # print(f)

# dd = "".concat("ertyu")
# print(dd)




# def eg(a=1):
#   return a

# print(eg(2))





# print(  True is (not None)  )

# a = 10

# print( a==10 )



# a = 1
# b = 0
# c = 3

# if a:
#   print("i'm confused!!")

# if b:
#   print("I got it now")

# if c:
#   print("Ohh Yeah!!")

# if 1:
#   print("I am the one")



# isOpen = True

# if isOpen:
#   print("Enter")

# a = None


# if a:
#   print(None)

# if not a:
#   print(1)


# if not None:
#   print(1)

# if True:
#   print(1)

# if not False:
#   print(1)

# if None:
#   print(None)