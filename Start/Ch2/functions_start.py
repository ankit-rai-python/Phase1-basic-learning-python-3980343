# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions

# function nameing conventions
# - function names should be descriptive and use lowercase letters
# - use underscores to separate words in function names (e.g., hello_function)
# - avoid using reserved keywords as function names (e.g., def, class, if, etc.)
# - use verbs for function names to indicate actions (e.g., calculate_total, print_report)
# - keep function names concise but meaningful
# - avoid using spaces or special characters in function names
# - use underscores for readability in longer function names
# - consider using camelCase for function names in some coding styles (e.g., helloFunction)

# In Python, when a function does not return anything, it implicitly returns None.



# define a basic function

def hello_function():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

# call the function
hello_function()

# function that takes parameters
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old!")

# call the function with arguments
greet_user("Alice", 30)


# function that returns a value
def add_numbers(a, b):
    return a + b
# call the function and store the result
result = add_numbers(5, 10)
print("The sum is:", result)


# function with default value for an parameter

def greet(name="Guest"):
    print(f"Hello {name}!")
# call the function without providing an argument
greet()  # Output: Hello Guest!
# call the function with an argument
greet("Alice")  # Output: Hello Alice!


def add_numbers_with_default(a, b=10):
    return a + b

print(add_numbers_with_default(b=100,a=5))  # calling the function with named parameters

print(add_numbers_with_default(5))  # calling the function with one positional argument, b will take the default value of 10


# function with variable number of parameters

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
# call the function with multiple arguments
print("The sum is:", sum_numbers(1, 2, 3, 4, 5))  # Output: The sum is: 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
# call the function with keyword arguments
print_info(name="Alice", age=30, city="New York")

# function first argument fixed and others variable
def print_fixed_and_variable(fixed_arg, *args):
    print("Fixed argument:", fixed_arg)
    print("Variable arguments:", args)
# call the function with one fixed argument and multiple variable arguments
print_fixed_and_variable("Fixed", "Variable1", "Variable2", "Variable3")

# function with a return type hint
# Python 3.5+ supports type hints for function parameters and return types
# note: Type hints are optional and do not enforce type checking at runtime, but they can help with code readability and IDE support.
def multiply(a: int, b: int) -> int:
    return a * b
# call the function with type hints
print("The product is:", multiply(5, 10))  # Output: The product is: 50
