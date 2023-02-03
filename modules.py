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









