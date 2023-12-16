#!/usr/bin/env python

# Write function that creates 10 files with target content inside target folder.
# Requirements:
# function name: createTenFilesInDir(path, phrase="default_text")
# input args: path to target dir, content for each file
# tip: try to use recursion for it

import os 
import sys

def createTenFilesInDir(path, phrase="default_text"):

    def file_recursion(i):
        file_path = os.path.join(path, 'test' + str(i)) # add file to the folder path
        with open(file_path, 'a') as file:
                file.writelines(f"{phrase}\n")
                file.close()
        if i == 1:
            print(f"10 files in '{path}' with content created !")
        else:
             file_recursion(i-1)

    file_recursion(10)
    
if __name__ == '__main__':
    createTenFilesInDir("/tmp", "param pam pam")