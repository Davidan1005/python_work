prompt = "If you could visit one place in the world where would you go ?"
poll_results = {}
username = ""

while username != 'quit':

    username = input("what is your name ?")
    if username == 'quit':
        break
    dream_spot = input(prompt)
    poll_results[username] = dream_spot


for user in poll_results:
    print(poll_results[user])
