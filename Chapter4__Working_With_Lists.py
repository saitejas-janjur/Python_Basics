# Looping Through an Entire List
starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
for character in starwars:
    print(character)

# -> We begin by defining a list, just as we did in Chapter 3. At line 3, we define a for loop.
# This line tells Python to pull a name from the list magicians, and associate it with the variable character.
# At line 4 we tell Python to print the name that’s just been assigned to character.
# Python then repeats lines 3 and 4, once for each name in the list.
# It might help to read this code as “For every character in the list of starwars, print the character’s name.”
# The output is a simple printout of each name in the list.


# Doing More Work Within a for Loop

starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
for character in starwars:
    print(f"Star Wars character - {character.title()}")


# Making Numerical Lists

# Using the range() Function

for value in range(1, 5):
    print(value)

# -> In this example, range() prints only the numbers 1 through 4.
# This is another result of the off-by-one behavior you’ll see often in programming languages.
# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.

# Using range() to Make a List of Numbers -

numbers = list(range(1, 6))
print(numbers)

# -> We can also use the range() function to tell Python to skip numbers in a given range.
# If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# -> In this example, the range() function starts with the value 2 and then adds 2 to that value.
# It adds 2 repeatedly until it reaches or passes the end value, 11.

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Lowest number in the list
print(min(digits))
# Highest number in the list
print(max(digits))
# Sum of all number's in the list
print(sum(digits))

# Working with Part of a List

# Slicing a List

starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
print(starwars[0:3])

# -> The code prints a slice of this list, which includes just the first three characters.
# The output retains the structure of the list and includes the first three players in the list.

# -> If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

print(starwars[:4])

# -> Without a starting index, Python starts at the beginning of the list

# -> A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index:

print(starwars[2:])

# -> Python returns all items from the third item through the end of the list

# -> This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list.
# Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list.

print(starwars[-3:])

# -> This prints the names of the last three characters and would continue to work as the list of characters changes in size.

# Looping Through a Slice

starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
for characters in starwars[:-3]:
    print(characters.title())

# -> Instead of looping through the entire list of characters, Python loops through only the first three characters.

