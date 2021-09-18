# Reading from a File

# -> An incredible amount of data is available in text files.
# Text files can contain weather data, traffic data, socioeconomic data, literary works, and more.
# Reading from a file is particularly useful in data analysis applications, but it’s also applicable to any situation in which you want to analyze or modify information stored in a file.
# For example, you can write a program that reads in the contents of a text file and rewrites the file with formatting that allows a browser to display it.

# -> When you want to work with the information in a text file, the first step is to read the file into memory.
# You can read the entire contents of a file, or you can work through the file one line at a time.

# Reading an Entire File

# To begin, we need a file with a few lines of text in it. Let’s start with a file that contains pi to 30 decimal places, with 10 decimal places per line.

# pi_digits.txt
# 3.141592653
# 58979323846264
# 3383279

# file_reader.py
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# -> The first line of this program has a lot going on. Let’s start by looking at the open() function.
# To do any work with a file, even just printing its contents, you first need to open the file to access it.
# The open() function needs one argument: the name of the file you want to open.
# Python looks for this file in the directory where the program that’s currently being executed is stored.
# In this example, file_reader.py is currently running, so Python looks for pi_digits.txt in the directory where file_reader.py is stored.
# The open() function returns an object representing the file.
# Here, open('pi_digits.txt') returns an object representing pi_digits.txt.
# Python assigns this object to file_object, which we’ll work with later in the program.

# -> The keyword with closes the file once access to it is no longer needed.
# Notice how we call open() in this program but not close().
# You could open and close the file by calling open() and close(), but if a bug in your program prevents the close() method from being executed, the file may never close.
# This may seem trivial, but improperly closed files can cause data to be lost or corrupted.
# And if you call close() too early in your program, you’ll find yourself trying to work with a closed file (a file you can’t access), which leads to more errors.
# It’s not always easy to know exactly when you should close a file, but with the structure shown here, Python will figure that out for you.
# All you have to do is open the file and work with it as desired, trusting that Python will close it automatically when the with block finishes execution.

# -> Once we have a file object representing pi_digits.txt, we use the read() method in the second line of our program to read the entire contents of the file and store it as one long string in contents.
# When we print the value of contents, we get the entire text file back.

# -> The only difference between this output and the original file is the extra blank line at the end of the output.
# The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line.
# If you want to remove the extra blank line, you can use rstrip() in the call to print().

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# -> Recall that Python’s rstrip() method removes, or strips, any whitespace characters from the right side of a string. Now the output matches the contents of the original file exactly.

# File Paths

# -> When you pass a simple filename like pi_digits.txt to the open() function, Python looks in the directory where the file that’s currently being executed (that is, your .py program file) is stored.

# -> Sometimes, depending on how you organize your work, the file you want to open won’t be in the same directory as your program file.
# For example, you might store your program files in a folder called python_work; inside python_work, you might have another folder called text_files to distinguish your program files from the text files they’re manipulating.
# Even though text_files is in python_work, just passing open() the name of a file in text_files won’t work, because Python will only look in python_work and stop there; it won’t go on and look in text_files.
# To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.

# -> Because text_files is inside python_work, you could use a relative file path to open a file from text_files.
# A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored.

# For example, you’d write:
# with open('text_files/filename.txt') as file_object:

# -> This line tells Python to look for the desired .txt file in the folder text_files and assumes that text_files is located inside python_work (which it is).

# -> You can also tell Python exactly where the file is on your computer regardless of where the program that’s being executed is stored.
# This is called an absolute file path.
# You use an absolute path if a relative path doesn’t work.
# For instance, if you’ve put text_files in some folder other than python_work—say, a folder called other_files—then just passing open() the path 'text_files/filename.txt' won’t work because Python will only look for that location inside python_work.
# You’ll need to write out a full path to clarify where you want Python to look.

# -> Absolute paths are usually longer than relative paths, so it’s helpful to assign them to a variable and then pass that variable to open():
# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# -> Using absolute paths, you can read files from any location on your system.
# For now it’s easiest to store files in the same directory as your program files or in a folder such as text_files within the directory that stores your program files.

# Reading Line by Line

# -> When you’re reading a file, you’ll often want to examine each line of the file.
# You might be looking for certain information in the file, or you might want to modify the text in the file in some way.
# For example, you might want to read through a file of weather data and work with any line that includes the word sunny in the description of that day’s weather.
# In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
# You can use a for loop on the file object to examine each line from a file one at a time.

# file_reader.py

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# -> At 95 we assign the name of the file we’re reading from to the variable filename.
# This is a common convention when working with files.
# Because the variable filename doesn’t represent the actual file—it’s just a string telling Python where to find the file—you can easily swap out 'pi_digits.txt' for the name of another file you want to work with.
# After we call open(), an object representing the file and its contents is assigned to the variable file_object 96.
# We again use the with syntax to let Python open and close the file properly. To examine the file’s contents, we work through each line in the file by looping over the file object 97.

# -> When we print each line, we find even more blank lines, These blank lines appear because an invisible newline character is at the end of each line in the text file.
# The print function adds its own newline each time we call it, so we end up with two newline characters at the end of each line: one from the file and one from print().
# Using rstrip() on each line in the print() call eliminates these extra blank lines.

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File

# -> When you use with, the file object returned by open() is only available inside the with block that contains it.
# If you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the block and then work with that list.
# You can process parts of the file immediately and postpone some processing for later in the program.

# The following example stores the lines of pi_digits.txt in a list inside the with block and then prints the lines outside the with block.

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
for line in lines:
    print(line.rstrip())

# -> At 125 the readlines() method takes each line from the file and stores it in a list.
# This list is then assigned to lines, which we can continue to work with after the with block ends.
# At 126 we use a simple for loop to print each line from lines.
# Because each item in lines corresponds to each line in the file, the output matches the contents of the file exactly.

# Working with a File’s Contents

# -> After you’ve read a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits of pi.
# First, we’ll attempt to build a single string containing all the digits in the file with no whitespace in it.

# pi_string.py

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
pi_sting = ' '
for line in lines:
    pi_sting += line.rstrip()
print(pi_sting)
print(len(pi_sting))

# -> We start by opening the file and storing each line of digits in a list, just as we did in the previous example.
# At 144 we create a variable, pi_string, to hold the digits of pi.
# We then create a loop that adds each line of digits to pi_string and removes the newline character from each line 145.
# At 147 we print this string and also show how long the string is.

# -> The variable pi_string contains the whitespace that was on the left side of the digits in each line, but we can get rid of that by using strip() instead of rstrip().

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
pi_sting = ' '
for line in lines:
    pi_sting += line.strip()
print(pi_sting)
print(len(pi_sting))

# Large Files: One Million Digits

# -> So far we’ve focused on analyzing a text file that contains only three lines, but the code in these examples would work just as well on much larger files.
# If we start with a text file that contains pi to 1,000,000 decimal places instead of just 30, we can create a single string containing all these digits.
# We don’t need to change our program at all except to pass it a different file.
# We’ll also print just the first 50 decimal places, so we don’t have to watch a million digits scroll by in the terminal.

# pi_million_digits.txt
# https://github.com/ehmatthes/pcc/blob/master/chapter_10/pi_million_digits.txt

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readline()
pi_sting = ' '
for line in lines:
    pi_sting += line.strip()
print(f"{pi_sting[:52]}......")
print(len(pi_sting))                

# Writing to a File

# -> One of the simplest ways to save data is to write it to a file.
# When you write text to a file, the output will still be available after you close the terminal containing your program’s output.
# You can examine output after a program finishes running, and you can share the output files with others as well.
# You can also write programs that read the text back into memory and work with it again later.

# Writing to an Empty File

# -> To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.
# To see how this works, let’s write a simple message and store it in a file instead of printing it to the screen:

filename = 'programing.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming")

# -> The call to open() in this example has two arguments 198. The first argument is still the name of the file we want to open.
# The second argument, 'w', tells Python that we want to open the file in write mode.
# You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+').
# If you omit the mode argument, Python opens the file in read-only mode by default.

# -> The open() function automatically creates the file you’re writing to if it doesn’t already exist.
# However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.

# -> At 199 we use the write() method on the file object to write a string to the file.
# This program has no terminal output, but if you open the file programming.txt, you’ll see one line

# programming.txt
# I love programming

# Writing Multiple Lines
# -> The write() function doesn’t add any newlines to the text you write.
# So if you write more than one line without including newline characters, your file may not look the way you want it to:

filename = 'programing.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming\n")
    file_object.write("I love gaming\n")

# Appending to a File

# -> If you want to add content to a file instead of writing over existing content, you can open the file in append mode.
# When you open a file in append mode, Python doesn’t erase the contents of the file before returning the file object.
# Any lines you write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.


filename = 'programing.txt'
with open(filename, 'a') as file_object:
    file_object.write("Python\n")
    file_object.write("Python Program\n")

# -> At 232 we use the 'a' argument to open the file for appending rather than writing over the existing file.
# At 233 we write two new lines, which are added to programming.txt
