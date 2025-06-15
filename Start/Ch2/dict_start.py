# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
myDict = {
    "name": "Joe",
    "age": 30,
    "city": "San Francisco",
    3.14: "pi",
    "is_student": False,
    4.5 : ["apple", "banana", "cherry"]
}

print(myDict)  # print the entire dictionary
# Dictionaries rules 
# - Dictionaries are unordered collections of key-value pairs
# - Keys must be unique and immutable (strings, numbers, or tuples)
# - Values can be of any type and can be duplicated
# - Dictionaries are mutable, meaning you can change their contents
# - You can access values using their keys, similar to how you access values in a list using indices



# dictionaries are accessed via keys
print(myDict["name"])  # access the value associated with the key "name"
print(myDict["age"])   # access the value associated with the key "age"


# you can also set dictionary data by creating a new key
myDict["country"] = "USA"  # add a new key-value pair to the dictionary
print(myDict)  # print the updated dictionary


# Trying to access a nonexistent key will produce an error
# print(myDict["nonexistent_key"])  # this will raise a KeyError



# To avoid this, you can use the "in" operator to see if a key exists
print("name" in myDict)  # check if the key "name" exists in the dictionary
# This will return True if the key exists, otherwise False


# You can retrieve all of the keys and values from a dictionary

print(myDict.keys())  # get all keys in the dictionary
print(myDict.values())  # get all values in the dictionary


# You can also iterate over all the items in a dictionary
for key, value in myDict.items():
    print(f"{key}: {value}")  # print each key-value pair in the dictionary
