# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
myList = [1, 2, "one", 4, 5]  # a list of mixed types

print(len(myList))  # length of the list




# to access a member of a sequence type, use []
print(myList[0])  # access the first element of the list
print(myList[2])  # access the third element of the list
print(myList[-1])  # access the last element of the list
myList[0] = 10  # change the first element of the list
print(myList)  # now it will print 10



# add a list to another list
anotherList = [5, 6, 7, 8]
myList += anotherList  # this will concatenate the two lists
print(myList)  # now it will print the concatenated list

mystr = "This is a string"
print(mystr[0])  # access the first character of the string
# mystr[0] = "t"  # this will cause an error because strings are immutable



# use slices to get parts of a sequence
    # Slicing allows you to get a sub-sequence from a sequence

print(myList[1:4])  # get elements from index 1 to 3 (4 is not included)
print(myList[:3])  # get the first three elements
print(myList[3:])  # get elements from index 3 to the end
print(myList[-3:])  # get the last three elements
print(myList[::2])  # get every second element



# you can use slices to reverse a sequence
print(myList[::-1])  # reverse the list

# Tuples are like lists, but they are immutable
myTuple = (1, 2, "one", 4, 5)  # a tuple of mixed types
print(myTuple)  # print the tuple
print(myTuple[0])  # access the first element of the tuple
# myTuple[0] = 10  # this will cause an error because tuples are immutable


# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 4, 5}  # a set of unique values
print(myset)  # print the set
# Sets are unordered collections of unique elements

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error
# You can add elements to a set
myset.add(6)  # add an element to the set
print(myset)  # now it will print the set with the new element
# You can remove elements from a set
myset.remove(1)  # remove an element from the set
print(myset)  # now it will print the set without the removed element
# what is purpose of sets then?
# Sets are useful for membership testing and eliminating duplicate entries



# Test for membership
print(1 in myset)  # Test for membership, returns True if 1 is in the set
print(7 in myset)  # Test for membership, returns False if 7 is not in the set
