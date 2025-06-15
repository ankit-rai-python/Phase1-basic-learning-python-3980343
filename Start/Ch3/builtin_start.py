# battary included functions
# https://docs.python.org/3/index.html
# https://docs.python.org/3/library/functions.html

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# len()
# the len() function calculates the length of a sequence
print(len(mystring))  # length of the string
print(len(mynumbers))  # length of the list

# max() and min()
# the max() and min() functions will find the largest and smallest value in a sequence
print(max(mynumbers))  # maximum value in the list
print(min(mynumbers))  # minimum value in the list
print(max(mystring))  # maximum character in the string (based on ASCII value)
print(min(mystring))  # minimum character in the string (based on ASCII value)

# str()
# the str() function will return a string version of an object
prefix = "result: "
result = 5
print(prefix + str(result))  # concatenate string and integer after converting integer to string
print(prefix + str(3.14)) # concatenate string and float after converting float to string

# range()
# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
# ending value is not included in the range
for i in range(1, 11):  # from 1 to 10
    print(i)  # prints numbers from 1 to 10

for i in range(0, 20, 2):  # from 0 to 18, step of 2
    print(i)  # prints even numbers from 0 to 18

for i in range(5, len(mystring), 2) :  # from 5 to the end of the string, step of 2
    print(mystring[i])  # prints every second character from index 5 to the end of the string

# print()
# the print function itself is pretty flexible - you can embed variables directly in it

greeting = "Hello!"
count = 10

# interpolation using f-strings (Python 3.6+)
print(f"{greeting} You have {count} new messages.")  # prints: Hello! You have 10 new messages.

# input()
# the input() function will read input from the user
user = input("Enter your name: ")  # prompts the user for input
print(f"Hello, {user}!")  # prints a greeting with the user's name

# type()
# the type() function will return the type of an object
print(type(user))  # prints the type of the user input (usually <class 'str'>)

# abs()
# the abs() function will return the absolute value of a number
print(abs(-5))  # prints 5

# round()
# the round() function will round a number to a specified number of decimal places
print(round(3.14159, 2))  # prints 3.14 (rounded to 2 decimal places)

# sum()
# the sum() function will return the sum of all elements in an iterable (like a list)
print(sum(mynumbers))  # prints the sum of all numbers in the list

# sorted()
# the sorted() function will return a sorted version of an iterable
print(sorted(mynumbers))  # prints the numbers in ascending order

# reversed()
# the reversed() function will return a reversed iterator of an iterable
print(list(reversed(mynumbers)))  # prints the numbers in reverse order 

# zip()
# the zip() function will combine multiple iterables into tuples
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)  # combines names and ages into tuples
print(list(zipped))  # prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# enumerate()
# the enumerate() function will add a counter to an iterable
for index, value in enumerate(mynumbers):
    print(f"Index: {index}, Value: {value}")  # prints the index and value of each element in the list

# all()
# the all() function will return True if all elements in an iterable are true
print(all([True, True, False]))  # prints False (not all are True)

# any()
# the any() function will return True if any element in an iterable is true
print(any([False, False, True]))  # prints True (at least one is True)

# filter()
# the filter() function will filter elements from an iterable based on a function
def is_even(num):
    return num % 2 == 0
filtered_numbers = filter(is_even, mynumbers)  # filters even numbers from the list
print(list(filtered_numbers))  # prints [6, 12, 14, 20] (even numbers from the list)

# map()
# the map() function will apply a function to each element in an iterable
def square(num):
    return num ** 2
squared_numbers = map(square, mynumbers)  # squares each number in the list
print(list(squared_numbers))  # prints [1, 9, 25, 36, 81, 144, 196, 289, 400, 900] (squared numbers)

# filter() with lambda
# the filter() function can also be used with lambda functions
filtered_numbers_lambda = filter(lambda x: x % 2 == 0, mynumbers)  # filters even numbers using a lambda function
print(list(filtered_numbers_lambda))  # prints [6, 12, 14, 20] (even numbers from the list)

# map() with lambda
# the map() function can also be used with lambda functions
squared_numbers_lambda = map(lambda x: x ** 2, mynumbers)  # squares each number using a lambda function
print(list(squared_numbers_lambda))  # prints [1, 9, 25, 36, 81, 144, 196, 289, 400, 900] (squared numbers)

# dir()
# the dir() function will return a list of attributes and methods of an object
print(dir(mystring))  # prints all attributes and methods of the string object

# help()
# the help() function will provide documentation for an object or function
# help(mystring)  # prints documentation for the string object

# isinstance()
# the isinstance() function will check if an object is an instance of a specified class
print(isinstance(mystring, str))  # prints True (mystring is a string)
print(isinstance(mynumbers, list))  # prints True (mynumbers is a list)

# id()
# the id() function will return the unique identifier of an object
print(id(mystring))  # prints the unique identifier of the string object
print(id(mynumbers))  # prints the unique identifier of the list object

# globals()
# the globals() function will return a dictionary of the current global symbol table
print(globals())  # prints all global variables and their values

# locals()
# the locals() function will return a dictionary of the current local symbol table
print(locals())  # prints all local variables and their values

# eval()
# the eval() function will evaluate a string as a Python expression
# print(eval("3 + 5"))  # prints 8 (evaluates the expression as Python code)
