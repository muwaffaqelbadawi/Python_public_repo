l = [i for i in range(5)]

def iterRec(i):
  if i == 1:
    return 1
  return l[i-1] * l[iterRec(i-1)]

print(iterRec(len(l)))