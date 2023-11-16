import os
from os import path

dir_path = os.path.dirname(os.path.realpath(__file__))

# os.path.dirname()

# print(os.path.realpath(__file__))


print(__file__)



# current working directory
cwd = os.getcwd()

# base name
base_name = path.basename(cwd)

my_path = path.join(base_name, "Controller", "vews")

# print(my_path)
# print(cwd)
