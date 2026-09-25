
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """init attribute to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """set the odometer reading to the given value
        reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """print a statement indicating that the car's gas tank is being filled"""
        print("Filling the gas tank...")

# my_new_car = Car('Audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.increment_odometer(2)

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at 65 kWh or higher.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        then init attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size"""
        self.battery.describe_battery()

    def get_range(self):
        """Print a statement about the range this battery provides"""
        self.battery.get_range()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This is an electric car, it doesn't have a gas tank.")

# my_leaf = ElectricCar('Nissan', 'Leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.fill_gas_tank()
# my_leaf.battery.get_range()

# my_electric_car = ElectricCar('Tesla', 'Model S', 2024)
# my_electric_car.battery.get_range()
# my_electric_car.battery.upgrade_battery()
# my_electric_car.battery.get_range()