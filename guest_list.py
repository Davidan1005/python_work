guest_list = ['Jesus Christ', 'Nicola Tesla', 'Kobe Bryant']

print(guest_list[0] + ' Is my lord and saviour ')
print(guest_list[1] + ' would probably have alot to teach me ')
print(guest_list[2] + ' was one of the greats')

absent_guest = guest_list.pop()
print('\n' + absent_guest.title())

guest_list.append('George Washington')
print(guest_list)

print('\n' + guest_list[0] + ' sir you have been invited to dinner')
print(guest_list[1] + ' sir you have been invited to dinner')
print(guest_list[2] + ' sir you have been invited to dinner')

print('I found a bigger table')
guest_list.insert(0,'Alexander Hamilton')
print(guest_list)

guest_list.insert(2,'Tony Stark')
print(guest_list)

guest_list.append('Mark Zuckerberg')
print(guest_list)

print('\nI can only invite two people to dinner')
print('There isnt enough room for you ' + guest_list.pop(0))
print('There isnt enough room for you ' + guest_list.pop(2))
print('There isnt enough room for you ' + guest_list.pop(3))
print('There isnt enough room for you ' + guest_list.pop(2))

print(guest_list)
print('\nYou are still welcome ' + guest_list[0] + ' and ' + guest_list[1])

del guest_list[0]
del guest_list[0]
print(guest_list)
print('I will have ' + str(len(guest_list)) + ' guests')
