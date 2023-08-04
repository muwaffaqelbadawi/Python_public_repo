my_list_of_names = ["Muwaffaq", "Moazzar", "Moyassar", "Maeen", "Dave", "Wendy"]

message = "You have the below list feel free to delete any of them\n{}:\n".format(
    my_list_of_names)

Entered_name = input(message)

# anonymous function with ternary operator
def remove_name(name): return True if name != Entered_name else False

# if you want to delete somthing
filtered_list = list(filter(remove_name, my_list_of_names))

print("You deleted the name {} now your list is\n{}".format(
    Entered_name, filtered_list))
