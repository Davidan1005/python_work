guest_name = ""
print('type q to guit at any time')
while guest_name != 'q':
    guest_name = input('What are your first and last names?')
    
    if guest_name == 'q':
        break
    with open('guest_book.txt','a') as file_object:
        file_object.write(guest_name + '\n')