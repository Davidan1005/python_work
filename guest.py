guest_name = input("What are your first and last names?")
with open('guest.txt', 'a') as file_object:
    file_object.write('\n'+guest_name)
