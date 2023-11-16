class Order(object):
  def __init__(self):
    self._item_list = None
    self._item_count = 0
    self._total = 0
  
  @property
  def item_list(self):
    return self._item_list

  @item_list.setter
  def item_list(self):
    if self._item_list is None:
        self._item_list = []
        return

  def AddItem(self, item):
    self.item_list.append(item)
  
  @property
  def item_count(self):
    return self._item_count

  @item_count.setter
  def item_count(self, item_no):
    self._item_count += item_no

  @property
  def total(self):
    return  self._total

  @total.setter
  def total(self, price):
    self._total += price

o = Order()

o.item_count = 1
o.item_count = 2

print(o.item_count)

# print(o._item_count)
  