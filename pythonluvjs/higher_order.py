from functools import reduce

List1 = [1,2,3,4,5]
List2 = [6,7,8,9,10]

Reduce = reduce(lambda total, sum: total+sum, List1)
print(Reduce)






# A = reduce(lambda x, y: x[i] + y[i], List1, List2)
# print(A)
# true = filter(lambda x: True if x>=2 else False, List)
# print(list(true))

'''
Filter = filter(lambda element: element%2==1, List)
print(list(Filter))

mapping = map(lambda element: element*2 , List)
print(list(mapping))

lam = lambda x: x/2

# print(lam(2))
# print(type(lam(2)))

double_list = map(lambda x: x*2, array)
print(list(double_list))

new_array = filter(lambda x: x>=3, array)

# print(list(new_array))
'''