class Hash_Map:
  def __init__(self):
    self.size = 6
    self.map = [None] * self.size

  def _get_hash(self, key):
    _hash = 0
    for char in str(key):
      _hash += ord(char)
    return _hash % self.size

  def add(self, key, value):
    key_hash = self._get_hash(key)
    key_value = [key, value]

    if self.map[key_hash] is None:
      self.map[key_hash] = [key_value]
      return self.map
    else:
      for pair in self.map[key_hash]:
        if pair[0] == key:
          pair[1] = value
          return True
        self.map[key_hash].append(key_value)
        return True
  
  def get(self, key, value):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is not None:
      for pair in self.map[key_hash]:
        if pair[0] == key:
          return pair[1]
      return None

  def delete(self, key):
    key_hash = self._get_hash(key)
    if self.map[key_hash] is None:
      return None
    for i in range(0, len(self.map[key_hash])):
      if self.map[key_hash][i][0] == key:
        self.map[key_hash].pop(i)
        return True

  def _print(self, key):
    for item in self.map:
      if item is not None:
        print(item)




h = Hash_Map()
print(h.add(0, 'k'))
h.add(1, 'k')

# import string

# l = [5,8,9,4,5]
# t1 = (1,2,3,4)
# t2 = ('q','e','t','r')

# for i,y in zip(l,t2):
#   print(i,y, end=' ')


# a = []
# for i,y in zip([i for i in range(5)],[i for i in range(5,10)]):
#   a.append([i,y])

# for pair in a:
#   print(pair[0], end=' ')


# key, value = 1, 'a'

# a = [key, value]


# print(list([a]))


# nested_array = [[1, 'apple'], [2, 'orange']]

# print(nested_array[1][1][0])


# no = 123

# print(ord(str(no)[0]))




# def char_map(*args):
#   _map = {}
#   for char, no in zip(args[0], args[1]):
#     _map[char]  = ord(char)
#     _map[no] = ord(str(no))

#   return _map


# print(char_map(string.ascii_lowercase, [i for i in range(10)]))