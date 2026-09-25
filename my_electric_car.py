from electric_car import ElectricCar

my_electric_car = ElectricCar('Tesla', 'Model S', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()