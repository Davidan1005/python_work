pizzas = ['Pepperoni', 'Hawaiian', 'Bacon']
#for pizza in pizzas:
#	print("I haven't had " + pizza + " pizza in a while\n")
#print('Pizza is my comfort meal')
#one_million = list(range(1,1000001))
#print(sum(one_million))
friend_pizza = pizzas[:]
pizzas.append('Meatlovers')
friend_pizza.append('Vegetarian')
print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('My friends favoutrite pizzas are: ')
for pizza in friend_pizza:
    print(pizza)
