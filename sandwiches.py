def item_to_string(Arr):
    """concatenates elements in a list or tuple to a single string"""
    final_string = ""
    for item in Arr:
        if Arr.index(item) < len(Arr)-1:
            string = item + ", "
            final_string = final_string + string

        if Arr.index(item) == len(Arr) - 1:
            string = item + "."
            final_string = final_string + string

    return final_string


def sandwich_order(*sandwich_ingredients):
    print("Your order will have " + item_to_string(sandwich_ingredients))


sandwich_order("Tomatoes", "Bacon", "Eggs", "Lettuce")
sandwich_order("eggs")
sandwich_order("Tomatoes", "Bacon", "Eggs", "Lettuce", "Onions", "Pickles")
