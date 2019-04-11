def car_info(name, type, **others):
    car_profile = {}
    car_profile['name'] = name
    car_profile['type'] = type
    for key, value in others.items():
        car_profile[key] = value
    print(car_profile)

car_info('奔腾', '宝马', color="blue", tow_package=True)