# If Statements

# -> The loop in this example first checks if the current value of character is 'Han Solo'.
# If it is, the value is printed in uppercase. If the value of character is anything other than 'Han Solo', it’s printed in lower case


starwars = ('Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker')
for character in starwars:
    if character == 'Han Solo':
        print(character.upper())
    else:
        print(character.lower())

# Conditional Tests -

# -> At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.
# Python uses the values True and False to decide whether the code in an if statement should be executed.
# If a conditional test evaluates to True, Python executes the code following the if statement.
# If the test evaluates to False, Python ignores the code following the if statement

# Checking for Equality -

# -> Most conditional tests compare the current value of a variable to a specific value of interest.
# The simplest conditional test checks whether the value of a variable is equal to the value of interest.

character = 'Han Solo'
if character == 'Han Solo':
    print(f"The character is - {character}")
# >> True

# -> The line at 26 sets the value of character to 'Han Solo' using a single equal sign.
# The line at 27 checks whether the value of character is 'Han Solo' using a double equal sign (==).
# This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match.
# The values in this example match, so Python returns True.

character = 'Chewbacca'
if character == 'Han Solo':
    # >>  If statement returns False, so nothing is printed
    print()


# Ignoring Case When Checking for Equality -

# -> Testing for equality is case sensitive in Python.

character = 'Chewbacca'
if character == 'chewbacca':
    # >> If statement returns False, so nothing is printed
    print()

# -> This test would return True no matter how the value 'Chewbacca' is formatted because the test is now case insensitive.
# The lower() function doesn’t change the value that was originally stored in character, so you can do this kind of comparison without affecting the original variable.


character = 'Chewbacca'
if character.lower() == 'chewbacca':
    print(f"The character is - {character}")
# >> True

# Checking for Inequality -

# -> When you want to determine whether two values are not equal, you can combine an exclamation point and an equal sign (!=).
# The exclamation point represents not, as it does in many programming languages.

character = 'Chewbacca'
if character != 'Han Solo':
    print(f"The character is not Han Solo")

# -> The line at 66 compares the value of characters to the value 'Han Solo'.
# If these two values do not match, Python returns True and executes the code following the if statement.

# Numerical Comparisons -

# -> Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:

age = 18
if age == 18:
    print("The person is 18 years old.")

# -> You can also test to see if two numbers are not equal. For example, the following code prints a message if the given answer is not correct.

age = 17
if age != 18:
    print("The person is not 18 years old")

# -> You can include various mathematical comparisons in your conditional statements as well, such as less than,
# less than or equal to, greater than, and greater than or equal to.

age = 19
   # Less Than
if age < 21:
    print(True)
    # Less Than or Equal Too
if age <= 21:
    print(True)
    # Greater Than
if age > 21:
    print(False)
    # Greater Than or Equal Too
if age >= 21:
    print(False)


# Checking Multiple Conditions -

# Using and to Check Multiple Conditions
# -> To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests;
# if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.

age1 = 19
age2 = 21
if age1 == 19 and age2 == 21:
    print(True)
if age1 >= 18 and age2 <= 25:
    print(True)

# Using or to Check Multiple Conditions

# -> The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass.
# An or expression fails only when both individual tests fail.

if age1 == 19 or age2 == 20:
    print(True)

# Checking Whether a Value Is in a List

starwars = ('Chewbacca', 'Han Solo', 'Darth Vader', 'Luke Skywalker', 'Padme Amidala', 'Anakin Skywalker')
print('Han Solo' in starwars)
# >> True

# Checking Whether a Value Is Not in a List
print('Han Solo' not in starwars)
# >> False

# Boolean Expressions
# -> As you learn more about programming, you’ll hear the term Boolean expression at some point.
# A Boolean expression is just another name for a conditional test.
# A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

# if-else Statements
# -> Often, you’ll want to take one action when a conditional test passes and a different action in all other cases.
# Python’s if-else syntax makes this possible.
# An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of
# actions that are executed when the conditional test fails.

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# If the conditional test at 147 passes, the first block of indented print() calls is executed.
# If the test evaluates to False, the else block at 150 is executed.
# Because age is less than 18 this time, the conditional test fails and the code in the else block is executed.


# The if-elif-else Chain

# -> Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s if-elif-else syntax.
# Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes.
# When a test passes, the code following that test is executed and Python skips the rest of the tests.

age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# -> The lines at 168, 170, and 172 set the value of price according to the person’s age, as in the previous example.
# After the price is set by the if-elif-else chain, a separate unindented print() call 173 uses this value to display a message reporting the person’s admission price.

# -> This code produces the same output as the previous example, but the purpose of the if-elif-else chain is narrower.
# Instead of determining a price and displaying a message, it simply determines the admission price.
# In addition to being more efficient, this revised code is easier to modify than the original approach.
# To change the text of the output message, you would need to change only one print() call rather than three separate print() calls.


