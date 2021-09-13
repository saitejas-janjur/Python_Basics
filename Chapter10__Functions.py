# FUNCTIONS
# -> In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job.
# When you want to perform a particular task that you’ve defined in a function, you call the function responsible for it.
# If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again;
# you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function.
# You’ll find that using functions makes your programs easier to write, read, test, and fix.

# Defining a Function -

def greet_user():
    """Display a simple greeting"""
    print("Hello User")


greet_user()


# -> This example shows the simplest structure of a function.
# The line at 10 uses the keyword def to inform Python that you’re defining a function.
# This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job.
# The parentheses hold that information. In this case, the name of the function is greet_user(), and it needs no information to do its job, so its parentheses are empty.
# (Even so, the parentheses are required.) Finally, the definition ends in a colon.

# -> Any indented lines that follow def greet_user(): make up the body of the function.
# The text at 11 is a comment called a docstring, which describes what the function does.
# Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.

# -> When you want to use this function, you call it. A function call tells Python to execute the code in the function.
# To call a function, you write the name of the function, followed by any necessary information in parentheses, as shown at 14.
# Because no information is needed here, calling our function is as simple as entering greet_user().


# Passing Information to a Function

# -> Modified slightly, the function greet_user() can not only tell the user Hello! but also greet them by name.
# For the function to do this, you enter username in the parentheses of the function’s definition at def greet_user().
# By adding username here you allow the function to accept any value of username you specify.
# The function now expects you to provide a value for username each time you call it.
# When you call greet_user(), inside the parentheses.

def greet_user(username):
    print(f"Hello, {username.title()}")


greet_user('john doe')


# -> Entering greet_user('john doe') calls greet_user() and gives the function the information it needs to execute the print() call.
# The function accepts the name you passed it and displays the greeting for that name.

# Arguments and Parameters

# -> In the preceding greet_user() function, we defined greet_user() to require a value for the variable username.
# Once we called the function and gave it the information (a person’s name), it printed the right greeting.

# -> The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
# The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that’s passed from a function call to a function.
# When we call the function, we place the value we want the function to work with in parentheses.
# In this case the argument 'jesse' was passed to the function greet_user(), and the value was assigned to the parameter username.

# Passing Arguments

# -> Because a function definition can have multiple parameters, a function call may need multiple arguments.
# You can pass arguments to your functions in a number of ways.
# You can use positional arguments, which need to be in the same order the parameters were written; keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.

# Positional Arguments

# -> When you call a function, Python must match each argument in the function call with a parameter in the function definition.
# The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')


# -> The definition shows that this function needs a type of animal and the animal’s name.
# When we call describe_pet(), we need to provide an animal type and a name, in that order.
# For example, in the function call, the argument 'hamster' is assigned to the parameter animal_type and the argument 'harry' is assigned to the parameter pet_name.
# In the function body, these two parameters are used to display information about the pet being described.

# Multiple Function Calls

# -> You can call a function as many times as needed. Describing a second, different pet requires just one more call to describe_pet()

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# -> In this second function call, we pass describe_pet() the arguments 'dog' and 'willie'.
# As with the previous set of arguments we used, Python matches 'dog' with the parameter animal_type and 'willie' with the parameter pet_name.
# As before, the function does its job, but this time it prints values for a dog named Willie. Now we have a hamster named Harry and a dog named Willie.


# Keyword Arguments

# -> A keyword argument is a name-value pair that you pass to a function.
# You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion
# (you won’t end up with a harry named Hamster).
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')


# -> The function describe_pet() hasn’t changed. But when we call the function, we explicitly tell Python which parameter each argument should be matched with.
# When Python reads the function call, it knows to assign the argument 'hamster' to the parameter animal_type and the argument 'harry' to pet_name.
# The output correctly shows that we have a hamster named Harry.

# Default Values

# -> When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses the argument value.
# If not, it uses the parameter’s default value. So when you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call.
# Using default values can simplify your function calls and clarify the ways in which your functions are typically used.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name='willie')


# -> We changed the definition of describe_pet() to include a default value, 'dog', for animal_type.
# Now when the function is called with no animal_type specified, Python knows to use the value 'dog' for this parameter.

# Making an Argument Optional

# -> Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to.
# You can use default values to make an argument optional.

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, formatted properly"""
    full_name = f"\n{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jhon', 'lee', 'cooper')
print(musician)


# -> This function works when given a first, middle, and last name. The function takes in all three parts of a name and then builds a string out of them.
# The function adds spaces where appropriate and converts the full name to title case

# -> But middle names aren’t always needed, and this function as written would not work if you tried to call it with only a first name and a last name.
# To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value.
# To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty string and move it to the end of the list of parameters.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, formatted properly"""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()


person = get_formatted_name('jhon', 'cooper')
print(person)

person = get_formatted_name('jhon', 'cooper', 'lee')
print(person)


# -> In this example, the name is built from three possible parts.
# Because there’s always a first and last name, these parameters are listed first in the function’s definition.
# The middle name is optional, so it’s listed last in the definition, and its default value is an empty string.

# -> In the body of the function, we check to see if a middle name has been provided.
# Python interprets non-empty strings as True, so if middle_name evaluates to True if a middle name argument is in the function call.
# If a middle name is provided, the first, middle, and last names are combined to form a full name.
# This name is then changed to title case and returned to the function call line where it’s assigned to the variable musician and printed.
# If no middle name is provided, the empty string fails the if test and the else block runs.
# The full name is made with just a first and last name, and the formatted name is returned to the calling line where it’s assigned to musician and printed.

# -> Calling this function with a first and last name is straightforward.
# If we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly.

# -> This modified version of our function works for people with just a first and last name, and it works for people who have a middle name as well.

# Returning a Dictionary

# -> A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.
# For example, the following function takes in parts of a name and returns a dictionary representing a person.

def build_person(first_name, last_name):
    """Return a dictionary"""
    person = {'first': first_name, 'last': last_name}
    return person


character = build_person('jhon', 'cooper')
print(character)


# -> The function build_person() takes in a first and last name, and puts these values into a dictionary.
# The value of first_name is stored with the key 'first', and the value of last_name is stored with the key 'last'.
# The entire dictionary representing the person is returned.
# The return value is printed with the original two pieces of textual information now stored in a dictionary.

# Using a Function with a while Loop


def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nEnter your name: ")
    print("Enter 'q' to quit.")
    f_name = input("first name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello {formatted_name}!")


# Passing a List

# -> You’ll often find it useful to pass a list to a function, whether it’s a list of names, numbers, or more complex objects, such as dictionaries.
# When you pass a list to a function, the function gets direct access to the contents of the list.

def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Modifying a List in a Function

# -> When you pass a list to a function, the function can modify the list.
# Any changes made to the list inside the function’s body are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)


def show_compleated_models(compleated_models):
    print("\nThe following models have been printed: ")
    print(compleated_models)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
compleated_models = []

print_models(unprinted_designs, compleated_models)
show_compleated_models(compleated_models)


# -> At 249 we define the function print_models() with two parameters: a list of designs that need to be printed and a list of completed models.
# Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models.
# At 254 we define the function show_completed_models() with one parameter: the list of completed models.
# Given this list, show_completed_models() displays the name of each model that was printed.

# Passing an Arbitrary Number of Arguments

# -> Sometimes you won’t know ahead of time how many arguments a function needs to accept.
# Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# -> The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple.
# The print() call in the function body produces output showing that Python can handle a function call with one value and a call with three values.
# It treats the different calls similarly. Note that Python packs the arguments into a tuple, even if the function receives only one value.

# Mixing Positional and Arbitrary Arguments

# -> If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for toppings in toppings:
        print(f"\t{toppings}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -> In the function definition, Python assigns the first value it receives to the parameter size.
# All other values that come after are stored in the tuple toppings. The function calls include an argument for the size first, followed by as many toppings as needed.

# Using Arbitrary Keyword Arguments

# -> Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function.
# In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
# One example involves building user profiles: you know you’ll get information about a user, but you’re not sure what kind of information you’ll receive.
# The function build_profile() in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well.

def build_profile(first, last, **user_info):
    print(f"First name - {first.title()} Last name - {last.title()} \nAdditional info - {user_info}")
build_profile('albert', 'einstein',location='princeton',field='physics')

# -> The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want.
# The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.
# Within the function, you can access the key-value pairs in user_info just as you would for any dictionary.


# Importing an Entire Module

# -> To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program.
# Let’s make a module that contains the function make_pizza().
# To make this module, we’ll remove everything from the file pizza.py except the function make_pizza():

"""File - pizza.py"""

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for toppings in toppings:
        print(f"\t{toppings}")

# -> Now we’ll make a separate file called making_pizzas.py in the same directory as pizza.py.
# This file imports the module we just created and then makes two calls to make_pizza().

"""File - Make_pizza.py"""

# import pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -> When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program.
# You don’t actually see code being copied between files because Python copies the code behind the scenes just before the program runs.
# All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py.

# To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot.
# This code produces the same output as the original program that didn’t import a module.

# Importing Specific Functions -
# -> from module_name import function_name

# -> You can import as many functions as you want from a module by separating each function’s name with a comma -
# -> from module_name import function_0, function_1, function_2

# -> The making_pizzas.py example would look like this if we want to import just the function we’re going to use:

# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias

# -> f the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function.
# You’ll give the function this special nickname when you import the function.

# -> Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function using the alias you provide.

# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# -> The import statement shown here renames the function make_pizza() to mp() in this program.
# Any time we want to call make_pizza() we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file.

# -> The general syntax for providing an alias is:
# from module_name import function_name as fn

# Importing All Functions in a Module

# -> You can tell Python to import every function in a module by using the asterisk (*) operator:

# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# -> The asterisk in the import statement tells Python to copy every function from the module pizza into this program file.
# Because every function is imported, you can call each function by name without using the dot notation.
# However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results.
# Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions.












































