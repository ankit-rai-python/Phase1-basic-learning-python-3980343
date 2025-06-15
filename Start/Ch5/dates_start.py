#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
# print out the date's components
print("Today's date is:", today)


# print out the date's individual components
print("Today's year is:", today.year)
print("Today's month is:", today.month)
print("Today's day is:", today.day)



# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's weekday is:", today.weekday())
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Today's weekday is:", days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
now = datetime.now()
print("The current date and time is:", now)


# Get the current time
print("The current time is:", now.time())
