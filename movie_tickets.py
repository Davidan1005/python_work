prompt = ("How old are you?\n")

age = int(input(prompt))

if age < 3:
    print("Your ticket is free!")
elif age > 3 and age < 12:
    print("Yur ticket costs $10")
else:
    print("Your ticket costs $15")
