from ast import For


total = 0

n = int(input())

for num in range(4, n + 1, 3):
    print("{}, {}".format(total, num))
    total = total + num


print("total = ", total)
