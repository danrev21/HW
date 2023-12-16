#!/usr/bin/env python

# creates folders as defined in list

import os 
root_path = '/home/dan/Workdir/it_station_lab/HW/python_lessons/python_lesson_05/homework/gen/'
list = ['car', 'truck', 'bike', 'cycle', 'train'] 
for items in list: 
    path = os.path.join(root_path, items) 
    os.mkdir(path) 

#=======================================================================================
# create a target folder if not exists
# function which create folders inside


import os 

folder = "test00"
isExist = os.path.exists(folder)
if not isExist:
   os.makedirs(folder)

def inside():
    list = ['car', 'truck', 'bike', 'cycle', 'train'] 
    for items in list: 
        path = os.path.join(folder, items) 
        os.mkdir(path) 
inside()

#============================================================================
# create one folder 'test00'and in it function creates defined number of folders 'test0x'
import os 
import sys

folder = "test00"
isExist = os.path.exists(folder)
if not isExist:
   os.makedirs(folder)

def inside(num):
    items = 0
    for items in range(num):
        path = os.path.join(folder, 'test0' + str(items))
        os.mkdir(path)
        items += 1
    return        
num = int(sys.argv[1])
inside(num)

#======================================================================================
# function create defined number of folders
import os 
import sys

def parent(i):
    items = 0
    for items in range(i):
        folder = "test0" + str(items)
        isExist = os.path.exists(folder)
        if not isExist:
            os.makedirs(folder)
            items += 1
parent(1)

#==============================================================================================
import os 
import re
import shutil

# remove dirs   
pattern = r'test0*'
for f in os.listdir("."):
    if re.search(pattern, f):
        shutil.rmtree(f)

#==================================================================================        
# create list of dirs with names 'test0x'
current = os.getcwd()
list_dirs = os.listdir(current)
list_dirs.sort()
r = re.compile("test0*")
new_list = list(filter(r.match, list_dirs))
print(new_list)

#======================================================================#!/usr/bin/env python

# create a target folder if not exists
# function which create 10 folders inside(10 is default value, funcsion should have input argument with folders quantity)
# main part which create 10 folders and then 10 folders inside each one.
# другой порядок создания папок
    
import os 
import sys


def inside(*num):
    items = 0      
    for items in range(*num):
        path = os.path.join(folder, 'test0' + str(items))
        os.mkdir(path)
        items += 1 

if __name__ == '__main__':

    for items in range(10):
        folder = "test0" + str(items)
        isExist = os.path.exists(folder)
        if not isExist:
            os.makedirs(folder)
            items += 1
            
            if len(sys.argv) > 1:
                num = int(sys.argv[1])
                inside(num)               
            else:
                inside(10)   

#================================================================================
                #!/usr/bin/env python

# create a target folder if not exists
# function which create 10 folders inside(10 is default value, function should have input argument with folders quantity)
# main part which create 10 folders and then 10 folders inside each one.

import os 
import sys
import glob

# creating a target folderS if not exists
items = 0
for items in range(10):
    folder = "test0" + str(items)
    if not os.path.exists(folder):
        os.makedirs(folder)
        items += 1

# creating folders inside (10 is default value, function have input argument with folders quantity)
def inside(*num):
    for folder in glob.iglob("test0*"):
        items = 0
        for items in range(*num):
            path = os.path.join(folder, 'test0' + str(items)) 
            os.mkdir(path)
            items += 1          

# main part which create 10 folders and then 10 folders inside each one.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        inside(num)
    else:
        inside(10)










