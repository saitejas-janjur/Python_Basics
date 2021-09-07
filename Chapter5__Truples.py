# Defining a Tuple

# -> Lists work well for storing collections of items that can change throughout the life of a program.
# The ability to modify lists is particularly important when you’re working with a list of users on a website or a list of characters in a game.
# However, sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that.
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

# -> A tuple looks just like a list except you use parentheses instead of square brackets.
# Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

starwars = ('Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker')
print(starwars[1])

# -> Tuples are technically defined by the presence of a comma;
# the parentheses make them look neater and more readable.
# If you want to define a tuple with one element, you need to include a trailing comma:

starwars_exaple = ('Chewbacca',)

# Looping Through All Values in a Tuple

for characters in starwars:
    print(characters)

# Writing over a Tuple

# -> Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple

starwars_1 = ('Chewbacca', 'Han Solo', 'Darth Vader')
print("Original Truple -- ")
for characters in starwars_1:
    print(characters)

starwars_1 = ('Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker')
print("Modified Truple -- ")
for characters in starwars_1:
    print(characters)

# -> The lines starting at 30 define the original tuple and print the initial characters.
# At 35, we associate a new tuple with the variable characters. We then print the new characters at 38.
# Python doesn’t raise any errors this time, because reassigning a variable is valid






























