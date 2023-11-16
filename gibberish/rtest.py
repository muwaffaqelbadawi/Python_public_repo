class List:
  def __init__(self):
    self.l = [i for i in range(5)]
    self.index = 0
  
  @property
  def p_list(self):
    return self.l[self.index]
  
  @p_list.setter
  def m_forward(self, idx):
    if self.index == len(self.l)-1:
      self.index = idx
    self.index+=1
  
  @p_list.setter
  def m_backward(self, idx):
    if self.index == -1:
      self.index = idx
    self.index-=1
  
  
l = List()

while True:
  i = input("< >\n")
  
  if i == ">":
    l.m_forward = -1
  elif i == "<":
    l.m_backward = len(l.l)-1

  print(l.p_list)