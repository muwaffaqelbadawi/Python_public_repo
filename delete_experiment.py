my_list_of_names = ["Muwaffaq", "Moazzar", "Moyassar", "Maeen", "Dave", "Wendy"]

message = "You have the below list feel free to delete any of them\n{}:\n".format(
    my_list_of_names)

Entered_name = input(message)

# anonymous function with ternary operator
def remove(name): return True if name != Entered_name else False


def search(name): return True if name == Entered_name else False

# if you want to delete somthing
filtered_list = list(filter(remove, my_list_of_names))
searched_name = list(filter(search, my_list_of_names))[0]

# print("You deleted the name {} now your list is\n{}".format(
#     Entered_name, searched_name))

print("You searched for the name '{}' and your search result is\n{}".format(
    Entered_name, searched_name))
