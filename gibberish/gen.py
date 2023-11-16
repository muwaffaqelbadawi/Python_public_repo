l = [i for i in range(5)]


def new_syntax():
  yield from l
  
n = new_syntax()

print(next(n))




# def g():
#   for i in l:
#     yield i
    
# a = g()

# for i in range(len(l)):
#   print(next(a))