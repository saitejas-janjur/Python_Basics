# User Input

# -> Most programs are written to solve an end user’s problem. To do so, you usually need to get some information from the user.

# -> The input() function pauses your program and waits for the user to enter some text.
# Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

firstname = input("Enter your First name - ")
lastname = input("Enter your Last name - ")
print(f"Hello {lastname.title()} {firstname.title()}")

# -> The input() function takes one argument: the prompt, or instructions, that we want to display to the user so they know what to do.
# In this example, when Python runs the first line, the user sees the prompt Enter your First name - .
# The program waits while the user enters their response and continues after the user presses ENTER.
# The response is assigned to the variable firstname, then print(firstname) displays the input back to the user.

# Writing Clear Prompts -

# -> Each time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you’re looking for.
# Any statement that tells the user what to enter should work.

# -> Add a space at the end of your prompts (after the colon in the preceding example) to separate the prompt from the user’s response and to make it clear to your user where to enter their text.

# Using int() to Accept Numerical Input

# -> When you use the input() function, Python interprets everything the user enters as a string.

age = input("How old are you? ")
print(type(age))

# -> he user enters the number 21, but when we ask Python for the value of age, it returns '21', the string representation of the numerical value entered.
# We know Python interpreted the input as a string because the number is now enclosed in quotes.
# If all you want to do is print the input, this works well. But if you try to use the input as a number, you’ll get an error

age = int(input("What is you age? "))
print(type(age))

# -> We are converting the input to integer while taking the input from the user.

# The Modulo Operator
# -> A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder

print(4 % 3)
print(2 % 4)
print(6 % 3)

# -> The modulo operator doesn’t tell you how many times one number fits into another; it just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0.
# You can use this fact to determine if a number is even or odd.










