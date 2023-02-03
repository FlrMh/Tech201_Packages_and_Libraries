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


