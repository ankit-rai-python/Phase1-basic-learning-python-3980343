
# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types
# 📌 Python Variable Naming Conventions

# ✅ Use snake_case for variable and function names
# Example: total_amount, user_name, get_user_input()

# ✅ Variable names can start with an underscore (_) for internal use
# Example: _temp_value, _private_method()

# ✅ Use lowercase letters with underscores for multi-word names
# Example: account_balance, customer_id

# ✅ Constants should be in UPPER_SNAKE_CASE
# Example: MAX_RETRIES = 5

# ✅ Dunder (double underscore) methods are for special behavior
# Example: __init__, __str__

# ❌ Avoid starting names with numbers or using special characters other than _
# ❌ Don't use Python reserved keywords like 'class', 'def', 'for', etc.

# ✅ Choose meaningful names for readability and maintainability
# Python variables are case sensitive


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 

# Running Python code in the terminal:
# $ python3 ch2-variables.py
# Highlight lines of code, right-click, and choose "Run Selection/Line in Python Terminal"
# Right-click the file in the file explorer and select "Run Python File in Terminal"
# Right-click the file name in the explorer and choose "Run Python File in Terminal"

myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint)
print(mystr)

# Operators are used to perform operations on variables
print(myint + myfloat)  # Addition
print(myint * myfloat)  # Multiplication
print(myint / myfloat)  # Division
print(myint % 3)  # Modulus (remainder)

another_str = "This is another string"
print(mystr + " " + another_str)  # String concatenation
print("ankit " * 3)  # String repetition
# print("ankit" + 1)  # This will raise an error because we cannot concatenate a string and an integer directly
# We can use the type() function to check the type of a variable
print(type(myint))  # <class 'int'>

# Logical and comparison operators 

# Comparison operators
print(myint == 10)  # Equal to
print(myint != 10)  # Not equal to
print(myint > 5)    # Greater than
print(myint < 20)   # Less than
print(myint >= 10)  # Greater than or equal to
print(myint <= 10)  # Less than or equal to

# Logical operators
print(myint > 5 and myfloat < 20)  # Logical AND
print(myint < 5 or myfloat > 20)   # Logical OR
print(not mybool)  # Logical NOT - flipping the boolean value



# re-declaring a variable works

myint = 20  # Re-declaring the variable with a new value
print(myint)  # Output: 20
