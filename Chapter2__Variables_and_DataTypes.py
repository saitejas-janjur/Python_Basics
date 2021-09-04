#  ->VARIABLES

#  ->Every variable is connected to a value, which is the information associated with that variable.

#  ->When it processes line 8, it associates the variable message with the "Hello, world!" text.
#  ->When it reaches line 9, it prints the value associated with message to the screen.

message = "Hello, World!"
print(message)

#  ->This code will print "Hello, World"

message = "Hello, Python!"
print(message)

#  ->You can change the value of a variable in your program at any time, and Python will always keep track of its current value.


# NAMING CONVENTION AND USING VARIABLES -

#  -> Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number.
#  -> Spaces are not allowed in variable names, but underscores can be used to separate words in variable names.
#  -> Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved
# for a particular programmatic purpose, such as the word print.


# VARIABLES -

# STRINGS -

#  -> A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single
# or double quotes around your strings like this:
#
print("This is a string.")
print('This is also a string.')

# Changing Case in a String with Methods -

name = "star wars"
print(name.title())

#  -> In this example, the variable name refers to the lowercase string "star wars". The method title() appears after the
# variable in the print() call. A method is an action that Python can perform on a piece of data. The dot (.)
# after name in name.title() tells Python to make the title() method act on the variable name.
# Every method is followed by a set of parentheses, because methods often need additional information to do their work.
# That information is provided inside the parentheses. The title() function doesn’t need any additional information, so
# its parentheses are empty.


#  -> The title() method changes each word to title case, where each word begins with a capital letter.
# This is useful because you’ll often want to think of a name as a piece of information. For example,
# you might want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as Ada.

name = "Star Wars"
print(name.upper())
print(name.lower())


#  -> The lower() method is particularly useful for storing data. Many times you won’t want to trust the capitalization
# that your users provide, so you’ll convert strings to lowercase before storing them.
# Then when you want to display the information, you’ll use the case that makes the most sense for each string.


first_name = "Star"
last_name = "Wars"
full_name = f"{first_name}{last_name}"
print(full_name)

#  -> To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark.
# Put braces around the name or names of any variable you want to use inside the string.
# Python will replace each variable with its value when the string is displayed.
#
#  -> These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of
# any variable in braces with its value.

#  ->To add a tab to your text, use the character combination \t.
print("\tStar Wars")

# -> To add a newline in a string, use the character combination \n.

print("Star\nWars")

# -> Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace exists at
# the right end of a string, use the rstrip() method.

name = " Star Wars "
print(name.rstrip())

# -> You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():

print(name.lstrip())
print(name.strip())


# INTEGERS

# -> You can add (+), subtract (-), multiply (*), and divide (/) integers in Python.

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# ->  Python uses two multiplication symbols to represent exponents:

print(3 ** 2)

# -> Python supports the order of operations too, so you can use multiple operations in one expression.
# You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.

print((2 + 3) * 4)


# FLOATS

# -> Python calls any number with a decimal point a float. This term is used in most programming languages,
# and it refers to the fact that a decimal point can appear at any position in a number.
# Every programming language must be carefully designed to properly manage decimal numbers so numbers behave
# appropriately no matter where the decimal point appears.

print(0.1 + 0.1)

# -> But be aware that you can sometimes get an arbitrary number of decimal places in your answer:

print(0.2 + 0.1)
