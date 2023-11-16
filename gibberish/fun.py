# import tkinter as tk
# from tkinter.filedialog import askdirectory



# root = tk.Tk()
# root.withdraw()
# askdirectory()





# def Sentence(text):
#   sentence = text.split()
  
#   for words in sentence:
#     yield words
    
# my_sentence = Sentence('This is my sentence')


# for words in my_sentence:
#   print(words)

# for words in my_sentence:
#   print(next(my_sentence))

# class Sentense:
#   def __init__(self, text):
#     self.text = text
#     self.index = 0
#     self.word = text.split()
    
#   def __iter__(self):
#     return self
  
#   def __next__(self):
#     if self.index >= len(self.word):
#       raise StopIteration
#     index = self.index
#     self.index+=1
#     return self.word[index]

# my_sentence = Sentense('This is my solution')

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))

# for word in my_sentence:
#   print(word)

# for word in my_senten


# for word in my_sentence:
#   print(word)

# for word in my_sentence:
#   print(word)

# l = [i for i in range(5)]

# a = iter(l)

# e = (1,2,3,5,8,7)

# print(Exception)

# s = iter(e)

# while s:
  
#   # print(next(s))
#   try:
#     print(next(s))
#   except Exception as e:
#     print(e)

# for i in range(6):
#   print(next(s))


# class PrintNumber:
#     def __init__(self, max):
#         self.max = max

#     def __iter__(self):
#         self.num = 0
#         return self

#     def __next__(self):
#         if(self.num >= self.max):
#             raise StopIteration
#         self.num += 1
#         return self.num

# printNum = PrintNumber(3)

# printNumIter = iter(printNum)

# # prints '1'
# print(type(printNumIter))

# prints '2'
# print(next(printNumIter))

# prints '3'
# print(next(printNumIter))

# raises StopIteration
# print(next(printNumIter))

# for i in range(len(l)):
#   print(next(a))


# quit()
# exit()
# os._exit()
# sys.exit()
# raise SystemExit
