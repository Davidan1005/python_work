magicians = ["Houdini", "The Modern day Wizard", "Vanisher", "Bunny Man"]
great_magicians = []


def show_magicians():
    for magician in magicians:
        print(magician)


def replace(Arr, Item_1, Item_2):
    Arr[Arr.index(Item_1)] = Item_2


def make_great(Arr):
    for item in Arr:
        great_magician = "The great " + item
        replace(Arr, item, great_magician)
        great_magicians.append(great_magician)


make_great(magicians[:])
show_magicians()
print(great_magicians)
