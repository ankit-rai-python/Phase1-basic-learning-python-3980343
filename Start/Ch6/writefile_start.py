# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
sample_file = open("textfile.txt","w+")
sample_file.write("This is a sample text file.\n")
sample_file.close()  # close the file when done

# Open the file for appending text to the end
sample_file = open("textfile.txt", "a")
# Append some text to the file
sample_file.write("Appending a new line to the file.\n")
# Close the file after writing
sample_file.close()


# write some lines of data to the file
sample_file = open("textfile.txt", "a+")
sample_file.write("This is the first line.\n")
sample_file.write("This is the second line.\n")
sample_file.write("This is the third line.\n")
# close the file when done
sample_file.close()


# Read the file contents
sample_file = open("textfile.txt", "r")
file_contents = sample_file.read()
# Print the file contents
print("File contents:")
print(file_contents) 




