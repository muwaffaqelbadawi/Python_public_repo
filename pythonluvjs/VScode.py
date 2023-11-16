
'''
class Book:
    def __init__(self, title, auther, year):
        self.title = title
        self.auther = auther
        self.year = year

class Magazine(Book):
    def __init__(self, title, auther, year, month):
        super.__init__(self, title, auther, year)
        self.month = month

class Magazine(Book):
      def __init__(self, title, auther, year):
        super(Book, self).__init__(title, auther, year)
'''


class Protos:
    def __init__(self):
        pass

pro = Protos()
pro.a = "a"
pro.b = "b"

print(pro.a)
print(pro.b)