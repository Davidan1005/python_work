#usernames = ['Admin','Newman','Icebear','Harley','Peter']
usernames = []
if usernames:
    for user in usernames:
        if user == 'Admin':
            print("welcome admin")
        else:
            print("welcome player")
else: 
    print('We need more users')
      