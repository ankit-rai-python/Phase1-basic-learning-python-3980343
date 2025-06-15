#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
print("Today's date is:", now)


# print today's date one year from now
print("In one year it will be:", now + timedelta(days=365))


# create a timedelta that uses more than one argument
print("In two weeks and 3 days it will be:", now + timedelta(weeks=2, days=3))


# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
print("One week ago it was:", t.strftime("%A, %B %d, %Y"))


### How many days until April Fools' Day?
today = date.today()
today = date(today.year, 1, 1)  # ensure today is a date object
april_fools = date(today.year, 4, 1)
if april_fools < today:
    # if April Fools' Day has already occurred this year, calculate for next year
    # april_fools= april_fools.replace(year=today.year + 1)
    april_fools = date(today.year + 1, 4, 1)

print("Days until April Fools' Day:", (april_fools - today).days)
