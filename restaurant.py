class Restaurant():
    """Modelling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """makes the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(self.restaurant_name.title() +
              " serves " + self.cuisine_type.title())

    def open_restaurant(self):
        """Prints an open message"""
        print(self.restaurant_name.title() + " is now open.")

    def set_number_served(self, number):
        """Changes the number served"""
        self.number_served = number

    def increment_number_served(self, served_customers):
        """Increments the number of customers served"""
        self.number_served = + served_customers

class Icecreamstand(Restaurant):
    """Represents an Ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


new_restaurant = Restaurant("The hill", "Breakfast food")
print(new_restaurant.restaurant_name.title())
print(new_restaurant.cuisine_type.title())

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

restaurant_1 = Restaurant("Krusty krab", "Fast food")
restaurant_2 = Restaurant("splat burger", "fast food")
restaurant_3 = Restaurant("Mcdonalds", "fast food")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

restaurant_3.increment_number_served(8)


print(str(restaurant_3.number_served))
my_stand = Icecreamstand("Superb Icecream", "Dessert","Vannilla","Chocolate","Strawberry")
my_stand.show_flavors()