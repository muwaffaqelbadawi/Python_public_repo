people = {
    "first_name": ['Muwaffuq', 'Ahmed', 'Tariq'],
    "last_name": ['Albadawi', 'Elmisbah', 'Ali'],
    "email": ['muwaffuq@gmail.com', 'ahmed@gmail.com', 'tariq@gmail.com']
}


get1 = people.get('first_name', 'Unknown')
get2 = people.get('midle_name', 'Unknown')

print(get1)
print(get2)
