reason = ""

print('Type q to exit at any time')
while reason != 'q':
    reason =input('Why do you like programming?')
    if reason == 'q':
        break
    with open('programming_poll.txt', 'a') as file_object:
        file_object.write(reason + '\n')
