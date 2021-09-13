# DICTIONARIES

# -> A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python as a value in a dictionary.
# In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces.

character1 = {'health': 80, 'points': 360}
character2 = {'health': 45, 'points': 289}
print(f"Character 1 has {character1['points']} points with {character1['health']} health remaining.")
print(f"Character 2 has {character2['points']} points with {character2['health']} health remaining.")

#  -> A key-value pair is a set of values associated with each other.
#  When you provide a key, Python returns the value associated with that key.
#  Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.
#  You can store as many key-value pairs as you want in a dictionary.

# Adding New Key-Value Pairs

# -> Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.

character1['name'] = "Ava"
character2['name'] = "Jack"

# -> The final version of the dictionary contains three key-value pairs.
# The original two specify health and points value, and the last one specifies the character’s name.

# character1 = {'health': 80, 'points': 360, 'name': "Ava"}
# character2 = {'health': 45, 'points': 289, 'name': "Jack"}

print(f"Character {character1['name']} has {character1['points']} points with {character1['health']} health remaining.")
print(f"Character {character2['name']} has {character2['points']} points with {character2['health']} health remaining.")

# Starting with an Empty Dictionary

EmptyCharacter = {}

EmptyCharacter['health'] = 250
EmptyCharacter['points'] = 340

print(EmptyCharacter)

# -> Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or
# when you write code that generates a large number of key-value pairs automatically.

# Modifying Values in a Dictionary

# -> To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.

# Removing Key-Value Pairs

# -> When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.
# All del needs is the name of the dictionary and the key that you want to remove.

character1 = {'name': "Ava", 'health': 80, 'points': 360}
print(character1)
del character1['points']
print(character1)

# Using get() to Access Values

# -> Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem:
# if the key you ask for doesn’t exist, you’ll get an error.

character1 = {'name': "Ava", 'health': 80, 'points': 360}
status = character1.get('status', 'No status available')
print(status)

# -> If the key 'points' exists in the dictionary, you’ll get the corresponding value.
# If it doesn’t, you get the default value. In this case, points doesn’t exist, and we get a clean message instead of an error.

# -> If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation.

# Looping Through a Dictionary

# Looping Through All Key-Value Pairs

character1 = {
    'name': "Ava",
    'health': 80,
    'points': 360
}

for key, value in character1.items():
    print(f"\nKey: {key}")
    print(f"\nvalue: {value}")

# -> As shown at 85, to write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair.
# You can choose any names you want for these two variables.

# Looping Through only Keys in a Dictionary

character1 = {
    'name': "Ava",
    'health': 80,
    'points': 360
}

for key in character1.keys():
    print(key.title())

# -> The keys() method is useful when you don’t need to work with all of the values in a dictionary.

# Looping Through a Dictionary’s Keys in a Particular Order

character = {
    'name': "Ava",
    'health': 80,
    'points': 360,
    'status': 'Alive'
}

for key in sorted(character.keys()):
    print(f"{key.title()}")

# -> This for statement is like other for statements except that we’ve wrapped the sorted() function around the dictionary.keys() method.
# This tells Python to list all keys in the dictionary and sort that list before looping through it.

# Looping Through All Values in a Dictionary

# -> If you are primarily interested in the values that a dictionary contains, you can use the values() method to return a list of values without any keys.

character = {
    'name': "Ava",
    'health': 80,
    'points': 360,
    'status': 'Alive'
}
for values in character.values():
    print(values)

# -> The for statement here pulls each value from the dictionary and assigns it to the variable language.
# When these values are printed, we get a list of all chosen languages

# > This approach pulls all the values from the dictionary without checking for repeats.
# That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list.
# To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique.

characters = {
    'person1': 'C3PO',
    'person2': 'Han Solo',
    'person3': 'Luke Skywalker',
    'person4': 'C3PO'
}

for people in set(characters.values()):
    print(people.title())

# -> When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items.
# At 147 we use set() to pull out the unique languages in characters.values().


# Nesting

# -> Sometimes you’ll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary.
# This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.
# Nesting is a powerful feature, as the following examples will demonstrate.

character1 = {'name': 'Ava', 'health': 80, 'points': 360}
character2 = {'name': 'Jack', 'health': 45, 'points': 289}
character3 = {'name': 'Brian', 'health': 65, 'points': 159}

characters = [character1, character2, character3]

print(characters)

# -> We first create three dictionaries, each representing a different alien.
# At 165 we store each of these dictionaries in a list called characters. Finally, we loop through the list and print out each character.

# A List in a Dictionary

# -> Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary.

pizza = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']} crust pizza, with the following toppings- ")
for toppings in pizza['toppings']:
    print("\t" + toppings.title())

# -> We begin at 176 with a dictionary that holds information about a pizza that has been ordered.
# One key in the dictionary is 'crust', and the associated value is the string 'thick'. The next key, 'toppings', has a list as its value that stores all requested toppings.

# -> You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.

# A Dictionary in a Dictionary

users = {
    'jodoe': {
        'first': 'John',
        'last': 'Doe',
    },
    'jadoe':{
        'first': 'Jane',
        'last': 'Doe'
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    print("\t" + fullname)

# -> We first define a dictionary called users with two keys: one each for the usernames 'jodoe' and 'jadoe'.
# The value associated with each key is a dictionary that includes each user’s first name and last name.


























