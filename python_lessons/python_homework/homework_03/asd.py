#!/usr/bin/env python

# Python program to demonstrate
# shutil.copytree()
 
import shutil
import errno


# function tries to copy the entire directory 
# tree from src to dest:
def copy_backup(src = ".", dest = "./backup/documents/"):

# the errno module is used to check the type of error, 
# and if the error is due to the source 
# not being a directory (errno.ENOTDIR), then shutil.copy2() 
# is used to copy the source file to the destination.
    try:
        shutil.copytree(src, dest)
    except OSError as err:
 
        # error caused if the source was not a directory
        if err.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print("Error: {}".format(err))

if __name__ == "__main__":
    # define Source path and Destination path:    
    copy_backup()  