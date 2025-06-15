#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#
# https://www.w3schools.com/html/tryit.asp?filename=tryhtml_editor

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.THURSDAY)
thestr = c.formatmonth(2026,1,0,0)
print(thestr)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.THURSDAY)
htmlstr = hc.formatmonth(2026,1)
print(htmlstr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2026, 8):
    print(i, end=' ')
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name, end=' ')

for day in calendar.day_name:
    print(day, end=' ')


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("\nFirst Fridays of 2026:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        firstfriday = weekone[calendar.FRIDAY]
    else:
        firstfriday = weektwo[calendar.FRIDAY]


    print(f"{calendar.month_name[m]}: {firstfriday}")
