# Tech201_Packages_and_Libraries
Introduction to Packages and Libraries in Python. 

# Python Libraries

# Library = chunk of code that contains things that you know you will use later so we do not have to write things again. Usually methods and functions.
# Python has a huge amount of libraries: 1. because it s open source; 2. it s been around for a long time; 3. it s easy to write.
# Base liraries = methods, functions that are so useful, that is within the python language and gives you access as soon as you start using python.

# import random # import statement to access a certain library.
#
# print(random.random()) # output = a random float every time you run the library

from random import random # if we want to access a specific method or function
import math

print(random()) # outputs the same thing as above, but without us mentioning that we want a certain function/method from a certain library. prints only the specifies area of the library rather than the entire library.

num_float = 23.66
print(math.ceil(num_float)) # outputs 24 = .ceil rounds it up to the closest whole number.
print(math.floor(num_float)) # outputs 23 = .floor rounds it down to the closest whole number.
print(math.pi) # outputs 3.141592653589793(pi number).


# Modules

# Classes and inheritance = modules
# Modules = pieces of software that deliver a certain type of functionality

import os
import math, datetime, sys

working_directory = os.getcwd() # getcwd = get current working directory
print(working_directory) # outputs C:\Users\flori\PycharmProjects\Tech201_packages_libraries\Tech201_Packages_and_Libraries - the directory you are in and working.

# Module vs library = module is referencing a file; libraries are referencing functions and methods.

def return_user_id():
    print(os.getpid()) # getpid =

def return_user_name():
    print(os.uname())


print(datetime.date.today()) # having () at the end means that it can take arguments

print((sys.path)) # outputs current path within the computer # sys method allows us to interact with files and folders within our machine # not having () is because it does not take arguments


print(math.remainder(1, 5)) # outputs 1.0


# We do things with one line of code by using libraries and modules, compared to actually writing the chunk of code

# When you re building a program, it s really important to think whether you need to make a class/object yourself, or if we could use a function. You may not even need to make a function yourself, if there is a module that does what you are looking for already (base library/ module or outside ones).


# Built-in functions

# print()
# len()
# type()


# Pip and Packages

# Pip = Python`s Package Manager and installer
# pip -v = shows the commands for pip
# pip -V = shows the version we have installed
