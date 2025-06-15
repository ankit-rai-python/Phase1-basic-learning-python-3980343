#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("textfile.txt") or path.exists("textfile.txt.bak") or path.exists("newfile.txt"):

    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")

        
    # # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"

    # # now use the shell to make a copy of the file
    shutil.copy(src, dst)
    # shutil.copy2(src, dst) # copy metadata as well like timestamps

    # # rename the original file
    os.rename("textfile.txt", "newfile.txt")
    waiting = input("Press Enter to continue...")
    os.rename("newfile.txt", "textfile.txt")  # rename it back

    
    # now put things into a ZIP archive
    root_dir, tail = path.split(src)  # split the path into root and tail
    shutil.make_archive("archive", 'zip', root_dir, tail)  # create a ZIP archive of the file
    # shutil.make_archive("archive", 'zip', root_dir)  # create a ZIP archive of the entire directory


    # more fine-grained control over ZIP files
    with ZipFile('newarchive1.zip', 'w') as newzip:
        newzip.write("textfile.txt", arcname="textfile.txt")
        newzip.write("textfile.txt.bak", arcname="textfile.txt.bak")
    # benefit of using zipfile is that you can add files to an existing archive
    # no need to close the ZipFile object explicitly, it will be closed automatically when exiting the with block
