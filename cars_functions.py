def make_cars(manufacturer, model, **details):
    car = {}
    car["manufacturer"] = manufacturer
    car["moodel"] = model
    for key, value in details.items():
        car[key] = value
    return car


print(make_cars("Subaru", "Sports", Color="Red", Scratches="None", Mileage="50000"))
