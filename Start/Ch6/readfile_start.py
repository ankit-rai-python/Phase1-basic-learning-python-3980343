#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents

    # use the read() function to read the entire file

# Read the file contents
sample_file = open("textfile.txt", "r")

if sample_file.mode == 'r' :
    file_contents = sample_file.read()
    # Print the file contents
    print("File contents:")
    print(file_contents) 
    print("===================================================")
    
    print("File lines:")
    sample_file.close()  # close the file when done
    sample_file = open("textfile.txt", "r")  # reopen to read lines
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line.strip())  # strip() removes leading/trailing whitespace including newlines
