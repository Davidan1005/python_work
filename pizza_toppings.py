message = "What topping would you like on your pizza\n"
message += "To finish your order enter 'quit'\n "
topping = ""

while topping != 'quit':
    topping = input(message)
    print("I will add " + topping + " to your pizza")
