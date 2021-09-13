# WHILE LOOPS

# -> The for loop takes a collection of items and executes a block of code once for each item in the collection.
# In contrast, the while loop runs as long as, or while, a certain condition is true.

num = 1
while num <= 5:
    print(num)
    num += 1

# -> In the first line, we start counting from 1 by assigning num the value 1.
# The while loop is then set to keep running as long as the value of num is less than or equal to 5.
# The code inside the loop prints the value of num and then adds 1 to that value with current_number += 1.
# (The += operator is shorthand for current_number = current_number + 1.)
#
# Python repeats the loop as long as the condition num <= 5 is true.
# Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2.
# Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on.
# Once the value of current_number is greater than 5, the loop stops running and the program ends.

# Letting the User Choose When to Quit

starting_number = 0
user_input_number = int(input("How many times do you want to multiply by 2? "))
while starting_number <= user_input_number:
    print(f"{starting_number} * 2 = {starting_number*2}")
    starting_number += 1

# -> Initializing the starting number of the multiplication table to 0.
# Then we ask the user for the end number for the multiplication table.
# In line 25 we are testing if the starting number is less than the user input.
# Then we print out the multiplication's for how many ever times the user requested for.

# Using a Flag

# -> For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
# This variable, called a flag, acts as a signal to the program.
# We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.
# As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True.
# Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.

active = True
while active:
    message = input("Enter you message: ")
    if message == 'quit':
        active = False
    else:
        print(message)

# -> We set the variable active to True so the program starts in an active state.
# Doing so makes the while statement simpler because no comparison is made in the while statement itself; the logic is taken care of in other parts of the program.
# As long as the active variable remains True, the loop will continue running.

# -> In the if statement inside the while loop, we check the value of message once the user enters their input.
# If the user enters 'quit', we set active to False, and the while loop stops.
# If the user enters anything other than 'quit', we print their input as a message.

# Using break to Exit a Loop

# -> To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.
# The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only executes code that you want it to, when you want it to.

while True:
    message = input("Enter you message: ")
    if message == 'quit':
        break
    else:
        print(message)

# -> A loop that starts with while True ➊ will run forever unless it reaches a break statement.
# The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'.
# When they enter 'quit', the break statement runs, causing Python to exit the loop.

# Using continue in a Loop -

# -> Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# -> First we set current_number to 0. Because it’s less than 10, Python enters the while loop.
# Once inside the loop, we increment the count by 1, so current_number is 1.
# The if statement then checks the modulo of current_number and 2.
# If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of the loop and return to the beginning.
# If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.

# Using a while Loop with Lists and Dictionaries

# Moving Items from One List to Another

# start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'jake']
confirmed_users = []
# verify each user until there are no more unconfirmed users
# move each verified user into confirmed user list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_users in confirmed_users:
    print(confirmed_users.title())

# -> We begin with a list of unconfirmed users (Alice, Brian, and Candace) and an empty list to hold confirmed users.
# The while loop runs as long as the list unconfirmed_users is not empty.
# Within this loop, the pop() function removes unverified users one at a time from the end of unconfirmed_users.
# Here, because Candace is last in the unconfirmed_users list, her name will be the first to be removed, assigned to current_user, and added to the confirmed_users list.
# Next is Brian, then Alice.

# -> We simulate confirming each user by printing a verification message and then adding them to the list of confirmed users.
# As the list of unconfirmed users shrinks, the list of confirmed users grows.
# When the list of unconfirmed users is empty, the loop stops and the list of confirmed users is printed.

# Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# -> We start with a list containing multiple instances of 'cat'.
# After printing the list, Python enters the while loop because it finds the value 'cat' in the list at least once.
# Once inside the loop, Python removes the first instance of 'cat', returns to the while line, and then reenters the loop when it finds that 'cat' is still in the list.
# It removes each instance of 'cat' until the value is no longer in the list, at which point Python exits the loop and prints the list again

# Filling a Dictionary with User Input


responses = {}
# set flag to indicate that polling is active
polling_activity = True
while polling_activity:
    # prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("What is your favorite programing language? ")
    # store the responses in the dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another response? (yes/no) ")
    if repeat == 'no':
        polling_activity = False
    # polling is complete. show the results
for name, response in responses.items():
    print(f"{name} answered {response}.")

# -> The program first defines an empty dictionary (responses) and sets a flag (polling_active) to indicate that polling is active.
# As long as polling_active is True, Python will run the code in the while loop.
#
# -> Within the loop, the user is prompted to enter their name and a favorite programing language.
# That information is stored in the responses dictionary, and the user is asked whether or not to keep the poll running.
# If they enter yes, the program enters the while loop again.
# If they enter no, the polling_active flag is set to False, the while loop stops running, and the final code block at displays the results of the poll.


