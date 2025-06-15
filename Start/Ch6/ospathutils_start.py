#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path


# Print the name of the OS
print("Operating System:", os.name)

# Check for item existence and type
print("Item exists:", path.exists("textfile.txt"))
print("Is it a file?", path.isfile("textfile.txt"))
print("Is it a directory?", path.isdir("textfile.txt"))


# Work with file paths
print("Item path:", path.realpath("textfile.txt"))
print("Item's path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
mod_time = path.getmtime("textfile.txt")
print("Last modified time (timestamp):", mod_time)
from datetime import datetime
# Convert the modification time to a readable format
mod_time_readable = datetime.fromtimestamp(mod_time)
print("Last modified time:", mod_time_readable)

# t = time.ctime(path.getmtime("textfile.txt"))
# print("Last modified time (ctime):", t)



# Calculate how long ago the item was modified
td = datetime.now() - mod_time_readable
print("Last modified time was:", td.days, "days ago")
print("Last modified time was:", td.seconds, "seconds ago")

# Size of the file
file_size = path.getsize("textfile.txt")
print("File size in bytes:", file_size)
