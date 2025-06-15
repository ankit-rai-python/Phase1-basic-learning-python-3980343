# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions

# Errors can happen in programs, and we need a clean way to handle them.
# Exceptions provide a way to catch and handle errors gracefully.

# This code will cause an error because you can't divide by zero:
# Uncommenting the line below will raise a ZeroDivisionError.
# x = 10 / 0

# Example 1: Catching a general exception
try:
    # This code might cause an error
    x = 10 / 0
except:
    # This code runs if there is any exception (not recommended to catch all exceptions)
    print("You can't divide by zero!")

# Example 2: Catching a specific exception
try:
    # This code might cause an error
    x = 10 / 0
except ZeroDivisionError:
    # This code runs only if there is a ZeroDivisionError
    print("You can't divide by zero!")

# Example 3: Handling multiple exceptions
try:
    # Prompt the user for input
    answer = input("What should I divide 10 by? ")
    # Convert the input to an integer and perform division
    x = 10 / int(answer)
except ZeroDivisionError as e:
    # Handle division by zero
    print("You can't divide by zero!")
except ValueError as e:
    # Handle invalid input (e.g., non-numeric input)
    print("Please enter a valid number!")
    print(e)  # Print the exception message for debugging
finally:
    # The finally block runs no matter what, even if there was an error
    print("This code runs no matter what, even if there was an error.")

# Key Notes:
# - Use `try` to wrap code that might raise an exception.
# - Use `except` to handle specific exceptions or a general exception.
# - Use `finally` to execute code that should run regardless of whether an exception occurred.
# - Avoid catching all exceptions with a bare `except` unless absolutely necessary.
