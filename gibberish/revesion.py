class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class linkedlist:
  def __init__(self):
    self.head = None

  def print_node(self):
    cur_node = self.head
    while cur_node:
      print(cur_node.data, end=' ')
      cur_node = cur_node.next

  def add_node(self, data):
    new_node = Node(data)

    cur_node = self.head
    if cur_node is None:
      self.head = new_node
      return
    
    while cur_node.next:
      cur_node = cur_node.next
    cur_node.next = new_node

  def insert_before_node(self, node, data):
    new_node = Node(data)

    cur_node = self.head
    if node == cur_node.data:
      new_node.next = cur_node
      self.head = new_node
      return

    prev_node = None
    while cur_node and cur_node.data != node:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node == None:
      return

    prev_node.next = new_node
    new_node.next = cur_node

  def insert_after_node(self, node, data):
    new_node = Node(data)

    cur_node = self.head
    while cur_node and cur_node.data != node:
      cur_node = cur_node.next

    if cur_node == None:
      return

    new_node.next, cur_node.next = cur_node.next, new_node    

  def delete(self, node):
    cur_node = self.head

    if node == cur_node.data:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    while cur_node and cur_node.data != node:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node == None:
      return

    prev_node.next = cur_node.next
    cur_node = None
    
  def delete_by_pos(self, key):
    cur_node = self.head
    pos = 0

    if key == pos:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    while cur_node and pos != key:
      prev_node = cur_node
      cur_node = cur_node.next
      pos+=1
    
    if cur_node == None:
      return

    prev_node.next = cur_node.next
    cur_node = None

  def len_linkedlist(self):
    cur_node = self.head

    _sum = 0
    while cur_node:
      cur_node = cur_node.next
      _sum+=1

    if cur_node == None:
      return _sum

  def len_recursive(self, cur_node):
    if cur_node is None:
      return 0
    return 1 + self.len_recursive(cur_node.next)

  def swap_nodes(self, node1, node2):

    if node1 == node2:
      return

    prev_node1 = None
    cur_node1 = self.head
    while cur_node1 and cur_node1.data != node1:
      prev_node1 = node1
      cur_node1 = cur_node1.next
    
    prev_node2 = None
    cur_node2 = self.head
    while cur_node2 and cur_node2.data != node2:
      prev_node2 = node2
      cur_node2 = cur_node2.next
    
    if not node1 or not node2:
      return

    if prev_node1:
      prev_node1.next = node2
    else:
      self.head = node2

    if prev_node2:
      prev_node2.next = node1
    else:
      self.head = node1




l = linkedlist()

l.add_node(1)
l.add_node('A')
l.add_node(2)
l.add_node('C')

l.insert_before_node(2, 'f')

l.insert_after_node(2, 'r')

l.delete('A')

l.insert_before_node(1, 'p')

l.insert_after_node('C', '97')

l.delete('p')

l.delete_by_pos(0)

l.delete_by_pos(3)

# print(l.len_linkedlist())

print(l.len_recursive(l.head))

l.print_node()







# def _map(chars):
#   char_map = {}
#   for i,y in enumerate(chars):
#     i+=1
#     char_map[i] = y
#   return char_map

# char_map = _map(string.ascii_lowercase)
# print(char_map[8])


# def mod(nums, capacity=7):
#   for no in nums:
#     mod = no % capacity
#     print(mod, end=' ')

# mod([i for i in range(30)])

# from string import ascii_lowercase

# def jargon(args):
#   for i,y in enumerate(args):
#     print(f'{i} : {y}')

# jargon(ascii_lowercase)

# a = [[str(i) for i in range(10, 13)] for y in range(4)]

# print(a)

# def get(key):
#   for i in range(0, len(a[key])):
#     print(a[key][i][0])

# get(0)