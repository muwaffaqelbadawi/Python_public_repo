names = ["Muwaffaq", "Moazzar", "Moyassar", "Maeen", "Dave", "Wendy"]


# Python ternary operator
def start_with_Char(name):
    return name if name[0] == "M" else None



# anonymous function with ternary operator
start_with_Char_anonymous = lambda name: name if name[0] == "M" else None
# start_with_Char_anonymous = lambda name: name if name[0] == "M" else None


m_starter_name_list = list(map(start_with_Char_anonymous, names))
m_starter_name_l = list(filter(start_with_Char, names))

# m_starter_name = list(map(start_with_Char, names))

# print(m_starter_name_list)
print(m_starter_name_l)
