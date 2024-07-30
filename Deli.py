sandwich_orders = ["Pastrami", "Tuna sandwich", "Pastrami",
                   "Chicken sandwich", "Pastrami", "Steak sandwhich", "Panini", "Pastrami"]
finished_sandwiches = []

print("We are out of Pastrami")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich.title())
    finished_sandwiches.append(sandwich)


for sandwich in finished_sandwiches:
    print(sandwich)
