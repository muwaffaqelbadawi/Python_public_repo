class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class linkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return

    last_node = self.head

    while last_node.next:
      last_node = last_node.next

    last_node.next = new_node

_list = linkedList()
_list.append('A')
_list.append('B')