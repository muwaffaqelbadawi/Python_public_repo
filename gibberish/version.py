l = ['n',',','h']

idx = -1


def forward_gen():
  yield from l
  idx += 1

def backward_gen(idx):
  for i in range(idx,-1,-1):
    yield l[i]


g = forward_gen()
s = backward_gen(idx)



a = input('')

print(next(g))
print(next(s))


# print(backward_gen())
# print(next(g))
# print(next(g))
# print(next(g))