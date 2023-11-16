from abc import ABCMeta, abstractmethod

class Shape(object):
  
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def aria(self): pass

  @abstractmethod
  def perimeter(self): pass

class Rectangle(Shape):
  def __init__(self,height,width):
    self.height = height
    self.width = width
    
    super(Rectangle,self).__init__()
  
  def area(self):
    return self.width * self.height
  
  def premiter(self):
    return self.width * 2 + self.height * 2


class square(Rectangle):
  def __init__(self, sidelength):
    self.sidelength = sidelength
    super(square, self).__init__(sidelength, sidelength)

  
s = square(5)
print(s.area())
print(s.premiter())

print(square.mro())