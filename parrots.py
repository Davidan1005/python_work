statement = "What would you like me to repeat to you?"
echo = ""

active = True
while active:
    echo = input(statement)
    print(echo)

    if echo == 'quit':
        active = False
