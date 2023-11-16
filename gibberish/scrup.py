ll = [[i for i in range(2)] for y in range(5)]

# print(ll)

for x in range(len(ll)-1):
  print(list(zip(ll[x], ll[x+1])))