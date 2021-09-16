# Inheritance

# -> You don’t always have to start from scratch when writing a class.
# If the class you’re writing is a specialized version of another class you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes and methods of the first class. The original class is called the parent class, and the new class is the child class.
# The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.

# The __init__() Method for a Child Class

# -> When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method from the parent class.
# This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.

# As an example, let’s model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class we wrote in last chapter.
# Then we’ll only have to write code for the attributes and behavior specific to electric cars.

# Let’s start by making a simple version of the ElectricCar class, which does everything the Car class does.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# -> At 18 we start with Car. When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
# At 37 we define the child class, ElectricCar.
# The name of the parent class must be included in parentheses in the definition of a child class.
# The __init__() method at 28 takes in the information required to make a Car instance.

# -> The super() function at 39 is a special function that allows you to call a method from the parent class.
# This line tells Python to call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method.
# The name super comes from a convention of calling the parent class a superclass and the child class a subclass.

# -> We test whether inheritance is working properly by trying to create an electric car with the same kind of information we’d provide when making a regular car.
# At 40 we make an instance of the ElectricCar class and assign it to my_tesla.
# This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car.
# We provide the arguments 'tesla', 'model s', and 2019.

# -> Aside from __init__(), there are no attributes or methods yet that are particular to an electric car.
# At this point we’re just making sure the electric car has the appropriate Car behaviors.

# Defining Attributes and Methods for the Child Class

# -> Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class.
#
# Let’s add an attribute that’s specific to electric cars (a battery, for example) and a method to report on this attribute.
# We’ll store the battery size and write a method that prints a description of the battery.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,)
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# -> At 89 we add a new attribute self.battery_size and set its initial value to, say, 75.
# This attribute will be associated with all instances created from the ElectricCar class but won’t be associated with any instances of Car.
# We also add a method called describe_battery() that prints information about the battery at 90.
# When we call this method, we get a description that is clearly specific to an electric car.

# Overriding Methods from the Parent Class

# -> You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class.
# Python will disregard the parent class method and only pay attention to the method you define in the child class.

# Say the class Car had a method called fill_gas_tank().
# This method is meaningless for an all-electric vehicle, so you might want to override this method. Here’s one way to do that.

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,)
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")

# -> Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead.
# When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class.


# Instances as Attributes

# -> When modeling something from the real world in code, you may find that you’re adding more and more detail to a class.
# You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy.
# In these situations, you might recognize that part of one class can be written as a separate class.
# You can break your large class into smaller classes that work together.

# For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to the car’s battery.
# When we see this happening, we can stop and move those attributes and methods to a separate class called Battery.
# Then we can use a Battery instance as an attribute in the ElectricCar class.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery:
    def __init__(self, batter_size = 75):
        self.battery_size = batter_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# -> At 154 we define a new class called Battery that doesn’t inherit from any other class.
# The __init__() method at 155 has one parameter, battery_size, in addition to self.
# This is an optional parameter that sets the battery’s size to 75 if no value is provided.
# The method describe_battery() has been moved to this class as well 157.

# -> In the ElectricCar class, we now add an attribute called self.battery 162.
# This line tells Python to create a new instance of Battery (with a default size of 75, because we’re not specifying a value) and assign that instance to the attribute self.battery.
# This will happen every time the __init__() method is called; any ElectricCar instance will now have a Battery instance created automatically.

# -> We create an electric car and assign it to the variable my_tesla.
# When we want to describe the battery, we need to work through the car’s battery attribute.

# my_tesla.battery.describe_battery()

# -> This line tells Python to look at the instance my_tesla, find its battery attribute, and call the method describe_battery() that’s associated with the Battery instance stored in the attribute.

# -> This looks like a lot of extra work, but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class.
# Let’s add another method to Battery that reports the range of the car based on the battery size.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class Battery:
    def __init__(self, batter_size = 75):
        self.battery_size = batter_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,)
        self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# -> The new method get_range() at 210 performs some simple analysis.
# If the battery’s capacity is 75 kWh, get_range() sets the range to 260 miles, and if the capacity is 100 kWh, it sets the range to 315 miles.
# It then reports this value. When we want to use this method, we again have to call it through the car’s battery attribute at 223.

# Importing Classes

# -> As you add more functionality to your classes, your files can get long, even when you use inheritance properly.
# In keeping with the overall philosophy of Python, you’ll want to keep your files as uncluttered as possible.
# To help, Python lets you store classes in modules and then import the classes you need into your main program.

# Importing a Single Class

# -> Let’s create a module containing just the Car class.
# This brings up a subtle naming issue: we already have a file named car.py in this chapter, but this module should be named car.py because it contains code representing a car.
# We’ll resolve this naming issue by storing the Car class in a module named car.py, replacing the car.py file we were previously using.
# From now on, any program that uses this module will need a more specific filename, such as my_car.py. Here’s car.py with just the code from the class Car.

# car.py


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# -> At 245 we include a module-level docstring that briefly describes the contents of this module. You should write a docstring for each module you create.

# -> Now we make a separate file called my_car.py. This file will import the Car class and then create an instance from that class.

# my_car.py

# From car import Car
# (This should be uncommented when using in a separate new python file, Commented here because its al written in same file)

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# -> The import statement at 271 tells Python to open the car module and import the class Car.
# Now we can use the Car class as if it were defined in this file.
# The output is the same as we saw earlier.

# -> Importing classes is an effective way to program.
# Picture how long this program file would be if the entire Car class were included.
# When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program file clean and easy to read.
# You also store most of the logic in separate files; once your classes work as you want them to, you can leave those files alone and focus on the higher-level logic of your main program.

# Storing Multiple Classes in a Module

# You can store as many classes as you need in a single module, although each class in a module should be related somehow.
# The classes Battery and ElectricCar both help represent cars, so let’s add them to the module car.py.

# car.py

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def updated_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You cant roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, batter_size = 75):
        self.battery_size = batter_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year,)
        self.battery = Battery()

# -> Now we can make a new file called my_electric_car.py, import the ElectricCar class, and make an electric car.

# my_electric_car.py

# from car import ElectricCar
# (This should be uncommented when using in a separate new python file, Commented here because its al written in same file)

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing Multiple Classes from a Module

# -> You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same file, we need to import both classes, Car and ElectricCar.

# my_cars.py

# from car import Car, ElectricCar
# (This should be uncommented when using in a separate new python file, Commented here because its al written in same file)

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# -> You import multiple classes from a module by separating each class with a comma 351.
# Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.
# In this example we make a regular Volkswagen Beetle at 354 and an electric Tesla Roadster at 356.

# Importing an Entire Module

# -> You can also import an entire module and then access the classes you need using dot notation.
# This approach is simple and results in code that is easy to read.
# Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts with any names used in the current file.

# Here’s what it looks like to import the entire car module and then create a regular car and an electric car:

# my_cars.py

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# -> At 375 we import the entire car module.
# We then access the classes we need through the module_name.ClassName syntax. At 374 we again create a Volkswagen Beetle, and at 377 we create a Tesla Roadster.

#  Importing All Classes from a Module
# -> You can import every class from a module using the following syntax:

# from module_name import *

# -> This method is not recommended for two reasons.
# First, it’s helpful to be able to read the import statements at the top of a file and get a clear sense of which classes a program uses.
# With this approach it’s unclear which classes you’re using from the module.
# This approach can also lead to confusion with names in the file.
# If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard to diagnose.
# I show this here because even though it’s not a recommended approach, you’re likely to see it in other people’s code at some point.

# -> If you need to import many classes from a module, you’re better off importing the entire module and using the module_name.ClassName syntax.
# You won’t see all the classes used at the top of the file, but you’ll see clearly where the module is used in the program.
# You’ll also avoid the potential naming conflicts that can arise when you import every class in a module.