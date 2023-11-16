class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
class linkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    cur_node = self.head
    
    while cur_node:
      print(cur_node.data, end=' ')
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return

    last_node = self.head

    while last_node.next:
      last_node = last_node.next

    last_node.next = new_node

  def pappend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insertAfter(self, node, data):

    if not node:
      return 'node isn\'t found!!'

    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

    # new_node = Node(data)
    # cur_node = self.head
    # while cur_node.next:
    #   if node == cur_node.data:
    #     new_node.next = cur_node.next
    #     cur_node.next = new_node
    #     return
    #   cur_node = cur_node.next

  def delete_node(self, node):
    cur_node = self.head

    if node is cur_node:
      self.head = node.next
      node = None
      return
    
    prev_node = None

    while cur_node and cur_node.data != node:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev_node.next = cur_node.next
    cur_node = None

  def delete_at_pos(self, pos):
    cur_node = self.head

    if pos == 0:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    count = 1

    while cur_node and count != pos:
      prev_node = cur_node
      cur_node = cur_node.next
      count+=1

    if cur_node is None:
      return

    prev_node.next = cur_node.next
    cur_node = None

  def len_iterative(self):
    cur_node = self.head
    count = 0

    while cur_node:
      count+=1
      cur_node = cur_node.next
    return count

  def len_recursave(self, node):
    if node == None:
      return 0
    return 1 + self.len_recursave(node.next) 


  def swap_node(self, key_1, key_2):
    if key_1 == key_2:
      return
    
    prev_node1 = None
    cur_node1 = self.head

    while cur_node1 and cur_node1.data != key_1:
      prev_node1 = cur_node1
      cur_node1 = cur_node1.next

    prev_node2 = None
    cur_node2 = self.head

    while cur_node2 and cur_node2.data != key_2:
      prev_node2 = cur_node2
      cur_node2 = cur_node2.next

    if not cur_node1 or not cur_node2:
      return

    if cur_node1:
      prev_node1.next = cur_node2
    else:
      self.head = cur_node2

    if cur_node2:
      prev_node2.next = cur_node1
    else:
      self.head = cur_node1

    cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next


  def print_Nth_from_last(self, n):
    total_length = self.len_iterative()
    cur = self.head

    while cur:
      if total_length == n:
        print(cur.data)
        return cur
      total_length -= 1
      cur = cur.next
      if cur is None:
        return




_list = linkedList()
_list.append('A')
_list.append('B')
_list.append('C')
_list.append('D')

# print(_list.len_iterative())
# _list.print_list()

# print(_list.len_recursave(_list.head))

# _list.swap_node('B','D')

print(_list.print_Nth_from_last(7))

# _list.print_list()










# class Hash_Map:
#   def __init__(self):
#     self.size = 6
#     self.map = [None] * self.size

#   def _get_hash(self, key):
#     _hash = 0
#     for char in str(key):
#       _hash += ord(char)
#       return _hash % self.size

#   def add(self, key, value):
#     key_hash = self._get_hash(key)
#     key_value = [key, value]

#     if self.map[key_hash] is None:
#       self.map[key_hash] = list([key_value])
#       return True
#     else:
#       for pair in self.map[key_hash]:
#         if pair[0] == key:
#           pair[1] = value
#           return True
#       self.map[key_hash].append(key_value)
#       return True

#   def get(self, key):
#     key_hash = self._get_hash(key)
#     if self.map[key_hash] is not None:
#       for pair in self.map[key_hash]:
#         if pair[0] == key:
#           return pair[1]
#     return None

#   def delete(self, key, value):
#     key_hash = self._get_hash(key)

#     if self.map[key_hash] is None:
#       return False
#     for i in range(0, len(self.map[key_hash])):
#       if self.map[key_hash][i][0] == key:
#         self.map[key_hash].pop(i)
#         return True

#   def Print(self, key, value):
#     print('-----phonebook-----')
#     for item in self.map:
#       if item is not None:
#         print(str(item))

# # class Hash_Map:
# #   def __init__(self):
# #     self.size = 6
# #     self.list = [None] * self.size

# # h = Hash_Map()

# # # a = 1
# # # if not a:
# # #   print('kkk')
# # # print(a)

# # # for i in range(5):
# # #   x +=1
# # #   y +=1

# # # print(x, y)

# # # def coordinate(x,y):
# # #   if x & y is 0:
# # #     return 'either x or y is equal to zero'
# # #   return 'none of the coordinates is equal to zero'

# # # print(coordinate(5,5))

# # # l = [None]

# # # if l :
# # #   print(l[0])

# # # map_ = {
# # #   0:'a',
# # #   1:'b',
# # #   2:'c',
# # #   3:'d',
# # #   4:'e',
# # #   5:'f'
# # # }

# # # for i in range(5):
# # #   print(map_[i])

# # # _list = [1,2,3,4,5,6,7,8,9,10]

# # # _iter = (0,1,2,3,4,5,6,7,8,9)
# # # while _list and _iter%2==0:
# # #   try:
# # #     print(_list[_iter], end=' ')
# # #     _iter+=1
# # #   except IndexError:
# # #     break

# # # if ['']:
# # #   print('list')

# # # if not a:
# # #   print('l')

# # # a = 0

# # # def test(cur):
# # #   if cur:
# # #     return cur

# # # print(test(1))

# # # _list = [1,2,3]

# # # _list.append(0)

# # # def g():
# # #   for i in range(len(_list)-1):
# # #     print(i)
# # #     _list[i] = _list[-i]
# # #   return _list

# # # print(g())

# # # list_ = []

# # # class a:
# # #   def __init__(self, name):
# # #     self.name = name

# # # s = a('s')
# # # d = a('d')
# # # f = a('f')
# # # g = a('g')

# # # list_.append(s)
# # # list_.append(d)
# # # list_.append(f)
# # # list_.append(g)

# # # for i in list_:
# # #   print(i.name)

# # # a = False
# # # while not a:
# # #   print(1)
# # #   a = True

# # # class A:
# # #   def __init__(self, a):
# # #     self.a = a
# # #     self.b = None

# # # class b:
# # #   def __init__(self):
# # #     self.b = None

# # #   def get(self):
# # #     c = self.b.a

# # #   def g(self, a):
# # #     d = A(a)
# # #     self.b = d

# # # class A(object):
# # #   def __init__(self):
# # #     self._var1 = None

# # #   @property
# # #   def var1(self):
# # #     if self._var1 is not None:
# # #       return self._var1
# # #     return False

# # #   @var1.setter
# # #   def var1(self, var1):
# # #     self._var1 = var1

# # #   @var1.deleter
# # #   def var1(self):
# # #     print('deleted!')
# # #     self._var1 = None

# # #   @var1.getter
# # #   def var1(self):
# # #     return self._var1

# # # a = A()
# # # print(a._var1)
# # # a.var1 = 10
# # # print(a._var1)
# # # del(a.var1)
# # # print(a._var1)    

# # # class _property(object):
# # #   def __init__(self, fname='a', lname='b', names=None, age=10):
# # #     self.fname = fname
# # #     self.lname = lname
# # #     self.names = names
# # #     self.age = age

# # #   # @property
# # #   def fullName(self):
# # #     return '{0} {1}'.format(self.fname, self.lname)
# # #   # @fullName.setter
# # #   def setNames(self, name):
# # #     if self.names is not None:
# # #     self.fname, self.lname = name.split(' ') 

# # #   def delName(self, name):
# # #     self.fname = None
# # #     self.lname = None
# # #   def getName(self, name):

# # # p = _property('a', 'b', 5)
# # # print(p.fullName())
# # # p.setFullName('a d')
# # # print(p.fullName())

# # # var = None
# # # print(var is not None)
# # # print(var is None)

# # # help(is)
# # # print(10 is 10)

# # # if var is not None:
# # #   print(var)
# # # else:
# # #   var = []
# # #   var.append(None)

# # # print(var)



# # # import os, pygame
# # # from tkinter.filedialog import askdirectory
# # # from tkinter import*
# # # # from mutagen.easyid3 import EasyID3
# # # # from mutagen.mp3 import MP3
# # # from mutagen.id3 import ID3, ID3NoHeaderError

# # # root = Tk()
# # # root.minsize(300,300)

# # # listOfItems = []
# # # realNames=[]
# # # index = 0


# # # def directoryChooser():
# # #   directory = askdirectory()
# # #   os.chdir(directory)

# # #   for files in os.listdir(directory):
# # #     try:
# # #         if files.endswith(".mp3"):
# # #           listOfItems.append(files)

# # #           realdir = os.path.realpath(files)
# # #           # print(realdir)
# # #           audio = ID3(realdir)
# # #           # realNames.append(audio['TIT2'].text[0])
# # #     except ID3NoHeaderError:
# # #            audio = ID3(realdir)
      
# # #   pygame.mixer.init()
# # #   pygame.mixer.music.load(listOfItems[0])
# # #   # pygame.mixer.music.play()

# # # directoryChooser()

# # # label = Label(root, text='Music Player')
# # # label.pack()

# # # listbox = Listbox(root)
# # # listbox.pack()

# # # realNames.reverse()
# # # # listOfItems.reverse()

# # # for items in realNames:
# # #     listbox.insert(0,items)


# # # realNames.reverse()
# # # # listOfItems.reverse()


# # # nextButton = Button(root, text="next Music")
# # # nextButton.pack()

# # # previousButton = Button(root, text="previous Music")
# # # previousButton.pack()

# # # stopButton = Button(root, text="stop Music")
# # # stopButton.pack()

# # # root.mainloop()