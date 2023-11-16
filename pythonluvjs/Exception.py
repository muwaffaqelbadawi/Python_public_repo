class Stack():
    def __init__(self):
        self.items = []

    def Push(self, item):
        self.items.append(item)

    def Pop(self, item):
        self.items.pop()

    def Peek(self, item):
        if not self.is_empty():
           return self.items[-1]
    def get_stack(self, item):
        return self.items
        