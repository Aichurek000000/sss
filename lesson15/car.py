def make_car(make, model, **kwargs):
    car_info = {
        'make': make,
        'model': model
    }
    car_info.update(kwargs)
    return car_info

def print_car_info(car):
    for key, value in car.items():
        print("{:<10}: {}".format(key, value))

car = make_car('subaru', 'outback', color='blue', engine='V8')
print_car_info(car)