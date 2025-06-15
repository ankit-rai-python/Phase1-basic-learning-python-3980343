# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# import the math module, which contains features for working with mathematics

# import math

# print("The value of pi is:", math.pi)  # print the value of pi
# print("The square root of 16 is:", math.sqrt(16))  # calculate the square root of 16


# import a specific part of the module so you can refer to it more easily
from math import pi
print("The value of pi is:", pi)  # now you can use pi directly without math. prefix

# import a module and give it a different name
import random as r
print(r.randint(100, 200))  # use the random module to generate a random integer between 100 and 200



# the math module contains lots of pre-built functions


# in addition to functions, some modules contain useful constants 


# Generate a random number between 100 and 200


# try some of the math functions for yourself here:

# Use the 3rd party tabulate module to print tabulated data:
# pip3 install tabulate
# https://pypi.org/project/tabulate/
from tabulate import tabulate
# class tabulate contains tabulate() function to create a formatted table from data
# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
print(tabulate(data, headers="firstrow", tablefmt="grid"))
