# Classes

# -> Making an object from a class is called instantiation, and you work with instances of a class.
# In this chapter you’ll write classes and create instances of those classes.
# You’ll specify the kind of information that can be stored in instances, and you’ll define actions that can be taken with these instances.
# You’ll also write classes that extend the functionality of existing classes, so similar classes can share code efficiently.
# You’ll store your classes in modules and import classes written by other programmers into your own program files.

# Creating the Dog Class

# -> Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

# -> At 13 we define a class called Dog.
# By convention, capitalized names refer to classes in Python.
# There are no parentheses in the class definition because we’re creating this class from scratch.

# The __init__() Method

# -> A function that’s part of a class is a method.
# Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call methods.
# The __init__() method at 14 is a special method that Python runs automatically whenever we create a new instance based on the Dog class.
# This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names.
# Make sure to use two underscores on each side of __init__().
# If you use just one on each side, the method won’t be called automatically when you use your class, which can result in errors that are difficult to identify.

# -> We define the __init__() method to have three parameters: self, name, and age. The self parameter is required in the method definition, and it must come first before the other parameters.
# It must be included in the definition because when Python calls this method later (to create an instance of Dog), the method call will automatically pass the self argument.
# Every method call associated with an instance automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class.
# When we make an instance of Dog, Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; self is passed automatically, so we don’t need to pass it.
# Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.

# -> The two variables defined at 15 each have the prefix self.
# Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.
# The line self.name = name takes the value associated with the parameter name and assigns it to the variable name, which is then attached to the instance being created.
# The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.

# -> The Dog class has two other methods defined: sit() and roll_over() 19.
# Because these methods don’t need additional information to run, we just define them to have one parameter, self.
# The instances we create later will have access to these methods.
# In other words, they’ll be able to sit and roll over.
# For now, sit() and roll_over() don’t do much. They simply print a message saying the dog is sitting or rolling over.
# But the concept can be extended to realistic situations: if this class were part of an actual computer game, these methods would contain code to make an animated dog sit and roll over.
# If this class was written to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.

# Making an Instance from a Class

# -> Think of a class as a set of instructions for how to make an instance.
# The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# -> At 58 we tell Python to create a dog whose name is 'Willie' and whose age is 6.
# When Python reads this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6.
# The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided.
# Python then returns an instance representing this dog. We assign that instance to the variable my_dog.

# Accessing Attributes

# -> To access the attributes of an instance, you use dot notation. At ➋ we access the value of my_dog’s attribute name by writing:
# my_dog.name

# -> Dot notation is used often in Python.
# This syntax demonstrates how Python finds an attribute’s value.
# Here Python looks at the instance my_dog and then finds the attribute name associated with my_dog.
# This is the same attribute referred to as self.name in the class Dog. At 61 we use the same approach to work with the attribute age.

# Calling Methods

# -> After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. Let’s make our dog sit and roll over.

my_dog.sit()
my_dog.roll_over()

# -> To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot.
# When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code.
# Python interprets the line my_dog.roll_over() in the same way.

# Creating Multiple Instances

# -> You can create as many instances from a class as you need. Let’s create a second dog called your_dog.

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# -> In this example we create a dog named Willie and a dog named Lucy.
# Each dog is a separate instance with its own set of attributes, capable of the same set of actions.

# -> Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class.
# You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

# Working with Classes and Instances

# -> You can use classes to represent many real-world situations.
# Once you write a class, you’ll spend most of your time working with instances created from that class.
# One of the first tasks you’ll want to do is modify the attributes associated with a particular instance.
# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

# -> Let’s write a new class representing a car.
# Our class will store information about the kind of car we’re working with, and it will have a method that summarizes this information.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# -> At 122 in the Car class, we define the __init__() method with the self parameter first, just like we did before with our Dog class.
# We also give it three other parameters: make, model, and year. The __init__() method takes in these parameters and assigns them to the attributes that will be associated with instances made from this class.
# When we make a new Car instance, we’ll need to specify a make, model, and year for our instance.

# At 127 we define a method called get_descriptive_name() that puts a car’s year, make, and model into one string neatly describing the car.
# This will spare us from having to print each attribute’s value individually.
# To work with the attribute values in this method, we use self.make, self.model, and self.year.
# At 130 we make an instance from the Car class and assign it to the variable my_new_car.
# Then we call get_descriptive_name() to show what kind of car we have.

# Setting a Default Value for an Attribute

# -> When an instance is created, attributes can be defined without being passed in as parameters.
# These attributes can be defined in the __init__() method, where they are assigned a default value.

# -> Let’s add an attribute called odometer_reading that always starts with a value of 0. We’ll also add a method read_odometer() that helps us read each car’s odometer.

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
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# -> This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example.
# Then Python creates a new attribute called odometer_reading and sets its initial value to 0.
# We also have a new method called read_odometer() that makes it easy to read a car’s mileage.

# Modifying Attribute Values

# -> You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches.

# Modifying an Attribute’s Value Directly

# -> The simplest way to modify the value of an attribute is to access the attribute directly through an instance. Here we set the odometer reading to 23 directly.

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
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# -> At 192 we use dot notation to access the car’s odometer_reading attribute and set its value directly.
# This line tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23.

# Modifying an Attribute’s Value Through a Method

# -> It can be helpful to have methods that update certain attributes for you.
# Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.

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
        self.odometer_reading = milage
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.updated_odometer(23)
my_new_car.read_odometer()

# -> The only modification to Car is the addition of update_odometer() at 215.
# This method takes in a mileage value and assigns it to self.odometer_reading. At 219 we call update_odometer() and give it 23 as an argument (corresponding to the mileage parameter in the method definition).
# It sets the odometer reading to 23, and read_odometer() prints the reading.

# -> We can extend the method update_odometer() to do additional work every time the odometer reading is modified.
# Let’s add a little logic to make sure no one tries to roll back the odometer reading.

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
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.updated_odometer(23)
my_new_car.read_odometer()

# -> Now update_odometer() checks that the new reading makes sense before modifying the attribute. If the new mileage, mileage, is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage 242.
# If the new mileage is less than the existing mileage, you’ll get a warning that you can’t roll back an odometer 245.

# Incrementing an Attribute’s Value Through a Method

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
my_new_car = Car('subaru', 'outback', 2015)
print(my_new_car.get_descriptive_name())
my_new_car.updated_odometer(23500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

# -> The new method increment_odometer() at 273 takes in a number of miles, and adds this value to self.odometer_reading.
# At 275 we create a used car, my_used_car.
# We set its odometer to 23,500 by calling update_odometer() and passing it 23_500 at 277.
# At 279 we call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it.