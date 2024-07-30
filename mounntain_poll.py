responses = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("Which mountain would you like to climb?")

    responses[name] = response

    repeat = input("Would you like another person to respond? (yes/no)\n")
    if repeat == 'no':
        print("Thank you for your response")
        break
    else: 
        continue

for name, response in responses.items():
    print(name)

