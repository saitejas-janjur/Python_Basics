# -> A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or names.
# -> In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

starwars = ['Anakin Skywalker', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala']
print(starwars)

# -> Lists are ordered collections, so you can access any element in a list by telling Python the position,
# or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

print(starwars[0])

# Index Positions Start at 0, Not 1
# -> Python considers the first item in a list to be at position 0, not position 1.

# ['Anakin Skywalker', 'Darth Vader', 'Luke Skywalker',  'Padme Amidala']
# [       0         ]   [    1    ]    [      2       ]  [       3      ]

print(starwars[1])
print(starwars[2])


# -> Python has a special syntax for accessing the last element in a list. By asking for the item at index -1,
# Python always returns the last item in the list:

print(starwars[-1])

# -> You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create
# a message based on a value from a list.

print(f"Star Wars Character - {starwars[0]}")


# Changing, Adding, and Removing Elements

# Modifying Elements in a List
# -> The syntax for modifying an element is similar to the syntax for accessing an element in a list.
# To change an element, use the name of the list followed by the index of the element you want to change,
# and then provide the new value you want that item to have.

starwars[0] = 'Han Solo'
print(starwars)

# Adding Elements to a List
# -> The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list,
# the new element is added to the end of the list.

starwars.append('Anakin Skywalker')
print(starwars)

# -> The append() method at ➊ adds 'Anakin Skywalker' to the end of the list without affecting any of the other elements in the list.

# Inserting Elements into a List

starwars.insert(0, "Chewbacca")
print(starwars)

# -> The insert() method opens a space at position 0 and stores the value 'Chewbacca' at that location. This operation
# shifts every other value in the list one position to the right.

# Removing Elements from a List -

del starwars[0]
print(starwars)

# -> The code uses del to remove the first item, 'Chewbacca', from the list of starwars.
# -> You can remove an item from any position in a list using the del statement if you know its index.

# Removing an Item Using the pop() Method

# -> The pop() method removes the last item in a list, but it lets you work with that item after removing it.
# The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.
# In this analogy, the top of a stack corresponds to the end of a list.

starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
print(starwars)
print(starwars.pop())

# Popping Items from any Position in a List

print(starwars.pop(0))
print(starwars)

# Removing an Item by Value

starwars.remove('Han Solo')
print(starwars)

# -> The code tells Python to figure out where 'Han Solo' appears in the list and remove that element.
# -> The remove() method deletes only the first occurrence of the value you specify.
# If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.

# Organizing a List

starwars = ['Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker']
starwars.sort()
print(starwars)

# -> The sort() method, changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order

# -> You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
# The following example sorts the list of cars in reverse alphabetical order

starwars.sort(reverse=True)
print(starwars)

# Sorting a List Temporarily with the sorted() Function

# -> To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
# The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list

# Sorted list
print(sorted(starwars))
# Original List
print(starwars)

# Printing a List in Reverse Order
starwars.reverse()
print(starwars)

# -> To reverse the original order of a list, you can use the reverse() method.
# If we originally stored the list of starwars in chronological order according to when we owned them,
# we could easily rearrange the list into reverse chronological order

# -> The reverse() method changes the order of a list permanently, but you can revert to the original order
# anytime by applying reverse() to the same list a second time

# Finding the Length of a List

# -> You can quickly find the length of a list by using the len() function.

print(len(starwars))

