import numpy as np

arr = np.array(([[[1], [2]], [[3], [4]]]))


print(arr)


print(arr.shape)
print()
print()
print()


new_arr = np.squeeze(arr)

print(new_arr)
print(new_arr.shape)
